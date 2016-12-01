#!/bin/bash

set -euo pipefail

declare -a DEPENDENCIES=(git wget tar)
for prog in ${DEPENDENCIES[@]}; do if ! $(command -v ${prog} > /dev/null 2>/dev/null); then echo "Failed to find ${prog}, exiting..." >&2; exit 1; fi; done

ROOT=$(pwd -P)/examples
mkdir -P ${ROOT}

echo -e "Now downloading SAMTools, BioPython, and Scythe to ${ROOT}" >&2

#   Download SAMTools
echo "Downloading SAMTools" >&2
cd ${ROOT}
SAMTOOLS='samtools-1.3.1.tar.bz2'
(set -x; wget -O ${SAMTOOLS} https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2)
echo "Unpacking tarball" >&2
(set -x; tar -xjf ${SAMTOOLS})
echo "Cleaning up tarball" >&2
(set -x; rm -f ${SAMTOOLS})

#   Download BioPython
echo "Downloading BioPython" >&2
(set -x; git clone https://github.com/biopython/biopython.git)

#   Download Scythe
echo "Downloading Scythe" >&2
cd ${ROOT}
(set -x; git clone https://github.com/vsbuffalo/scythe.git)
