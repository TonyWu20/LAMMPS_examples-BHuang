# Molecular dynamics simulation

The calculations were performed using the software package LAMMPS (large-scale
atomic/molecular massively parallel simulator). The Pd-Pd interaction was
modelled with the embedded-atom method. The system was minimized first using the cg style to reach
the equilibrium configuration first. The time-integration on Nose-Hoover
style non-Hamiltonian equations of motion was performed, using the canonical
(nvt) ensembles at 298 for 10 ns to obtain the atom positions and velocity under
the configuration. A final minimization was performed after the nvt time-integration
to obtain the stabilized structure. The potential energy of the system and the
cohesive energy per atom were computed by LAMMPS. The velocity Verlet algorithm
was used with an integration time step of 1.0 fs. Periodical boundary conditions were applied along the
x, y, and z directions. The strain levels on the surface after nvt were visualized
by the software package OVITO by calculating the atomic strain, using the
initial configuration as the data reference.

Reference:

1. S. Plimpton, Fast Parallel Algorithms for Short-Range Molecular Dynamics, J Comp Phys, 117, 1-19 (1995).
2. Alexander Stukowski 2010 Modelling Simul. Mater. Sci. Eng.18 015012
