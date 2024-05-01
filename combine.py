import os, glob, sys
from rdkit import Chem
from multiprocessing import Pool
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

###########################################################################
#                                                                         #
# This program takes in one argument for the file index for the file      #
# inside the directory called moleculeLists.txt named something like      #
# file000, file001 etc. that contains the names of five drugs. The energy #
# calculations for these drugs is submitted together. This way, I         #
# parallelize the calculations with brute force separate job submitions.  #
#                                                                         #
###########################################################################

molList = open('moleculeLists/fiveSplits/file' + sys.argv[1] + '.txt', 'r').readlines()
molList = [mol.strip() for mol in molList]
enzymeFile = '../../3sxr_dasatinib_removed.pdb'

os.chdir('rDock_inputs/')
for ligandName in molList:
    os.chdir(ligandName)
    suppl = Chem.SDMolSupplier(ligandName + '_docking_out_sorted.sd')
    mols = [x for x in suppl]
    m1 = mols[-1]
    m2 = Chem.rdmolfiles.MolFromPDBFile(enzymeFile)

    #Generating the ligand + protein geometry
    combo = Chem.CombineMols(m1, m2)
    combo = Chem.AddHs(combo, addCoords=True)
    Chem.rdmolfiles.MolToPDBFile(combo, 'combo.pdb')

    #Calculating the energy for the (ligand + protein) geometry
    #As I say in the other document, xtb did not work and I ended up using rdkit
    #for this step
    #os.system('xtb --gfnff combo.xyz > combo.log')
    res = AllChem.MMFFOptimizeMoleculeConfs(combo, maxIters=0, numThreads=0)

    #Calculating the energies for the ligand only geometry
    m1 = Chem.AddHs(m1, addCoords=True)
    res1 = AllChem.MMFFOptimizeMoleculeConfs(m1, maxIters=0, numThreads=0)

    #Saving the energies for the (ligand + protein) and the ligand only geometry in a file
    np.savetxt('energies.txt', [res[0][1], res1[0][1]])
    os.chdir('../')
os.chdir('../')


