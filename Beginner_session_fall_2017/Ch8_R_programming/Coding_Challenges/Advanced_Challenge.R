#!/usr/bin/env Rscript

#   Finish writing this script to accept a Thetas file
#   from the command line and write 3 plots to a PDF
#   This script must accept both example Thetas files
#   without any modifications to the program
#   Your 3 plots are Watterson's Theta, Pairwise
#   Theta, and Tajima's D
#   NOTHING can be written outside of the three functions
#   started for you, and arguments to the functions
#   CANNOT be changed


#   Accept command line arguments
#   All command line arguments come in
#   to the vector 'args' in the order
#   they were passed

args <- commandArgs(TRUE)

#   A function to read in a Thetas file, fix the data frame, and return a data frame
readThetas <- function(thetasfile){
    return(NULL)
}

#   A function to plot a Theta's graph
#   For Watterson's Theta, you need to divide tW by nSites
#   For Pairwise Theta, you need to divide tP by nSites
#   For Tajima's D, you don't need to divide anything
#   This math should NOT happen in this function
plotThetas <- function(window.center, thetas, label = 'Theta', color = 'red'){
    return(NULL)
}

#   A driver function
main <- function(){
    #   Get the name of the Thetas file
    #   Get an output file name
    #   Read the Thetas file into a data frame
    #   Start the PDF printer
    #   Make the page 6x6
    #   Plot Watterson's Theta
    #   Plot Pairwise Theta
    #   Plot Tajima's D
    #   Turn the PDF printer off
}

main()
