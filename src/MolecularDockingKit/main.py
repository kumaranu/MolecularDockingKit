from src.MolecularDockingKit import get_smiles_from_file, xyz_from_smiles
import os


def generate_docking_inputs():
    """
    Generates the xyz coordinates and rDock inputs for drug molecules.

    This function extracts names and SMILES for all drug molecules from a file,
    creates separate directories for docking calculations, generates xyz coordinates
    from SMILES for each drug molecule, and generates rDock input files.

    Returns:
    None.
    """

    # Extract names and SMILES for all drug molecules
    mol_names, smiles = get_smiles_from_file.get_smiles_from_file('drugs.txt')

    # Create a separate directory for docking calculations
    if not os.path.exists('rDock_inputs'):
        os.mkdir('rDock_inputs')
    os.chdir('rDock_inputs')

    # Load a prm file template to be edited later for each molecule
    template = open('../../prm-template.prm', 'r').read()

    for i in range(len(mol_names)):
        # Create a separate directory for each drug's calculation
        if not os.path.exists(mol_names[i]):
            os.mkdir(mol_names[i])
        os.chdir(mol_names[i])

        # Generate xyz coordinates from SMILES for the drug molecule
        # and write to a file in the sdf format
        xyz_from_smiles.xyz_from_smiles(smiles[i], mol_names[i])

        # Generate prm file using the loaded template
        prm_content = template.replace('YYYYY', mol_names[i])
        with open(mol_names[i] + '_rdock.prm', "w") as prm_file:
            prm_file.write(prm_content)

        os.chdir('../../../')
    os.chdir('../../../')


if __name__ == '__main__':
    generate_docking_inputs()
