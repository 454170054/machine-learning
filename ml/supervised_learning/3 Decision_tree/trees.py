from math import  log
import operator

def calcshannonent(dataset):
    ##计算信息熵
    numbers = len(dataset)
    labelscounts = {}
    for feavtor in dataset:
        currentlabel = feavtor[-1]
        labelscounts[currentlabel] = labelscounts.get(currentlabel,0) + 1
        # if currentlabel not in labelscounts.keys():
        #     labelscounts[currentlabel] = 0
        # labelscounts[currentlabel] += 1
    shannonent = 0.0
    for key in labelscounts:
        prob = float(labelscounts[key])/numbers
        shannonent -= prob*log(prob,2)
    return shannonent

def splitdataset(dataset,axis,value):
    retdataset = []
    for featvec in dataset:
        if featvec[axis] == value:
            reducedfeatvec = featvec[:axis]
            reducedfeatvec.extend(featvec[axis+1:])
            retdataset.append(reducedfeatvec)
    return retdataset

def createdataset():
    dataset = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataset,labels

def bestchoosefeat(dataset):
    numfeatures = len(dataset[0])-1
    baseentropy = calcshannonent(dataset)
    bestinfogain = 0.0
    bestfeature = -1
    for i in range(numfeatures):
        featlist = [example[i] for example in dataset]
        uniquevals = set(featlist)
        newentropy = 0.0
        for value in uniquevals:
            subdataset = splitdataset(dataset,i,value)
            prob = len(subdataset)/float(len(dataset))
            newentropy += prob * calcshannonent(subdataset)
        infogain = baseentropy - newentropy
        if infogain > bestinfogain:
            bestinfogain = infogain
            bestfeature = i
    return bestfeature
# def chooseBestFeatureToSplit(dataSet):
#     numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
#     baseEntropy = calcshannonent(dataSet)
#     bestInfoGain = 0.0
#     bestFeature = -1
#     for i in range(numFeatures):        #iterate over all the features
#         featList = [example[i] for example in dataSet]#create a list of all the examples of this feature
#         uniqueVals = set(featList)       #get a set of unique values
#         newEntropy = 0.0
#         for value in uniqueVals:
#             subDataSet = splitdataset(dataSet, i, value)
#             prob = len(subDataSet)/float(len(dataSet))
#             newEntropy += prob * calcshannonent(subDataSet)
#         infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
#         if infoGain > bestInfoGain:       #compare this to the best gain so far
#             bestInfoGain = infoGain         #if better than current best, set to best
#             bestFeature = i
#     return bestFeature
def majoritycnt(classlist):
    classcount = {}
    for vote in classlist:
        classcount[vote] = classcount.get(vote,0) +1
    sortedclasscount = sorted(classcount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]

def createTree(dataset,labels):
    classlist = [example[-1] for example in dataset]
    if classlist.count(classlist[0]) == len(classlist):
        return classlist[0]
    if len(dataset[0]) ==1:
        return majoritycnt(classlist)
    bestfeat = bestchoosefeat(dataset)
    bestfeatlabel = labels[bestfeat]
    mytree = {bestfeatlabel:{}}
    del(labels[bestfeat])
    featvalues = [example[bestfeat] for example in dataset]
    uniquevals = set(featvalues)
    for value in uniquevals:
        sublabels = labels[:]
        mytree[bestfeatlabel][value] = createTree(splitdataset(dataset,bestfeat,value),sublabels)
    return mytree

def classify(inputtree,featlabels,testvec):
    firststr = list(inputtree.keys())[0]
    secondict = inputtree[firststr]
    featindex = featlabels.index(firststr)
    for key in seconddict.keys():
        if testvec[featindex] == key:
            if str(type(secondict[key])) == "class 'dict'":
                classlabel = classify(secondict[key],featlabels,testvec)
            else:
                classlabel = secondict[key]
    return classlabel

def storeTree(inputtree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputtree,fw)
    fw.close()
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
