from ase.build import mx2
from ase.io import write
import numpy as np

a_WS2 = 3.153
a_WSe2 = 3.282

# Build strained supercells
ws2 = mx2("WS2", kind="2H", a=a_WS2, size=(26, 26, 1))
wse2 = mx2("WSe2", kind="2H", a=a_WSe2, size=(25, 25, 1))

# Align W-atom rows at interface
wse2.positions[:, 0] += ws2.cell[0, 0] + 0.3

# Combine the structures
hetero = ws2 + wse2
hetero.cell = [(ws2.cell[0] + wse2.cell[0]), wse2.cell[1], [0.0, 0.0, 60]]
hetero.positions[:, 2] += 7.0
hetero.center(40, axis=0)

# Identify atoms to remove to create dislocation defect
del_list = []
interface_x = ws2.cell[0, 0]  # x-coordinate of the interface

# Parameters for dislocation region
dislocation_width = 5.0  # Width of the dislocation region in Å
dislocation_offset = 2.0  # How far from interface to start removing atoms

# Remove atoms near the interface to create dislocation
for i in range(len(hetero)):
    # For WS2 side (left of interface)
    if (
        hetero.positions[i, 0] < interface_x
        and hetero.positions[i, 0] > interface_x - dislocation_width
        and hetero.positions[i, 1] < dislocation_offset
    ):
        del_list.append(i)

    # For WSe2 side (right of interface)
    if (
        hetero.positions[i, 0] > interface_x
        and hetero.positions[i, 0] < interface_x + dislocation_width
        and hetero.positions[i, 1] < dislocation_offset
    ):
        del_list.append(i)

# Remove overlapping atoms first to prevent too close distances
for i in range(len(ws2)):
    for j in range(len(ws2), len(hetero)):
        dist = np.linalg.norm(hetero.positions[i] - hetero.positions[j])
        if dist < 2.0:
            if j not in del_list:  # Don't add duplicates
                del_list.append(j)

# Remove the selected atoms (sort in reverse to avoid index shifting)
del_list = sorted(list(set(del_list)), reverse=True)
for index in del_list:
    del hetero[index]

# Center the structure with vacuum
hetero.center(vacuum=10.0, axis=1)  # Add vacuum in y-direction
hetero.center(vacuum=10.0, axis=2)  # Add vacuum in z-direction

# Output in different formats
write("ws2_wse2_junction_periodic_disloc.lmp", hetero, format="lammps-data")
write("ws2_wse2_junction_periodic_disloc.cif", hetero, format="cif")
write("ws2_wse2_junction_periodic_disloc.xyz", hetero, format="xyz")
