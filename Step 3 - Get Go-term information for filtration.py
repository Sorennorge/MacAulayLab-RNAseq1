# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:03:46 2020

@author: dcs839
"""

## Import Packages ##
import mygene
import os

## Import lookup table function ##
mg = mygene.MyGeneInfo()

## Folders and Files ##

Folder1 = "Lookup data"
Folder2 = "TPM"

File1 = "GO_term_information_file.csv"
File2 = "Information_collection_file.csv"
File3 = "Sample_TPM_Counts.csv"

    
#variables

Ensemble_list = []
Info_list = {}
Gene_list = []

#import lookup file

with open(os.path.join(Folder2,File3),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Gene_list.append(line[0].lower())
read.close

with open(os.path.join(Folder1,File2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if line[1].lower() in Gene_list:
            Ensemble_list.append(line[0])
read.close

#Initialize progress counter
counter = 0

## Program ##
with open(os.path.join(Folder1,File1),'w+',encoding="utf-8") as out:
    out.write("ID;BP;CC;MF\n")
    for key in Ensemble_list:
        #progress info
        counter += 1
        print("{} - {}/{}".format(key,counter,len(Ensemble_list)))
        ### Get lookup values ###
        #Initialize
        lookup = []

        Info_list[key] = {}
        
        try:
            lookup = mg.getgene(key)
        except:
            print("Case 2: {}".format(key))
            break
        ### Initialize dicts ###
        
        ## Info_list ##
        Info_list[key] = {}
        Info_list[key]['BP'] = []
        Info_list[key]['CC'] = []
        Info_list[key]['MF'] = []

        
        ## Complete info list ##
        if not lookup:
            out.write("{};;;;;;\n".format(key))
            continue
        
        ### Handle Go terms ###
        if lookup:
            if 'go' in lookup.keys():
                ### Handle BP ###
                if 'BP' in lookup['go']:
                    if lookup['go']['BP']:
                        if not 'term' in lookup['go']['BP']:
                            for item in lookup['go']['BP']:
                                if 'term' in item:
                                    if item['term'].lower() not in Info_list[key]['BP']:
                                        Info_list[key]['BP'].append(item['term'].lower())
                        else:
                            if lookup['go']['BP']['term'].lower() not in Info_list[key]['BP']:
                                Info_list[key]['BP'].append(lookup['go']['BP']['term'].lower())
                    else:
                        pass
                else:
                    pass
                ### Handle CC ###
                if 'CC' in lookup['go']:
                    if lookup['go']['CC']:
                        if not 'term' in lookup['go']['CC']:
                            for item in lookup['go']['CC']:
                                if 'term' in item:
                                    if item['term'].lower() not in Info_list[key]['CC']:
                                        Info_list[key]['CC'].append(item['term'].lower())
                        else:
                            if lookup['go']['CC']['term'].lower() not in Info_list[key]['CC']:
                                Info_list[key]['CC'].append(lookup['go']['CC']['term'].lower())
                    else:
                        pass
                else:
                    pass
                ### Handle MF ###
                if 'MF' in lookup['go']:
                    if lookup['go']['MF']:
                        if not 'term' in lookup['go']['MF']:
                            for item in lookup['go']['MF']:
                                if 'term' in item:
                                    if item['term'].lower() not in Info_list[key]['MF']:
                                        Info_list[key]['MF'].append(item['term'].lower())
                        else:
                            if lookup['go']['MF']['term'].lower() not in Info_list[key]['MF']:
                                Info_list[key]['MF'].append(lookup['go']['MF']['term'].lower())
                    else:
                        pass
                else:
                    pass
                
        ### Save to file ###
        if lookup:
            out.write("{};{};{};{}\n".format(key,"||".join(Info_list[key]['BP']),"||".join(Info_list[key]['CC']),"||".join(Info_list[key]['MF'])))
        else:
            pass
out.close
