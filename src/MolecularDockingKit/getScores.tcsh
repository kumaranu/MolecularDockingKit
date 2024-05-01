#!/bin/tcsh

###################################################################
#                                                                 #
# This script extracts the docking scores for all the drugs and   #
# sorts them.                                                     #
#                                                                 #
###################################################################

# Remove existing allScores.txt file
rm -f allScores.txt

# Navigate to the rDock_inputs directory
cd rDock_inputs/

# Loop through each molecule in the fileList.txt
foreach mol (`cat ../moleculeLists/fileList.txt | xargs`)
    cd $mol

    # Extract the docking score for the current molecule
    set score = `grep -iwA1 "<SCORE>" "${mol}_docking_out_sorted.sd" | tail -1`

    # Write the molecule name and its score to allScores.txt
    echo "$mol $score" >> ../../allScores.txt

    cd ..
end

# Navigate back to the main directory
cd ..

# Sort the allScores.txt file based on the docking scores and save it to sorted_allScores.txt
sort -k2g allScores.txt > sorted_allScores.txt
