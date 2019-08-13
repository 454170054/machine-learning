from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import mglearn
x, y = mglearn.datasets.load_extended_boston()
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)
model = Lasso(alpha=0.01,max_iter=10000).fit(x_train,y_train)
print("score:{}".format(model.score(x_train,y_train)))
print("score:{}".format(model.score(x_test,y_test)))
