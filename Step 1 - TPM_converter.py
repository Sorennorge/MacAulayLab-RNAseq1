# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:14:17 2020

@author: dcs839
"""

###  TPM  Nomalization ####

## Import packages ##

import os

## Folders and Files ##

Folder1 = "Lookup_data"
Folder2 = "TPM"

File1 = "geneLength_Rnor.txt" #The gene length of rat genes
File2 = "Sample1ReadsPerGene.out.tab" #RNA STAR Quantmode output
File3 = "Sample1_TPM_counts.csv" #Rat genes with TPM count

## Global Variables ##

Gene_lengths = {}
Gene_counts = {}

## Load data ###

with open(os.path.join(Folder1,File1),'r') as read1:
    next(read1)
    for line in read1:
        line = line.strip().split(' ')
        Gene_lengths[line[0].replace('"','')] = float(line[-1])
read1.close

with open(os.path.join(Folder2,File2),'r') as read2:
    for line in read2:
        line = line.strip().split('\t')
        if not line[0].startswith("N_"):
            Gene_counts[line[0]] = float(line[2])
        else:
            pass
read2.close

## Variables ###

Sum_of_transcripts = 0.0
Transcript_list = {}
    
## Function ###
def transcripts(counts, lengths):
  rate = counts / lengths
  return(float(rate))


## Get transcripts and sum of all transcripts ##
for key in Gene_counts:
    if Gene_counts[key] > 0:
        trans = transcripts(Gene_counts[key],Gene_lengths[key])
        Sum_of_transcripts += trans
        Transcript_list[key] = trans
    else:
        pass

### TPM  ###
        
TPM = {}
for key in Transcript_list:
    TPM[key] = (Transcript_list[key]/Sum_of_transcripts*1e6)

### Write results ###
with open(os.path.join(Folder2,File3),'w+') as out:
    for key in TPM:
        out.write("{};{}\n".format(key,float(TPM[key])))
out.close