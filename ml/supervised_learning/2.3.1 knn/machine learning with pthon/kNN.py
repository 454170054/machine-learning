import numpy as np
import mglearn
import operator
# import matplotlib.pyplot as plt
# import mglearn
def createDataset():
    group = np.array([[1.0,1.1],
                      [1.0,1.0],
                      [0.0,0.0],
                      [0.0,0.1]])
    labels = ['A','A','B','B']
    return group,labels
# group,labels = createDataset()
# labels_array = np.reshape(labels,4,1)
# new_data = np.hstack(group,labels_array)
# mglearn.discrete_scatter(group[:, 0], group[:, 1], labels_array)
# plt.legend(["A", "B"],loc=4)
# plt.show()

