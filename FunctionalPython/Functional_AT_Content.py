#!/usr/bin/env python3

import utilities # Import user-defined module

sequences = utilities.setup() # Setup or list of sequences

checkAT = lambda base : base == 'A' or base == 'T' # Lambda expression to check a single base to see if we have an 'A' or a 'T'
getAT = lambda sequence : round(sum(map(checkAT, sequence))/len(sequence)*100, 2) # A lambda expression that maps the first lambda expression to a sequence. Since Python converts `True' to 1 and `False' to 0, we use `sum' to add up all of the `Trues', divide it by the length of the sequence, converts it to a percentage, and rounds to two decimal places
allAT = list(map(getAT, sequences)) # Map the second lambda expression to all sequences provided and make a list out of it

utilities.showAT(allAT) # Special `print' wrapper that makes the AT content all nice and pretty
