#!/bin/tcsh

#########################################################################
#                                                                       #
# This script submits slurm jobs for ligand+protein and the ligand only #
# calculations.                                                         #
#                                                                       #
#########################################################################


#Call to the energy calculations for the ligand+protein and the ligand
set nSplits = `ls -ltr moleculeLists/fiveSplits/file* | wc`

foreach i(`seq -w 0 $nSplits`)
  sed "s/XX/$i/g" run_template.slurm > run$i.slurm
  sbatch run$i.slurm
end

