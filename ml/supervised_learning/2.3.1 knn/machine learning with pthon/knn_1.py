from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import mglearn
import matplotlib.pyplot as plt
x,y = mglearn.datasets.make_forge()
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)
# clf = KNeighborsClassifier(n_neighbors=3)
# clf.fit(x_train,y_train)
# print(clf.predict(x_test))
# print("test set accuracy:{:.2f}".format(clf.score(x_test,y_test)))

fig,axes = plt.subplots(1,3,figsize=(10,5))
for neighbors,ax in zip([1,3,9],axes):
    clf = KNeighborsClassifier(n_neighbors=neighbors).fit(x,y)
    mglearn.plots.plot_2d_separator(clf, x, fill=True, eps=0.5, ax=ax, alpha=.4)
    mglearn.discrete_scatter(x[:, 0], x[:, 1], y, ax=ax)
    ax.set_title("{} neighbor(s)".format(neighbors))
    ax.set_xlabel("Feature 0")
    ax.set_ylabel("Feature 1")
axes[0].legend(loc=3)
plt.show()
