import os
import numpy as np

def calculate_binding_energy(mol_list: list[str], protein_energy: float) -> None:
    """
    Extracts the energies for the three components required in the binding energy calculations,
    which are (protein + ligand), protein, and ligand energies. It calculates the binding energies
    for all the drug molecules and prints them in kcal/mol.

    Args:
        mol_list (list[str]): List of molecules.
        protein_energy (float): Energy of the protein component.

    Returns:
        None
    """
    # Change directory to moleculeLists to access fileList.txt
    os.chdir('../../moleculeLists')
    mol_list = open('fileList.txt', 'r').readlines()
    mol_list = [mol.strip() for mol in mol_list]
    os.chdir('../../../')

    e_protein = np.loadtxt('energy_protein/energies.txt')

    os.chdir('rDock_inputs')
    for mol in mol_list:
        os.chdir(mol)
        try:
            e_combined = np.loadtxt('energies.txt')
            ligand_energy, binding_energy = calculate_energy_components(e_combined, e_protein)
            print(f"{mol}, {e_combined[0]}, {e_combined[1]}, {e_protein}, {binding_energy}, {binding_energy * 627.503}")
            os.chdir('../../../')
        except Exception as e:
            os.chdir('../../../')
            print(f"{mol} skipped due to error: {e}")
            continue
    os.chdir('../../../')

def calculate_energy_components(e_combined: np.ndarray, e_protein: float) -> tuple[float, float]:
    """
    Calculates the energy of the ligand and binding energy.

    Args:
        e_combined (np.ndarray): Array containing energies for (protein + ligand).
        e_protein (float): Energy of the protein component.

    Returns:
        Tuple containing ligand energy and binding energy.
    """
    ligand_energy = e_combined[0] - e_combined[1]
    binding_energy = ligand_energy - e_protein
    return ligand_energy, binding_energy

# Example usage
if __name__ == "__main__":
    molList = ['mol1', 'mol2']  # Example list of molecules
    proteinEnergy = 10.0  # Example protein energy
    calculate_binding_energy(molList, proteinEnergy)
