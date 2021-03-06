# Daniel Alabi and Cody Wang
# jaccard.py

import time
import random
import heapq
import sys
import math
from collections import defaultdict


# Calculates the exact Jaccard Similarity of the two documents
# with ids i and j
def jac(docs, i, j):
    doci = set(docs[i-1])
    docj = set(docs[j-1])
    intersectij = doci.intersection(docj)
    unionij = doci.union(docj)
    return float(len(intersectij))/float(len(unionij))

# This helper function uses a hash function that calculates
# the hash value of a particular word
def calchash(hashtuple, word, W):
    (a, b) = hashtuple
    return (a*word + b)%W

# This function estimates the Jaccard similarity of two documents
# with the information from the signature matrix
def sim(sigmatrix, id1, id2):
    numsamerows = 0
    for i in range(len(sigmatrix)):
        if sigmatrix[i][id1-1] == sigmatrix[i][id2-1]:
            numsamerows += 1
    return float(numsamerows)/float(len(sigmatrix))

def constructsigmatrix(docs, W, numhashes):
    # stores all the hash functions
    hashes = [None]*numhashes
    # 42 -> the meaning of life
    random.seed(42)
    # generates random hash functions using seed 42
    for i in range(numhashes):
        hashes[i] = (random.randrange(1, W), random.randrange(1, W))
    # initiates the signature matrix filled with infinity
    sigmatrix = [[float("inf")]*len(docs) for i in range(numhashes)]
    # fills the sigmatrix
    for i in range(len(docs)):
        for j in range(numhashes):
            for k in range(len(docs[i])):
                h = calchash(hashes[j], docs[i][k], W)
                if h < sigmatrix[j][i]:
                    sigmatrix[j][i] = h
    
    return sigmatrix

# Returns the Jaccard similarity of two documents calculated
# from the signature
def sigmatrixsim(docs, W, numhashes, id1, id2):
    sigmatrix = constructsigmatrix(docs, W, numhashes)

    return sim(sigmatrix, id1, id2)

# Returns the k nearest neighbors using the brute force
# approach for the document with docid
def knnsim(docs, docid, k):
    neighbors = []
    # Using a priority queue to estimate the documents that
    # are most similar to the document with docid
    for i in range(len(docs)):
        if i != docid-1:
            heapq.heappush(neighbors, (-jac(docs, docid, i+1), i+1))
    knearest = []
    # Get the nearest k neighbors
    for i in range(k):
        topop = heapq.heappop(neighbors)
        knearest.append(-topop[0])
    return knearest

# Calculates the average of the average similarities using
# the brute force approach 
def avgjaccardsimbf(docs, k):
    s = 0
    for i in range(len(docs)):
        if i > 0 and (i+1)%100 == 0: 
            sys.stderr.write(str(i+1) + " ") 
        knn = knnsim(docs, i+1, k)
        s += float(sum(knn))/k
    sys.stderr.write("\n")
    return s/len(docs)

# Constructs the buckets based on the number of rows in
# each band and the signature matrix
def consbuckets(docs, k, sigmatrix, b, r):
    buckets = defaultdict(list)
    # Going through every documents in each band and hash
    # them to the buckets
    for i in range(b):
        for j in range(len(docs)):
            start = i*r
            end = min((i+1)*r, len(sigmatrix))
            vec = []
            for k in range(start, end):
                vec.append(sigmatrix[k][j])
            vec = tuple(vec)
            buckets[vec].append(j+1) 
    return buckets

# Searches for the potential candidates for the document
# with docid using the banding technique
def candidatepairs(docs, buckets, docid, sigmatrix, b, r):
    possiblebuckets = []
    candidates = []

    for i in range(b):
        start = i*r
        end = min((i+1)*r, len(sigmatrix))
        vec = []
        for j in range(start, end):
            vec.append(sigmatrix[j][docid-1])
        vec = tuple(vec)
        possiblebuckets.append(vec)
    # Get the candidates
    for i in range(len(possiblebuckets)):
        vec = possiblebuckets[i]
        for each in buckets[vec]:
            candidates.append(each)
    candidates = set(candidates)
    if len(candidates) > 0:
        candidates.remove(docid)
    return list(candidates)

# Gets the list of the jaccard similarities of the k-nearest
# neighbors in the candidates
def jaccardlist(docs, candidates, docid, k):
    ls = []
    for i in candidates:
        ls.append(jac(docs, docid, i))
    ls = sorted(ls)[len(ls)-k:]
    return ls

# Calculates the average of the average similarities using
# the lsh approach, returns the estimated average value and
# the number of documents that had at least one document
# chosen at random as its nearest neighbor
def avgjaccardsimlsh(docs, W, k, numhashes, r):
    b = int(math.ceil(numhashes/r))
    sigmatrix = constructsigmatrix(docs, W, numhashes)
    buckets = consbuckets(docs, k, sigmatrix, b, r)
    neighbors = []
    
    # The number of documents that had at least one document
    # chosen at random as its nearest neighbor
    affected = 0

    # Goes through every document and gets the candidates for
    # each document, and gets the knearest neighbors in those
    # lists of candidates
    for i in range(len(docs)):
        candidates = candidatepairs(docs, buckets, i+1, sigmatrix, b, r)
        if k <= len(candidates):
            nearests = jaccardlist(docs, candidates, i+1, k)
        else:
            # If not enough candidates are found, fill in the
            # void with random documents
            affected +=1
            randlist = []
            while len(randlist) < k-len(candidates):
                num = random.randint(1, len(docs))
                if num not in candidates and num != i+1:
                    randlist.append(num)
            nearests = jaccardlist(docs, candidates+randlist, i+1, k)
        neighbors.append(nearests)
    s = 0
    for i in range(len(neighbors)):
        if i > 0 and (i+1)%100 == 0: 
            sys.stderr.write(str(i+1) + " ") 
        s += float(sum(neighbors[i]))/len(neighbors[i])
    sys.stderr.write("\n")
    return (affected, s/len(docs))
    

# Takes in the file and returns the relevant information
def getdocs(filename):
    f = open(filename)

    D = int(f.readline())
    W = int(f.readline())
    NNZ = int(f.readline())
    n = int(raw_input("How many documents to read?\t"))
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
        
    f.close()
    
    return (D, W, n, docs)
    
if __name__ == "__main__":
    # location of data file in /tmp/docword.enron.txt
    (D, W, n, docs) = getdocs("/tmp/docword.enron.txt")
    
    k = int(raw_input("What is k?\t"))
    numhashes = int(raw_input("Enter num rows for Sig Matrix:\t"))
    r = int(raw_input("Enter the number of rows in each band: "))
    print

    t1 = time.time()    
    print "Averages of averages using Brute-force: ", avgjaccardsimbf(docs, k)
    t2 = time.time()
    print "bruteforce time: %.2f"% (t2-t1)
    print
    t3 = time.time()
    (affected, avglsh) = avgjaccardsimlsh(docs, W, k, numhashes, r)
    print "Averages of averages using LSH:", avglsh
    print "No. of docs that used random nearest neighbors: ", affected
    
    t4 = time.time()
    print "lsh time: %.2f"% (t4-t3)
