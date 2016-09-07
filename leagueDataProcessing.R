cat("\014") 
rm(list=ls())

setwd("C:/Users/Andrew/Documents/Projects/RiotAPI/LeagueOfLegendsHeatMap")
getwd();
df <- read.table("testData.txt", sep = ",", col.names = c('X' , 'Y'))

processed <- data.frame(matrix(0, 128, 128))

for (row in df[1]){
  print(row)
}