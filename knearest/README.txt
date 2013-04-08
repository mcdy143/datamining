Daniel Alabi and Cody Wang

Files included:
euclideanresults.png: plot of percentage predicted correctly for odd k-values of 1
to 101 using euclidean distance metrics.

manhattanresults.png: plot of percentage predicted correctly for odd k-values of 1
to 101 using manhattan distance metrics.

StandardizedExcelSheet.csv: our standardized data from part 1.

knearestpart2.py:

- To obtain results using manhattan metrics, 
use "result.append(knearest(k, i, cols, data, manhattan))" in allknearest.
- To obtain results using euclidean metrics, 
use "result.append(knearest(k, i, cols, data, euclidean))" in allknearest.
- To change the range of k-values being plotted, change
the line "kvalues = range(1, 102, 2)"
- For the rest of instructions, see comments in file.

