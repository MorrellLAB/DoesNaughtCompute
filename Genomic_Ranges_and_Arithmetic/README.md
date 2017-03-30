<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->



# Follow along with the presentation
---

## Go to: 
## http://z.umn.edu/bedtoolsbedops


To download data:

```bash
git clone https://github.com/MorrellLAB/DoesNaughtCompute.git
```

Or `git pull` to update if you have previously cloned the `DoesNaughtCompute` repository.

The data will be located in `DoesNaughtCompute/Genomic_Ranges_and_Arithmetic/Data-Slides/`.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Genomic Ranges and Arithmetic: `bedtools` & `BEDOPS`
---

##### Does[0]compute?

##### December 15th, 2016

Chaochih Liu

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# What are `bedtools` and `BEDOPS`?
---

Both `bedtools` and `BEDOPS` utilities are a set of tools for many genomics analysis tasks.

Both tools have utilities for file management and file conversion.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Why use `bedtools` or `BEDOPS`?
---

Both tools are fast, flexible command-line tools that can be used to analyze genomic intervals.

Some features are available in `bedtools` but not `BEDOPS`.

`BEDOPS` is more scalable and memory efficient.

![](https://github.com/MorrellLAB/DoesNaughtCompute/blob/master/Genomic_Ranges_and_Arithmetic/Slide_Figures/Neph_et_al_2012_fig1_time_mem_BEDTools_BEDOPS.jpg?raw=true)

<sub> [Neph et al. 2012 - Figure 1a](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3389768/) </sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `bedtools`
---

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `bedtools` supported files:
---

[`bedtools` supports the following file formats](http://bedtools.readthedocs.io/en/latest/content/general-usage.html):

- BED files
- SAM/BAM format sequence alignments
- GFF files
- VCF files

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `bedtools` data conversion:
---

`bedtools` can [do the following file conversions](http://bedtools.readthedocs.io/en/latest/content/overview.html):
- BAM to BED
- BAM to FASTQ
- BED12 to BED6
- BEDPE to BAM
- BED to BAM

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Summary of `bedtools` operations
---

`bedtools` includes many available tools summarized on their [website overview page](http://bedtools.readthedocs.io/en/latest/content/overview.html).

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `bedtools` basics
---

`bedtools` consists of many [sub-commands](http://bedtools.readthedocs.io/en/latest/content/bedtools-suite.html).

The general structure of running `bedtools` on the command-line is:

```bash
bedtools [sub-command] [options]
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `bedtools` basics
---

To bring up help, type on the command-line:

```bash
bedtools
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `bedtools intersect`
---

Using `bedtools intersect`, you can find which regions from two BED files overlap.

![](http://bedtools.readthedocs.org/en/latest/_images/intersect-glyph.png)

In this example, we will find the overlap between `toy_bopa_masked.bed` and `toy_barley_capture.bed` in `/DoesNaughtCompute/Genomic_Ranges_and_Arithmetic/Data-Slides`:

```bash
#   -a option is first bed/gff/vcf/bam files
#   -b option is one or more bed/gff/vcf/bam files used for comparison
bedtools intersect -a toy_bopa_masked.bed -b toy_barley_capture.bed
```

---
<sub> [Image from bedtools website](http://quinlanlab.org/tutorials/bedtools/bedtools.html) </sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `bedtools intersect`
---

If we want to know which regions do not overlap:

```bash
#   -a option is first bed/gff/vcf/bam files
#   -b option is one or more bed/gff/vcf/bam files used for comparison
#   -v option shows what does not overlap
bedtools intersect -a toy_bopa_masked.bed -b toy_barley_capture.bed -v | head
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `bedtools` caveats
---

- Runs out of memory when using more than 100 million alignments.
- Runs faster when data is sorted.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `BEDOPS`
---

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `BEDOPS` supported files:
---

- BED files
- SAM/BAM format sequence alignments
- GFF/GTF files
- VCF files
- PSL files
- WIG files

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `BEDOPS` data conversion
---

`BEDOPS` can [convert the following file formats into BED format](https://bedops.readthedocs.io/en/latest/content/reference/file-management/conversion.html):
- VCF
- GFF/GTF/GVF
- BAM/SAM
- PSL (Blat)
- WIG
- And more

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Summary of `BEDOPS` operations
---

- Everything
- Element-of
- Not-element-of sets
- Complement
- Difference
- Symmetric Difference
- intersect
- Merge
- Partition
- Chop
- Stagger
- Exclude
- Per-chromosome operations
- Range
- Error checking

<sub> [BEDOPS operations](https://bedops.readthedocs.io/en/latest/content/reference/set-operations/bedops.html) </sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `BEDOPS` basics
---

`BEDOPS` consists of many process-flags and operations.

The general structure of running `BEDOPS` on the command-line is:

```bash
bedops [process-flags] <operation> <File(s)>
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `BEDOPS` basics
---

To bring up help, type on the command-line:

```bash
bedops
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `BEDOPS` error checking
---

`BEDOPS` offers a tool that stringently checks if input and output files are comply with `BEDOPS` requirements.

Error checking outputs needed corrections (i.e. extra spaces to be removed, etc.)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `BEDOPS` intersect
---

Using `bedops --intersect`, you can find which regions from two BED files overlap.

![](https://bedops.readthedocs.io/en/latest/_images/reference_setops_bedops_intersect_ab@2x.png)

In this example, we will find the overlap between `toy_bopa_masked.bed` and `toy_barley_capture.bed` in `/DoesNaughtCompute/Genomic_Ranges_and_Arithmetic/Data-Slides`:

```bash
bedops --intersect toy_bopa_masked.bed toy_barley_capture.bed
```

---
<sub> [Image from bedops documentation](https://bedops.readthedocs.io/en/latest/content/reference/set-operations/bedops.html) </sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `BEDOPS` difference
---

Using `bedops --difference`, you can find which regions are in the first input file but not in all other input files.

![](https://bedops.readthedocs.io/en/latest/_images/reference_setops_bedops_difference_ab@2x.png)

```bash
bedops --difference toy_bopa_masked.bed toy_barley_capture.bed
```

---
<sub> [Image from bedops documentation](https://bedops.readthedocs.io/en/latest/content/reference/set-operations/bedops.html#difference-d-difference) </sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# `BEDOPS` caveats
---

`BEDOPS` is optimized using a sorted BED file (the `sort-bed` utility can be used to do sorting).

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Exercise
---

Data in `/DoesNaughtCompute/Genomic_Ranges_and_Arithmetic/Data-Exercises` will be used for the following exercises.
- [bedtools documentation](http://bedtools.readthedocs.io/en/latest/content/bedtools-suite.html)
- [bedops documentation](https://bedops.readthedocs.io/en/latest/content/reference/set-operations/bedops.html#intersect-i-intersect)


Sort the BED files and find the intersection between cpg.bed and exons.bed using `bedtools` and `BEDOPS`. (Hint: in `bedtools`, use `-sorted` at end of command-line to sort BED files).
   - What is the total number of regions that intersect using each tool?
   - Did you get the same result for both tools? Discuss with your group.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Discussion
---

### Group 1

Briefly look through some of the tools available in `bedtools`. Write on the board cases where you would use the tool and the sub-command you would use.
- [bedtools documentation](http://bedtools.readthedocs.io/en/latest/content/bedtools-suite.html)

### Group 2

Briefly look through some of the tools available in `BEDOPS`. Write on the board cases where you would use the tool and the operation you would use.
- [bedops documentation](https://bedops.readthedocs.io/en/latest/content/reference/set-operations/bedops.html#intersect-i-intersect)