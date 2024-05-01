# MolecularDockingKit

MolecularDockingKit is a Python tool designed for molecular docking computations. It provides a simple and efficient way to perform docking simulations and analyze the results.

## Overview

The repository contains scripts and supplementary files necessary for running molecular docking simulations and analyzing the output data. Below is a brief overview of the main components:

- **Main Script**: `make.bash`
- **Supplementary Scripts**:
  - `main.py`
  - `getSmilesFromFile.py`
  - `xyzFromSmiles.py`
  - `getScores.tcsh`
  - `call_combine.tcsh`
  - `combine.py`
  - `run.slurm` (inside the `energy_protein` directory)
  - `getEnergy.py`
  - `run_template.slurm`

## Usage

To use MolecularDockingKit, follow these steps:

1. Prepare input files:
   - Create a `drugs.txt` file containing initial data.
   - Obtain a `3sxr_dasatinib_removed.pdb` file representing the protein without dasatinib.
   - Set up a directory named `energy_protein` with a `run.py` script for submitting protein jobs.
   - Provide a template file named `prm-template.prm` for the prm input file used in docking calculations.

2. Execute the main script `make.bash` to initiate the docking computations.

3. Follow the instructions provided in the comments of each script to understand their specific functions and requirements.

## Contributing

Contributions to MolecularDockingKit are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Author
Anup Kumar
