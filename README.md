# MacAulayLab RNAseq1 #
The work and scripts are done by the MacAulay Lab.\
All programs used are free and open-source.
In the interest of open science and reproducibility, all data and source code used in our research is provided here.\
Feel free to copy and use code, but please cite: (coming soon) and/or (coming soon) \
*Remember* rewrite file_names and folder_names suitable for your pipeline.\
Note: Many of the tables output have converted dot to comma for danish excel annotation.

## Raw data analysis - Library Build, Mapping and Quantification ##
*Remember* rewrite file_names and folder_names suitable for your pipeline.

### RNA-STAR and RSEM Library build and indexing ###
Use these two files:\
1.1.RNA_STAR_Indexing.sh\
2.1.RSEM_Indexing.sh

### RNA-STAR Mapping and RSEM quantification ###
Use:\
1.2.RNA_STAR_RNAseq1.sh\
2.2.RSEM_RNAseq1.sh
## Data analysis ##
### 3 - Count Tables with gene information ###
Requirements:\
Biomart of Rnor6.0 with Attributes: (was used)\
Gene stable ID,Gene stable ID version,Transcript stable ID,Transcript stable ID version,Exon stable ID,Gene start (bp),Gene end (bp),Transcript length (including UTRs and CDS),Gene name,Transcript name,Transcript count\
One could rewrite code and use (Gene stable ID,Gene name)\
Use:\
3.1_RSEM_to_count_tables.py

### 4 - Generate categories - transporters & pumps, and ion & water channels ###
Requirements:\
targets_and_families.csv (download: https://www.guidetopharmacology.org/DATA/targets_and_families.csv)\
Use:\
4.1_Categories_Transporters_and_pumps.py\
4.2_Water_and_ion_channels.py\

### 5 - GO-term information for filtration ###
Use:\
5.1_Generate_Filtration_list_for_Transporters_and_pumps.py\
5.2_Generate_Filtration_list_for_Ion_channels.py\

### 6 - Filtration based on GO-terms ###
Use:\
6.1_Filtration_Transporter_and_pumps.py\
6.2_Filtration_Ion_Channels.py\

### 7 - Filtration based on location - Membrane  ###
Use:\
7.1_Membrane_Transporters.py\
7.2_Membrane_water_and_ion_channels.py\

### 8 - Generate kinase list  ###
Requirements:\
XXXXX \
Use:\
8.1_Kinases.py
