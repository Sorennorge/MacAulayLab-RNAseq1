# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:35:34 2021

@author: dcs839
"""

### Get Water and Ion channels ###

### Water and ion channels ###

### list from https://www.guidetopharmacology.org/ ###

import os

from operator import itemgetter

### Files and folders ###


Folder1 = "Lists"
Folder2 = "TPM"
folder3_1 = "Results"
Folder3_2 = "Results/Categories"
Folder3_3 = "Results/Categories/Ion and Water channels"


if not os.path.exists(folder3_1):
    os.mkdir(folder3_1)
else:
    pass

if not os.path.exists(Folder3_2):
    os.mkdir(Folder3_2)
else:
    pass

if not os.path.exists(Folder3_3):
    os.mkdir(Folder3_3)
else:
    pass



File1 = "targets_and_families.csv"
File2 = "Sample_TPM_counts.csv"
File3 = "Information_collection_file.csv"
File1_out = "Water_and_Ion_channels.csv"


### load Channel list ###

Header_flag = 1

RGD_id = {}
RGD_symbol = []

with open(os.path.join(Folder1,File1),'r') as read:
    for line in read:
        line = line.strip().split('","')
        if Header_flag == 1:
            Header = line
            Header_flag = 0
        else:
            if line[0] == '"vgic' or line[0] == '"lgic' or line[0] == '"other_ic':
                if line[18]:
                    RGD_symbol.append(line[18].lower())
                else:
                    pass
            else:
                pass
read.close

RGD_symbol_sorted = list(set(RGD_symbol))


#Global variables

Information_dict = {}
Channel_dict = {}
Sorted_Channel_list = []
Sorted_Information_dict = []

#load file

with open(os.path.join(Folder2,File2),'r') as read1:
    next(read1)
    for line in read1:
        line = line.strip().split(";")
        Information_dict[line[0]] = float(line[1])
read1.close

with open(os.path.join(Folder1,File3),'r') as read1:
    next(read1)
    for line in read1:
        line = line.strip().split(";")
        if line[1].lower() in RGD_symbol_sorted:
            Channel_dict[line[1].upper()] = line[2]        
read1.close

Gene_max = max(Information_dict.values())
Gene_min = min(Information_dict.values())


#sort lists by value
for key, value in sorted(Information_dict.items(), key = itemgetter(1), reverse = True):
    Sorted_Information_dict.append(key)

Placing_list = {}

for key in Channel_dict:
    if key in Information_dict:
        Placing_list[key] = int(Sorted_Information_dict.index(key))

Placing_sorted = sorted(Placing_list.items(), key=itemgetter(1))


Rank = 0
with open(os.path.join(Folder3_3, File1_out),'w+') as oot:
    oot.write("Gene;TPM;Rank\n".format(len(Information_dict)))
    for key in Placing_sorted:
        Rank += 1
        if Information_dict[key[0]] > 1:
            oot.write("{};{};{}\n".format(key[0].upper(), str(round(Information_dict[key[0]],1)).replace(".",","),Rank))
        else:
            oot.write("{};{};{}\n".format(key[0].upper(), str(round(Information_dict[key[0]],4)).replace(".",","),Rank))
oot.close