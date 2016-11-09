cat("\014")
rm(list=ls())

setwd("C:/Users/Andrew/Documents/Projects/RiotAPI/LeagueOfLegendsHeatMap")
df <- read.table("heatMapData.txt", sep = ",", col.names = c('X' , 'Y'))

library("entropy")

# seperate X and Y values for discretizing function
xValues <- df$X
yValues <- df$Y

# discretize values and transform to dataframe
binnedData <- discretize2d(xValues, yValues, numBins1 = 128, numBins2 = 128, r1 = c(-120,14780), r2 = c(-120,14980))
binnedDataDF <- as.data.frame(binnedData)
colnames(binnedDataDF) <- c('X', 'Y', 'freq')

# create color palette
library(RColorBrewer)
rf <- colorRampPalette(rev(brewer.pal(11,'Spectral')))
r <- rf(32)

# plot of all point
library("ggplot2")
p <- (ggplot(df, aes(x=xValues, y=yValues)) + 
        geom_point(shape=1))
print(p)

# plot discretized data using log scale
p2 <- ggplot(df, aes(x=xValues, y=yValues)) + stat_bin2d(bins=128) + scale_fill_gradientn(colors=r, trans='log') + coord_fixed()
print(p2)
print('alldone')