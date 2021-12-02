<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Computing for Next Generation Biology

## [Thomas Girke Tutorial](http://manuals.bioinformatics.ucr.edu/home/linux-basics)

#### Lab: [Peter Morrell](https://github.com/MorrellLAB)

#### Chaochih Liu

##### August 14, 2015

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Novel Problems in Biology

1. Hundreds of gigabytes of data
2. Computationally-intense algorithms
3. Solution: Use a super computer!

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# MSI Quirks

### Module system
- Local user: account on your computer
- login.msi.umn.edu: any of the MSI login nodes
- resource.msi.umn.edu: any one of the systems behind MSI login nodes
    - i.e. Lab, Mesabi, etc.

### MSI queuing system (PBS Queue)
- Called PBS (Portable Batch System)
- Create PBS job scripts to submit a job
- Use `qsub scriptname` to submit a job
- Use `qstat –u username` to check on all jobs you have submitted
- Use `qdel jobIDnumber` to cancel a submitted job

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Scripts

You will likely find yourself working in a UNIX-like environment (MSI runs Linux)
- Specific, optimized tools
- Easy-to-parse text files
- Pipeline-like flow of data between tools

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# General Workflow

![General NGS Workflow](https://raw.githubusercontent.com/liux1299/Linux-NGS_Tutorial/master/images/General_workflow.jpg)

Tools are given at the end of slides.

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Mapping and Alignment

![](https://raw.githubusercontent.com/liux1299/Linux-NGS_Tutorial/master/images/Mapping_and_Alignment.png)

This figure was from GATK Broad Institute.

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# File Formats

Most are plain text

Well-defined and easy to parse
- Pre-built tools for parsing (SAMTools, VCF Tools, etc...)

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# FASTQ File Format

Four Fields

![](https://raw.githubusercontent.com/liux1299/Linux-NGS_Tutorial/master/images/FASTQ_File_Fields.png)

- Name (description line) - starts with `@`
- Sequence data
- End of sequence
- Quality data - same length as sequence

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Git

Version Control System
- Keep track of changes
- Use specific version of code
- Free software

Command-line tool or GUI application

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Git Vs. MS Word

Git Track Changes               | MS Word Track Changes          
:-----------------------------: | :-----------------------------:
![](https://raw.githubusercontent.com/liux1299/Linux-NGS_Tutorial/master/images/Git_Track_Changes.png) | ![](https://raw.githubusercontent.com/liux1299/Linux-NGS_Tutorial/master/images/ms%20word%20track%20changes.png)

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Intro to GitHub

Collaboration
- Review changes
- Comment on code
- Report issues

Sharing of code
- Get feedback

User friendliness
- Web-based graphical interface
- READMEs and Wiki pages

An account is not necessary to view and download public repositories.

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Vince Buffalo's *Bioinformatic Data Skills* Book

![](https://raw.githubusercontent.com/liux1299/Linux-NGS_Tutorial/master/images/Screen%20Shot%20VBuffalo%20GitHub%20Page%202015-07-31.png)

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Useful Git Commands

**Create Repositories**
- To obtain a repository from and existing URL

```
git clone [url]
```

- To create a new repository

```
git init [project_name]
```

**Synchronize Changes**
- Downloads history and updates changes
- You must be in the repository before you run this command

```
git pull
```

- Uploads all local changes (use all three commands in order)
- You add the change, commit the change, and push the change

```
git add
git commit -m "commit message"
git push
```

For more git commands, refer to [Git Cheat Sheet](https://services.github.com/kit/downloads/github-git-cheat-sheet.pdf)

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Exercise 3.1: Downloading Dataset from GitHub

Dataset used: from Vince Buffalo's book *Bioinformatics Data Skills" - Chapters 10 and 11

[Vince Buffalo's GitHub Page](https://github.com/vsbuffalo) is open to the public
- Creating an account is free but not necessary for *today*

Use the following git commands in terminal:

```
#   Make sure you are in the directory ~/Itasca
#   To download files in Vince's GitHub repository (this may take a couple minutes)
git clone https://github.com/vsbuffalo/bds-files.git
```

Now check to make sure it has been downloaded to `~/Itasca`

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Exercise 3.2: Viewing FASTQ File

Now that we have a directory called `bds-files` in ~/Itasca with Vince's dataset, go into `bds-files` and see what's there (hint: use `cd` command).

We will use the `find` command we used in Lec 1 to find which directory the `.fastq` files are located in. Don't remember the exact command? Use a combination of `history` and `grep` commands to find it

We will search through our entire history with `history` and pipe the STDOUT to `grep`.

```
history | grep '*.fasta'
```

Once we find the command, we will change the `*.fasta` part to `*.fastq`

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# FASTQ File Format

This file format is used to store high-throughput sequencing data, reported with a per-base quality score indicating confidence of each base call.

Four Fields

![](https://raw.githubusercontent.com/liux1299/Linux-NGS_Tutorial/master/images/FASTQ_File_Fields.png)

- Name (description line) - starts with `@`
- Sequence data </font>
- End of sequence </font>
- Quality data - same length as sequence

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# BED/GFF3 Format

Describe regions or intervals.

Must be paired with a reference.

BED: usually just intervals. Useful for masking or extracting pieces of sequence.
- BED12 format is the more modern version and more descriptive

GFF3: intervals and qualifiers. Used in genome browsers to list mRNA, CDS, UTR, repeat regions, restriction sites...

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# BED file format

Example BED file from [Vince's Chapter 11](https://github.com/vsbuffalo/bds-files/blob/master/chapter-11-alignment/USH2A_exons.bed)

```
1	216596556	216596738
1	216595194	216595882
1	216591856	216592021
1	216538295	216538427
1	216500933	216500996
1	216498647	216498941
1	216497510	216497694
1	216496816	216497037
1	216495225	216495318
1	216465517	216465712
1	216462622	216462752
1	216424245	216424440
1	216419927	216420568
1	216405295	216405478
1	216390729	216390892
1	216380615	216380773
1	216372969	216373463
1	216371657	216371926
```

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# GFF File Format

Columns in `Morex_Annotations_WithPhase.gff`:
1. Seqname: name of chromosome
2. Source: name of program that generated feature
3. Feature type name: i.e. Gene, Variation, Similarity
4. Start position
5. End position
6. Score – floating point value
7. Froward (+) or reverse(-) strand
8. Frame: either 0 (first base of codon),1 (2nd base of codon) or 2
9. Additional info about each feature

Example GFF file:

```
morex_contig_1083669    mips    predicted_gene  1       212     .       -       .       ID=MLOC_1000
morex_contig_1083669    mips    mRNA    1       212     .       -       .       ID=MLOC_1000.1;Parent=MLOC_1000
morex_contig_1083669    mips    exon    1       212     .       -       .       ID=MLOC_1000.1_exon_1;Parent=MLOC_1000.1
morex_contig_1083669    mips    CDS     3       212     .       -       0       ID=MLOC_1000.1_cds_1;Parent=MLOC_1000.1
morex_contig_1558214    mips    predicted_gene  4442    9055    .       -       .       ID=MLOC_10001
morex_contig_1558214    mips    mRNA    4442    9055    .       -       .       ID=MLOC_10001.1;Parent=MLOC_10001
morex_contig_1558214    mips    exon    4442    4563    .       -       .       ID=MLOC_10001.1_exon_1;Parent=MLOC_10001.1
morex_contig_1558214    mips    exon    7038    7143    .       -       .       ID=MLOC_10001.1_exon_2;Parent=MLOC_10001.1
morex_contig_1558214    mips    exon    7702    7832    .       -       .       ID=MLOC_10001.1_exon_3;Parent=MLOC_10001.1
morex_contig_1558214    mips    CDS     4559    4563    .       -       2       ID=MLOC_10001.1_cds_1;Parent=MLOC_10001.1
morex_contig_1558214    mips    CDS     7038    7143    .       -       0       ID=MLOC_10001.1_cds_2;Parent=MLOC_10001.1
morex_contig_1558214    mips    CDS     7702    7832    .       -       2       ID=MLOC_10001.1_cds_3;Parent=MLOC_10001.1
morex_contig_1558214    mips    mRNA    4870    9055    .       -       .       ID=MLOC_10001.2;Parent=MLOC_10001
```

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Exercise 3.3: View BED Files

Let's try viewing a bed file:

```
#   Go back to the bds-files directory
cd ..

#   Run the same find command we've been using to find where the BED file is located
find `pwd` -name "*.bed" | sort
```

Where are the .bed files located?

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Exercise 3.3: View BED Files

We see the .bed files are located in chapters 6, 7, 8, 9 and 11. We'll use the .bed fild in `chapter-11-alignment` called `USH2A_exons.bed`.

```
#   First, go into that directory and find a file called 'USH2A_exons.bed'

#   View the file using the 'less' command
less USH2A_exons.bed
```

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# SAM/BAM Format

Contains alignment information
- Start/end coordinates
- Mappling quality
- Mates
- And so on

SAM: Plain text human readable format (cut, grep, sed, etc...)
- Use [SAMTools view](http://www.htslib.org/doc/samtools.html) to view SAM files

BAM: Binary(Compressed)

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# BAM Format

Order of magnitude smaller than SAM file

Computer readable

Here is what a BAM file looks like if you try to view it with `head` (not very useful to us):

```
?????#~x?˹??ծ?>?????*?i?q????zż?R???]s?O\??/S?I??h?g???i??.??j??P?*??ˣ??:??O\f?~?js?+_?]x?៸?yW??W?}??O^s?K???5*L?'?Y?????@??'??8?V???W?&?␇??~?Z??)?b©?~??=?m??8?A?w?\?;T?R?w??Y?o?:???+??4?OV???:?`??R??1CXpo?݈3??OX???Δb?/?<q???V\?pe?8???_?i
                                         ????J??űG???o??f[?
                                                           ?c2?ЬՉ
                                                                 6?	s??>5??wI???~???33??8y??q!??u??D????4?
                                                                                                              .?r?N?4;??C?(I?~2ﱗ?R??b<pn?+?/вr?|8,??s??#7
                          ?Z???~?QS²?????;??m_
ᆰ?;	.????}?7??
                  ?BOKpV=L??`]??G??????)a?w????|?ca??r??.@cd??Bo?#
                                                                  ????	t??_??0?Y?M&?[???ּI?h?e?
nڪ ???aՖ
F????_i3??_鈓?O*ѵS??B?4<2
,?(`?)Φ???6'?\?m??P?.?]``nX???qa8?????-???_??UJ{El?W,??K`?F?
?P&i\???>OzĬ+??e?x3?0?o}z>n?ȁ
>?"x0y?%[?VD8?[#?^????"???8????}???#C?EXa??
                                           ??:G?-?B???+??/L?X/??rZz@
```

To view BAM files, use `samtools view -u file_name.bam | head -n 20`:

```
?BC#???BAM?>?@SQ	SN:morex_contig_1	LN:340
@SQ	SN:morex_contig_2	LN:456
@SQ	SN:morex_contig_3	LN:387
@SQ	SN:morex_contig_4	LN:1055
@SQ	SN:morex_contig_5	LN:820
@SQ	SN:morex_contig_6	LN:1875
@SQ	SN:morex_contig_7	LN:2064
@SQ	SN:morex_contig_8	LN:333
@SQ	SN:morex_contig_9	LN:261
@SQ	SN:morex_contig_10	LN:430
@SQ	SN:morex_contig_11	LN:1259
@SQ	SN:morex_contig_12	LN:1705
@SQ	SN:morex_contig_13	LN:375
@SQ	SN:morex_contig_14	LN:338
@SQ	SN:morex_contig_15	LN:2057
@SQ	SN:morex_contig_16	LN:302
@SQ	SN:morex_contig_17	LN:554
@SQ	SN:morex_contig_18	LN:258
@SQ	SN:morex_contig_19	LN:2877
@SQ	SN:morex_contig_20	LN:209
```

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# SAM Format

`@SQ` header: stores info about the reference sequence

`@RG` header: contains read group and sample metadata

`@PG` header: metadata about programs used to create/process SAM/BAM files

First line of alignment section – doesn’t begin with ‘@’

Note: some programs need SAM files to have an @HD header at the beginning to work

To view SAM file headers use `samtools view -H file_name.sam | head -n 10`:

```
@SQ	SN:I	LN:15072434
@SQ	SN:II	LN:15279421
@SQ	SN:III	LN:13783801
@SQ	SN:IV	LN:17493829
@SQ	SN:MtDNA	LN:13794
@SQ	SN:V	LN:20924180
@SQ	SN:X	LN:17718942
@RG	ID:VB00023_L001	SM:celegans-01
@PG	ID:bwa	PN:bwa	VN:0.7.10-r789	CL:bwa mem -R @RG\tID:VB00023_L001\tSM:celegans-01 Caenorhabditis_elegans.WBcel235.dna.toplevel.fa celegans-1.fq celegans-2.fq
```

To view SAM files, use `samtools view file_name.sam | head -n 10`:

```
X_10624440_10624943_0:0:0_2:0:0_3498	99	X	10624440	60	50M	=	10624894	504	ACGCCTATTCGCTAGTCAAACAATAACAACAGTTCCTGTCAGATAAATAG	22222222222222222222222222222222222222222222222222	NM:i:0	MD:Z:50	AS:i:5XS:i:0	RG:Z:VB00023_L001
I_2839164_2839619_2:0:0_1:0:0_c72b	83	I	2839570	60	50M	=	2839164	-456	ATTGCTTTTCGAAAAACCTAAAGAATCATCAATCATCATGTTTCAAAAAA	22222222222222222222222222222222222222222222222222	NM:i:1	MD:Z:39T10	AS:i:45	XS:i:1RG:Z:VB00023_L001
III_1100739_1101246_1:0:0_1:0:0_8c36	83	III	1101197	60	50M	=	1100739	-508	AGGCTTAAGCTTAGGCTCTGGGTTTCCCTGAGGCTTGGCGTCAGTGGCGA	22222222222222222222222222222222222222222222222222	NM:i:1	MD:Z:18A31	AS:i:45	XS:i:2RG:Z:VB00023_L001
III_3499131_3499606_1:0:0_0:0:0_e378	99	III	3499131	60	50M	=	3499557	476	CTCTTTACAATTTTTTTTTGAGAAAAAGTGGGATTTTTCCGCTATTTTAA	22222222222222222222222222222222222222222222222222	NM:i:1	MD:Z:30C19	AS:i:45	XS:i:2RG:Z:VB00023_L001
I_13215087_13215552_1:0:0_0:0:0_17033	99	I	13215087	60	50M	=	13215503	466	CTTCAACTCAGTCCCGAGACAAACTTCAATTTTGAGTTCTTTTTCTGAAG	22222222222222222222222222222222222222222222222222	NM:i:1	MD:Z:16T33	AS:i:45	XS:i:20	RG:Z:VB00023_L001
II_12288502_12289038_1:0:0_0:0:0_1fa2	83	II	12288989	60	50M	=	12288502	-537	AGCCGCCATAACTTTTTTTTGAGAAGTTTGCAAGAGGTTTCATTATAAAA	22222222222222222222222222222222222222222222222222	NM:i:0	MD:Z:50	AS:i:5XS:i:36	RG:Z:VB00023_L001
X_588991_589529_0:0:0_1:0:0_11ad9	83	X	589480	60	50M	=	588991	-539	TGGAGCAAGGTTATTAGATGAATTTAAATTTATTAAGTTTTCAGGTTTAA	22222222222222222222222222222222222222222222222222	NM:i:1	MD:Z:2T47	AS:i:47	XS:i:2RG:Z:VB00023_L001
X_4515157_4515639_2:0:0_1:0:0_1228	99	X	4515157	60	50M	=	4515590	483	CAGCTCATCGAGCCGGGTGAAAATTGATCTACATGTTAAAAAGCATAAGG	22222222222222222222222222222222222222222222222222	NM:i:2	MD:Z:36G4T8	AS:i:40	XS:i:0RG:Z:VB00023_L001
I_14715941_14716459_1:0:0_0:0:0_4553	147	I	14716410	60	50M	=	14715941	-519	GACCACCAAAATAACCAGTCACATATCAAATCTCTCTCAATCAATTACAA	22222222222222222222222222222222222222222222222222	NM:i:0	MD:Z:50	AS:i:5XS:i:0	RG:Z:VB00023_L001
II_3921519_3922009_0:0:0_1:0:0_20013	163	II	3921519	60	50M	=	3921960	491	AAATTCTACCGTACTCCCAATTCAAAACTTTTAAATTTTTTTGATTAAAA	22222222222222222222222222222222222222222222222222	NM:i:0	MD:Z:50	AS:i:50	XS:i:19	RG:Z:VB00023_L001
```

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Exercise 3.4: View SAM/BAM Files

Use the same `find` command we've been using to find where the `.sam` file is located:

```
find `pwd` -name "*.sam" | sort
```

We see the `.sam` files are located in `chapter-11-alignment`. Go into `chapter-11-alignment` and look for `.sam` file.

```
#   View head of SAM file celegans.sam with 'head' command
head celegans.sam
```

Now try to view `celegans.bam` using the `head` command. This doesn't output information that is very useful to us. Try using `samtools view celegans.bam | head -n 10` to view the `.bam` file.

*Note:* `.sam` and `.bam` files are typically relatively large in real datasets so using `less` command or opening `.sam`/`.bam` files in text editors takes too long.

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# VCF/BCF Files

Describes mismatches from reference.

Must be paired with reference sequence.

Information includes:
- Type (SNP, MNP, Indel...)
- Chromosome (or contig)
- Position
- Quality, depth...

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Exercise 3.5: View VCF Files

If you are not already in the directory, `cd` into the directory containing `.vcf` file.

Since the file extension is `.gz`, we will have to unzip the file first. To unzip the gzipped file use `zcat` command (If using a local Mac, use `gzcat` instead) then pipe to `head` to view beginning of file.

```
zcat NA12891_CEU_sample.vcf.gz | head
```

Run the same command without piping to head and see what happens.

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Tools

Aligners
- [BWA](http://bio-bwa.sourceforge.net/): software package for mapping sequences against large reference genomes.
- [Bowtie/Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml): fast and memory efficient tool for aligning sequencing reads to long reference sequences.
- [MOSAIK-aligner](https://code.google.com/archive/p/mosaik-aligner/): a reference-guided aligner for NGS technologies.

SAM/BAM handlers
- [SAMtools](http://samtools.sourceforge.net/): includes various utilities for sorting, merging, indexing and generating alignments in the SAM format.
- [Picard](http://broadinstitute.github.io/picard/): provides command line tools for manipulating high-throughput sequencing data and file formats such as SAM/BAM/CRAM and VCF. 
- [BamTools](https://github.com/pezmaster31/bamtools): toolkit for handling BAM files.

Refining Assemblies
- [GATK](https://www.broadinstitute.org/gatk/): toolkit for high-throughput sequencing data analysis.
- [Picard](http://broadinstitute.github.io/picard/)
- [SAMtools](http://samtools.sourceforge.net/)

Some Analysis
- SNP calling, [FreeBayes](https://github.com/ekg/freebayes)
- Splice-aware mapping, [Tophat](https://ccb.jhu.edu/software/tophat/index.shtml)

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# PacBio RS II
Newer sequencing technology than NGS.

Single Molecule, Real-Time (SMRT) DNA sequencing system.
- High consensus accuracy
- Long read lengths

Ideal for:
- *de novo* assembly
- Characterization of genetic variation
- Methylation analysis
- Microbiology studies
- And more...

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Exercise 3.6: More Useful Commands to Know

Go into directory with `contam.fastq` file. We'll use the one from `chapter-10-sequence`.

Now we'll copy `contam.fastq` from `chapter-10-sequence` to `~/Itasca` and rename the file. Use th `cp` command to copy. We will rename by specifying directory the file will be copied to and giving it a new name `contam1.fastq`

```
cp contam.fastq ~/Itasca/contam1.fastq
```

Next, go into `~/Itasca` to view the copied file.

There is already an existing file `contam.fastq` that we used `wget` to download earlier. Let's see if there are any differences between the file we just copied and the original file. We will use `diff` command to compare differences between files. The format will be `diff -y file_1 file_2`

```
diff -y contam.fastq contam1.fastq
```

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Exercise 3.6: More Useful Commands to Know

Let's create differences and use `diff` again to compare the files. We will be using Vim as our text editor for today. To do this, type `vim` followed by the file you want to edit.

```
vim contam1.fastq
```

In Vim you won't be able to use your mouse to make changes. 
- Type `:` to start entering command. 
- Hit `i` to enter INSERT MODE to edit file

We will delete lines 16-19, but first let's jump to line 16:

```
:16
```

Use `dd` to delete current line and repeat this 4 times.

```
dd
```

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Exercise 3.6: More Useful Commands to Know

If you accidentally delete too many lines, use the undo command to undo your last change.

```
:u
```

If you type `:u` again it will undo 2 changes before that and so on.

Now let's redo our last undo. Use `CTRL+r` to redo last two changes. Now that we have made changes to our file, we will save and exit.
- `:w` saves the file
- `:q` exits out of Vim

```
:wq
```

Let's use `diff` again to see if there are any differences between `contam1.fastq` and `contam.fastq`.

```
diff -y contam.fastq contam1.fastq 
```

The `>` symbol denotes where the differences in the file are.

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Additional Resources

Vince Buffalo's *Bioinformatics Data Skills* - Ch. 10 and 11

Answer key to today's exercises can be viewed and downloaded from my [Gist repository](https://gist.github.com/liux1299/af6fffc5d96e8d44dc9b).