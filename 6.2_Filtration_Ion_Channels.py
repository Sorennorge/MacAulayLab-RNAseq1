# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:24:14 2021

@author: dcs839
"""

### Transport filtration ###


## import libs ##

import os

### Folder and files ###

## Folders ##

folder1 = "Lists/Filtration lists"
folder2 = "Results/Categories/Unfiltrated"
folder3 = "Results/Categories/Filtrated"

if os.path.exists(folder3):
    pass
else:
    os.mkdir(folder3)

## Files ##

Filtration_list = "Filtration_list_ion_channels.csv"

# Files input #
Sample1_file = "Sample1_Ion_Channels_unfiltered.csv"


# Files output #
Filtered_file = "Sample1_Ion_channels_Membrane_filtered.csv"


## Global variables ##

Sample1_genes = {}


Genes_of_interest_Sample1 = {}


## Sample 1 ##
with open(os.path.join(folder2,Sample1_file),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Sample1_genes[line[0]] = line[1]
read.close


with open(os.path.join(folder1,Filtration_list),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(';')
    
        ## Sample 1 - FACS - membrane filtration ##
        
        if line[0] in Sample1_genes:
            # If Cellular Component (CC) is empty - Add empty tag
            if line[1] == '':
                Genes_of_interest_Sample1[line[0]] = 'Empty tag'
            # If Cellular Component (CC) contains plasma membrane tag - add Plasma membrane tag 
            elif "integral component of plasma membrane".upper() in line[1].upper() or "plasma membrane".upper() in line[1].upper():
                Genes_of_interest_Sample1[line[0]] = 'Plasma membrane tag'
            # If Cellular Component (CC) contains membrane tag, but is not part of lysosome, endosome, mitochondrial,gologi, vacular - add Filtered tag
            elif ("integral component of membrane".upper() in line[1].upper() or "membrane".upper() in line[1].upper() or "transmembrane".upper() in line[1].upper()):
                if not ("lysosome".upper() in line[1].upper() or "endosome membrane".upper() in line[1].upper() or "lysosomal".upper() in line[1].upper()):
                    if not ("mitochondrion".upper() in line[1].upper() or "mitochondrial".upper() in line[1].upper()):
                        if not ("golgi apparatus".upper() in line[1].upper() or "vacuolar".upper() in line[1].upper() or "endoplasmic".upper() in line[1].upper()):
                            Genes_of_interest_Sample1[line[0]] = 'Filtered tag'
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
read.close


### Save filtered lists to files ###

## Sample 1 - filtered ##
with open(os.path.join(folder3,Filtered_file),'w+') as out:
    out.write("Ensembl id;Gene;Filtration tag\n")
    for key in Genes_of_interest_Sample1:
        out.write("{};{};{}\n".format(key,Sample1_genes[key],Genes_of_interest_Sample1[key]))
out.close

