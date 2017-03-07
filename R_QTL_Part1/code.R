#1. Read file
install.packages("qtl")
library(qtl)
mapthis <- read.cross("csv", "https://raw.githubusercontent.com/MorrellLAB/DoesNaughtCompute/master/R_QTL_Part1/", "3A_PHS.csv", genotypes=c("AA","AB"), na.string="-",estimate.map=FALSE, alleles=c("A","B"))
#2.Check the general information
summary(mapthis)
plot(mapthis)
plotMap(mapthis,show.marker.names=F)
plotPheno(mapthis, pheno.col=1)
plotMissing(mapthis, reorder=TRUE)
#3. Remove markers without genotype data
mapthis <- drop.nullmarkers(mapthis)
totmar(mapthis)
#4. Estimate recombination fractions between all pairs of markers and plot them
mapthis <- est.rf(mapthis)
plotRF(mapthis)
#5. Re-estimate the genetic map and plot the original map against the newly estimated one
newmap <- est.map(mapthis, error.prob=0.01)
plotMap(mapthis, newmap)
#6. Replace the  the genetic map with the estimated one
mapthis <- replace.map(mapthis, newmap)
mapthis <- calc.errorlod(mapthis, error.prob=0.01)
top.errorlod(mapthis)
#7. Calculate the erro LOD score
mapthis <- calc.genoprob(mapthis, step=2, off.end=0.0, error.prob=1.0e-4,map.function="haldane",stepwidth="fixed")
#8. List the genotypes that maybe in erro
top.errorlod(mapthis)
#9. QTL mapping
mapthis.scan1 <- scanone(mapthis, pheno.col=1,model="normal",method="em")
plot(mapthis.scan1)
#10. Significance threshold
mapthis.scan1.perm <- scanone(mapthis, n.perm=100)
thresh1 <- summary(mapthis.scan1.perm , alpha=c(0.63,0.10,0.05))
thresh1 

abline(h=thresh1[1],lty="dotted",lwd=1,col="blue")
abline(h=thresh1[2],lty="dotted", lwd=1,col="green")
abline(h=thresh1[3],lty="dotted",lwd=1,col="red")

summary(mapthis.scan1, perm=mapthis.scan1.perm , lodcolumn=1, alpha=0.01) 
