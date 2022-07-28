# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:38:58 2021

@author: dcs839
"""

### Rsem to count tables ###

## Import libs ##

import os

### Folder and Files ###

## Folders ##
folder = "Lists"
folder1 = folder+"/Samples/Sample1"


folder_out = folder+"/Count Table"

# if output folder doesn't exists, make one
if os.path.exists(folder_out):
    pass
else:
    os.mkdir(folder_out)

## Files ##

#biomart used here with 
#"Gene stable ID,Gene stable ID version,Transcript stable ID,Transcript stable ID version,Exon stable ID,Gene start (bp),Gene end (bp),Transcript length (including UTRs and CDS),Gene name,Transcript name,Transcript count"
#this could be reduced to Ensembl id + transcripts + Gene name #
file_biomart = "Rat_biomart.txt"

file1 = "rsem.genes.results"

file1_out = "Sample1_TPM.csv"

## Variables ##

biomart = {}

sample1_rsem_gene_ids = {}


### Read files ###

## Read biomart ##
with open(os.path.join(folder,file_biomart),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        #check if there is dublicates of Ensembl stable gene ids to gene conversion
        if line[0] in biomart:
            #if same, just pass
            if biomart[line[0]] == line[8].upper():
                pass
            else:
                #if not the same, print the scoundrel and break.
                print(line[0],biomart[line[0]],line[8])
                break
        else:
            #if not in dict, add to dict
            biomart[line[0]] = line[8].upper()
read.close


## Sample 1 ##

with open(os.path.join(folder1,file1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        #if TPM > 0, add to dict
        if float(line[5]) > 0:
            # Make sure there isnt dublicates
            if not line[0] in sample1_rsem_gene_ids:
                sample1_rsem_gene_ids[line[0]] = line[1:]
            else:
                print(line[0])
                break
read.close

### Save count table to file ###

## Sample 1 ##

with open(os.path.join(folder_out,file1_out),'w+') as out:
    #Add header
    out.write("Ensembl gene id;Ensembl transcripts;Gene Symbol;TPM\n")
    for key in sample1_rsem_gene_ids:
        if biomart[key] == '':
            out.write("{};{};Missing information;{}\n".format(key,sample1_rsem_gene_ids[key][0],sample1_rsem_gene_ids[key][4].replace(".",",")))
        else:
            out.write("{};{};{};{}\n".format(key,sample1_rsem_gene_ids[key][0],biomart[key],sample1_rsem_gene_ids[key][4].replace(".",",")))
out.close
