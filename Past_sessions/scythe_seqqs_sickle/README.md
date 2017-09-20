<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->


# Follow along with the presentation
---

## Go to: http://z.umn.edu/cleaningqc

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Quality Control: seqqs, Scythe, sickle
---

##### Does[0]compute?

##### October 13th, 2016

Chaochih Liu

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Why do we need to process raw data?
---

After we get our raw FASTQ files back from the sequencing center, we will want to:

- Remove sequence contamination from adapters
- Remove bases that are poorly identified
- Know the proportion of duplicate reads
   - Very common transcripts
   - Primer/PCR bias

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Overview
---

#### Adapter Trimming

[`Scythe`](https://github.com/vsbuffalo/scythe)

#### Quality Control

[`seqqs`](https://github.com/vsbuffalo/seqqs)

#### Quality Trimming

[`sickle`](https://github.com/najoshi/sickle)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Where are we in the workflow?
---

[`sequence_handling`](https://github.com/MorrellLAB/sequence_handling)

![](https://raw.githubusercontent.com/MorrellLAB/sequence_handling/master/.Sequence_Handling_Workflow.png)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# When would we use `Scythe`?
---

`Scythe` is used to trim contaminated adapters from sample reads.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# More about `Scythe`
---

`Scythe` uses a Naive Bayesian approach with a prior contaminant estimate to classify contaminant substrings.

Takes into account quality information when trimming.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# What types of data can `Scythe` handle?
---

FASTQ files:

- Paired-end
- Single-end

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Recommended Workflow: `Scythe`
---

Run `Scythe` before quality-based trimming.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Where are we in the workflow?
---

[`sequence_handling`](https://github.com/MorrellLAB/sequence_handling)

![](https://raw.githubusercontent.com/MorrellLAB/sequence_handling/master/.Sequence_Handling_Workflow.png)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# When would we use `seqqs`?
---

`seqqs` will generate quality statistics from sequence data.

Bad data quality can lead to downstream analysis problems and cause programs to misbehave.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Quality Control: `seqqs`
---

- Checks nucleotide composition
- K-mer abundance
- Length distribution
- Base quality

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# When would we use `sickle`?
---

`sickle` is used to trim low quality reads.

Trimming is dependent on quality and length thresholds.

Incorrectly called bases impacts mapping and downstream analyses.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# More about `sickle`
---

`sickle` uses sliding windows to trim 3'-end of reads with low quality and trims the 5'-end of reads once it detects a high enough quality.

`sickle` also discards reads (or replaces reads with an "N") based on a length threshold.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Quality values supported by `sickle`
---

Types of quality values supported:

1. Illumina

2. Solexa

3. Sanger

Note: Illumina quality refers to qualities encoded with CASAVA versions 1.3-1.7. Quality using CASAVA >= 1.8 is Sanger encoded.

This info is provided in the FastQC reports.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# What types of data can `sickle` handle?
---

FASTQ files:

- Paired-end
- Single-end

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Software Installation
---

### [Scythe](https://github.com/vsbuffalo/scythe)

```bash
#   Clone the repository
git clone https://github.com/vsbuffalo/scythe.git

#   Go into the directory you cloned
make all

#   To run Scythe
./scythe
```

### [seqqs](https://github.com/vsbuffalo/seqqs)

```bash
#   Clone the repository
git clone https://github.com/vsbuffalo/seqqs.git

#   Go into the repository you cloned
make

#   To run seqqs
./seqqs
```

### [sickle](https://github.com/najoshi/sickle)

```bash
#   Clone the repository
git clone https://github.com/najoshi/sickle.git

#   Go into the repository you cloned
make

#   To run sickle
./sickle
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Coding Challenge!
---

- Adapter trim the forward (R1) and reverse (R2) toy data

To access data, go to [MorrellLAB/DoesNaughtCompute/scythe_seqqs_sickle/toy_data](https://github.com/MorrellLAB/DoesNaughtCompute/tree/master/scythe_seqqs_sickle/toy_data)

- Use seqqs to generate the following files:
   - Quality distribution by position matrix
   - Nucleotide distribution by position matrix
   - Length distribution by position matrix

- Use sickle to quality trim the paired end samples:
   - Generate forward and reverse quality trimmed samples
   - For the toy data, the quality type is sanger

- Use seqqs again to check your quality trimmed samples.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# References
---

Buffalo V. Scythe - A Bayesian adapter trimmer 
(Version 0.994 BETA) [Software]. Available at https://github.com/vsbuffalo/scythe.

Buffalo V. seqqs.
Available at https://github.com/vsbuffalo/seqqs.

Hoffman PJ, Wyant SR, Kono TJY, Morrell PL. (2016). sequence_handling: A pipeline to automate sequence workflows [Software]. Available at https://github.com/MorrellLAB/sequence_handling.

Joshi NA, Fass JN. (2011). Sickle: A sliding-window, adaptive, quality-based trimming tool for FastQ files 
(Version 1.33) [Software].  Available at https://github.com/najoshi/sickle.