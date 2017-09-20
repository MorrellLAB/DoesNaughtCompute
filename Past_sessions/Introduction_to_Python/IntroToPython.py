#!/usr/bin/env python3

#   Import modules from the standard Python library
import re # Import the regex module, this is for something later on

#   Import user defined modules
import utilities

#   Setup our data and get some translation tables
header, sequence, seq50 = utilities.setup()
nucleotide_table, protein_dictionary = utilities.make_trans()

#   We have a fasta file containing a region of chromosome 10 of Zea mays
#   There are several things that this code will do once complete

print("The first 50 nucleotides of this FASTA sequence are:")
print(seq50)
print("\n")

#   First, the sequence is in lowercase; convert the sequence to all uppercase and print off the first 50 nucleotides
#       Use the upper method of the string `sequence' to do this; store this as the variable sequence
#       Remember: Python starts counting at 0 and slices are partially inclusive

# Use the upper method to change the sequence in to uppercase

print("The first 50 nucleotides in upper case are:")
# Print the first 50 nucleotides of the sequence in uppercase
print("\n")


#   Second, is to get the length of the sequence using the `len()' function
print("The length of the sequence is:")
# Print the length of the sequence
print("\n")

#   Third, we're going to get GC content of the sequence
#   Do this using a for loop and an if statement

GC = 0 # A variable to hold the number of 'G's and 'C's we find in our sequence
#   Use a for loop and an if statement to find the number of 'G's and 'C's in our sequence

#   Calculate the percent of all nucleotides that are 'G' or 'C'
#   Remember, `GC' is an integer type, we can do division using the '/' operator
GC_content = # Store the GC content here
print("The GC content of this sequence is: " + str(round(GC_content, 1)))
print("\n")


#   Fourth, convert this DNA sequence into it's complementary RNA sequence and print the last 50 nucleotides
#   Use the translate *method* of the string `sequence' to conver from DNA nucleotides to RNA nucleotides
#   The translate method takes one argument, a translation table
#   The translation table has been made for you, it's called `nucleotide_table'
#   Remember to reverse the sequence, otherwise your RNA sequence will be backwards
#   Hint: use a slice to reverse the sequence

# Use the translate method of the string `sequence' to convert your DNA sequence into RNA, don't forget to reverse the sequence to get the complementary sequence!

print("The last 50 nucleotides of the RNA sequence are:")
# Print the last 50 nucleotides of the RNA sequence
print("We're now checking if this is correct...")
utilities.check_RNA(RNA_sequence) # We're checking your work...
print("\n")


#   Finally, write a function to translate an RNA sequence into a protein sequence
#   We recommend solving this problem in YY steps:
#       First, figure out where the start codon occurs in the RNA sequence
#           Do this using the find method of strings
#           This takes a query string as an argument and outputs the position where that starts
#       Next, create a new sequence that starts at this position, use a slice for this
#       The next step is to split the sequence up into codons
#           We've taken care of this for you, as it involves regular expressions
#           The output of this step is a list of codons
#       Finally, use a for loop to iterate over the codon list and translate each codon into an amino acid
#           This amino acid should be appended to the full protein sequence
#           All codon:amino acid pairs are stored in the `protein_dictionary' dictionary
#           You can search for an amino acid given a codon with the following command: 'protein_dictionary[codon]
#           Be aware: some of the codons in the dictionary are Stop codons: these are written as 'Stop'
#           Make sure that you check to see if the codon is a stop codon or not before adding it to the protein sequence

#   Convert an RNA sequence into a protein sequence
def RNA_to_Protein(RNA):
    '''This function converts an RNA sequence into a protein sequence'''
    protein = '' # An empty string to hold the protien sequence
    # Get the start position of the translated region
    # Get sequence above the 5' untranslated region
    byCodon = re.compile(r'...', re.M) # A regex object to split our sequence into codons
    sequence_in_codons = byCodon.findall(translated_sequence) # Get the sequence as a list of codons
    # Create a for loop to look up each codon in the protein dictionary and add the amino acid to the protein sequence
    #   Remember to check for stop codons
    return(protein) # Return the protein sequence


#   Run your function, and check the results
protein_sequence = RNA_to_Protein(RNA_sequence)
print("Your protein sequence is:")
print(protein_sequence)
print("We're now checking if your protein sequence is correct...")
utilities.check_protein(protein_sequence) # We're now checking your protein sequence

print("\n")
print("Congratulations! You've successfully completed the introduction to Python!")
