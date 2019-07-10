import mglearn
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import numpy as np
# mglearn.plots.plot_knn_regression(n_neighbors=3)
# plt.show()

x,y = mglearn.datasets.make_wave(n_samples=40)
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)
# knr = KNeighborsRegressor(n_neighbors=3)
# knr.fit(x_train,y_train)
# print("test accuracy:{:.2f}".format(knr.score(x_test,y_test)))
fig,axes = plt.subplots(1,3,figsize=(15,4))
line = np.linspace(-3,3,1000).reshape(-1,1)
print(line)
for neighbors,ax in zip([1,3,9],axes):
    reg = KNeighborsRegressor(n_neighbors=neighbors)
    reg.fit(x_train,y_train)
    ax.plot(line,reg.predict(line))
    ax.plot(x_train,y_train,'^',c=mglearn.cm2(0),markersize=8)
    ax.plot(x_test,y_test,'o',c=mglearn.cm2(1),markersize=8)
    ax.set_title("{}neighbors \ntrain score{:.2f} test score{:.2f} ".format(neighbors,
                 reg.score(x_train,y_train),reg.score(x_test,y_test))
                 )
    plt.xlabel("Feature")
    plt.ylabel("Target")
axes[0].legend(["model predictions","train data/target","test data/target"],loc='best')
plt.show()