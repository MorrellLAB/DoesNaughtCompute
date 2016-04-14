#!/usr/bin/env python3

import utilities

sequences = utilities.setup()

ATcontent = []

for seq in sequences:
    thisAT = 0
    for base in seq:
            if base == 'A' or base == 'T':
                    thisAT += 1
    thisAT = round(thisAT / len(seq) * 100.0, 2)
    ATcontent.append(thisAT)

utilities.showAT(ATcontent)
