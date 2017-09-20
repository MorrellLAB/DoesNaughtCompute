#!/usr/bin/env python3

import sys
import os

#   Setup our example sequence
def setup():
    '''This function reads in a fasta sequence and prepares it for the Introduction to Python tutorial for Does[0]Compute?'''
    try: # Try to read in our test file
        fasta = open('Zea_mays.fasta', 'r')
    except FileNotFoundError: # If it's not there, exit with error
        sys.exit("Failed to find fasta file, are we in the 'Introduction_to_Python' directory?")
    header = fasta.readline() # Get the header line from the fasta file
    sequence = '' # Create an empty sequence
    for line in fasta: # For every line in our fasta file
        line = line.strip('\n') # Get rid of new lines
        sequence += line # Add the line to the sequence
    seq50 = sequence[:50]
    return(header, sequence, seq50)


#   Make translation tables and dictionaries
def make_trans():
    '''This function make a nucleotide translation table and a dictionary representing the codon table'''
    nuc_dict = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    prot_dict = {
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
        'UGU': 'C', 'UGG': 'W', 'UGA': 'Stop', 'UGC': 'C',
    }
    nuc_tab = str.maketrans(nuc_dict)
    return(nuc_tab, prot_dict)


#   Check the RNA sequence
def check_RNA(RNA_sequence):
    '''This function checks to see if the DNA sequence was properly converted to a complementary RNA sequence'''
    if RNA_sequence.find('AUG') == 32:
        print("Good job, you sucessfully converted the DNA sequence into it's complementary RNA sequence!")
    elif RNA_sequence.find('TAC') == 32:
        sys.exit("You reversed your sequence, but didn't convert it to RNA. Try again")
    elif RNA_sequence.find('GUA') == 345:
        sys.exit("You converted your sequence to RNA, but didn't reverse it. Try again")
    else:
        sys.exit("The DNA sequence was neither converted to RNA nor reversed. Try again")


#   Check the protein sequence
def check_protein(protein_sequence):
    '''This function checks to see if the RNA sequence was translated into the proper protein sequence'''
    if 'Stop' in protein_sequence:
        sys.exit("We found a stop codon in your protein sequence!")
    if protein_sequence[0] == 'M':
        print("Good job, your protein starts with a methionine!")
    else:
        sys.exit("Your protein does not start with a methionine; make sure you're starting your protein sequence at the start codon")
    if len(protein_sequence) == 6:
        print("Good job, your protein sequence is the correct length!")
    elif len(protein_sequence) > 6:
        sys.exit("Your protein sequence is too long!")
    else:
        sys.exit("Your protein sequence is too short!")

