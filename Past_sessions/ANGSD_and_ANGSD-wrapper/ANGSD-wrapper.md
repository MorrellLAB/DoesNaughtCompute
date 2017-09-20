<!-- background: #ffffff-->
<!-- color: #181816 -->
<!-- font: metronova -->

# Follow along with the presentation
---

## Go to:
## http://z.umn.edu/angsdwrapper

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Population Genetics: ANGSD-wrapper
---

##### Does[0]Compute?

##### April 25<sup>th</sup>, 2017

Chaochih Liu

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# What is ANGSD-wrapper?
---

ANGSD-wrapper is a user-friendly utility to aid in the analysis of Next Generation Sequencing data.

ANGSD-wrapper also comes with a visualization package.

<sub> GitHub Page: https://github.com/mojaveazure/angsd-wrapper </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# What is ANGSD-wrapper?
---

ANGSD-wrapper's likelihood based approaches are used in ANGSD to calculate summary statistics from next generation sequencing data.

ANGSD-wrapper's population genetic analyses can be calculated without the need to make SNP calls.

ANGSD-wrapper uses a probabilistic approach to handle variants.

<sub> GitHub Page: https://github.com/mojaveazure/angsd-wrapper </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# What does ANGSD-wrapper do?
---

![](https://github.com/MorrellLAB/DoesNaughtCompute/blob/master/ANGSD_and_ANGSD-wrapper/figures/ANGSD-wrapper.jpg?raw=true)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# ANGSD-wrapper Dependencies
---

Dependencies that are downloaded and installed when `angsd-wrapper` is installed:
- ANGSD
- ngsPopGen
- ngsF
- ngsAdmix

Dependencies that users need to provide:
- SAMTools
- GNU Scientific Library
- Git
- Wget

<sub> GitHub Page: https://github.com/mojaveazure/angsd-wrapper </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Some Format Caveats
---

- BAM files must have an `@HD` header line
- BAM files must be indexed

To check for `@HD` header lines, use the following command:

Note: this command is from the [readme](https://github.com/mojaveazure/angsd-wrapper)

```bash
for sample in `cat ~/path/to/sample_list.txt`
do
    echo $sample
    samtools view -H $sample | head -1
done
```

If you need to add `@HD` header lines to your samples, use the [`fakeHeader.sh`](https://gist.github.com/mojaveazure/d194c4705642eecf8437).

<sub> GitHub Page: https://github.com/mojaveazure/angsd-wrapper </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Some Format Caveats
---

ANGSD-wrapper's regions file runs most efficiently in the following format:

```bash
chr:startPos-endPos
```

If given the following format, ANGSD-wrapper will take much longer to run:

```bash
chr    startPos    endPos
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Basic Usage
---

```bash
angsd-wrapper <wrapper> <config>
```

`angsd-wrapper` can be run from anywhere, you don't have to be in the same directory as `angsd-wrapper`.

```bash
angsd-wrapper
```

Output:

```bash
angsd-wrapper running from /panfs/roc/groups/9/morrellp/liux1299/software_development/angsd-wrapper

Usage:  angsd-wrapper <wrapper> <config>
where:  <wrapper> is one of SFS, Fst, Abbababa, Ancestral, Genotypes, Thetas, Inbreeding, Admixture
and:    <config> is the corresponding configuration file

This version of angsd-wrapper uses ANGSD to calculate Fst
To use the Shiny graphing interface to visualize Fst calculated with ngsPopGen, run the following command:
        git checkout ngsPopGen_Fst

The following is a list of calls and what they do:
    SFS         Site frequency spectrum
    Fst         Fst estimations
    Abbababa    Abba baba test
    Ancestral   Extract ancestral sequence from BAM file
    Genotypes   Genotype likelihood calculations
    PCA         Principal component analysis
    Thetas      Estimate thetas and calculate neutrality test statistics
    Inbreeding  Use ngsF to calculate per-individual inbreeding coefficients
    Admixture   Perform admixture analysis

To download the example dataset, please run
    angsd-wrapper setup data

To start the Shiny graphing interface, please run
    angsd-wrapper shiny graphing
```

<sub> GitHub Page: https://github.com/mojaveazure/angsd-wrapper </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Configuration Files
---

ANGSD-wrapper uses configuration (config) files to store variables used by the wrapper scripts.

Within the config file, you can specify filepaths of sample lists and parameters used for summary statistic calculations.

The `Common_Config` contains file paths and parameters that are common for all methods.

Additional parameters that are not shared among methods can be specified in config files corresponding to the specific method.

<sub> GitHub Page: https://github.com/mojaveazure/angsd-wrapper </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# ANGSD-wrapper Visualization Package
---

Packages to install:
- shiny
- shinythemes
- DT
- data.table
- ape
- lattice
- Hmisc
- [genomeIntervals](https://bioconductor.org/packages/release/bioc/html/genomeIntervals.html)

To install dependencies for visualization on your local machine, run:

```bash
cd angsd-wrapper

./angsd-wrapper setup dependencies
source ~/.bash_profile
```

To start visualization web application:

```bash
angsd-wrapper shiny graphing
```

<sub> GitHub Page: https://github.com/mojaveazure/angsd-wrapper </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Exercise: Example Data Setup
---

First, `cd` into `angsd-wrapper` directory.

In `angsd-wrapper`, run the following command:

```bash
angsd-wrapper setup data
```

<sub> GitHub Page: https://github.com/mojaveazure/angsd-wrapper </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Exercise
---

We will use the example data set for the following exercise.

Basic steps for all methods:

1. Fill out file paths and parameters in config file(s)
2. Run angsd-wrapper
3. Graph results in web application

Exercise:

1. Calculate a site frequency spectrum
2. Estimate Thetas
3. Run admixture analysis
4. Run Principal Component Analysis (PCA)
5. Graph results using ANGSD-wrapper's web application

Hint: All files used for graphing will have a `*.graph.me` file extension

Steps for this exercise are provided in detail in [ANGSD-wrapper's tutorial](https://github.com/mojaveazure/angsd-wrapper/wiki/Tutorial).
