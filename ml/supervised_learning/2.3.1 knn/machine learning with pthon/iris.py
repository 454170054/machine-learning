from sklearn.datasets import load_iris
import pandas as pd
##(train_test_split将数据集划分为训练和测试集)
from sklearn.model_selection import train_test_split
import numpy as np
import mglearn
import matplotlib.pyplot as plt
iris_dataset = load_iris()
# print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))
# print(iris_dataset)
# print(iris_dataset["target_names"])
# print("Shape of data: {}".format(iris_dataset['data'].shape))
# print("First five rows of data:\n{}".format(iris_dataset['data'][0:5]))
# print("target:\n{}".format(iris_dataset['target']))
# print("type:\n{}".format(type(iris_dataset['target'])))


# ###划分训练和测试集合
x_train,x_test,y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset['target']
                                                   ,random_state=0)
# print("x_train shape:\n{}".format(x_train.shape))
# print("x_test shape:\n{}".format(x_test.shape))

##绘制散点图
# 利用X_train中的数据创建DataFrame
# 利用iris_dataset.feature_names中的字符串对数据列进行标记


# iris_1 = pd.DataFrame(x_train,columns=iris_dataset.feature_names)
# #利用DataFrame创建散点图矩阵,按y_train着色
# grr = pd.plotting.scatter_matrix(iris_1, c=y_train, figsize=(15, 15), marker='o',
#                         hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
# plt.show()

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)
x_new = np.array([[5,2.9,1,0.2]])
# print("x_new shape:{}".format(x_new.shape))
prediction = knn.predict(x_test)
# print(type(prediction))
# print("Predicted target name: {}".format(iris_dataset["target_names"][prediction]))
# print(iris_dataset)
# print('test score:{:.2f}'.format(np.mean(prediction==y_test)))


mglearn.plots.plot_knn_classification(n_neighbors=3)
plt.show()
