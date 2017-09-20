# Does[0]compute Week 2: Plink 1.9 Part II Coding Challenge

Convert 23andMe data to VCF file:

```bash
#   Generate a list of indels
plink --23file EmmaB_genome.txt f --out EmmaB --list-23-indels

#   Remove indels
plink --23file EmmaB_genome.txt f --out EmmaB --exclude EmmaB.indel --recode vcf
```

Calculate allele frequency:

```bash
plink --vcf EmmaB.vcf --out EmmaB --freqx
```