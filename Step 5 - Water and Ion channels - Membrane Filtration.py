# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:37:04 2021

@author: dcs839
"""

### Water and ion channel membrane filtration ###

import os

#Folder and files

folder1 = "Lookup data"
folder2 = "Results/Categories/Water and Ion channels"

file_go_term = "GO_term_information_file.csv"

file_input = "Water_and_Ion_channels.csv"
Filtered_file = "Water_and_Ion_channels_Menbrane_filtered.csv"

#Variables

Genes_of_interest = {}
Rat_genes = []
Info_genes = {}

#read files

with open(os.path.join(folder2,file_input),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Rat_genes.append(line[0])
read.close

with open(os.path.join(folder1,file_go_term),'r') as read:
     next(read)
     for line in read:
         line = line.strip().split(";")
         Info_genes[str(line[1]).upper()] = str(line[3])
read.close

#Membrane Filtration analysis

with open(os.path.join(folder1,file_go_term),'r') as read2:
    next(read2)
    for line in read2:
        line = line.strip().split(';')
        if line[1].upper() in Rat_genes:
            if line[3] == '':
                Genes_of_interest[line[1].upper()] = 'Empty tag'
            elif "integral component of plasma membrane".upper() in line[3].upper() or "plasma membrane".upper() in line[3].upper():
                Genes_of_interest[line[1].upper()] = 'Plasma membrane tag'
            elif ("integral component of membrane".upper() in line[3].upper() or "membrane".upper() in line[3].upper() or "transmembrane".upper() in line[3].upper()):
                if not ("lysosome".upper() in line[3].upper() or "endosome membrane".upper() in line[3].upper() or "lysosomal".upper() in line[3].upper()):
                    if not ("mitochondrion".upper() in line[3].upper() or "mitochondrial".upper() in line[3].upper()):
                        if not ("golgi apparatus".upper() in line[3].upper() or "vacuolar".upper() in line[3].upper() or "endoplasmic".upper() in line[3].upper()):
                            Genes_of_interest[line[1].upper()] = 'Filtered tag'
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
read2.close

#Write results

Header = "Gene;TPM;Rank;Filter Tag\n" #initialize header

with open(os.path.join(folder2,Filtered_file),'w+') as out:
    out.write(Header)
    with open(os.path.join(folder2,file_input),'r') as read:
         next(read)
         for line in read:
             line = line.strip().split(";")
             if line[0].upper() in Genes_of_interest:
                 out.write("{};{};{}\n".format(line[0],";".join(line[1:]),Genes_of_interest[line[0].upper()]))
             else:
                 pass
    read.close
out.close