#!/usr/bin/env python3

import sys
if sys.version_info.major is not 3:
    sys.exit("Please use Python 3 for this script")

import re

samples = [ 'TIL01.bam', 'TIL12.bam', 'WIL03.bam', 'TIL33.bam', 'PIL03.bam', 'HIL04.bam', 'TIL94.bam', 'TIL04.bam', 'TIL37.bam', 'TIL77.bam', 'WWL09.bam', 'WIL09.bam', 'TIL09.bam', 'TIL10.bam']

print(sorted(samples, key=lambda name : ''.join(re.findall(r'(\d+)', name))))
