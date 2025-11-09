from ase.build import mx2
from ase.io import write
import numpy as np

a_WS2 = 3.153
a_WSe2 = 3.282

# Build strained supercells
ws2 = mx2("WS2", kind="2H", a=a_WS2, size=(26, 26, 1))
wse2 = mx2("WSe2", kind="2H", a=a_WSe2, size=(25, 25, 1))

# Transform WS2 to match WSe2's y-dimension
# scale_y = ws2.cell[1] / 26 * 0.5
# print(scale_y)
# ws2.positions[:] += scale_y
# ws2.cell[1] *= scale_y
# print(ws2.cell)
# Align W-atom rows at interface
wse2.positions[:, 0] += ws2.cell[0, 0] + 0.3

# Combine
hetero = ws2 + wse2
hetero.cell = [(ws2.cell[0] + wse2.cell[0]), wse2.cell[1], [0.0, 0.0, 60]]


# min_z = np.min(hetero.positions[:, 2])
# hetero.positions[:, 2] -= min_z - 7
hetero.positions[:, 2] += 7.0

hetero.center(40, axis=0)

# compute the dislocation core position to insert the w
# the middle point of the line sector between w_1 and w_2
# is roughly the center of the heptagonal ring, so we choose it
# as the insertion position
# hetero += new_s
# del_list = []
# for i in range(len(ws2)):
#     for j in range(len(ws2), len(hetero)):
#         dist = np.linalg.norm(hetero.positions[i] - hetero.positions[j])
#         if dist < 2.0:
#             del_list.append(j)

# del hetero[del_list]

# Place vacuum around to prevent periodic boundary interaction
# hetero.center(vacuum=20.0)

# output in different formats
print(np.linalg.norm(hetero.cell[0]))
print(np.linalg.norm(hetero.cell[1]))
print(np.linalg.norm(hetero.cell[2]))
write("ws2_wse2_junction_periodic.lmp", hetero, format="lammps-data")
write("ws2_wse2_junction_periodic.cif", hetero, format="cif")
write("ws2_wse2_junction_periodic.xyz", hetero, format="xyz")
