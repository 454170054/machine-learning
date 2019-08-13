import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
x,y = mglearn.datasets.make_wave(n_samples=60)
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42)
model = LinearRegression()
model.fit(x_train,y_train)
pred1 = model.predict(x_train)
pred2 = model.predict(x_test)
plt.scatter(x_train,y_train)
plt.plot(x_train,pred1)
plt.plot(x_test,pred2)
plt.show()
print(model.score(x_train,y_train))
print(model.score(x_test,y_test))