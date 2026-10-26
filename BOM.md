# Orbitrail — Bill of Materials

No funding was requested for this project. This list documents the materials needed for the planned build; it is not a request for reimbursement. Printing is planned at the university. The printer, filament brand and slicing settings have not been confirmed.

## Materials

| Item | Planned quantity | Purpose / specification | Supply and cost status |
| --- | --- | --- | --- |
| PLA filament | 500 g provisional material allowance | Print one of each of the 17 STL parts listed below. Match filament diameter to the university printer. | University printing planned; material availability and any charge to be confirmed. No funding requested. |
| M3 machine screws | Assorted lengths; exact count and lengths pending assembly review | Secure the housing/end supports and mounting feet and provide the gear-retainer fixing where required. | Purchase or use available hardware after reviewing each joint. No supplier or price selected. |
| M3 hex nuts | As required by the selected through-bolt joints; count pending | Retain bolts where the design provides suitable nut access or pockets. Do not assume every hole requires a nut. | Selection and fit to be confirmed. No funding requested. |
| M3 washers | As required; count pending | Use where suitable to distribute bolt load or protect printed surfaces. The reference washer in the CAD is not a printable part. | Optional per joint; do not count every hole as requiring a washer. |
| 8 mm marbles | At least 1 for initial testing | Reference marble diameter used by the elevator and channels. Add more only after testing circulation. | Supplier, pack quantity and cost not yet selected. |

The hardware rows are requirements, **not a finalized shopping list**. Do not substitute M2 hardware without checking or adapting the M3 mounting design. Final screw lengths depend on the actual joint stack, head seating, nut engagement and clearance to moving parts.

## Filament allowance and its limits

The combined CAD solid volume of the 17 printable parts is **270.816 cm³**. Assuming a PLA density of **1.24 g/cm³**, a completely solid model would contain approximately **335.8 g** of PLA, excluding supports, brims, purge and failed prints.

The density is a reference assumption, not a confirmed material property of the university's filament; see [Polymaker PLA technical data](https://polymaker.com/wp-content/tech-docs/PolyLite_PLA_PIS_EN_V1.1.pdf).

**500 g is a provisional stock allowance**, not a slicer prediction or guaranteed upper limit. Actual consumption depends on walls, infill, orientation, supports and reprints. A lower infill percentage does not reduce the entire model mass by that percentage because walls and surface layers remain. Replace this allowance with the university slicer's total before manufacturing.

## Printed parts — one of each

| Part | STL file |
| --- | --- |
| Base | [base.stl](cad/stl/base.stl) |
| Lift screw | [lift-screw.stl](cad/stl/lift-screw.stl) |
| Lift housing | [lift-housing.stl](cad/stl/lift-housing.stl) |
| Lower cap | [lower-cap.stl](cad/stl/lower-cap.stl) |
| Upper cap | [upper-cap.stl](cad/stl/upper-cap.stl) |
| Lower pedestal | [lower-pedestal.stl](cad/stl/lower-pedestal.stl) |
| Lift gear | [lift-gear.stl](cad/stl/lift-gear.stl) |
| Lift gear retainer | [lift-gear-retainer.stl](cad/stl/lift-gear-retainer.stl) |
| Crank gear — 18 teeth | [crank-gear-18t.stl](cad/stl/crank-gear-18t.stl) |
| Crank arm | [crank-arm.stl](cad/stl/crank-arm.stl) |
| Crank retainer | [crank-retainer.stl](cad/stl/crank-retainer.stl) |
| Rocker frame | [rocker-frame.stl](cad/stl/rocker-frame.stl) |
| Rocker | [rocker.stl](cad/stl/rocker.stl) |
| Rocker pin | [rocker-pin.stl](cad/stl/rocker-pin.stl) |
| Rocker pin cap | [rocker-pin-cap.stl](cad/stl/rocker-pin-cap.stl) |
| Drop guide | [drop-guide.stl](cad/stl/drop-guide.stl) |
| Connected return tracks, stairs, funnel and supports | [smooth-stairs-curves-funnel.stl](cad/stl/smooth-stairs-curves-funnel.stl) |

Read the [STL printing notes](cad/stl/README.md) before slicing. The reference marble, curves and hardware reference bodies are excluded from the printed inventory. No motor, electronics or bearings are specified in this hand-cranked version.

## Budget status

**Requested funding: $0.00.** This does not mean the materials have no value or that supplier costs have been verified. Final purchase totals, if any, remain pending the hardware selection and printing arrangements. [BOM.csv](BOM.csv) mirrors the material requirements with unquoted prices left blank.
