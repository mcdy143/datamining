#!/usr/local/bin/Rscript

# reads in 'census-income.data' file which is assumed to be comma-delimited.
# header=FALSE parameter tells R that there's no header. That is, the
# first row of the data file doesn't correspond to the header
census.data <- read.csv("../data/census-income.data", header=FALSE)

# assigns the vector c(1,31,40) to the variable contcols
contcols <- c(1,31,40)

# obtains a sample (a random permutation) of rows 1 to the last row in
# census.data and then selects the first 1000 rows.
# The result is stored in the variable rows.to.plot
rows.to.plot <- census.data[sample(1:nrow(census.data),1000),]

# quartz() opens a new plotting window
quartz()

# produces a matrix of scatterplots of the 1st, 31st, and 40th columns
# in rows.to.plot
# the ijth scatterplot contains rows.to.plot[,i] (column i) plotted against
# rows.to.plot[,j] (column j)
pairs(rows.to.plot[,contcols])

# initializes/creates the png file 'plotfile.png'
png("plotfile.png")

# produces a matrix of scatterplots of the 1st, 31st, and 40th columns
# in rows.to.plot
# the ijth scatterplot contains rows.to.plot[,i] (column i) plotted against
# rows.to.plot[,j] (column j)
# In addition, the matrix of scatterplots produces is written to
# 'plotfile.png'
pairs(rows.to.plot[,contcols])

# closes 'plotfile.png'
dev.off()
