import os, glob, sys
from rdkit import Chem
from multiprocessing import Pool
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

enzymeFile = '../3sxr_dasatinib_removed.pdb'
m = Chem.rdmolfiles.MolFromPDBFile(enzymeFile)
m = Chem.AddHs(m, addCoords=True)
res = AllChem.MMFFOptimizeMoleculeConfs(m, maxIters=0, numThreads=0)
np.savetxt('energies.txt', [res[0][1]])


