#This script extracts the smiles from the file named as drugs.txt
import os
def getSmilesFromFile(fileName):
    INF = open(fileName,'r').readlines()
    tmp1  = [i.strip().split() for i in INF][1:]
    molNames, smiles = [], []
    for i in tmp1:
        if (i[-1] == 'TRUE') or (i[-1] == 'FALSE'):
            continue
        else:
            if len(i) > 3:
                molNames.append('_'.join([j.replace('/','-') for j in i[:-2]]))
                smiles.append(i[-1])
            elif len(i) == 3:
                molNames.append(i[0])
                smiles.append(i[2])
            else:
                print('something wrong with ', i, '.')
    
    #Writing the names of molecules in a file inside a separate directory
    #for future calculations
    if not os.path.exists('../../moleculeLists'):
        os.mkdir('../../moleculeLists')
    os.chdir('../../moleculeLists')
    with open("fileList.txt", 'w') as file:
        file.write('\n'.join(molNames))

    return [molNames, smiles]

