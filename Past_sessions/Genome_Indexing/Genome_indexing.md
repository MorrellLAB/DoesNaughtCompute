**Indexing of Genomic Data**


**Indexing by index program**

-[bcftools](http://samtools.github.io/bcftools/bcftools.html#index)
*   Indexing for VCF/BCF files
*   Install with bcftools
*   Can index chromosomes up to 2^29 in length with TBI (tabix index)
*   Defaults to CSI index, works for chromosomes up to 2^31

-[bgzip](http://www.htslib.org/doc/bgzip.html)
*   Install with htslib
*   Blocked compression and decompression
*   Is a special implementation of gzip
*   Will index VCF files
*   Can compress a VCF with bgzip and create an index at the same time!

-[BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi)
*   Indexing of a multi-fast file for rapid search

-[faidx](http://www.htslib.org/doc/faidx.html)
*   Install with samtools
*   Indexing for FASTA and FASTQ files

-[samtools](http://www.htslib.org/doc/samtools-index.html)
*   Can index sam, bam, or cram format
*   Also FASTA & FASTQ
*   Commands include `faidx`, `faqidx` or `index` for FASTA, FASTQ, or alignments
*   Also an `idxstats` command for BAM index stats
*   BAM indexing is perhaps most important
*   File is coordinate sorted and BGZIP-compressed
*   BAI index is default
*   CSI index has minimum interval size of 2^14, can adjust

-[tabix](https://www.htslib.org/doc/tabix.html) - indexing for tab-delimited files
*   Install with htslib
*   Can be used with BED and GFF tab-delimited lists
*   Also used for SAM and VCF files
*   Can create a CSI (coordinate-sorted index) format index for larger chromosomes
*   Can be combined with compression of file in [bgzip](http://www.htslib.org/doc/bgzip.html)


**Indexing by programs requiring an index**

-[ANGSD](http://www.popgen.dk/angsd/index.php/ANGSD)
*   BAM files must be indexed

-[bedtools](https://bedtools.readthedocs.io/en/latest/)
*   Requires indexed BAM files for some operations (multicov)
*   May use indexed FASTA or FASTQ files in places
*   Prefers tabix indexed BED and GFF

-[BWA](http://bio-bwa.sourceforge.net)
*   Requires an index of the reference genome

-[IGV](http://software.broadinstitute.org/software/igv/)
*   Essentially every file in IGV needs an index
*   IGV has some builtin indexing capability
    *   From the Tools menu can run pick “Run igvtools”;  “sort” or “index”

-[VeP](https://useast.ensembl.org/info/docs/tools/vep/index.html)
*   Requires indexing of GFF and fasta


**Indexing by file type**

*   BAM/SAM/CRAM
    *   samtools index

*   BED or BEDPE (and variants)
    *   Index with tabix

*   Fasta or fastq
    *   Index with faidx
    *   Typically indexed as .fai
    *   Also an index is needed by:
    *   IGV
    *   samtools

*   GFF
    *   Needs to be sorted
    *   Tabix indexing is typically really fast
    *   Index typically must in the same directory as the file

*   VCF
    *  Tabix
    *  .gzi
