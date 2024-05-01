from rdkit import Chem
from rdkit.Chem import AllChem

###########################################################
#                                                         #
# This program generates the xyz coordinates for the      #
# molecules using SMILES. It tries for upto 20 iterations #
# inside the rdkit MM force field optimizer and only      #
# returns a geometry if converged. Most of the molecules  #
# were converged with an exception of four to five.       #
#                                                         #
###########################################################
def xyzFromSmiles(smiles, fileName):
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, useRandomCoords=True)
    try:
        AllChem.MMFFOptimizeMolecule(mol, maxIters=20)
        writer = Chem.rdmolfiles.SDWriter(fileName + '.sd')
        writer.write(mol)
    except:
        print('Skipping ', fileName)
        return

