<!-- background: #ffffff-->
<!-- color: #181816 -->
<!-- font: metronova -->

## Presentation Slides for ANGSD are posted below

***

# Follow along with the presentation
---

## Go to:
## http://z.umn.edu/angsd

Example data is on MSI located at: `/panfs/roc/groups/9/morrellp/public/ANGSD-example_data`

If you have never used Morrell Lab's Modules on MSI, run the following command on **Login**:

```bash
echo export MODULEPATH=/panfs/roc/groups/9/morrellp/public/Modules:'$MODULEPATH' >> ~/.bash_profile
```

Next, login to Lab or Mesabi and load ANGSD software:

```bash
module load angsd_ML/0.915
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Population Genetics: ANGSD
---

##### Does[0]Compute?

##### April 18<sup>th</sup>, 2017

Chaochih Liu

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# What can we use ANGSD for?
---

Summarize Next Generation Sequencing Data.

Generate population genetic summary statistics.

Perform association mapping and population genetic analyses.

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# What does ANGSD do?
---

ANGSD is a software used for analyzing next generation sequencing data.

Methods:
- Most take genotype uncertainty into account
- Useful for low/medium depth data

Software:
- Written in C++

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# What does ANGSD do?
---

![](https://github.com/MorrellLAB/DoesNaughtCompute/blob/master/ANGSD_and_ANGSD-wrapper/figures/ANGSD_Analyses.jpg?raw=true)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Input formats supported by ANGSD
---

![](https://yuml.me/diagram/dir:LR/class/[sequence%20data%7CBAM;CRAM;mpileup%7Bbg:orange%7D]-[genotype;likelihoods%7CVCF;GLF;beagle%7Bbg:orange%7D],%20[genotype;likelihoods%7CVCF;GLF;beagle%7Bbg:orange%7D]-[genotype;probability%7Cbeagle%7Bbg:orange%7D])

<sub>Citation: http://www.popgen.dk/angsd/index.php/Input </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# ANGSD filtering
---

1. Read level, MapQ, unique mapped reads, etc
2. Base level, qscore
3. Sequencing depth
4. Regions (active lookup using BAM indexing)
5. Single sites (passive lookup, allows for forcing major and minor)
6. Filtering based on downstream analysis (minimum MAF, LRT for SNP calling, etc)
7. Trimming ends of reads

...and more.

<sub>Citation: http://www.popgen.dk/angsd/index.php/Filters </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Genotype Likelihoods
---

In ANGSD, genotype likelihoods are the likelihood of the data given a genotype.

Use info from our data for a specific position for a single individual, and use info to calculate likelihood of different genotypes.

<sub>Citation:http://www.popgen.dk/angsd/index.php/Genotype_Likelihoods </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Genotype Likelihoods
---

Multiple methods in ANGSD are based on genotype likelihoods.

ANGSD can estimate genotype likelihoods from mapped reads.

There are 4 different genotype likelihood models:

1. SAMtools
2. GATK
3. SOAPsnp
   - need to generate calibration matrix for this method
4. SYK
   - requires file containing type specific errors using the `-errors` option
   - Model based on counts of bases and uses `-doCounts 1` option

<sub>Citation:http://www.popgen.dk/angsd/index.php/Genotype_Likelihoods </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Genotype Likelihoods
---

We can choose which type of genotype likelihoods to output from the following options:

0. Don't output the genotype likelihoods (default)
1. binary all 10 log genotype likelihood
2. beagle genotype likelihood format (use directly for imputation)
3. beagle binary
4. text output of all 10 log genotype likelihoods

```bash
-doGlf [int]
```

<sub>Citation:http://www.popgen.dk/angsd/index.php/Genotype_Likelihoods </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Genotype Likelihood Exercise
---

Use SAMTools genotype likelihood method:
- Infer major and minor allele from likelihoods
- Estimate allele frequencies
- Test for polymorphic sites
- Output only test statistics with minimum of 24

BAM file list: `/panfs/roc/groups/9/morrellp/public/ANGSD-example_data/bams/bam_file_list.txt`

```bash
angsd -bam path_to_bamfile_list.txt\
      -GL 1 \
      -out out_file_prefix \
      -nThreads 10 \
      -doGlf 2 \
      -doMajorMinor 1 \
      -doMaf 2 \
      -SNP_pval 2e-6
