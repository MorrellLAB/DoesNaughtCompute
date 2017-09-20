#!/bin/bash

# Basic commands to run ANNOVAR on your computer. I do not think this runs on
# Windows.

# Set these paths to the locations where you saved the required executable
# files. See links in the presentation for downloads.
GTF2GENEPRED=/path/to/gtfToGenePred
RETRIEVE=/path/to/retrieve_seq_from_fasta.pl
CONVERT=/path/to/convert2annovar.pl
ANNOVAR=/path/to/annotate_variation.pl

# Convert the GTF into 'genePred' format for predicting amino acid sequence
# impact.
${GTF2GENEPRED} -genePredExt Source_Files/Vrs1.gtf HV_refGene.txt
# Get the transcript sequences from the GTF, used for translating codons etc.
${RETRIEVE} --format refGene --seqfile Source_Files/morex_contig_135757.fasta --out HV_refGeneMrna.fa
# Convert the VCF into an ANNOVAR input file
${CONVERT} --format vcf4 --allsample --withfreq --includeinfo --outfile Vrs1_Annovar_in.txt Source_Files/Vrs1_Sample.vcf

# Move the HV_* files into a directory, called 'HV'. This is the ANNOVAR
# annotation database. As far as I know, the filenames have to be formatted
# in the weird way written into the output files above.
mkdir -p HV/
mv HV_* HV/

# Then annotate the variants
${ANNOVAR} --geneanno --dbtype refGene --buildver HV Vrs1_Annovar_in.txt HV/
