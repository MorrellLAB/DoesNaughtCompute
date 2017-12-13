setwd(dir="~/Applied-Bioinformatics-Discussion/Chapter8-R_Introduction/Coding_Challenges/")
thetas <- read.delim(file = "./ANGSD-wrapper_sample.thetas", header = TRUE, sep = "\t" )

Wattersons.Thetas  <- thetas$tW / thetas$nSites
Pairwise.Thetas  <- thetas$tP / thetas$nSites

plot (thetas$WinCenter, Wattersons.Thetas, main = "Watterson's Thetas Plot", type = "p", xlab = "WinCenter", ylab = "Watterson", pch = 19) 
plot (thetas$WinCenter, Pairwise.Thetas, main = "Pairwise Thetas Plot") 
plot (thetas$WinCenter, thetas$Tajima, main = "Tajima's D Plot") 
