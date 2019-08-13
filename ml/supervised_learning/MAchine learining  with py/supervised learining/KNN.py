import numpy as np
import pandas as pd
# from sklearn.model_selection import train_test_split
import mglearn

from sklearn.neighbors import KNeighborsClassifier
data = load_iris()
x_train,x_test,y_train,y_test = train_test_split(data['data'],data['target'],random_state=0)
model = KNeighborsClassifier(3)
model.fit(x_train,y_train)
print(model.score(x_test,y_test))

