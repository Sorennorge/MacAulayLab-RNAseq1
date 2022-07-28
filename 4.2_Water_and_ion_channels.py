# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:17:51 2021

@author: dcs839
"""

### Get transporters and pumps ###

### transport ###

### list from https://www.guidetopharmacology.org/ ###

import os

from operator import itemgetter

### Files and folders ###


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


File_targets_and_families = "targets_and_families.csv"

File1 = "Sample1_TPM.csv"

File1_out = "Sample1_Ion_Channels_unfiltered.csv"


### Global variables ###

TPM_cut_off = 'No'

Channel_list_RGD_symbols = []

Channel_TPM = {}
Channel_Genes = {}

Sorted_Channels = []


### load water and ion channel list ###

with open(os.path.join(Folder1,File_targets_and_families),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split('","')
        if line[0] == '"vgic' or line[0] == '"lgic' or line[0] == '"other_ic':
            if line[18]:
                if line[18].upper() not in Channel_list_RGD_symbols:    
                    Channel_list_RGD_symbols.append(line[18].upper())
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
        #If TPM > 0.5 add, else skip
        if TPM_cut_off == 'yes':
            if TPM >= 0.5:
                if line[2] in Channel_list_RGD_symbols:
                    Channel_TPM[line[0]] = TPM
                    Channel_Genes[line[0]] = line[2]
                else:
                    pass
            else:
                pass
        else:
            if line[2] in Channel_list_RGD_symbols:
                Channel_TPM[line[0]] = TPM
                Channel_Genes[line[0]] = line[2]
            else:
                pass
read.close


### sort channel list by value (TPM)
for key, value in sorted(Channel_TPM.items(), key = itemgetter(1,1), reverse = True):
    Sorted_Channels.append(key)

### Save unfiltrated channel list to file ###

## Sample 1 ##

# Ranking variable initialization #
Rank = 0 

# Save file (sorted based on TPM)
with open(os.path.join(Folder5, File1_out),'w+') as out:
    out.write("Ensembl_id;Gene;TPM;Rank\n")
    for key in Sorted_Channels:
        Rank += 1
        out.write("{};{};{};{}\n".format(key,Channel_Genes[key],Channel_TPM[key],Rank))
out.close