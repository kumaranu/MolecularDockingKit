#!/bin/bash

#Activating a conda environment that contains rdock
conda activate docking-rdock

#######################################################################
#                                                                     #
# The python program main.py below does the preprocessing on the data #
# provided inside the file drugs.txt. It extracts smiles format and   #
# generats the xyz coordinates for each molecule. It also creates the #
# prm files for each them and stores them in separate directories for #
# the docking calculations.                                           #
#                                                                     #
#######################################################################
python main.py

source deactivate

#Generating a mol2 file for the receptor from the user-provided pdb
babel -ipdb 3sxr_dasatinib_removed.pdb -omol2 receptorFile.mol2

########################################################################
#                                                                      #
# A serial implementation is written below and hence it should only be #
# used for small number of input drugs molecules. I ended up splitting #
# the calculations into multiple parts.                                #
#                                                                      #
########################################################################

cd rDock_inputs
  for mol in $( ls -d1 * ); do
    cd $mol
      echo "$mol"
      rm *log *docking*sd *.as *.mol2
      sed "s/YYYYY/$mol/g" ../../prm-template.prm > "$mol"_rdock.prm
      cp ../../receptorFile.mol2 "$mol"_rdock.mol2
      rbcavity -r "$mol"_rdock.prm -W > "$mol"_cavity.log
      rbdock -r "$mol"_rdock.prm -p dock.prm -n 10 -i "$mol".sd -o "$mol"_docking_out > "$mol"_docking_out.log
      sdsort -n -f'SCORE' "$mol"_docking_out.sd > "$mol"_docking_out_sorted.sd
    cd ..
  done
cd ..

#Extracting the docking scores for all the drug molecules
./getScores.tcsh

###############################################################
#                                                             #
# Calculating the binding energy for protein ligand complexes #
#                                                             #
###############################################################

#Splitting the drugs into sets of 5 to parallelize the energy calculation process
mkdir -p moleculeLists
cd moleculeLists
  mkdir -p fiveSplits
  cd fiveSplits
    split -n l/5 --suffix-length=3 --additional-suffix=.txt --numeric-suffixes ../fileList.txt file
  cd ..
cd ..

#Call to the energy calculations for the ligand+protein and the ligand
./call_combine.tcsh

#Calling a job submission script for the energy calculations for the protein.
#It requires the user to create a directory named energy_protein with the
#script protein.py and a slurm script run.slurm to be present in that directory.
#This step can obviously be done cleanly but this is how I did it.
cd energy_protein
  sbatch run.slurm
cd ..

#Call to energy grepping python script
python getEnergy.py > all_energies.txt
sort -k6rg all_energies.txt | column -t > sorted_energies.txt

