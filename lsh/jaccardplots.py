# Daniel Alabi and Cody Wang
# jaccardplots.py

import jaccard
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

# Reads in the first docsize documents and returns relevant info
def getdocs(docsize, filename):
    # location of data file in /tmp/docword.enron.txt
    f = open(filename)

    D = int(f.readline())
    W = int(f.readline())
    NNZ = int(f.readline())
    n = docsize
    docs = [None]*n
    
    line = f.readline().split()
    pastdoc = curdoc = int(line[0])
    ls = [] 
    while curdoc <= n:
        line = f.readline().split()
        curdoc = int(line[0])
        if curdoc > pastdoc:
            docs[pastdoc-1] = ls
            ls = []

        ls.append(int(line[1]))
        pastdoc = curdoc
    
    return (D, W, n, f, docs)

# Helper function for reading in one more document when changing
# document size
def readonemoredoc(f, lastdocid, docs):
    curdoc = pastdoc = lastdocid
    ls = []
    while True:
        line = f.readline().split()
        curdoc = int(line[0])
        if curdoc == pastdoc:
            ls.append(int(line[1]))
        else:
            break
    return ls

if __name__ == "__main__":
    # Set the constant variables, so we can vary each to test
    KCONS = 5
    RCONS = 3
    SIGCONS = 500
    SIZECONS = 1000
 
    (D, W, n, f, docs)  = getdocs(SIZECONS,"/tmp/docword.enron.txt")

    # Varying the number of nearest neighbors, k
    # This is the independent variable x
    kvals = range(1, 22, 2)
    # Represents the difference between the average value of
    # average similarities between the two methods used
    # This is the dependent variable y
    diffs = []

    for k in kvals:
        jac1 = jaccard.avgjaccardsimbf(docs, k)
        (aff, jac2) = jaccard.avgjaccardsimlsh(docs, W, k, SIGCONS, RCONS)
        diffs.append(abs(jac2-jac1))

    xdata = np.array(kvals)
    ydiffs = np.array(diffs)
    plt.xlabel("k-values")
    plt.ylabel("diff btwn avg of avg of similarities")
    plt.axis([0, max(xdata)*1.1, 0, 1.1*max(ydiffs)])

    xnew = np.linspace(xdata.min(), xdata.max(), len(kvals)*5)
    ysmooth = spline(xdata, ydiffs, xnew)

    plt.plot(xnew, ysmooth)
    plt.show()
    
    # Varying the number of rows in each band, r
    # This is the independent variable x
    rvals = range(1, 22, 2)
    diffs = []

    for r in rvals:
        jac1 = jaccard.avgjaccardsimbf(docs, KCONS)
        (aff, jac2) = jaccard.avgjaccardsimlsh(docs, W, KCONS, SIGCONS, r)
        diffs.append(abs(jac2-jac1))

    xdata = np.array(rvals)
    ydiffs = np.array(diffs)
    plt.xlabel("r-values")
    plt.ylabel("diff btwn avg of avg of similarities")
    plt.axis([0, max(xdata)*1.1, 0, 1.1*max(ydiffs)])

    xnew = np.linspace(xdata.min(), xdata.max(), len(rvals)*5)
    ysmooth = spline(xdata, ydiffs, xnew)

    plt.plot(xnew, ysmooth)
    plt.show()

    # Varying the rows in the signature matrix
    # This is the independent variable x
    sigvals = range(50, 1001, 50)
    diffs = []

    for sig in sigvals:
        jac1 = jaccard.avgjaccardsimbf(docs, KCONS)
        (aff, jac2) = jaccard.avgjaccardsimlsh(docs, W, KCONS, sig, RCONS)
        diffs.append(abs(jac2-jac1))

    xdata = np.array(sigvals)
    ydiffs = np.array(diffs)
    plt.xlabel("# of rows in the signature matrix")
    plt.ylabel("diff btwn avg of avg of similarities")
    plt.axis([0, max(xdata)*1.1, 0, 1.1*max(ydiffs)])

    xnew = np.linspace(xdata.min(), xdata.max(), len(sigvals)*5)
    ysmooth = spline(xdata, ydiffs, xnew)

    plt.plot(xnew, ysmooth)
    plt.show()

    # Varying the dataset size
    # This is the independent variable x
    smallest = 100
    largest = 1000+1
    step = 200
    numdocsvals = range(smallest, largest, step)
    
    diffs = []
    current = smallest

    ls = []
    while current < largest:
        # read 'step' more documents
        # assume readonemoredoc(f, lastdocid, currentdocs) function
        for i in range(step):
            docs.append(readonemoredoc(f, len(docs), docs))
        jac1 = jaccard.avgjaccardsimbf(docs, KCONS)
        (aff, jac2) = jaccard.avgjaccardsimlsh(docs, W, KCONS, SIGCONS, RCONS)
        diffs.append(abs(jac2-jac1))
        
        current += step

    xdata = np.array(numdocsvals)
    ydiffs = np.array(diffs)
    plt.xlabel("# of docs read")
    plt.ylabel("diff btwn avg of avg of sim")
    plt.axis([0, max(xdata)*1.1, 0, 1.1*max(ydiffs)])

    xnew = np.linspace(xdata.min(), xdata.max(), len(numdocsvals)*5)
    ysmooth = spline(xdata, ydiffs, xnew)

    plt.plot(xnew, ysmooth)
    plt.show()
    
    

    

        
    

