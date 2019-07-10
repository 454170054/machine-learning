import numpy as np
from os import listdir
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
def img2vector(filename):
    fr = open(filename)
    returnvector = np.zeros((1,1024))
    for i in range(32):
        linestr = fr.readline()
        for j in range(32):
            returnvector[0,i*32+j] = int(linestr[j])
    return returnvector
def handwritingclasstest():
    ##
    hwlabels = []
    filenames = listdir('trainingDigits')
    m = len(filenames)
    train_datasets = np.zeros((2000,1024))
    for i in range(m):
        filename_1 = filenames[i]
        filename_2 = filename_1.split('.')[0]
        filename_3 = filename_2.split('_')[0]
        hwlabels.append(int(filename_3))
        train_datasets[i,:] = img2vector('trainingDigits/%s'%filenames[i])
    ##
    test_list_dir = listdir('testDigits')
    n = len(test_list_dir)
    test_datasets = np.zeros((n,1024))
    testhdlabels = []
    for i in range(n):
        testfilename_1 = test_list_dir[i]
        testfilename_2 = testfilename_1.split('.')[0]
        testfilename_3 = testfilename_2.split('_')[0]
        testhdlabels.append(int(testfilename_3))
        test_datasets[i,:] = img2vector('testDigits/%s'%test_list_dir[i])

    a = classify0(test_datasets,train_datasets,3,hwlabels)
    errorcount = 0
    for i in range(len(a)):
        if a[i] != testhdlabels[i]:
            print("The classifier came back with :{:d} , the real answer is :{:d}".format(a[i],testhdlabels[i]))
            errorcount += 1
    print(str(errorcount/len(a)))
handwritingclasstest()

