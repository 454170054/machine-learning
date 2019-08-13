# -*- coding: utf-8 -*-
from sklearn.linear_model import  Ridge
from sklearn.model_selection import train_test_split
import mglearn
from sklearn.linear_model import LinearRegression
import pandas as pd
import pyecharts
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False

x,y = mglearn.datasets.load_extended_boston()
fig,axes = plt.subplots(2,1,figsize=(10,5))
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)
model1 = LinearRegression()
model1.fit(x_train,y_train)
alpha = [0.1,1,10]
classlabel = ['s','^','v']
for i in range(len(alpha)):
    model = Ridge(alpha=alpha[i]).fit(x_train,y_train)
    axes[0].plot(model.coef_,'{}'.format(classlabel[i]),label = "Ridge alpha = {}".format(alpha[i]))
axes[0].plot(model1.coef_,'o',label = 'LinearRegression')
axes[0].hlines(0,0,len(model1.coef_))
axes[0].set_ylim(-25,25)
axes[0].set_xlabel("特征")
axes[0].set_ylabel("回归系数")
axes[0].legend(loc='best')
mglearn.plots.plot_ridge_n_samples()
plt.show()
# data = np.array([
#         [-2.95507616,10.94533252],
#         [-0.44226119,2.96705822],
#         [-2.13294087,6.57336839],
#         [1.84990823,5.44244467],
#         [0.35139795,2.83533936],
#         [-1.77443098,5.6800407],
#         [-1.8657203 ,6.34470814],
#         [1.61526823,4.77833358],
#         [-2.38043687,8.51887713],
#         [-1.40513866,4.18262786]
#             ])
# plt.scatter(data[:,0],data[:,1])
# print(data[:,0])
# x = data[:,0].reshape(-1,1)
# y = data[:,1]
# print(np.shape(x))
# print(x)
# Ridge = Ridge(alpha=0.1).fit(x,y)
# predict = Ridge.predict(x)
# plt.plot(x,predict)
# plt.show()