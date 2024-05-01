from src.MolecularDockingKit import getSmilesFromFile, xyzFromSmiles
import os

############################################################
#                                                          #
# This program generates the xyz coordinates for the drugs #
# molecules and the rdock inputs                           #
#                                                          #
############################################################

#Extracting the names and the smiles for all the drug molecules
molNames, smiles = getSmilesFromFile.getSmilesFromFile('drugs.txt')

#Creating a separate directory for the docking calculations
if not os.path.exists('rDock_inputs'):
    os.mkdir('rDock_inputs')
os.chdir('rDock_inputs')

#Loading a prm file template to be edited later for each molecule
f = open('../../prm-template.prm', 'r').read()

for i in range(len(molNames)):
    #Creating a separate directory for each drug's calculation
    if not os.path.exists(molNames[i]):
        os.mkdir(molNames[i])
    os.chdir(molNames[i])

    #Generating the xyz coordinates from smiles for the drug molecule
    #and writing to a file in the sdf format
    xyzFromSmiles.xyzFromSmiles(smiles[i], molNames[i])

    #Generate prm file with the use of the template loaded earlier
    f1 = f.replace('YYYYY', molNames[i])
    file1 = open(molNames[i] + '_rdock.prm', "w") 
    file1.write(f1)
    file1.close() 

    os.chdir('../../../')
os.chdir('../../../')

