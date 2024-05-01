import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem


def xyz_from_smiles(smiles: str, file_name: str) -> None:
    """
    Generates the xyz coordinates for molecules using SMILES.

    Parameters:
    smiles (str): The SMILES string of the molecule.
    file_name (str): The name of the output file to save the molecule coordinates.

    Returns:
    None. Saves the coordinates to a file in SD format.
    """

    # Convert SMILES to RDKit molecule object
    mol = Chem.MolFromSmiles(smiles)

    # Add hydrogen atoms to the molecule
    mol = Chem.AddHs(mol)

    # Embed the molecule and optimize using the MMFF force field
    AllChem.EmbedMolecule(mol, useRandomCoords=True)
    try:
        AllChem.MMFFOptimizeMolecule(mol, maxIters=20)

        # Write the molecule to an SD file
        writer = Chem.rdmolfiles.SDWriter(file_name + '.sd')
        writer.write(mol)
    except:
        print('Skipping ', file_name)
        return
