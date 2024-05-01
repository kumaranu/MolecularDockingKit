import os
import sys
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

def calculate_energy(file_index: str) -> None:
    """
    Perform energy calculations for a list of drugs specified in the file indexed by `file_index`.

    Args:
        file_index (str): Index of the file containing the list of drugs.

    Returns:
        None
    """
    mol_list = open(f'moleculeLists/fiveSplits/file{file_index}.txt', 'r').readlines()
    mol_list = [mol.strip() for mol in mol_list]
    enzyme_file = '../../3sxr_dasatinib_removed.pdb'

    os.chdir('rDock_inputs/')
    for ligand_name in mol_list:
        os.chdir(ligand_name)
        m1, m2 = load_molecules(ligand_name, enzyme_file)

        # Generate the ligand + protein geometry
        combo = Chem.CombineMols(m1, m2)
        combo = Chem.AddHs(combo, addCoords=True)
        Chem.rdmolfiles.MolToPDBFile(combo, 'combo.pdb')

        # Calculate the energy for the (ligand + protein) geometry
        res = AllChem.MMFFOptimizeMoleculeConfs(combo, maxIters=0, numThreads=0)

        # Calculate the energies for the ligand only geometry
        res1 = AllChem.MMFFOptimizeMoleculeConfs(m1, maxIters=0, numThreads=0)

        # Save the energies for the (ligand + protein) and the ligand only geometry in a file
        np.savetxt('energies.txt', [res[0][1], res1[0][1]])
        os.chdir('../../../')
    os.chdir('../../../')

def load_molecules(ligand_name: str, enzyme_file: str) -> tuple[Chem.Mol, Chem.Mol]:
    """
    Load ligand and enzyme molecules from SD and PDB files, respectively.

    Args:
        ligand_name (str): Name of the ligand molecule.
        enzyme_file (str): Path to the enzyme PDB file.

    Returns:
        Tuple containing the ligand and enzyme molecules.
    """
    suppl = Chem.SDMolSupplier(f'{ligand_name}_docking_out_sorted.sd')
    mols = [x for x in suppl]
    m1 = mols[-1]
    m2 = Chem.rdmolfiles.MolFromPDBFile(enzyme_file)
    return m1, m2

# Example usage
if __name__ == "__main__":
    file_index = sys.argv[1]
    calculate_energy(file_index)
