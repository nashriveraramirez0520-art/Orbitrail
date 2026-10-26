"""Export named printable solids from Orbitrail STEP. Requires CadQuery/OCP and numpy."""
from pathlib import Path
import json, re, struct
import numpy as np
import cadquery as cq
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.XCAFDoc import XCAFDoc_DocumentTool
from OCP.TDF import TDF_LabelSequence
from OCP.TDataStd import TDataStd_Name

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'cad' / 'stl'
EXCLUDE = {'Curve 1', 'Curve 4', 'Screw Head Envelope - Reference', 'Marble  - 08', 'M3 Washer Reference'}

def check_mesh(path):
    data=path.read_bytes(); count=struct.unpack_from('<I',data,80)[0]
    assert len(data)==84+50*count
    dtype=np.dtype([('normal','<f4',(3,)),('v','<f4',(3,3)),('attr','<u2')])
    triangles=np.frombuffer(data, dtype=dtype, offset=84)['v'].astype(float)
    assert np.isfinite(triangles).all()
    verts, inverse=np.unique(np.round(triangles.reshape(-1,3),5),axis=0,return_inverse=True)
    faces=inverse.reshape(-1,3)
    edges=np.sort(np.concatenate([faces[:,[0,1]],faces[:,[1,2]],faces[:,[2,0]]]),axis=1)
    _, uses=np.unique(edges,axis=0,return_counts=True)
    areas=np.linalg.norm(np.cross(triangles[:,1]-triangles[:,0],triangles[:,2]-triangles[:,0]),axis=1)
    assert np.all(uses==2), 'Non-manifold/open mesh'
    assert np.all(areas>1e-10), 'Degenerate triangles'
    return {'triangles':count,'closed_edge_check':True,'degenerate_triangles':0}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    reader=STEPCAFControl_Reader(); reader.SetNameMode(True)
    reader.ReadFile(str(ROOT/'cad'/'Orbitrail.step'))
    doc=TDocStd_Document(TCollection_ExtendedString('Orbitrail')); assert reader.Transfer(doc)
    tool=XCAFDoc_DocumentTool.ShapeTool_s(doc.Main()); labels=TDF_LabelSequence();tool.GetFreeShapes(labels)
    results=[]
    for i in range(1,labels.Length()+1):
        label=labels.Value(i); name=TDataStd_Name();label.FindAttribute(TDataStd_Name.GetID_s(),name)
        name=name.Get().ToExtString()
        if name in EXCLUDE: continue
        shape=cq.Shape.cast(tool.GetShape_s(label)); assert shape.isValid() and len(shape.Solids())==1,name
        box=shape.BoundingBox(); offset=(-(box.xmin+box.xmax)/2,-(box.ymin+box.ymax)/2,-box.zmin)
        shape=shape.translate(offset)
        filename=re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')+'.stl'
        if name=='Crank Gaer - 18T':filename='crank-gear-18t.stl'
        path=OUT/filename
        cq.exporters.export(shape,str(path),exportType='STL',tolerance=.02,angularTolerance=.1,opt={'ascii':False})
        result={'source_name':name,'file':filename,'size_mm':[round(v,3) for v in [box.xlen,box.ylen,box.zlen]],'solid_valid':True,'translation_mm':list(offset),**check_mesh(path)}
        results.append(result)
    (OUT/'validation.json').write_text(json.dumps({'units':'mm','linear_tolerance_mm':.02,'angular_tolerance_rad':.1,'orientation':'STEP orientation retained; XY centered and minimum Z set to zero. Not a printing orientation recommendation.','excluded':sorted(EXCLUDE),'parts':results},indent=2)+'\n')
    print(json.dumps(results,indent=2))
if __name__=='__main__':main()
