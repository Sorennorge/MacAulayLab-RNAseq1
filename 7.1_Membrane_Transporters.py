# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 12:38:16 2021

@author: dcs839
"""

### List of membrane ion channels ###

## import libs ##

import os

### Folder and files ###

## Folders ##

folder1 = "Results/Categories/Unfiltrated"
folder2 = "Results/Categories/Filtrated"
folder3 = "Results/Categories/Transporter and pumps"

if os.path.exists(folder3):
    pass
else:
    os.mkdir(folder3)

## Files ##
    
Filtered_file = "Sample1_Transport_Membrane_filtered.csv"
Unfiltered_file = "Sample1_Transport_unfiltered.csv"

File_out = "Membrane_Transporter_and_pumps.csv"

## Variables ##

Gene_list = []
Info_dict = {}

## Sample 1 - filtered ##
with open(os.path.join(folder2,Filtered_file),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Gene_list.append(line[1])
read.close

## Sample 1 - information from unfiltered ##
with open(os.path.join(folder1,Unfiltered_file),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Info_dict[line[1]] = [line[0],line[2]]
read.close

Rank = 0
with open(os.path.join(folder3,File_out),'w+') as out:
    out.write("Ensembl ID;Gene Symbol;TPM;Rank\n")
    for key in Gene_list:
        Rank += 1
        out.write("{};{};{};{}\n".format(Info_dict[key][0],key,Info_dict[key][1],Rank))
out.close
        