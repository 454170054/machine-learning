import matplotlib
import KNN_1
from numpy import *
import matplotlib.pyplot as plt
datingDataMat,datingLabels = KNN_1.filel2matrix('datingTestSet2.txt')
print(datingDataMat)
plt.scatter(datingDataMat[:,1],datingDataMat[:,2]