```

<sub>Citation: http://www.popgen.dk/angsd/index.php/Genotype_Likelihoods </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# SFS Estimation
---

ANGSD estimates the site frequency spectrum (SFS) in two steps:

1. Generate a `.saf` file (site allele frequency likelihood)

2. Optimize the `.saf` file to estimate SFS

![](https://yuml.me/diagram/dir:LR/class/[sequence%20data%7Bbg:orange%7D]-%3EGL[genotype%20likelihoods%7CSAMtools;GATK;SOAPsnp;Kim%20et.al],%20[genotype%20likelihoods%7CSAMtools;GATK;SOAPsnp;Kim%20et.al]-%3EdoSaf[.saf%20file%7Bbg:blue%7D],%20[.saf%20file%7Bbg:blue%7D]-%3Eoptimize('realSFS')

<sub>Citation: http://www.popgen.dk/angsd/index.php/SFS_Estimation </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# SFS Estimation Exercise
---

Now we will estimate SFS using GATK genotype likelihoods:

BAM file list: `/panfs/roc/groups/9/morrellp/public/ANGSD-example_data/bams/bam_file_list.txt`

Ancestral sequence: `/panfs/roc/groups/9/morrellp/public/ANGSD-example_data/ancestral/chimpHg19.fa.gz`

```bash
#   Generating .saf file with 4 threads
#   -doSaf 1 calcualtes site allele frequency likelihood based on individual genotype likelihoods assuming HWE
#   -GL is one of four models:
    #   1. SAMtools model
    #   2. GATK model
    #   3. SOAPsnp model
    #   4. SYK model
#   -P is the number of threads to use
angsd -bam path_to_bamfile_list.txt\
      -anc path_to_ancestral_seq.fa.gz \
      -out path_to_out_directory \
      -doSaf 1 \
      -GL 2 \
      -P 4
```

<sub>Citation: http://www.popgen.dk/angsd/index.php/SFS_Estimation </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# SFS Estimation Exercise
---

After running the command above, you should have the following output files:

1. `prefix.arg`
2. `prefix.saf.gz`
3. `prefix.saf.idx`
4. `prefix.saf.pos.gz`

<sub>Citation: http://www.popgen.dk/angsd/index.php/SFS_Estimation </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Thetas Estimation
---

ANGSD estimates different thetas as population scaled mutation rate. Based on these methods, ANGSD will calculate Tajima's D and other neutrality test statistics.

ANGSD uses two methods to estimate Thetas:

1. ML method
2. Empirical Bayes (EB) method.

For today, we will use the EB method in our exercise.

We will use 3 steps to estimate Thetas:

[1] Estimate an SFS
- output file: `out.sfs` file

[2] Calculate per-site thetas
- output files: `.thetas.idx` and `.thetas.gz`

[3] Calculate neutrality test statistics
- output file: `.thetas.idx.pestPG` file

<sub>Citation: http://www.popgen.dk/angsd/index.php/Thetas,Tajima,Neutrality_tests </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Thetas Estimation Exercise
---

We will follow the 3 step procedure on the last slide to estimate thetas.

BAM file list: `/panfs/roc/groups/9/morrellp/public/ANGSD-example_data/bams/bam_file_list.txt`

Ancestral sequence: `/panfs/roc/groups/9/morrellp/public/ANGSD-example_data/ancestral/chimpHg19.fa.gz`

Path to realSFS: `/panfs/roc/groups/9/morrellp/public/Software/angsd_ML/misc/realSFS`

Step 1: Estimate an SFS:

```bash
angsd -bam path_to_bamfile_list.txt\
      -anc path_to_ancestral_seq.fa.gz \
      -out path_to_out_directory \
      -doSaf 1 \
      -GL 2 \
      -P 16

#   Obtain maximum likelihood estimate of SFS with realSFS
/panfs/roc/groups/9/morrellp/public/Software/angsd_ML/misc/realSFS outFile.saf.idx \
      -P 16 > out.sfs
```

<sub>Citation: http://www.popgen.dk/angsd/index.php/Thetas,Tajima,Neutrality_tests </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

Thetas Estimation Exercise
---

BAM file list: `/panfs/roc/groups/9/morrellp/public/ANGSD-example_data/bams/bam_file_list.txt`

Ancestral sequence: `/panfs/roc/groups/9/morrellp/public/ANGSD-example_data/ancestral/chimpHg19.fa.gz`

Step 2: Calculate per-site thetas

```bash
angsd -bam path_to_bamfile_list.txt\
      -anc path_to_ancestral_seq.fa.gz \
      -out path_to_out_directory \
      -doSaf 1 \
      -doThetas 1 \
      -pest out.sfs \
      -GL 2
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

Thetas Estimation Exercise
---

BAM file list: `/panfs/roc/groups/9/morrellp/public/ANGSD-example_data/bams/bam_file_list.txt`

Ancestral sequence: `/panfs/roc/groups/9/morrellp/public/ANGSD-example_data/ancestral/chimpHg19.fa.gz`

Path to thetaStat: `/panfs/roc/groups/9/morrellp/public/Software/angsd_ML/misc/thetaStat`

Step 3: Calculate neutrality test statistics

```bash
#   Calculate Tajima's D
/panfs/roc/groups/9/morrellp/public/Software/angsd_ML/misc/thetaStat do_stat out.thetas.idx

#   Sliding window analysis based on make_bed command
/panfs/roc/groups/9/morrellp/public/Software/angsd_ML/misc/thetaStat do_stat out.thetas.idx \
        -win 50000 \
        -step 10000 \
        -outnames theta.thetasWindow.gz
```

<sub>Citation: http://www.popgen.dk/angsd/index.php/Thetas,Tajima,Neutrality_tests </sub>

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

Slides will be posted on [MorrellLAB DoesNaughtCompute GitHub](https://github.com/MorrellLAB/DoesNaughtCompute/)
