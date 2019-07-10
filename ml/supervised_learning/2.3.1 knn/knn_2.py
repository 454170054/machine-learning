from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
cancer = load_breast_cancer()
x_train,x_test,y_train,y_test = train_test_split(cancer.data,cancer.target,stratify=cancer.target
                                                 ,random_state=66)
train_accuracy = []
test_accuracy = []
neighbors = range(1,11)
for neighbor in neighbors:
    model = KNeighborsClassifier(n_neighbors=neighbor)
    model.fit(x_train,y_train)
    train_accuracy.append(model.score(x_train,y_train))
    test_accuracy.append(model.score(x_test,y_test))
plt.plot(neighbors,train_accuracy,label="train_accuracy")
plt.plot(neighbors,test_accuracy,label="test_accuracy",linestyle="--")
plt.legend()
plt.xlabel("neighbors")
plt.ylabel("accuracy")
plt.show()
