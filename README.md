# LAMMPS_examples

`LAMMPS` example projects

## Overview

This repository holds a few example projects in `LAMMPS` for education and
demonstrations. Necessary input scripts, potential files and input structure
data files are provided. Students are encouraged to run these projects
independently, experiment modifying the scripts to their needs, and study the
properties from the systems by adding necessary outputs in scripts and/or
writing post processing scripts for the output data.

## Example projects

### WS2_WSe2

This folder contains:

- `sw_mx2`

  An example code to study the deformation in WS<sub>2</sub>-WSe<sub>2</sub>
  from misfit strain.

- `WSe2_triangle_in_WS2`

  A group of WSe<sub>2</sub> atoms in the shape of triangle is
  surrounded by WS<sub>2</sub> atoms.

- `WS2_WSe2_dislocation_growth`

  Heterojunction models of WS<sub>2</sub>-WSe<sub>2</sub> with dislocations. The MD simulation runs are designed to study the dislocation growth through the diffusion of S atoms toward the WSe<sub>2</sub> region. Python scripts are written to create the heterojunction structures with dislocation.

### Transition_metals

- `simple_example_runs`

  This subfolder presents demonstrative MD simulations for
  transition metals. Only elements that are supported by published or `LAMMPS`
  built-in potential files are presented in this subproject.
  The initial structure are created by `LAMMPS` command in `fcc` or `hcp` lattice
  structure, which is demonstrated by the provided input scripts.

- `high_index`

  This project aims to study the surface atomic strain levels and distributions
  on various nanoparticles enclosed with facets in different miller-indices
  (from 100 to 554).

  Systems include:

  1. Mono-metal nanoparticles
  2. Bi-metal alloy nanoparticles
  3. Ternary alloy nanoparticles
  4. High-entropy alloy (HEA) nanoparticles

### Pd_icosahedrons

This project studies the surface atomic strain trends on Pd icosahedron
nanoparticles with increasing number of atoms.

### tem2

This project studies the surface atomic strain distributions on a Cu pentagonal
nanowire model.
