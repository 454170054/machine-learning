from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import mglearn
# x,y = mglearn.datasets.make_forge()
# x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1)
# fig,axes = plt.subplots(1,2,figsize=(10,5))
# for model,ax in zip([LinearSVC(),LogisticRegression()],axes):
#     clf = model.fit(x_train,y_train)
#     mglearn.plots.plot_2d_separator(clf, x, fill=False, eps=0.5,ax=ax, alpha=.7)
#     mglearn.discrete_scatter(x[:, 0], x[:, 1], y, ax=ax)
#     ax.set_title("{}".format(clf.__class__.__name__))
#     ax.set_xlabel("Feature 0")
#     ax.set_ylabel("Feature 1")
# axes[0].legend()
# plt.show()

from sklearn.datasets import load_breast_cancer
cancer_data = load_breast_cancer()
x_train,x_test,y_train,y_test = train_test_split(cancer_data.data,cancer_data.target,stratify=cancer_data.target,
                                                 random_state=42)

# lsvm = LinearSVC(C=100).fit(x_train,y_train)
# print("Training set score: {:.3f}".format(lsvm.score(x_train, y_train)))
# print("Test set score: {:.3f}".format(lsvm.score(x_test, y_test)))
# mglearn.plots.plot_linear_svc_regularization()
# plt.show()
