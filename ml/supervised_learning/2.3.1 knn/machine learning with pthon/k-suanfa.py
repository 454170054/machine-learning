import numpy as np
import operator
def classify0(inX,dataset,labels,k):

    ##计算距离
    datasetsize = dataset.shape[0]
    diffmat = np.tile(inX,(datasetsize,1))-dataset
    sqdiffmat = diffmat**2
    sqdistaces = np.sum(sqdiffmat,axis=1)
    distances = sqdistaces**0.5


    ##选择距离最小的k个点
    sorteddistindicies = distances.argsort()
    classcount = {}
    for i in range(k):
        voteilabel = labels[sorteddistindicies[i]]
        classcount[voteilabel] = classcount.get(voteilabel,0)+1
    sortedclasscount = sorted(classcount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]
