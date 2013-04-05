# Daniel Alabi and Cody Wang
# knearestpart1.py
# standardizes the specified columns in writingportfolio.csv 

import csv
import numpy as np
from scipy import stats

def standardize(data):
    newdata = []
    data = np.array(data, dtype=np.float64)
    stds = np.std(data, axis=0)
    avgs = np.mean(data, axis=0)
    
    for line in data:
        newdata.append((line-avgs)/stds)

    return newdata

if __name__ == "__main__":
    f = open("writingportfolio.csv")
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)
    toprocess = range(1, len(row)-1)
    newdata = []
    for line in data[1:]:
        newdata.append([line[i] for i in range(len(line)) if i in toprocess])
    data = newdata
    print standardize(data)
    print stats.zscore(np.array(data))
    
