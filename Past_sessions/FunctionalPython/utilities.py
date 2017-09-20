#!/usr/bin/env python3

import sys
import re

formatFasta = lambda sequence : re.sub(r'\n', '', sequence).upper()

def setup():
    try:
        sequence_1 = open('Zea_mays.fasta').read()
        sequence_2 = open('Zea_Mays_Tail.fasta').read()
        sequence_3 = open('Zea_Mays_Weird.fasta').read()
    except FileNotFoundError:
        sys.exit("Failed to find FASTA files!")
    sequences = list(map(formatFasta, [sequence_1, sequence_2, sequence_3]))
    return(sequences)


def showAT(AT_Contents):
    for i in range(len(AT_Contents)):
        print("AT content of Sequence " + str(i) + ": " + str(AT_Contents[i]))