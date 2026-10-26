# Orbitrail STL parts

17 individual binary STL files exported from [Orbitrail.step](../Orbitrail.step). Import using **millimeters**, at 100% scale. Print one of each part for the current CAD assembly.

The return tracks, stairs, funnel and their supports are a **single connected solid** in the source, so they are provided together as `smooth-stairs-curves-funnel.stl`.

## Before slicing

- These are geometry exports, not printer profiles or G-code. Rotate each part in the slicer to choose a suitable build face; the inclined screw, gears, caps and housing retain their CAD orientation.
- Every STL is centered in XY and rests at minimum Z = 0. This translation does not change its size or relative geometry, but the separate files are not positioned for assembling together.
- Review overhangs, supports, bed adhesion, shaft fits, and gear clearances. Avoid leaving support scars on running surfaces where possible.
- Check the slicer's usable bed area, including brim/support margins. The base is 180 mm across and the return module is approximately 178.2 × 150.8 × 67 mm in the exported orientation.
- No slicer or physical print validation has been performed. Test fitting and marble motion remain pending.
- A 3MF print project is not included because a printer, material and slicing settings have not been selected.

## Included parts

Dimensions are bounding boxes in the exported orientation, not a recommended print orientation.

| File | Source part | Bounding box (mm) |
| --- | --- | --- |
| [lift-screw.stl](lift-screw.stl) | Lift Screw | 98.117 × 26.03 × 134.903 |
| [rocker-frame.stl](rocker-frame.stl) | Rocker Frame | 14.6 × 30.0 × 73.0 |
| [crank-retainer.stl](crank-retainer.stl) | Crank Retainer | 7.414 × 8.0 × 5.817 |
| [rocker.stl](rocker.stl) | Rocker | 10.0 × 24.0 × 12.5 |
| [lower-cap.stl](lower-cap.stl) | Lower Cap | 35.799 × 50.0 × 29.659 |
| [lower-pedestal.stl](lower-pedestal.stl) | Lower Pedestal | 30.188 × 60.0 × 21.229 |
| [base.stl](base.stl) | Base | 180.0 × 180.0 × 4.0 |
| [lift-gear.stl](lift-gear.stl) | Lift Gear | 24.166 × 26.0 × 19.009 |
| [lift-gear-retainer.stl](lift-gear-retainer.stl) | Lift Gear Retainer | 11.264 × 12.0 × 8.931 |
| [rocker-pin-cap.stl](rocker-pin-cap.stl) | Rocker Pin Cap | 4.1 × 8.0 × 8.0 |
| [crank-gear-18t.stl](crank-gear-18t.stl) | Crank Gaer - 18T | 19.09 × 20.0 × 18.868 |
| [upper-cap.stl](upper-cap.stl) | Upper Cap | 44.892 × 50.0 × 29.659 |
| [smooth-stairs-curves-funnel.stl](smooth-stairs-curves-funnel.stl) | Smooth_Stairs_Curves_Funnel | 178.214 × 150.834 × 67.0 |
| [crank-arm.stl](crank-arm.stl) | Crank Arm | 30.965 × 10.0 × 34.673 |
| [lift-housing.stl](lift-housing.stl) | Lift Housing | 105.694 × 50.0 × 132.462 |
| [drop-guide.stl](drop-guide.stl) | Drop Guide | 43.636 × 52.01 × 105.628 |
| [rocker-pin.stl](rocker-pin.stl) | Rocker Pin | 19.0 × 8.0 × 8.0 |

## Export checks

All 17 source solids passed OpenCascade validity checks. Exported meshes passed finite-coordinate, zero-degenerate-triangle and closed-edge checks (two triangles per welded edge, with vertex coordinates rounded to 0.00001 mm). These checks do not establish printability, collision-free motion or strength.

Export tolerances: 0.02 mm linear and 0.1 rad angular. See [validation.json](validation.json) and [the export script](../../scripts/export_stl.py).

Excluded inspection aids: Curve 1, Curve 4, the reference marble, screw-head envelope and M3 washer reference. Purchase actual marbles and hardware separately.
