#!/usr/bin/env python3

import utilities # User defined module, has functions to read in data and display it properly

sequences = utilities.setup() # Read in our data and return a list of three sequences

ATcontent = [] # Create a new list to hold AT content for our sequences

for seq in sequences: # For every sequence in our list of sequences
    thisAT = 0 # Start a counter for the AT content of this sequence
    for base in seq: # For every base in our sequence
            if base == 'A' or base == 'T': # If the base is an 'A' or 'T'
                    thisAT += 1 # Add one to our AT content counter
    thisAT = round(thisAT / len(seq) * 100.0, 2) # Change our AT counter to reflect percent AT
    ATcontent.append(thisAT) # Append the percent AT to our AT content list

utilities.showAT(ATcontent) # Print the AT content to the screen all pretty-like
