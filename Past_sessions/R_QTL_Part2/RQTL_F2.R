# A demo for reading sample F2 genotyping data and making a few quality control
# plots using R/QTL.

library(qtl)

# Read the cross data, in R/QTL csv format. See http://www.rqtl.org/sampledata/
# for descriptions of the file formats that R/QTL can read. This stores the
# data in a 'cross' object - genotypic, phenotypic, and genetic map data all
# stored in a single object.
pop <- read.cross(format="csv", file="Data/Simulated_Genotypes_F2.csv")

# Summarize the F2 individuals
summary(pop)

# Summarize the markers used here
summary.map(pop)

# Plot the missing genotypes. In the plot, the rows correspond to individuals,
# and the columns correspond to markers. Black pixels indicate missing values.
plotMissing(pop)

# Remove the markers with a lot of missing data. We will set a threshold of
# 5 maximum missing genotypes.
missing_threshold <- 5
todrop <- markernames(pop)[nmissing(pop, what="mar") > missing_threshold]
pop <- drop.markers(pop, todrop)

# And look at the genotypes again
plotMissing(pop)

# Try to identify potential genotyping errors. This function uses a LOD score
# and a method reported in Lincoln and Lander (1992) - basically it looks for
# more recombination events than expected.
#   error.prob is the assumed genotyping error rate overall
pop <- calc.errorlod(pop, error.prob=0.01)
#   Make a genotype plot for each chromosome. The second argument corresponds to
#   the chromosome. In this plot, white circles are homozygous parent 1, black
#   circles are homozygous parent 2, and grey are heterozygous genotypes.
#   Inferred crossover events are shown with blue crosses.
plotGeno(pop, "1")
plotGeno(pop, "2")

# To read a non-F2 population, use something like this. In this case, the data
# are from a F3 family.
pop <- read.cross(
    format="csv",
    file="Data/Simulated_Genotypes.csv",
    BC.gen=0,
    F.gen=3)

# Try repeating the same visualizations for the F3!
