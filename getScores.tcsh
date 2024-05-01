#!/bin/tcsh

#################################################################
#                                                               #
# This script extracts the docking scores for all the drugs and #
# sorts them.                                                   #
#                                                               #
#################################################################

rm -f allScores.txt

cd rDock_inputs/
  foreach mol(`cat ../moleculeLists/fileList.txt | xargs`)
    cd $mol
      set score = `grep -iwA1 "<SCORE>" "$mol"_docking_out_sorted.sd | tail -1`
      echo "$mol $score" >> ../../allScores.txt
    cd ..
  end
cd ..

sort -k2g allScores.txt > sorted_allScores.txt


