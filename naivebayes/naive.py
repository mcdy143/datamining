# Daniel Alabi and Cody Wang
# naive.py


import csv
import math
import numpy as np


# Creates the bins which keeps the feature and the counts of the
# number of people who passed and failed. Looks like:
# {"failed": {'(feature)':feature1: counts, feature2: counts...},
# "passed": {'(feature)':feature1: counts, feature2: counts...}}
def constructcountsbin(headers, data, bins):
    countsdict = {}
    countsdict["passed"] = {}
    countsdict["failed"] = {}
    countsdict["total"] = {}

    npass = 0
    nfail = 0
    # Calculate the number of people that passed and the number
    # of people that failed
    for row in data:
        if int(row[len(row)-1]) == 1:
            nfail += 1
        else:
            npass += 1

    for i in bins:
        countsdict["total"].setdefault(headers[i], {})
        countsdict["failed"].setdefault(headers[i], {})
        countsdict["passed"].setdefault(headers[i], {})
        # Go through every row in column i, and increment the
        # count of pass/fail for that feature
        for row in data:
            countsdict["total"][headers[i]].setdefault(row[i], 0)
            countsdict["failed"][headers[i]].setdefault(row[i], 0)
            countsdict["passed"][headers[i]].setdefault(row[i], 0)

            countsdict["total"][headers[i]][row[i]] += 1
            if int(row[len(headers)-1]) == 1:
                countsdict["failed"][headers[i]][row[i]] += 1
            else:
                countsdict["passed"][headers[i]][row[i]] += 1
    return (npass, nfail, countsdict)
        
    
# Gets the mean, variance, and avgsq, which is the average of all
# the values for a continuous feature's squares that is preprocessed
# and will be used later to calculate the variance for each individual
# record by ignoring its own values.

# Return the three items in dict that looks like:
# {passed: {'feature name': {mean: xxx, variance: xxx, avgsq: xxx}, ...}, 
# failed:  {'feature name': {mean: xxx, variance: xxx, avgsq: xxx}}}
# avgsq -> mean of squares
def statscontinuous(headers, data, continuous):
    continuousdict = {}
    continuousdict["passed"] = {}
    continuousdict["failed"] = {}
    
    # go through every column in the data set (feature)
    # and for each, determine the mean, variance, and
    # mean of squares for those who failed and those
    # who passed
    for column in continuous:
        pvalues = []
        fvalues = []
        psq = []
        fsq = []
        for row in data:
            if int(row[len(row)-1]) == 1:
                fvalues.append(float(row[column]))
                fsq.append(float(row[column])**2)
            else:
                pvalues.append(float(row[column]))
                psq.append(float(row[column])**2)
        fmean = np.mean(np.array(fvalues))
        pmean = np.mean(np.array(pvalues))
        fvar = np.var(np.array(fvalues))
        pvar = np.var(np.array(pvalues))
        pavgsq = np.mean(np.array(psq))
        favgsq = np.mean(np.array(fsq))

        # get the feature name, for example, Minnesota in column 0 (having stripped
        # Project ID)
        featname = headers[column]
        continuousdict["passed"][featname] = {"mean": pmean, "var": pvar, "avgsq": pavgsq}
        continuousdict["failed"][featname] = {"mean": fmean, "var": fvar, "avgsq": favgsq}
            
    return continuousdict

# Takes in the information from both dictionaries and calculate the
# probability of passing for each person
def computeprob(forpass, person, bindict, contdict, headers, npass, nfail, data):
    s = "failed"
    n = nfail
    prob = 1
    if forpass:
        # calculates the probability that a person would pass
        prob = float(npass)/(npass+nfail)
        s = "passed"
        n = npass
    else:
        # calculates prob that a person would fail
        prob = float(nfail)/(npass+nfail)

    # go through all the bin features
    
    for key in bindict[s]:
        # get the column number corresponding to key
        column = headers.index(key)
        # remember to skip the information of the person himself
        prob *= float(bindict[s][key][person[column]]-1)/(n-1)

    for key in contdict[s]:      
        column = headers.index(key)
        oldmean = contdict[s][key]["mean"]
        oldvar = contdict[s][key]["var"]
        curval = float(person[column])
        # Calculates the mean of the feature's value for everyone 
        # else except for the person being estimated
        # mk = (n*m-xk) / (n-1)
        newmean = (n*oldmean-curval)/(n-1)
        
        # Calculates the variance of the feature's value for everyone 
        # else except for the person being estimated
        # based on Var(X)=E(X^2)-(E(X))^2, where E is the expected value
        # and also the mean, so the new variance is
        # (E(X^2)-currentvalue) / (n-1) - newmean^2
        newvar = (n*contdict[s][key]["avgsq"]-curval)/(n-1) - newmean**2
        
        # Calculate the probability density based on the Gaussian distribution
        pdense = math.exp(-(curval-newmean)**2/(2*newvar)) / math.sqrt(2*math.pi*newvar)

        prob *= pdense
        
    return prob

# Predict whether a person fails or passes based on the probability
# calculated from computeprob
def predict(person, bindict, contdict, headers, npass, nfail, newdata):
    # threshold for categorizing a person
    threshold = 1
    # compute probability that person passed
    ppass = computeprob(True, person, bindict, contdict, headers, npass, nfail, data)
    # compute probability that person failed
    pfail = computeprob(False, person, bindict, contdict, headers, npass, nfail, data)
   
    if pfail > threshold*ppass:
        # person failed
        return 1
    else:
        # person passed
        return -1

if __name__ == "__main__":
    # read the file here
    f = open("writingportfolio.csv", 'U')

    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)
    headers = data[0][1:]

    # strip out the first column from the entire data (Project Id)
    newdata = []
    for line in data[1:]:
        # if line not empty
        if line[0] != "":
            newdata.append(line[1:])

    # Binned columns: Minnesota, International, Birth Year, AP Credits,
    # essays in portfolios, CS Credits, Science Credits, Writing Credits
    # we binned these columns based on the accuracies we
    # obtained from experimenting (treat as discrete)
    bins = [0, 1, 2, 6, 8, 9, 11, 12]

    # Use Gaussian distribution for the other columns 
    continuous = [i for i in range(0, len(newdata[0])-1) if i not in bins]
    
    # get stats about the binned features
    # npass -> number failed; nfail -> number failed; 
    # binsdict -> contains other stats about features in the past/fail category 
    (npass, nfail, binsdict) = constructcountsbin(headers, newdata, bins)

    # get stats about the continuous features to be used in the classifier
    contdict = statscontinuous(headers, newdata, continuous)

    # make predictions for every person (entry) using the 
    # naive bayes classifier
    predictions = []
    for person in newdata:
        predictions.append(predict(person, binsdict, contdict, headers, npass, nfail, newdata))

    # Calculate the percentage predicted correctly
    count = 0
    for i in range(len(predictions)):
        # compare prediction made with the last column (Needs work column)
        if predictions[i] == int(newdata[i][len(newdata[0])-1]):
            count += 1
    print "Percentage predicted correctly is: ", float(100*count) / len(predictions), "%"

