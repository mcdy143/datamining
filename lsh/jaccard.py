# Daniel Alabi and Cody Wang
# jaccard.py

import random

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

# Returns the Jaccard similarity of two documents calculated
# from the signature
def sigmatrixsim(docs, W, numhashes, id1, id2):
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
    
    return sim(sigmatrix, id1, id2)
    

if __name__ == "__main__":   
    # location of data file in /tmp/docword.enron.txt
    f = open("/tmp/docword.enron.txt")

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
    id1 = int(raw_input("What's the first document id?\t"))
    id2 = int(raw_input("What's the second document id?\t"))
    print "Exact Jac Similarity: ", jac(docs, id1, id2)
    print
    numhashes = int(raw_input("Enter num rows for Sig Matrix:\t"))
    print "Estimated Jac Similarity: ", sigmatrixsim(docs, W, numhashes, id1, id2)

