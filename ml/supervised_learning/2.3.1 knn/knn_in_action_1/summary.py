from numpy import *
import KNN_1
import KNN_3
import KNN_suanfa as clf
def datingClassTest():
    horatio = 0.1
    data, datalabels = KNN_1.filel2matrix("datingTestSet2.txt")
    normMat = KNN_3.autoNorm(data)
    ml = normMat.shape[0]
    numTestset = int(ml*horatio)
    errorcount = 0
    a=clf.classify0(normMat[0:numTestset,:],normMat[numTestset:ml,:],3,datalabels[numTestset:ml])
    for i in range(len(a)):
        if a[i] != datalabels[i]:
            errorcount += 1
    c = errorcount/100
    return c

def predictperson():
    level = ['not at all','in small does','in large does']
    percenttats = float(input("percentage of time spent playing video games?"))
    ffmiles = float(input("frequent flier miles earned per year?"))
    icecream = float(input("liters of ice cream consumed per year?"))
    data, datalabels = KNN_1.filel2matrix("datingTestSet2.txt")
    normMat = KNN_3.autoNorm(data)
    test_dataset = array([[percenttats,ffmiles,icecream]])
    a = clf.classify0(test_dataset,data,3,datalabels)
    print(level[a[0]-1])
predictperson()
