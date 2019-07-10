import mglearn
import numpy as np
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
# x,y = mglearn.datasets.make_forge()
# mglearn.discrete_scatter(x[:,0],x[:,1],y)
# plt.legend(["Class 0","Class 1"],loc=4)
#
# # X, y = mglearn.datasets.make_forge()
# # mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
# # plt.legend(["Class 0", "Class 1"], loc=4)
# plt.xlabel("First feature")
# plt.ylabel("Second feature")
# plt.show()

# x,y = mglearn.datasets.make_wave(n_samples=40)
# plt.plot(x,y,'o')
# plt.ylim(-3,3)
# plt.xlabel("feature")
# plt.ylabel("target")
# plt.show()
#
# data = load_breast_cancer()
# print("cancer keys:{}".format(data.keys()))
# print("cancer shape:{}".format(data.data.shape))
# print("Sample counts per class:{}".format(
#       {n:v for n,v in zip(data.target_names,np.bincount(data.target))}))

from sklearn.datasets import load_boston
data = load_boston()
print("data shape:{}".format(data.data.shape))
