<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->



# Follow along with the presentation
---

## Go to: http://z.umn.edu/plinkpart2

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# PLINK 1.9 Part II
---

##### Does[0]compute? Week 2 

##### September 29th, 2016

Chaochih Liu

***

# What can we do with PLINK 1.9?
---

![](https://raw.githubusercontent.com/MorrellLAB/DoesNaughtCompute/master/File_Conversions_I/data_management.png)

Note: You can find documentation for PLINK 1.9 at the following link: https://www.cog-genomics.org/plink2

***

# What can we do with PLINK 1.9?
---

![](https://raw.githubusercontent.com/MorrellLAB/DoesNaughtCompute/master/File_Conversions_I/basic_statistics.png)

***

# What can we do with PLINK 1.9?
---

![](https://raw.githubusercontent.com/MorrellLAB/DoesNaughtCompute/master/File_Conversions_I/association_analyses.png)

***

# PLINK File Formats

PLINK accepts and reformats a variety of file formats.

Here is a list of some of the formats accepted by PLINK:

- VCF/BCF
- 23andMe
- Oxford Genotype Table (IMUPTE2)
- SHAPEIT Recombination Map
- BEAGLE
- Hamming Distance Matrix
- GCTA Relationship Matrix
- GCTA Inbreeding Coefficient Report
- Birdsuite Genetic Variant Format
- Haploview Map
- BINBAM Genotype/Phenotype/Variant File
- fastPHASE Format
- STRUCTURE Format

For all PLINK 1.9 input and output file formats, go to PLINK's [File format reference page](https://www.cog-genomics.org/plink2/formats)

***

# PLINK Command Line

Each command line is parsed as a collection of flags. Each flag starts with `--`.

Parameters in PLINK immediately follow a flag.

Example of PLINK command line:

```bash
#   Input data denoted by '--file'
#   Output file prefix denoted by '--out prefix'
#   Calculation(s) to perform denoted by '--list-23-indels'
./plink --file filename --out prefix --list-23-indels 
```

We will walk through an example in the following slides.

***

# PLINK Standard Input
---

Today, we will be using raw 23andMe genotyping data.

Below is 23andMe data downloaded from a public database:

```bash
# rsid	chromosome	position	genotype
rs12564807	1	734462	AA
rs3131972	1	752721	AA
rs148828841	1	760998	CC
rs12124819	1	776546	AA
rs115093905	1	787173	GT
rs11240777	1	798959	AA
rs7538305	1	824398	AC
rs4970383	1	838555	AC
rs4475691	1	846808	CC
rs7537756	1	854250	AA
```

To access the data: 

```bash
#   Use 'wget' to download data
wget https://my.pgp-hms.org/user_file/download/2063

#   Unzip the file
#   Rename unzipped file
gzip -dc 2063 > EmmaB_genome.txt

#   To quickly view data
#   Skip first 20 lines of headers
tail -n +20 EmmaB_genome.txt | head
```

***

# PLINK Standard Input
---

Now we will read data into PLINK:

```bash
#   '--23file' is an uncompressed 23andMe-formatted file
#   'f' is the sex
#   '--out' is the prefix we will use today
plink --23file EmmaB_genome.txt f --out EmmaB
```

***

# PLINK Standard Output
---

The file outputs you should get is:

- `EmmaB.log`
- `EmmaB.bed`
- `EmmaB.fam`
- `EmmaB.bim`

***

# PLINK Standard Output: BED file
---

`EmmaB.bed` (PLINK binary biallelic genotype table)
- Accompanied by `.bim` and `.fam` files
- Starts with three "magic" bytes, and has V blocks on N/4 bytes (rounded up) where V is the number of variants and N is the number of samples

The `.bed` file will look like this:

```bash
#   Using 'xxd' command
xxd EmmaB.bed | head -n 3
0000000: 6c1b 0103 0303 0302 0302 0203 0303 0303  l...............
0000010: 0303 0303 0303 0303 0303 0303 0303 0303  ................
0000020: 0303 0303 0303 0303 0303 0302 0303 0303  ................
```

***

# PLINK Standard Output: FAM file
---

`EmmaB.fam` (PLINK sample information file)
- Accompanies `.bed` file
- It contains the following fields:
   1. Family ID 'FID'
   2. Within-family ID ('ID'; cannot be '0')
   3. Within-family ID of father ('0' if father isn't in dataset)
   4. Within-family ID of mother ('0' if mother isn't in dataset)
   5. Sex code ('1' = male, '2' = female, '0' = unknown)
   6. Phenotype value ('1' = control, '2' = case, '-9'/'0'/non-numeric = missing data if case/control)

The `.fam` file will look like this:

```bash
head EmmaB.fam
f ID001 0 0 1 -9
```

***

# PLINK Standard Output: BIM file
---

`EmmaB.bim` (PLINK extended MAP file)
- Extended variant information file
- Accompanies `.bed` file
- It contains the following fields:
   1. Chromosome code or name
   2. Variant identifier
   3. Position in morgans or centimorgans
   4. Base-pair coordinate
   5. Allele 1 (usually minor)
   6. Allele 2 (usually major)

The `bim` file will look like this:

```bash
head EmmaB.bim
1       rs12564807      0       734462  0       A
1       rs3131972       0       752721  0       A
1       rs148828841     0       760998  0       C
1       rs12124819      0       776546  0       A
1       rs115093905     0       787173  T       G
```

***

# PLINK Recode Function
---

Use PLINK's [`--recode` flag](https://www.cog-genomics.org/plink2/data#recode) to convert input file format to a new output file format.

For example, let's convert our 23andMe file to `.map` format:

```bash
#   Use '--recode rlist' to generate .map file
plink --23file EmmaB_genome.txt f --out EmmaB --recode rlist
```

Here's another example, let's generate a `.ped` file:

```bash
plink --23file EmmaB_genome.txt f --out EmmaB --recode
```

***

# PLINK Standard Output: MAP file
---

`EmmaB.map` (PLINK text fileset variant information file)
- Accompanies a `.ped` file
- It contains the following fields:
   1. Chromosome code or contig names
   2. Variant identifier
   3. Position in morgans or centimorgans
   4. Base-pair coordinate

The `.map` file will look like this:

```bash
head EmmaB.map
1       rs12564807      0       734462
1       rs3131972       0       752721
1       rs148828841     0       760998
1       rs12124819      0       776546
1       rs115093905     0       787173
```

***

# PED Format
---

`EmmaB.ped` (PLINK/MERLIN/Haploview text pedigree + genotype table)
- Accompanied by a `.map` file
- The PED format describes a text pedigree and genotype table

This is what a the beginning of a `.ped` file will look like:

```bash
f ID001 0 0 1 -9 A A A A C

```

***

# Coding Challenge!
---

1. Generate a VCF file from the 23andMe file with indels removed

2. Calculate allele frequency

3. Generate an output file format we have not generated yet

4. Perform a calculation you are interested in (there is more public data available at the link below if needed)

Documentation links:
- [PLINK file format page](https://www.cog-genomics.org/plink2/formats)
- [PLINK data management page](https://www.cog-genomics.org/plink2/data)
- [PLINK basic statistics page](https://www.cog-genomics.org/plink2/basic_stats)
- [Public Genetic Data from Personal Genome Project](https://my.pgp-hms.org/public_genetic_data?data_type=23andMe)
