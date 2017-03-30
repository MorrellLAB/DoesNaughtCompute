# Coding Challenge Answers

Below includes one way of completing the coding challenge. You can add more flags and play around with the options that work best for your own dataset.

---

Scythe:

```bash
scythe -a illumina_adapters.fa -o toy_R1_trimmed.fq toy_R1.fastq
scythe -a illumina_adapters.fa -o toy_R2_trimmed.fq toy_R2.fastq
```

seqqs:

```bash
seqqs -p toy_R1_trimmed toy_R1_trimmed.fq
seqqs -p toy_R2_trimmed toy_R2_trimmed.fq
```

sickle:

```bash
sickle pe -t sanger -q 20 \
    -f toy_R1_trimmed.fq \
    -r toy_R2_trimmed.fq \
    -o toy_R1_Q_trimmed.fq \
    -p toy_R2_Q_trimmed.fq \
    -s toy_singles_trimmed.fq
```

seqqs:

```bash
seqqs -p toy_R1_Q_trimmed toy_R1_Q_trimmed.fq
seqqs -p toy_R2_Q_trimmed toy_R2_Q_trimmed.fq
```