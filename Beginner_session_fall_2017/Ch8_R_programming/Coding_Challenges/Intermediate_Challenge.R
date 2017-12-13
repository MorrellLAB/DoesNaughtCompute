#!/usr/bin/env Rscript

############################################################
##########          Leave this alone              ##########
############################################################
Thetas <- read.table(file = 'ANGSD-wrapper_sample.thetas', header = TRUE, as.is = TRUE)

############################################################
##########          Start editing here            ##########
############################################################
#   Finish the function to plot Thetas values
plotThetas <- function(window.center, thetas, label = 'Thetas', color = 'red'){
    return(NULL)
}

#   Add two new columns to the data frame
#   to fix Watterson's and Pairwise Theta

#   Plot the values for Watterson's Theta,
#   Pairwise Theta, and Tajima's D using
#   the function you wrote
plotThetas(label = "Watterson's Theta")
plotThetas(label = "Pairwise Theta")
plotThetas(label = "Tajima's D")
