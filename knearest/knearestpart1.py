# Daniel Alabi and Cody Wang
# knearestpart1.py
# standardizes the specified columns in writingportfolio.csv 

import csv
import numpy as np
from scipy import stats

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
    sdata = stats.zscore(np.array(newdata, dtype=np.float64))
    for i in range(len(newdata)):
        for j in range(len(toprocess)):
            data[1+i][toprocess[j]] = sdata[i][j]
    for i in range(len(newdata)):
        print newdata[i]
        print sdata[i]
    with open("transformed.csv", "wb") as csvfile:
        csvw = csv.writer(csvfile)
        for line in data:
            csvw.writerow(line)
    
    
