import pandas as pd
import numpy as np
data_1 = pd.read_csv("titanic_dataset.csv")
'''
print(type(data_1))
print(data_1.dtypes)
print(data_1.head())
print(data_1.shape)
print(data_1.tail(3))
print(data_1.columns)

print(data_1["survived"])

age = data_1["age"]
age = age.astype(int)
print(age )
for i in range(len(age)):
    if age.loc[i] == 0:
        age.loc[i] = "NaN"
age_null = pd.isna(age)
print(age_null)

pclass_messenger = [1,2,3]
pclass_for_price = {}
for i in pclass_messenger:
    pclass_rows = data_1[data_1["pclass"] == i]
    pclass_price = pclass_rows["fare"]
    pclass_price_mean = pclass_price.mean()
    pclass_for_price[i] = pclass_price_mean
print(pclass_for_price)


messenger_survived_class = data_1.pivot_table(index="pclass",values="survived",aggfunc=np.mean)
print(messenger_survived_class)


messenger_pclass_fare = data_1.pivot_table(index="pclass",values="fare",aggfunc=np.mean)
print(messenger_pclass_fare)

new_data_survived = data_1.sort_values("fare",ascending=False)
print(new_data_survived[0:10])
new_data_survived_index = new_data_survived.reset_index(drop=True)
print(new_data_survived_index)

drop_data1_na = data_1.dropna(axis=1)
drop_data1_columns = drop_data1_na.columns
drop_data1_columns = drop_data1_na.columns.tolist()
print(drop_data1_columns)
print(drop_data1_na)

def age_survived(data):
    if data['age']<18:
        return "children"
    else:
        return "adult"


age_for_survived = data_1.apply(age_survived,axis=1)

print(age_for_survived)
data_1["old"] = age_for_survived
age_by_survived = data_1.pivot_table(index="old",values="survived",aggfunc=np.mean)
print(age_by_survived)
'''
###series
series_name = data_1["name"]
print(series_name)
series_fare = data_1["fare"]
print(series_fare)
from pandas import Series
name_name = series_name.values
name_fare = series_fare.values
name_for_fare = Series(name_fare,index=name_name)
print(name_for_fare)
print(name_for_fare[1])
print(name_for_fare[["Yousseff, Mr. Gerious ","Zabour, Miss. Hileni"]])