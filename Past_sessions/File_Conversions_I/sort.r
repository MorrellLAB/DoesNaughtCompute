#!/usr/bin/env Rscript

read_depths <- read.table(file = 'read_depths.txt', header = FALSE, as.is = TRUE)
names(read_depths) <- c('Sample', 'Depth')

read_depths[order(read_depths$Depth), ]
