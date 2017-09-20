<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Follow Along With the Presentation

http://z.umn.edu/files1

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# File Conversions and Other Utilities:
## UNIX `sort` and Plink 1.9 Part I
---

Li Lei and Paul Hoffman
Does[0]Compute? Week 1
September, 22<sup>nd</sup>, 2016

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# UNIX `sort`: A Background
---

UNIX `sort` is an implementation of the merge sort algorithm

`sort` has complete support for pipes

`sort` spits result to STD OUT by default, can redirect to file or pipe to another utility

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Merge Sort
---

![Merge Sort 1](https://upload.wikimedia.org/wikipedia/commons/c/c5/Merge_sort_animation2.gif)

<sub>Credit: [Wikipedia](https://www.wikiwand.com/en/Merge_sort)</sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Merge Sort
---

![Merge Sort 1](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

<sub>Credit: [Wikipedia](https://www.wikiwand.com/en/Merge_sort)</sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Using `sort`
---

Sort by key

```bash
$ cat read_depths.txt
2012BM7F418_CGATGT_L003.fastq 	 20082966
M012CM7F040P07_GCCAAT_L004.fastq  186850151
2012CM7F040P07_GCCAAT_L004.fastq  18685015
2012BM7F498_TTAGGC_L006.fastq 	 20657837
2012BM7F498_TTAGGC_L001.fastq 	 20770568
2012BM7F418_CGATGT_L008.fastq 	 20433391
2012CM8F030P07_ACTTGA_L005.fastq  19874013
2012CM7F040P05_TGACCA_L006.fastq  19251734
2012DM8F016P02_TAGCTT_L001.fastq  20082104
2012BM7F418_CGATGT_L002.fastq 	 20773497
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Using `sort`
---

Sort by key

```bash
$ sort -k 2 read_depths.txt
2012CM7F040P07_GCCAAT_L004.fastq  18685015
M012CM7F040P07_GCCAAT_L004.fastq  186850151
2012CM7F040P05_TGACCA_L006.fastq  19251734
2012CM8F030P07_ACTTGA_L005.fastq  19874013
2012DM8F016P02_TAGCTT_L001.fastq  20082104
2012BM7F418_CGATGT_L003.fastq 	 20082966
2012BM7F418_CGATGT_L008.fastq 	 20433391
2012BM7F498_TTAGGC_L006.fastq 	 20657837
2012BM7F498_TTAGGC_L001.fastq 	 20770568
2012BM7F418_CGATGT_L002.fastq 	 20773497
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Using `sort`
---

Sort numerically

```bash
$ sort -k 2n read_depths.txt
2012CM7F040P07_GCCAAT_L004.fastq  18685015
2012CM7F040P05_TGACCA_L006.fastq  19251734
2012CM8F030P07_ACTTGA_L005.fastq  19874013
2012DM8F016P02_TAGCTT_L001.fastq  20082104
2012BM7F418_CGATGT_L003.fastq 	 20082966
2012BM7F418_CGATGT_L008.fastq 	 20433391
2012BM7F498_TTAGGC_L006.fastq 	 20657837
2012BM7F498_TTAGGC_L001.fastq 	 20770568
2012BM7F418_CGATGT_L002.fastq 	 20773497
M012CM7F040P07_GCCAAT_L004.fastq  186850151
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Using `sort`
---

Reverse sort

```bash
$ sort -rnk 2 read_depths.txt 
M012CM7F040P07_GCCAAT_L004.fastq  186850151
2012BM7F418_CGATGT_L002.fastq    20773497
2012BM7F498_TTAGGC_L001.fastq    20770568
2012BM7F498_TTAGGC_L006.fastq    20657837
2012BM7F418_CGATGT_L008.fastq    20433391
2012BM7F418_CGATGT_L003.fastq    20082966
2012DM8F016P02_TAGCTT_L001.fastq  20082104
2012CM8F030P07_ACTTGA_L005.fastq  19874013
2012CM7F040P05_TGACCA_L006.fastq  19251734
2012CM7F040P07_GCCAAT_L004.fastq  18685015
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Using `sort`
---

Changing the delimiter

```bash
$ sort -nk 2 admixture.csv 
0.000000001,0.000000001,0.000000001,0.000000001,0.999999996
0.000000001,0.000000001,2.6963377151E-09,0.9999999943,0.000000001
0.1097852665,0.052551963,0.3413175712,0.0580726156,0.4382725836
0.1201941389,0.1230766395,0.4850635499,0.1231655845,0.1485000873
0.1306848257,0.0521018861,0.3142042286,0.1802697326,0.322739327
0.1858338841,0.2871404161,0.0734471842,0.2557056155,0.1978729001
0.2384857023,0.2231405071,0.087597386,0.3198728435,0.1309035611
0.2860439945,0.2871404161,0.0203002261,0.1889098678,0.2251264427
0.3333167072,0.3312762922,0.1867419727,0.0157786745,0.1328863534
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Using `sort`
---

Changing the delimiter

```shell
$ sort -t ',' -nk 2 admixture.csv 
0.000000001,0.000000001,0.000000001,0.000000001,0.999999996
0.000000001,0.000000001,2.6963377151E-09,0.9999999943,0.000000001
0.1306848257,0.0521018861,0.3142042286,0.1802697326,0.322739327
0.1097852665,0.052551963,0.3413175712,0.0580726156,0.4382725836
0.1201941389,0.1230766395,0.4850635499,0.1231655845,0.1485000873
0.2384857023,0.2231405071,0.087597386,0.3198728435,0.1309035611
0.2860439945,0.2871404161,0.0203002261,0.1889098678,0.2251264427
0.1858338841,0.2871404161,0.0734471842,0.2557056155,0.1978729001
0.3333167072,0.3312762922,0.1867419727,0.0157786745,0.1328863534
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Using `sort`
---

Sorting multiple columns

```bash
$ sort -t ',' -nk 2,2 -nk 1,1 admixture.csv
0.000000001,0.000000001,0.000000001,0.000000001,0.999999996
0.000000001,0.000000001,2.6963377151E-09,0.9999999943,0.000000001
0.1306848257,0.0521018861,0.3142042286,0.1802697326,0.322739327
0.1097852665,0.052551963,0.3413175712,0.0580726156,0.4382725836
0.1201941389,0.1230766395,0.4850635499,0.1231655845,0.1485000873
0.2384857023,0.2231405071,0.087597386,0.3198728435,0.1309035611
0.1858338841,0.2871404161,0.0734471842,0.2557056155,0.1978729001
0.2860439945,0.2871404161,0.0203002261,0.1889098678,0.2251264427
0.3333167072,0.3312762922,0.1867419727,0.0157786745,0.1328863534
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Using `sort`
---

Keep only unique entries

```bash
$ sort -n sfs.txt | wc -l
95
$ sort -un sfs.txt | wc -l
88
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Other Sorts
---

Python:
 - Uses a special algorithm called the Timsort
   - Timsort is a combination of the merge and insertion sorts
   - Achieved by finding and exploiting runs of order in data
 - Can be faster than UNIX `sort`, but is never slower

R:
 - Uses the quick sort algorithm
 - Can be faster than UNIX `sort`, can also be **much** slower

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Other Sorts
---

```python
>>> import re
>>> samples = [ 'TIL01.bam', 'TIL12.bam', 'WIL03.bam', 'TIL33.bam', 'PIL03.bam', 'HIL04.bam', 'TIL94.bam', 'TIL04.bam', 'TIL37.bam', 'TIL77.bam', 'WWL09.bam', 'WIL09.bam', 'TIL09.bam', 'TIL10.bam']
>>> sorted(samples, key=lambda name : int(''.join(re.findall(r'(\d+)', name))))
['TIL01.bam', 'WIL03.bam', 'PIL03.bam', 'HIL04.bam', 'TIL04.bam', 'WWL09.bam', 'WIL09.bam', 'TIL09.bam', 'TIL10.bam', 'TIL12.bam', 'TIL33.bam', 'TIL37.bam', 'TIL77.bam', 'TIL94.bam']
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Other Sorts
---

```R
> read_depths <- read.table(file = 'read_depths.txt', header = FALSE, as.is = TRUE)
> names(read_depths) <- c('Sample', 'Depth')
> read_depths[order(read_depths$Depth), ]
                             Sample     Depth
3  2012CM7F040P07_GCCAAT_L004.fastq  18685015
8  2012CM7F040P05_TGACCA_L006.fastq  19251734
7  2012CM8F030P07_ACTTGA_L005.fastq  19874013
9  2012DM8F016P02_TAGCTT_L001.fastq  20082104
1     2012BM7F418_CGATGT_L003.fastq  20082966
6     2012BM7F418_CGATGT_L008.fastq  20433391
4     2012BM7F498_TTAGGC_L006.fastq  20657837
5     2012BM7F498_TTAGGC_L001.fastq  20770568
10    2012BM7F418_CGATGT_L002.fastq  20773497
2  M012CM7F040P07_GCCAAT_L004.fastq 186850151
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Comparison of Sorting Algorithms (Worst Case)
---

![Sorting Performance](https://raw.githubusercontent.com/MorrellLAB/DoesNaughtCompute/master/File_Conversions_I/sorting.png)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Plink 1.9  Overview
---


![Plink Workflow](https://raw.githubusercontent.com/MorrellLAB/DoesNaughtCompute/master/File_Conversions_I/plink.png)

<sub>https://www.cog-genomics.org/plink2/assoc </sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Plink Standard Inputs
---

Plink format describes biallelic genotype calls and pedigree information

Can be flat text (MAP/PED) or compressed (BED/BIM/FAM)

**No** header lines in these files



<!-- background

Text file: map/ped

Compressed binary file: bed/bim/fame

-->

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# MAP Format
---

The MAP format describes variant information for an accompanying PED file

<table>
    <tr>
        <th>Chromosome</th>
        <th>Marker ID</th>
        <th>Genetic Distance</th>
        <th>Physical Position</th>
    </tr>
    <tr>
        <td>21</td>
        <td>rs11511647</td>
        <td>0</td>
        <td>26765</td>
    </tr>
    <tr>
        <td>X</td>
        <td>rs3883674</td>
        <td>0</td>
        <td>32380</td>
    </tr>
    <tr>
        <td>X</td>
        <td>rs12218882</td>
        <td>0</td>
        <td>48172</td>
    </tr>
    <tr>
        <td>9</td>
        <td>rs10904045</td>
        <td>0</td>
        <td>48426</td>
    </tr>
    <tr>
        <td>9</td>
        <td>rs10751931</td>
        <td>0</td>
        <td>49949</td>
    </tr>
    <tr>
        <td>8</td>
        <td>rs11252127</td>
        <td>0</td>
        <td>52087</td>
    </tr>
    <tr>
        <td>10</td>
        <td>rs12775203</td>
        <td>0</td>
        <td>52277</td>
    </tr>
    <tr>
        <td>8</td>
        <td>rs12255619</td>
        <td>0</td>
        <td>52481</td>
    </tr>
</table>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# PED Format
---

The PED format describes a text pedigree and genotype table; accompanied by a MAP file (usually) or INFO file (rarely)

<table>
    <tr>
        <th>Family ID</th>
        <th>Sample ID</th>
        <th>Paternal ID</th>
        <th>Maternal ID</th>
        <th>Sex</th>
        <th>Affection</th>
        <th>Genotypes</th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
    </tr>
    <tr>
        <td>FAM1</td>
        <td>NA06985</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>A</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
        <td>A</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
    </tr>
    <tr>
        <td>FAM1</td>
        <td>NA06991</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA06993</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>T</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>T</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA06994</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA07000</td>
        <td>0</td>
        <td>0</td>
        <td>2</td>
        <td>1</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>T</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>T</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA07019</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA07022</td>
        <td>0</td>
        <td>0</td>
        <td>2</td>
        <td>1</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>0</td>
        <td>0</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA07029</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
    </tr>
    <tr>
        <td>FAM2</td>
        <td>NA07056</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>2</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>A</td>
        <td>G</td>
        <td>C</td>
        <td>T</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>A</td>
        <td>G</td>
        <td>C</td>
        <td>T</td>
    </tr>
    <tr>
        <td>FAM2</td>
        <td>NA07345</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
        <td>C</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>G</td>
        <td>G</td>
        <td>C</td>
        <td>C</td>
    </tr>
</table>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# BED Format
---

The BED format is a binary biallelic genotype table

Starts with three "magic" bytes, and has **V** blocks on **N**/4 bytes (rounded up) where **V** is the number of variants and **N** is the number of samples

The following BED line has three variants and six samples

```
0x6c 0x1b 0x01 0xdc 0x0f 0xe7 0x0f 0x6b 0x01
```

To read the binary code, please consult [Plink's BED format specification](https://www.cog-genomics.org/plink2/formats#bed)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# BIM Format
---

The BIM format is an extended MAP file, also holding minor (A1) and major (A2) alleles

<table>
    <tr>
        <th>Chromosome</th>
        <th>Marker ID</th>
        <th>Genetic Distance</th>
        <th>Physical Position</th>
        <th>A1 (Minor)</th>
        <th>A2 (Major)</th>
    </tr>
    <tr>
        <td>21</td>
        <td>rs11511647</td>
        <td>0</td>
        <td>26765</td>
        <td>A</td>
        <td>T</td>
    </tr>
    <tr>
        <td>X</td>
        <td>rs3883674</td>
        <td>0</td>
        <td>32380</td>
        <td>C</td>
        <td>G</td>
    </tr>
    <tr>
        <td>X</td>
        <td>rs12218882</td>
        <td>0</td>
        <td>48172</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>9</td>
        <td>rs10904045</td>
        <td>0</td>
        <td>48426</td>
        <td>A</td>
        <td>T</td>
    </tr>
    <tr>
        <td>9</td>
        <td>rs10751931</td>
        <td>0</td>
        <td>49949</td>
        <td>C</td>
        <td>T</td>
    </tr>
    <tr>
        <td>8</td>
        <td>rs11252127</td>
        <td>0</td>
        <td>52087</td>
        <td>A</td>
        <td>C</td>
    </tr>
    <tr>
        <td>10</td>
        <td>rs12775203</td>
        <td>0</td>
        <td>52277</td>
        <td>A</td>
        <td>A</td>
    </tr>
    <tr>
        <td>8</td>
        <td>rs12255619</td>
        <td>0</td>
        <td>52481</td>
        <td>G</td>
        <td>T</td>
    </tr>
</table>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# FAM Format
---

The FAM format describes sample information (like PED files without genotype information)

<table>
    <tr>
        <th>Family ID</th>
        <th>Sample ID</th>
        <th>Paternal ID</th>
        <th>Maternal ID</th>
        <th>Sex</th>
        <th>Affection</th>
    </tr>
    <tr>
        <td>FAM1</td>
        <td>NA06985</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>FAM1</td>
        <td>NA06991</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA06993</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA06994</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA07000</td>
        <td>0</td>
        <td>0</td>
        <td>2</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA07019</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA07022</td>
        <td>0</td>
        <td>0</td>
        <td>2</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>NA07029</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>FAM2</td>
        <td>NA07056</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>2</td>
    </tr>
    <tr>
        <td>FAM2</td>
        <td>NA07345</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
</table>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Other Acceptable Formats
---

Plink accepts and writes to a variety of formats, including but not limited to:

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

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Data Management
---

![Data Management Workflow](https://raw.githubusercontent.com/MorrellLAB/DoesNaughtCompute/master/File_Conversions_I/data_management.png)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Basic Stats
---

![Basic Stats Workflow](https://raw.githubusercontent.com/MorrellLAB/DoesNaughtCompute/master/File_Conversions_I/basic_statistics.png)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Association Analyses
---

![Association Analyses Workflow](https://raw.githubusercontent.com/MorrellLAB/DoesNaughtCompute/master/File_Conversions_I/association_analyses.png)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Reference
---
Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M.A.R., Bender, D., Maller, J., Sklar, P., de Bakker, P.I., Daly, M.J., et al. (2007). PLINK: A tool set for whole-genome association and population-based linkage analyses. Am. J. Hum. Genet. 81, 559-575.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Example of `recode`
---
`plink --file toy  --recode vcf --out new`