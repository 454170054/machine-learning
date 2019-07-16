import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
titanic = pd.read_csv('titanic.csv')
fig,axes = plt.subplots(1,2,figsize=(10,5))
# #直方图
# age1 = titanic['age'].dropna()
# sns.distplot(age1,kde=False,bins=30,ax=axes[0])
# sns.distplot(age1,ax=axes[1],rug=True)
# plt.show()


# #条形图
# sns.barplot(x='class',y='survived',hue='sex',data=titanic) #以sex对x轴作细分
# plt.show()


##计数图
# sns.countplot(x='deck',data=titanic,hue='sex')
# plt.show()


# #散点图
# # stripplot() 使用的方法是用少量的随机“抖动”调整分类轴上的点的位置，
# # swarmplot() 表示的是带分布属性的散点图。
# fig,axes = plt.subplots(1,2,figsize=(10,5))
# sns.stripplot(x='embarked',y='fare',data=titanic,ax=axes[0],jitter=1)
# #'jitter'参数控制抖动的大小
# sns.swarmplot(x='embarked',y='fare',data=titanic,ax=axes[1],hue='sex')
# plt.show()


##盒图
# fig,axes = plt.subplots(1,2,figsize=(10,5))
# values = titanic['class'].values
# labels = []
# for i in range(len(values)):
#     if values[i] not in labels:
#         labels.append(values[i])
# hue_order=np.intersect1d(titanic['who'],titanic['who'])
# print(hue_order)
# sns.boxplot(x='class',y='age',data=titanic,ax=axes[0])
# sns.boxplot(x='class',y='age',data=titanic,ax=axes[1],hue='who',
#             order=sorted(labels),hue_order=hue_order)
# plt.show()


# ##回归图
# iris = sns.load_dataset('iris')
# # fig,axes = plt.subplots(1,2,figsize=(10,5))
# # print(iris.sample(10))
# # sns.regplot(x='sepal_length',y='petal_length',data=iris,ax=axes[0])
# sns.lmplot(x='sepal_length',y='petal_length',col='species',data=iris)
# plt.show()


##热力图
# flights = sns.load_dataset("flights")
# flights.sample(10)
# f = flights.pivot("year","month","passengers")
# cmap = sns.diverging_palette(200,20,sep=20,as_cmap=True)
# sns.heatmap(f,annot=True,fmt='d',cmap=cmap)
# plt.xlabel('x')
# plt.xticks(rotation=45)
# plt.show()


