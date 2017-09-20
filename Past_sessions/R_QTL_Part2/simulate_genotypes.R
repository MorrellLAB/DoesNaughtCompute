# Simulate some genotypes to use in the demo. We will do this with the simcross
# package, also from Karl Broman.

library(simcross)
set.seed(123)

# Read the pedigree file that we have defined. This is a simple F3 family. We
# have the founders, the F1 intermediate, F2 intermediate, and all of the F3
# individuals. The F3 has 20 individuals.
sim_pedigree <- read.csv("Data/sim_pedigree.csv", header=TRUE)

# Use the sim_from_pedigree function to generate crossover data for each of the
# individuals in the pedigree. We have two chromosomes: 150cM and 100cM. They
# are both autosomes.
sim_xo <- sim_from_pedigree(
    sim_pedigree,
    m=30,
    L=c("Chr1"=100, "Chr2"=150),
    xchr=c(FALSE, FALSE))

# Using the simulated crossover data, we generate simulated genotypes.
#   First, define a map. For Chr2, we want pretty even density all throughout.
#   For Chr1, we want high density in the arms, and low density in the arms. 
marker_locations <- list(
    "Chr1"=sort(sample(seq(1, 100, by=0.25), size=20, replace=FALSE)),
    "Chr2"=sort(c(
        sample(seq(1, 15, by=0.05), size=15, replace=FALSE),
        sample(seq(16, 130, by=1), size=5, replace=FALSE),
        sample(seq(131, 150, by=0.1), size=10, replace=FALSE)
        ))
    )
#   We have to set some names for the markers
for(i in seq_along(marker_locations)) {
    names(marker_locations[[i]]) <- paste0(
        "M_", i, "_", 1:length(marker_locations[[i]])
    )
}

# Then, use the convert2geno() function to generate the genotypes. simcross just
# stores the positions of the crossovers as continuous numbers, so we have to
# calculate what the genotypes at specific positions will be.
sim_geno <- convert2geno(sim_xo, marker_locations)

# Let's put some missing data in there
#   10 columns to make mostly missing. Let's say 4 on Chr1 and 6 on Chr2
bad_markers_chr1 <- sample(names(marker_locations[["Chr1"]]), 4, replace=FALSE)
#   These will be mostly missing
for(bm in bad_markers_chr1) {
    marker_index <- match(bm, colnames(sim_geno[["Chr1"]]))
    tomiss <- sample(1:nrow(sim_pedigree), 16, replace=FALSE)
    sim_geno[["Chr1"]][tomiss, marker_index] <- 0
}
#   Repeat for Chr2. But these will not be so bad
bad_markers_chr2 <- sample(names(marker_locations[["Chr2"]]), 6, replace=FALSE)
for(bm in bad_markers_chr2) {
    marker_index <- match(bm, colnames(sim_geno[["Chr2"]]))
    tomiss <- sample(1:nrow(sim_pedigree), 12, replace=FALSE)
    sim_geno[["Chr2"]][tomiss, marker_index] <- 0
}

# We want to put it in R/QTL format. We want to exlcude the parental calls
# (4 rows), but have to add three header rows. It should have 1 row less than
# the pedigree.
rqtl_mat <- matrix(
    NA,
    nrow=nrow(sim_pedigree)-1,
    ncol=1+length(marker_locations[["Chr1"]])+length(marker_locations[["Chr2"]])
    )
#   Start with the top rows that give marker names and positions
rqtl_mat[1,] <- c("Phe", as.character(unlist(lapply(marker_locations, names))))
rqtl_mat[2,] <- c("", rep("Chr1", 20), rep("Chr2", 30))
rqtl_mat[3,] <- c(
    "",
    as.character(marker_locations[["Chr1"]]),
    as.character(marker_locations[["Chr2"]])
    )
#   Then, the genotyping data. But only for the progeny!
for(i in 5:nrow(sim_pedigree)) {
    geno <- c(sim_geno[["Chr1"]][i-4,], sim_geno[["Chr2"]][i-4,])
    # Convert to A/B calls
    geno[geno == 1] <- "A"
    geno[geno == 2] <- "H"
    geno[geno == 3] <- "B"
    geno[geno == 0] <- "-"
    # Put a missing phenotype and append the genotype
    rqtl_mat[i-1,] <- c(NA, geno)
}
#   choose a couple genotypes to be wrong
genotype_cells <- which(rqtl_mat %in% c("A", "B", "H", "-"))
errors <- sample(genotype_cells, 10, replace=FALSE)
for(x in errors) {
    g <- rqtl_mat[x]
    # Swap A and B. If it's a het, randomly assign A or B
    if(g == "A") {
        repl <- "B"
    } else if(g == "B") {
        repl <- "A"
    } else if(g == "H") {
        repl <- sample(c("A", "B"), size=1)
    } else {
        repl <- "-"
    }
    rqtl_mat[x] <- repl
}
# Write it out
write.table(
    rqtl_mat,
    file="Data/Simulated_Genotypes.csv",
    sep=",",
    quote=FALSE,
    row.names=FALSE,
    col.names=FALSE
    )
