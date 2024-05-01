import os
from typing import List, Tuple


def get_smiles_from_file(file_name: str) -> Tuple[List[str], List[str]]:
    """
    Extracts smiles from the given file.

    Args:
        file_name (str): The name of the file containing smiles.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing lists of molecule names and smiles.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()[1:]

    mol_names, smiles = [], []

    for line in lines:
        elements = line.strip().split()
        if elements[-1] in {'TRUE', 'FALSE'}:
            continue
        else:
            if len(elements) > 3:
                mol_names.append('_'.join([element.replace('/', '-') for element in elements[:-2]]))
                smiles.append(elements[-1])
            elif len(elements) == 3:
                mol_names.append(elements[0])
                smiles.append(elements[2])
            else:
                print(f'Something wrong with {elements}.')

    # Writing the names of molecules in a file inside a separate directory for future calculations
    molecule_lists_dir = '../../moleculeLists'
    if not os.path.exists(molecule_lists_dir):
        os.mkdir(molecule_lists_dir)
    os.chdir(molecule_lists_dir)

    with open("fileList.txt", 'w') as file:
        file.write('\n'.join(mol_names))

    return mol_names, smiles
