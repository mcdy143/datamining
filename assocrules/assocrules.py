# Daniel Alabi and Cody Wang
# Frequent itemsets and Association Rules

# return True if the first k items of
# ls1 match with the first k items of ls2
def match(k, ls1, ls2):
    for i in range(len(ls1)-1):
        if ls1[i] != ls2[i]:
            return False
    return True

# Returns the result of k1-k1 join on ls, 
# which is lexicographic ordered
def k1k1join(ls):
    res = []
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            # does ls[i]'s first n-1 items match with ls[j]'s
            # first n-1 items. if so merge and put in res
            if match(len(ls[i])-1, ls[i], ls[j]):
                # append the last item of ls[j] to ls[i]
                res.append(ls[i]+[ls[j][-1]])
            else:
                # breaks when don't see a match, which means
                # there are no more joins on ls[i] to do
                break
    return res

# generates all candidate itemssets by performing k1-k1 join
# and then making sure every candidate's immediate subsets
# are frequent
def gencandidates(ls):
    nplus1 = k1k1join(ls)
    nplus1ret = []
    
    for each in nplus1:
        include = True
        for i in range(len(each)):
            if each[:i]+each[i+1:] not in ls:
                include = False
        if include:
            nplus1ret.append(each)
    return nplus1ret

# constructs the hashtree
def conshashtree(candidates):
    hashtree = {}
    for each in candidates:
        curtree = hashtree
        for i in range(len(each)-1):
            curtree.setdefault(each[i], {})
            # set the current level of hashtree
            curtree = curtree[each[i]]
        curtree[each[-1]] = 0
    return hashtree

# recursively count the candidates in the hashtree
def supportcounts(ht, basket, n):
    i = 0
    while i <= len(basket)-n:
        if basket[i] in ht:
            if n == 1:
                # arrived at a leaf, increment count for this branch
                ht[basket[i]] += 1
            else:
                # otherwise keep going down the branch
                supportcounts(ht[basket[i]], basket, n-1)
        i += 1

# returns the support for itemset
def support(hashtree, itemset):
    curtree = hashtree
    for i in range(len(itemset)-1):
        curtree = curtree[itemset[i]]
    return curtree[itemset[-1]]
            
# prunes the candidates using a hashtree construction to count
def prune(hashtree, candidates, baskets, s, n):
    # update the support of each baskets in the hashtree
    for key in baskets: 
        supportcounts(hashtree, baskets[key], n)
    pruned = []
    for cand in candidates:
        # get support of each candidate
        supp = support(hashtree, cand)
        if supp >= s:
            pruned.append(cand)
    return pruned

# returns the association rules with confidence level >= c
# for the itemsets in pruned 
def associate(pruned, c, hashtree, hashtreeprev):
    associations = []
    for each in pruned:
        for i in range(len(each)):
            immediate = each[:i]+each[i+1:]
            # calculate confident of rule (immediate) -> each[i]
            conf = float(support(hashtree, each))/float(support(hashtreeprev, immediate))
            if conf >= c:
                associations.append((immediate, each[i]))
    return associations

# run the apriori algorithm on the baskets using a support
# threshold s
def apriori(baskets, movies, s):
    # stores all the frequent itemsets of all sizes
    freqitems = []

    # get the frequent itemsets of size 1
    size1freq = {}
    for key in baskets:
        for item in baskets[key]:
            size1freq.setdefault(item, 0)
            size1freq[item] += 1
    # currently stores only the frequent itemsets of size 1
    freqitems = sorted([[item] for item in size1freq if size1freq[item] >= s])
    # pruned stores the frequent itemsets of current size (currently n=1)
    pruned = freqitems[:]
    # initialize the hashtree
    hashtree = size1freq
    
    n = 2
    # generate and prune steps to get the frequent itemsets
    # of size n from freq. itemsets of size n-1
    allassociations = []
    while len(pruned) > 0:
        # generate frequent itemsets of size n
        candidates = gencandidates(pruned)
        print "The number of candidate itemsets of size", n, " : ", len(candidates)       
        # remembers the old hashtree to calculate the confidence of
        # association rules
        hashtreeprev = hashtree
        # constructs the hashtree on candidates
        hashtree = conshashtree(candidates)
        # prune frequent itemsets of size n
        pruned = prune(hashtree, candidates, baskets, s, n)
        
        # generate all association rules >= the specified confidence
        associations = associate(pruned, c, hashtree, hashtreeprev)
        allassociations = allassociations + associations
        freqitems = freqitems + pruned

        n += 1

    # Translates movieids into actual movie names
    freqmoviesets = []
    for itemset in freqitems:
        movieset = [movies[item] for item in itemset]
        freqmoviesets.append(movieset)
    movieassociations = []
    for left, right in allassociations:
        movieleft = [movies[item] for item in left]
        movieright = movies[right]
        movieassociations.append((movieleft, movieright))
    return freqmoviesets, movieassociations

if __name__== "__main__":
    f1 = open("ratings.dat")
    f2 = open("movies.dat")
    s = int(raw_input("Give the support threshold: "))
    c = float(raw_input("Give the confidence threshold: "))

    # Use dictionaries to store movie data because some ids are skipped
    movies = {}
    for row in f2:
        line = row.split("::")
        movieid, moviename = int(line[0]), line[1]
        movies[movieid] = moviename

    baskets = {}        
    # Read in every line and store userid and movieid in the dictionary
    for row in f1:
        line = row.split("::")
        userid, movieid = int(line[0]), int(line[1])
        baskets.setdefault(userid, [])
        baskets[userid].append(movieid)
        
    
    # Remove duplicates, if any, from each basket
    for key in baskets:
        baskets[key] = list(set(baskets[key]))
    
    # freqs -> frequent itemsets with support threshold >= s
    freqs, associations = apriori(baskets, movies, s)
    print "Frequent itemsets of support >=", s
    print "================="
    for itemset in freqs:
        print itemset
    print "================="
    print
    print
    print
    print "Association rules with confidence >=", c
    print "================="
    for (left, right) in associations:
        print left, " -> ", right

