# Daniel Alabi and Cody Wang
# knearestpart1.py
# standardizes the specified columns in writingportfolio.csv 

import csv

if __name__ == "__main__":
    f = open("writingportfolio.csv")
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)
    toprocess = range(1, len(row)-1)
    for line in data:
        print [i for i in range(len(line)) if i in toprocess]

    # standardize(data)
