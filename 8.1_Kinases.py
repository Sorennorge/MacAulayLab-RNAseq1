# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:11:35 2021

@author: dcs839
"""

### Kinases ###

### Kinases ###

import os

from operator import itemgetter

### Files and folders ###


Folder1 = "Lists"
Folder2 = "Lists/Count Table"
Folder3 = "Results"
Folder4 = "Results/Categories"
Folder5 = "Results/Categories/Kinases"


if not os.path.exists(Folder3):
    os.mkdir(Folder3)
else:
    pass

if not os.path.exists(Folder4):
    os.mkdir(Folder4)
else:
    pass

if not os.path.exists(Folder5):
    os.mkdir(Folder5)
else:
    pass

Kinase_list_file = "RegPhos_kinase_rat.txt"

File3_Male = "Sample1_TPM.csv"

File3_out = "Sample1_Kinases.csv"


### Global variables ###

Kinase_list_ensembl = []

kinases_TPM = {}
kinases_Genes = {}

Sorted_Male_kinases = []

### load Transport list ###

with open(os.path.join(Folder1,Kinase_list_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip()
        Kinase_list_ensembl.append(line)
read.close

### load count tables ###

## Sample 3 - Male ##

with open(os.path.join(Folder2,File3_Male),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        #convert TPM to float
        TPM = float(line[3].replace(",","."))
        #If TPM > 0.5 add, else skip
        if TPM >= 0.5:
            if line[0] in Kinase_list_ensembl:
                kinases_TPM[line[0]] = TPM
                kinases_Genes[line[0]] = line[2]
            else:
                pass
        else:
            pass
read.close

### sort transport lists by value (TPM)

for key, value in sorted(kinases_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_Male_kinases.append(key)
    
### Save unfiltrated transport lists to files ###

## Sample 3 - Male ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File3_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_Male_kinases:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,kinases_Genes[key],kinases_TPM[key],Rank))
out.close
