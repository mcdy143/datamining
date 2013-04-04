#!/usr/bin/Rscript

# Daniel Alabi and Cody Wang

contcols <- c(1, 6, 17, 18, 19, 30, 39)

# reads in census data with headers included
census.data <- read.csv("../data/census-income-clean2.data")

quartz()
png("plotfile.png")
pairs(census.data[,contcols])
dev.off()
