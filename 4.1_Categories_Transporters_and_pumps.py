# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:17:51 2021

@author: dcs839
"""

### Get transporters and pumps ###

### transport ###

### list from https://www.guidetopharmacology.org/ ###

## Import libs ##

import os

from operator import itemgetter

## folders ##


Folder1 = "Lists"
Folder2 = Folder1+"/Count Table"
Folder3 = "Results"
Folder4 = Folder3+"/Categories"
Folder5 = Folder4+"/Unfiltrated"


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

## Files ##
File_targets_and_families = "targets_and_families.csv"

File1 = "Sample1_TPM.csv"

File1_out = "Sample1_Transport_unfiltered.csv"

### Global variables ###

TPM_cutoff = "yes"
#TPM_cutoff = "no"

Transporter_list_RGD_symbols = []

transporters_TPM = {}
transporters_Genes = {}

Sorted_transporters = []

### load Transport list ###

with open(os.path.join(Folder1,File_targets_and_families),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split('","')
        if line[0] == '"transporter':
            if line[18]:
                if line[18].upper() not in Transporter_list_RGD_symbols:    
                    Transporter_list_RGD_symbols.append(line[18].upper())
                else:
                    pass
            else:
                pass
        else:
            pass
read.close

### load count tables ###

## Sample 1 ##

with open(os.path.join(Folder2,File1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        #convert TPM to float
        TPM = float(line[3].replace(",","."))
        if TPM_cutoff == "yes":
            #If TPM >= 0.5 add, else skip
            if TPM >= 0.5:
                if line[2] in Transporter_list_RGD_symbols:
                    transporters_TPM[line[0]] = TPM
                    transporters_Genes[line[0]] = line[2]
                else:
                    pass
            else:
                pass
        else:
            if line[2] in Transporter_list_RGD_symbols:
                transporters_TPM[line[0]] = TPM
                transporters_Genes[line[0]] = line[2]
            else:
                pass
read.close


### sort transport lists by value (TPM)
for key, value in sorted(transporters_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_transporters.append(key)

### Save unfiltrated transport lists to files ###

## Sample 1 ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File1_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_transporters:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,transporters_Genes[key],transporters_TPM[key],Rank))
out.close
