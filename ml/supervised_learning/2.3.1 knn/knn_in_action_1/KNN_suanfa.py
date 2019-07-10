import numpy as np
import operator
def classify0(test_data,train_data,n_neighbors,label):
    summary_clf=[]
    for i in range(len(test_data)):
        m = len(train_data)
        distance =np.tile(test_data[i],(m,1))-train_data
        distance = distance**2
        distance = np.sum(distance,axis=1)
        distance =distance**0.5

        sortedlist = distance.argsort()
        classcount = {}
        for n_neighbor in range(n_neighbors):
            labelslist = label[sortedlist[n_neighbor]]
            classcount[labelslist ] = classcount.get(labelslist,0)+1
        sortedclasscount = sorted(classcount.items(),key =operator.itemgetter(1),reverse=True )
        summary_clf.append(sortedclasscount[0][0])
    return summary_clf






