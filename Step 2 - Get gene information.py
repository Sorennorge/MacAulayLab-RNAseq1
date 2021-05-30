# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:19:44 2020

@author: dcs839
"""

## Import Packages ##
import mygene
import os

## Import lookup table function ##
mg = mygene.MyGeneInfo()

## Folders and Files ##

Folder1 = "Sample folder"
Folder2 = "Lookup data"

File1 = "Sample_TPM_Counts.csv" #TPM counts from step 1
File2 = "Information_collection_file.csv" #The infomation collection file

#Create output folder if it doesn't exist
if not os.path.exists(Folder2):
    os.makedirs(Folder2)
    
#variables

Ensemble_list = []
Info_list = {}

#import lookup file
with open(os.path.join(Folder1,File1),'r') as read:
    for line in read:
        line = line.strip().split(";")
        Ensemble_list.append(line[0])
read.close

#Initialize progress counter
counter = 0

## Program ##
with open(os.path.join(Folder2,File2),'w+',encoding="utf-8") as out:
    out.write("ID;Gene;Name;Alias;Function;Go terms;summary\n")
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
        Info_list[key]['symbol'] = []
        Info_list[key]['alias'] = []
        Info_list[key]['name'] = []
        Info_list[key]['pathway'] = []
        Info_list[key]['go'] = []
        Info_list[key]['summary'] = []
        
        ## Complete info list ##
        if not lookup:
            out.write("{};;;;;;\n".format(key))
            continue

        ### Handle Symbol ###
        if lookup:
            if 'symbol' in lookup.keys():
                if isinstance(lookup['symbol'],str):
                    Info_list[key]['symbol'].append(lookup['symbol'])
                elif isinstance(lookup['symbol'],list):
                    for item in lookup['symbol']:
                        Info_list[key]['symbol'].append(item)
            else:
                pass
        else:
            pass
        
        ### Handle Alias ###
        if lookup:
            if 'alias' in lookup.keys():
                if isinstance(lookup['alias'],str):
                    Info_list[key]['alias'].append(lookup['alias'])
                elif isinstance(lookup['alias'],list):
                    for item in lookup['alias']:
                        Info_list[key]['alias'].append(item)
            else:
                pass
        else:
            pass
        
        ### Handle Names ###
        if lookup:
            if 'name' in lookup.keys():
                if isinstance(lookup['name'],str):
                    Info_list[key]['name'].append(lookup['name'].replace(';',','))
                elif isinstance(lookup['name'],list):
                    for item in lookup['name']:
                        Info_list[key]['name'].append(item.replace(';',','))
            else:
                pass
        else:
            pass
        
        ### Handle Function ###
        if lookup:
            if 'pathway' in lookup.keys():
                if 'reactome' in lookup['pathway']:
                    if 'name' in lookup['pathway']['reactome']:
                        Info_list[key]['pathway'].append(lookup['pathway']['reactome']['name'])
                    elif len(lookup['pathway']['reactome']) > 1:
                        for item in lookup['pathway']['reactome']:
                            Info_list[key]['pathway'].append(item['name'])
            else:
                pass
        
        ### Handle Go terms ###
        if lookup:
            if 'go' in lookup.keys():
                for category in lookup['go']:
                        if 'term' not in lookup['go'][category]:
                            for item in lookup['go'][category]:
                                if item['term'].lower() not in Info_list[key]['go']:
                                    Info_list[key]['go'].append(item['term'].lower())
                        else:
                            Info_list[key]['go'].append(lookup['go'][category]['term'].lower())
        else:
            pass

        
        ### Handle Summary ###
        if lookup:
            if 'summary' in lookup.keys():
                if isinstance(lookup['summary'],str):
                    Info_list[key]['summary'].append(lookup['summary'].replace(';',','))
                elif isinstance(lookup['summary'],list):
                    for item in lookup['summary']:
                        Info_list[key]['summary'].append(item.replace(';',','))
            else:
                pass
        else:
            pass
        ### Save to file ###
        if lookup:
            out.write("{};{};{};{};{};{};{}\n".format(key,"||".join(Info_list[key]['symbol']),"||".join(Info_list[key]['name']),"||".join(Info_list[key]['alias']),"||".join(Info_list[key]['pathway']),"||".join(Info_list[key]['go']),"||".join(Info_list[key]['summary'])))
        else:
            pass
out.close