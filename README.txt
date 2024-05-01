-------------------------------------- Outline of the program ---------------------------------------------
Main script to run:
  make.bash

Supplementary scripts:
  1) main.py
  2) getSmilesFromFile.py
  3) xyzFromSmiles.py
  4) getScores.tcsh
  5) call_combine.tcsh
  6) combine.py
  7) run.slurm inside a directory named energy_protein
  8) getEnergy.py
  9) run_template.slurm

Files and directories needed from the user:
  1) A file named "drugs.txt" which contains the initial data from the website given in the problem.
  2) A file named "3sxr_dasatinib_removed.pdb" containing the protein without dasatinib. I could have
     removed this user input but kept it this way.
  3) A directory named "energy_protein" that contains a slurm script run.py which would submit the job
     for protein.py such as run.slurm
  4) A template file named 'prm-template.prm' for the prm input file to be used for docking calculations.

-------------------------------------- Summary of the program ---------------------------------------------
All of the scripts contain comments to clarify their purpose in the program. A brief summary is provided below:
1) The bash script main.bash calls main.py.
   - main.py extracts the smiles formats for the drugs from the file called drugs.txt.
   - A directory structure is created for the docking calculations which looks like:
     |---- rDock_inputs/
     |     |----MoleculeName/
   - xyz coordinates are generated from the smiles using the script xyzFromSmiles
   - .prm input files are generated from the prm-template.prm and are stored as moleculeName_rdock.prm as:
     |---- rDock_inputs/
     |     |----MoleculeName/
     |     |    |----moleculeName_rdock.prm 
2) A 10 runs-per-ligand rDock job is submitted for each drug molecule.
3) getScores.tcsh is called to extract the scores from the docking output files.
4) The scores and the molecule names are put in a file and molecule are sorted according to their docking scores. 
5) A shell script call_combine is called which submits slurm jobs for binding energy calculations.
6) Energy calculations are submitted for the protein without ligand.
7) A python script getEnergy.py is called to extract energies and return binding energies in kcal/mol.
8) Molecules are sorted according to their binding energies to get their ranking.
__________________________________________________________________________________________________________

