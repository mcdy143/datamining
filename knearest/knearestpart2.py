# Daniel Alabi and Cody Wang
# knearest2.py

import math
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

# calculates the euclidean distance between
# record i and record j on the columns cols
def euclidean(i, j, cols, data):
    res = 0
    for l in cols:
        res += math.pow(float(data[i][l])-float(data[j][l]), 2)
    return math.sqrt(res)

# calculates the manhattan distance between record
# i and j on the columns cols
def manhattan(i, j, cols, data):
    res = 0
    for l in cols:
        res += abs(float(data[i][l])-float(data[j][l]))
    return res

# calculates the k-nearest neighbors of record
# i on the columns cols in the data, data
# dist=euclidean means use euclidean distance as default
# dist=manhattan means use manhattan distance as default
def knearest(k, i, cols, data, dist=euclidean):
    result = []
    # valid neighbors -- every other except i
    validn = [l for l in range(0,len(data)) if l != i]
    for j in validn:
        result.append((j, dist(i, j, cols, data)))
    # sorts list based on the distance metric
    result = sorted(result, key = lambda s: s[1])
    # return the k-nearest neighbors
    return result[:k]

# calculates the knearest neighbors for every
# record i in data using cols as attributes
def allknearest(k, data, cols):
    result = []
    for i in range(len(data)):
        # use euclidean distance as metric
        result.append(knearest(k, i, cols, data, manhattan))
    return result

# knearestcalculate
# obtains and plots the k nearest neighbors
# for every record in data
def knearestcalculate(kvalues, data):
    # store percent predicted correctly 
    percentp = []
    
    for kval in kvalues:
        # allknearest returns a list of list of k nearest neighbors
        # for each record in data
        kns = allknearest(kval, data, range(1, len(data[0])-1))
        
        # obtain the list of predictions on the "Needs work" column
        predictions = []
        for i in range(len(kns)):
            needswork = 0
            for each in kns[i]:
                if data[each[0]][len(data[0])-1] == "1":
                    needswork += 1
                else:
                    needswork -= 1
            yes = 1 if needswork > 0 else -1
            predictions.append((needswork, yes))
           
        # calculate how many predictions were actually correct
        correctcount = 0
        for i in range(len(kns)):
            if int(predictions[i][1]) == int(data[i][len(data[0])-1]):
                correctcount += 1
        percentp.append(float(correctcount)*100.0 / float(len(data)))
        
    # percentpk has entries that look like:
    # (kvalue, percentcorrect)
    percentpk = zip(kvalues, percentp)

    # print out (kvalue, percentageCorrect)
    # percentage correct for each value of k
    for (kval, percent) in percentpk:
        print (kval, percent)

    # ============= Plot kvalues against Percentage Correct ========== #
    xdata = np.array(kvalues)
    ydata = np.array(percentp)

    plt.xlabel("k-values")
    plt.ylabel("Percentage correct")

    xnew = np.linspace(xdata.min(), xdata.max(), len(kvalues)*5)
    ysmooth = spline(xdata, ydata, xnew)
    
    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#


if __name__ == "__main__":
    data = []
    header = []
    with open("StandardizedExcelSheet.csv", "rU") as f:
        csvw = csv.reader(f)
        header = csvw.next()
        for line in csvw:
            data.append(line)

    # use odd k-values from 1 to 101
    kvalues = range(1, 102, 2)

    knearestcalculate(kvalues, data)
