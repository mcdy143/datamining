# k-means clustering
# Daniel Alabi and Cody Wang

import math
import random
from heapq import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline


# selects centers using the "refined cluster centers"
# algorithm which clusters a random sample of the data
# n times (n=50 in this case) and then clusters
# the resulting centers
def selcentersfancy(data, k):   
    allcenters = []
    for i in range(50):
        # grab a random sample of size, 
        # a 10th of the size of the original dataset
        randomdata = [data[int(random.random()*(len(data)-1))] for j in range(len(data)/10)]
        (sse, centers, clusters) = kmeans(randomdata, k, 1)
        for j in range(len(centers)):
            if centers[j] not in allcenters:
                allcenters.append(centers[j])
    (sse, centers, clusters) = kmeans(allcenters, k, 1)
    return centers

# selects centers randomly
def selcentersrand(data, k):
    minmaxattrs = [(min([row[j] for row in data]), max([row[j] for row in data])) \
                   for j in range(1, 5)]
    return [[mini+random.random()*(maxi-mini) for (mini, maxi) in minmaxattrs] for i in range(k)]
    
# returns the euclidean squared distance
# between point1 and point2
def euclideansq(point1, point2):
    return sum([(point1[i]-point2[i])**2 for i in range(1, 5)])
 
# returns (centers, clusters)
# where centers (centroids, in this case) are the final centers of the 
# k-means clustering
# and clusters is a list of size k
# where clusters[i] -> cluster corresponding to centers[i]
def kmeans(data, k, method):
    if method == 1:
        centers = selcentersrand(data, k)
        # make selected centers look like rows of data
        for center in centers:
            center.insert(0, "")
    else:
        centers = selcentersfancy(data, k)

    lastclusters = None
    while True:
        clusters = [[] for i in range(k)]
        # heap used to store the SSE for each point
        pointerrors = []
        # assign points to the closest center
        for i in range(len(data)):
            row = data[i]
            closest = 0 
            closestdist = euclideansq(centers[closest], row)
            for j in range(len(centers)):
                d = euclideansq(centers[j], row)
                if d < euclideansq(centers[closest], row):
                    closest = j
                    closestdist = d
            clusters[closest].append(i)
            # use pointerrors as a max heap to get
            # the points with the most error
            heappush(pointerrors, (-closestdist, i))

        emptyclusterfound = False
        # get indices for all empty clusters
        for i in range(len(clusters)):
            if len(clusters[i]) == 0:
                (error, rowindex) = heappop(pointerrors)
                centers[i] = data[rowindex]
                clusters[i] = [rowindex]
                emptyclusterfound = True

        if lastclusters == clusters and not emptyclusterfound: break
        lastclusters = clusters        

        # re-calculate the new cluster centers (centroids)
        for i in range(k):
            cluster = clusters[i]
            centers[i] = [sum([data[rowindex][j] for rowindex in cluster])/float(len(cluster)) for j in range(1, 5)]
            # make centers "look like" actual data points
            centers[i].insert(0, "")
        sse = sum([-x for (x, y) in pointerrors])

    sse = sum([-x for (x, y) in pointerrors])
    # clusters[i] corresponds to the row indices of the data
    # belonging to the ith cluster
    return (sse, centers, clusters)

# Calculates the Euclidean magnitude of the line
def euclidean(line):
    return math.sqrt(sum([int((line[i]))**2 for i in range(1, 5)]))

if __name__=="__main__":
    f = open("wp_namespace.txt")
    cols = f.readline().split()
    data = []
    for line in f:
        newline = line.strip().split('\t')
        euclideansum = euclidean(newline)
        newline[1] = float(newline[1])/euclideansum
        newline[2] = float(newline[2])/euclideansum
        newline[3] = float(newline[3])/euclideansum
        newline[4] = float(newline[4])/euclideansum
        data.append(newline)
    # print data
    k = int(raw_input("Enter the value for k: "))
    print "Choose the method you wish to use to select initial cluster centers"
    method = int(raw_input("Enter 1 for random, 2 for fancy (farthest from closest center):  "))
    (sse, finalcenters, clusters) = kmeans(data, k, method)
    for i in range(len(finalcenters)):
        print "=============Center============"
        print finalcenters[i]
        print "================================"
        for j in clusters[i]:
            print data[j]
        print "================================"
    print "total sse: "
    print sse
    
    sses = []
    kvalues = range(1, 21)
    for k in kvalues:
        sses.append(kmeans(data, k, 2)[0])
    # ============= Code to Plot kvalues against Percentage Correct ========== #
    xdata = np.array(kvalues)
    ydata = np.array(sses)

    plt.xlabel("k-values")
    plt.ylabel("SSE")

    xnew = np.linspace(xdata.min(), xdata.max(), len(kvalues)*5)
    ysmooth = spline(xdata, ydata, xnew)
    
    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#
    
        
    
    
