#!/usr/bin/python
# By Daniel Alabi and Cody Wang

# returns the number of records in the data file
def numrecords(data):
    return len(data)

# returns the number of attributes in the data file
def numattributes(data):
    return len(data[0])

# return True iff val is continuous
# if a number
def iscontinuous(val):
    try:
        float(val)
        return True
    except:
        return False

def statscolnominal(data, colno):
    col = [] # first get column corresponding to colno
    for line in data:
        col.append(float(line[colno]))

    maxm = max(col)
    minm = min(col)
    avg = sum(col)/len(data)

    sortedcol = sorted(col)
    midindex = len(data)/2
    firsthalf = sortedcol[:midindex]
    secondhalf = sortedcol[midindex+1:]

    first = firsthalf[len(firsthalf)/2]
    med = sortedcol[midindex]
    third = secondhalf[len(secondhalf)/2]

    return (first, third, avg, med, maxm, minm)

def getdistinctvals(data, colno):
    col = [] # first et column corresponding to colno
    for line in data:
        col.append(line[colno])
    distinctvals = list(set(col))

    times = [0]*len(distinctvals) # number of times a distinct value appears
    for i in range(len(distinctvals)):
        for val in col:
            if distinctvals[i] == val:
                times[i] += 1

    return zip(distinctvals, times)

# stats(data)
# returns (lavg, lmed, lmaxm, lminm, ldistinctvals)
# lavg -> list of the averages of all continuous features
# lmed -> list of the medians of all continuous features
# lminm -> list of the minimums of all continuous features
# ldistinctvals -> list of lists of the distinct values of the nominal columns
def stats(data, contcols, noncont):
    lavg = []
    lmed = []
    lmaxm = []
    lminm = []
    lfirst = []
    lthird = []
    ldistinctvals = []

    # iterate over continouus values
    for i in contcols:
        first, third, avg, med, maxm, minm = statscolnominal(data, i)
        lavg.append(avg)
        lmed.append(med)
        lmaxm.append(maxm)
        lminm.append(minm)
        lfirst.append(first)
        lthird.append(third)

    # iterate over non-continuous values
    for i in noncont:
        ldistinctvals.append(getdistinctvals(data, i))

    return (lfirst, lthird, lavg, lmed, lmaxm, lminm, ldistinctvals)

if __name__ == "__main__":
    data = open("../data/census-income-clean.data")

    # first repair last column in data (fix - 50000)
    newdata = []
    for line in data:
        attrs = line.split(",")
        newdata.append([each.strip() for each in attrs[:-1]] + ["".join([c for c in attrs[-1] if c!="." and c!="\n" and c!=" " and c!="+"])])

    data = newdata

    contcols = [0, 5, 16, 17, 18, 29, 38]

    noncont = [i for i in range(len(data[0])) if i not in contcols]
    lfirst, lthird, lavg, lmed, lmaxm, lminm, ldistinctvals = stats(data, contcols, noncont)
    print "list of continuous columns: ", contcols
    print "list of averages: ", zip(contcols, lavg)
    print "list of medians: ", zip(contcols, lmed)
    print "list of maxs: ", zip(contcols, lmaxm)
    print "list of mins: ", zip(contcols, lminm)
    print "list of first quartiles: ", zip(contcols, lfirst)
    print "list of third quartiles: ", zip(contcols, lthird)
    print
    print
    print
    for (col, distinctvals) in zip(noncont, ldistinctvals):
        print "column: ", col
        for (distinctval, count) in distinctvals:
            print distinctval, count
        print

