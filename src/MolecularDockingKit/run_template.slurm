#!/bin/bash
#####  Constructed by HPC everywhere #####
#SBATCH --mail-user=kumaranu@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --time=0-3:59:00
#SBATCH --mem=58gb
#SBATCH --partition=general
#SBATCH --mail-type=FAIL,BEGIN,END
#SBATCH --job-name=XX

######  Module commands #####
module unload python
module load anaconda/python3.8/2020.07

conda activate docking-rdock

######  Job commands go below this line #####
python combine.py XX


