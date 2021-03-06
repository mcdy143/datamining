#!/usr/bin/python

def clean(data):
    # newdata should be data without the 24th attribute and the 42th
    newdata = []
    for line in data:
        linesplit = line.split(",")
        newdata.append(", ".join(linesplit[:24]+linesplit[25:-1])+"\n")
    return newdata

f = open("../data/census-income.data")
data = []
for line in f:
    data.append(line)
newdata = clean(data)
f.close()
f = open("../data/census-income-clean.data", "w")
for line in newdata:
    f.write(line)


