#!/usr/bin/env Rscript

#   This script generates a summary of BED files
#   including mean size and total length of the capture region
#   Script written by Chaochih Liu
#   July 7, 2016

#   To run the script: Rscript ./bed_file_summary.R <bed file>


#   Read in BED file
readFile <- function(filename) {
  bedFile <- read.delim(file = filename,
                        header = FALSE)
  return(bedFile)
}

#   Calculate capture region sizes
captureRegion <- function(bedFile) {
  regionSizes <- bedFile$V3 - bedFile$V2 # difference between start and end positions
  return(regionSizes)
}

#   Calculate mean capture region size and five number summary
regionSummary <- function(regionSizes, filename) {
  resultSummary <- summary(object = regionSizes)
  cat("Summary of ", basename(path = filename), ":\n", sep = "")
  print(resultSummary)
}

#   Calculate total length of capture region
totalLength <- function(regionSizes) {
  totalRegionLength <- sum(regionSizes)
  cat("Total Length of Capture Region:", totalRegionLength, sep = "\n")
}

#   Run the script
runScript <- function() {
  args <- commandArgs(trailingOnly = TRUE)
  inputData <- args[1] # bed file
  inputBED <- readFile(inputData)
  sizeOfRegions <- captureRegion(inputBED)
  regionSummary(sizeOfRegions, inputData)
  totalLength(sizeOfRegions)
}

runScript() # Run program
