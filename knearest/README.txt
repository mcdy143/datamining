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



Description of Results
======================

As detailed above, the results of our predictions are in euclideanresults.png and
manhattanresults.png.

Both plots appear to be very "similar" in curve-shape. 
- For very small values of k in the range 0-3, 
the k-nearest neighbors algorithm doesn't seem to work well because
we pick very few neighbors to classify on. 

- For medium values of k (in the range 20-50), the k-nearest
neighbors algorithm seems to work well. 

- But for very large values
of k (k > 80), the k-nearest neighbors doesn't work 
well because we pick too many neighbors to classify based on.

