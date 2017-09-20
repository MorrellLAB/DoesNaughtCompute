<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# SAMtools, Picard Tools, and sambamba part II
---

##### Does[0]compute?

##### November 17th, 2016

Colin Pierce

***

Before we begin, we need to get all of the SAM files and access our modules:

- Log in to MSI

```bash
ssh x500@login.msi.umn.edu

ssh pier0273@login.msi.umn.edu
```

- SSH into Lab in order to access available modules

```bash
ssh lab
```

- Now let's clone the git repository containing the SAM and FASTA files

```bash
git clone /panfs/roc/groups/9/morrellp/public/example-sam/

cd example-sam
```

```bash
ls
```

![](https://github.com/cpthrash/simulation_projects/blob/master/Screen%20Shot%202016-11-17%20at%208.55.18%20AM.png?raw=true)

***

# To reacp from last week: What are SAMtools, Picard, and sambamba used for?
---

![](https://github.com/cpthrash/simulation_projects/blob/master/NGS_handling.png?raw=true)

***


# To reacp from last week: What are samtools, Picard, and sambamba used for?
---

![](https://github.com/cpthrash/simulation_projects/blob/master/NGS_handling.png?raw=true)


- Interacting with and processing DNA sequence read alignments
- SAM files: 10GB or more, stores sequences aligned to a reference sequence
- SAM files: Human readable
- BAM files: Binary equivalent of SAM files, compressed, not human readable
- Some functions:
    - Variant calling
    - Sort and indx files
    - Alignment summaries
    - Compare SAM/BAM files

***

# What can we do with SAMtools?
---

![](https://github.com/cpthrash/simulation_projects/blob/master/samtools.png?raw=true)

***

# SAMtools: Syntax and examples
---

- Load a more recent version of SAMtools:

```bash
module load samtools
```

- Confirm you have SAMtools version 1.3 loaded:

```bash
samtools
```

- SAMtools commands are invoked as:

```bash
samtools some_command
```
***

# SAMtools: SAM and BAM files
---

First, let's look at a SAM file

```bash
vim IA3023.sam
```
***

# SAMtools: SAM and BAM files
---

![](https://github.com/cpthrash/simulation_projects/blob/master/SAM%20File%20Image.png?raw=true)

***

# SAMtools: SAM and BAM files
---

 Now let's do the actual converion

```bash
# Convert a SAM file to a BAM file, -b option compresses or leaves compressed data
samtools view -bS sample.sam > sample.bam
```

Once you can see the BAM file, go ahead and view it

***

# SAMtools: SAM and BAM files
---

What does a BAM file look like?

![](https://github.com/cpthrash/simulation_projects/blob/master/Bam%20File%20image.png?raw=true)

***

# SAMtools: Sorting a BAM file
---

```bash
# Read the specified unsorted_in.bam as input, sort it by aligned read position, and write it out to sorted_out.bam, the bam file whose name (without extension) was specified.
samtools sort unsorted_in.bam sorted_out
```

***

# SAMtools: Index a BAM file
---

```bash
# Creates an index file, sorted.bam.bai for the sorted.bam file.
samtools index sorted.bam
```

***

# SAMtools: Get simple alignment statistics

```bash
# Does a full pass through the input file to calculate and print statistics to stdout.
samtools flagstat in.bam
```

Does a full pass through the input file to calculate and print statistics to stdout.

Provides counts for each of 13 categories based primarily on bit flags in the FLAG field. Each category in the output is broken down into QC pass and QC fail, which is presented as "#PASS + #FAIL" followed by a description of the category.

The first row of output gives the total number of reads that are QC pass and fail (according to flag bit 0x200). For example:

122 + 28 in total (QC-passed reads + QC-failed reads)

Which would indicate that there are a total of 150 reads in the input file, 122 of which are marked as QC pass and 28 of which are marked as "not passing quality controls"

Following this, additional categories are given for reads which are:

secondary
0x100 bit set

supplementary
0x800 bit set

duplicates
0x400 bit set

mapped
0x4 bit not set

paired in sequencing
0x1 bit set

read1
both 0x1 and 0x40 bits set

read2
both 0x1 and 0x80 bits set

properly paired
both 0x1 and 0x2 bits set and 0x4 bit not set

with itself and mate mapped
0x1 bit set and neither 0x4 nor 0x8 bits set

singletons
both 0x1 and 0x8 bits set and bit 0x4 not set

And finally, two rows are given that additionally filter on the reference name (RNAME), mate reference name (MRNM), and mapping quality (MAPQ) fields:

with mate mapped to a different chr
0x1 bit set and neither 0x4 nor 0x8 bits set and MRNM not equal to RNAME

with mate mapped to a different chr (mapQ>=5)
0x1 bit set and neither 0x4 nor 0x8 bits set and MRNM not equal to RNAME and MAPQ >= 5

***

# SAMtools: Read depth

```bash
# Let's say we only want to look at reads with base quality of a certain score or higher in a certain region of chromosome 2
# We'll use the flag -q for for base quality
# We'll use the flag -r to sepcify the chromosome and region <Chr:FROM-TO>
samtools depth -q 1 -r Chr02:10000-20000 sorted_in.bam
```

Now try another, higher Q score and see if you get a different result

***

# Picard Tools
---

What can we do with Picard Tools?

![](https://github.com/cpthrash/simulation_projects/blob/master/Picard.png?raw=true)

Basic Picard Tools syntaz:

```bash
java jvm-args -jar picard.jar PicardToolName OPTION1=value1 OPTION2=value2...

java -Xmx2g -jar $CLASSPATH/picard.jar BamIndexStats \
I=input.bam
```

***

# Picard Tools: First example, BamIndexStats
---

First, we need to load the picard-tools module and look at the available tools within picard-tools

```bash
module load picard-tools
$PTOOL/picard.jar
```


BamIndexStats

Generate index statistics from a BAM file.  This tool calculates statistics from a BAM index (.bai) file, emulating the behavior of the "samtools idxstats" command. The statistics collected include counts of aligned and unaligned reads as well as all records with no start coordinate. The input to the tool is the BAM file name but it must be accompanied by a corresponding index file.


```bash
java -Xmx2g -jar $CLASSPATH/picard.jar BamIndexStats \
      I=input.bam \
```

***

# Picard Tools: AddCommentsToBam
---

Adds comments to the header of a BAM file.  This tool makes a copy of the input bam file, with a modified header that includes the comments specified at the command line (prefixed by @CO). Use double quotes to wrap comments that include whitespace or special characters. 

```bash
java -Xmx2g -jar $CLASSPATH/picard.jar AddCommentsToBam \
      I=input.bam \
      O=modified_bam.bam \
      C=comment_1 \
      C="comment 2"
```

***


# Picard Tools:  CompareSAMs
---

Compare two input ".sam" or ".bam" files. This tool initially compares the headers of SAM or BAM files. If the file headers are comparable, the tool will examine and compare readUnmapped flag, reference name, start position and strand between the SAMRecords. The tool summarizes information on the number of read pairs that match or mismatch, and of reads that are missing or unmapped (stratified by direction: forward or reverse).


```bash
java -Xmx2g -jar $CLASSPATH/picard.jar CompareSAMs \
      IA3023.sam \
      SRR2163293.sam
```

***

# Picard Tools: MergeSamFiles
---

Merges multiple SAM and/or BAM files into a single file. This tool is used for combining SAM and/or BAM files from different runs or read groups.

```bash
java -Xmx2g -jar $CLASSPATH/picard.jar MergeSamFiles \
      I=IA3023.sam \
      I=SRR2163293.sam \
      O=merged_files.bam
```
***

# Sambamba
---

![](https://github.com/cpthrash/simulation_projects/blob/master/sambamba.png?raw=true)

So what's it good for?

***

# Sambamba
---

PERFORMANCE

![](https://github.com/cpthrash/simulation_projects/blob/master/Screen%20Shot%202016-11-16%20at%207.10.51%20PM.png?raw=true)

***

# Sambamba: Indexing
---

sambamba-index - tool for building standard index files for BAM data

```bash
sambamba index -p sortedIA3023.bam indexedSAMBAMBA
```

***

# Sambamba: Slice
---

Outputs reads overlapping specified region into new BAM file. (Default destination is STDOUT.) Input file must be coordinate-sorted and indexed.

```bash
sambamba slice -o --output_filename <input.bam> region
```

***

# Coding challenge
---

- CRAM files can be particularly useful because they are further compressed relative to BAM files
- Files are compressed by comparing the BAM file to the reference sequence, and only 'saving' information regarding differences between the two, i.e. by saving information about SNPs, indels, inversions, etc...

---

- Your challenge is to convert one of the SAM files listed here into a CRAM file, and then convert it back into a BAM file

[SAMtools documentation page](https://www.cog-genomics.org/plink2/formats)


