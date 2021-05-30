#!/bin/bash

my_sample_dir="Sample_folder" \
R1=$my_sample_dir"Sample_1.fq.gz" \
R2=$my_sample_dir"Sample_2.fq.gz" \
Output_dir="./Data/RNA_Star_2/Sample_folder_results/" \
mysample=$Output_dir"Sample2"

STAR --genomeDir "./DB/STAR_Rat_Index/" \
--sjdbGTFfile "./DB/gtf_file.gtf" \
--runThreadN 28 \
--readFilesIn <(zcat $R1) <(zcat $R2) \
--sjdbOverhang 149 \
--outSAMtype BAM SortedByCoordinate \
--quantMode GeneCounts \
--outFileNamePrefix $mysample