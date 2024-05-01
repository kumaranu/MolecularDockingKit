import os, glob, re, sys
import numpy as np

#######################################################################
#                                                                     #
# This script extracts the energies for the three components required #
# in the binding energy calculations, which are (protein + ligand),   #
# protein, and ligand energies. It calculates the binding energies    #
# for all the drug molecules and prints them in kcal/mol.             #
#                                                                     #
#######################################################################


os.chdir('moleculeLists')
molList = open('fileList.txt', 'r').readlines()
molList = [mol.strip() for mol in molList]
os.chdir('../')

e1 = np.loadtxt('energy_protein/energies.txt')

os.chdir('rDock_inputs')
for mol in molList:
    os.chdir(mol)
    try:
        eCombined = np.loadtxt('energies.txt')
        print("%s, %3f, %3f, %3f, %3f, %3f" % (mol, eCombined[0], eCombined[1], e1, (eCombined[0] - eCombined[1] - e1), (eCombined[0] - eCombined[1] - e1)*627.503))
        os.chdir('../') 
    except:
        os.chdir('../') 
        continue
        print(mol, 'skipped due to some error')
os.chdir('../')
