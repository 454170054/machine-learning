# coding=gbk
import numpy as np
def loaddataset():
    datamat = []
    classlabels = []
    with open('testSet.txt','r') as fr:
        for line in fr.readlines():
            data = line.strip().split()
            datamat.append([1.0,float(data[0]),float(data[1])])
            classlabels.append(int(data[2]))
    return datamat,classlabels

def sigmoid(inx):
    return 1.0/(1+np.exp(-inx))

# def gradascent(datamatin,classlabels):
##梯度上升算法
#     datamatrix = np.mat(datamatin)
#     labelmat = np.mat(classlabels).transpose()
#     m,n = np.shape(datamatrix)
#     alpha = 0.001
#     maxcycles = 500
#     oldweights = np.zeros((n,1))
#     weights = np.ones((n,1))
#     for k in range(maxcycles):
#         h = sigmoid(datamatrix * weights)
#         error = (labelmat - h)
#         weights = weights + alpha * datamatrix.transpose() *error
#     return weights

def stogradscent(datamatrix,classlabel,numiter=150):
    m,n = np.shape(datamatrix)
    weights = np.ones(n)
    for j in range(numiter):
        dataindex = list(range(m))
        for i in range(m):
            alpha = 4/(1.0+i+j)+0.01
            randindex = int(np.random.uniform(0,len(dataindex)))
            h = sigmoid(sum(datamatrix[randindex]*weights))
            error = classlabel[randindex] - h
            weights = weights + alpha * error * np.array(datamatrix[randindex])
            del(dataindex[randindex])
    return weights

def plotbestfit(weights):
    import matplotlib.pyplot as plt
    data,labels = loaddataset()
    dataarr = np.array(data)
    n = np.shape(dataarr)[0]
    x1cord_0 = []
    x2cord_0 = []
    x1cord_1 = []
    x2cord_1 = []
    for i in range(n):
        if labels[i] == 0:
            x1cord_0.append(dataarr[i,1])
            x2cord_0.append(dataarr[i,2])
        else:
            x1cord_1.append(dataarr[i,1])
            x2cord_1.append(dataarr[i,2])
    x = np.arange(-3, 3, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    # y = y.getA() #梯度上升算法用
    y = np.reshape(y,-1,1)
    plt.scatter(x1cord_0,x2cord_0,s=30,c='r',marker='*',label='0')
    plt.scatter(x1cord_1,x2cord_1,s=30,c='g',marker='o',label='1')
    plt.xlabel('x1')
    plt.xlabel('x2')
    plt.plot(x,y)
    plt.show()

datamat,labels = loaddataset()
# weights = gradascent(datamat,labels)
weights = stogradscent(datamat,labels)
plotbestfit(weights)

