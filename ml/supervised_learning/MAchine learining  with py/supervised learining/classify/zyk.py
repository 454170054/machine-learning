import cv2
import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split,cross_val_score,cross_validate
from sklearn.externals import joblib

def getfilenames(file):
    file_name = os.listdir(file)
    return file_name


def grey_values():
    labels = []
    label = [0,1]
    list_means =[]
    root = ['D:\\zyk\\zyk\\1','D:\\zyk\\zyk\\0']
    for i in range(len(root)):
        allfilenames = getfilenames(root[i])
        for k in range(len(allfilenames)):
            filenames = root[i]+"\\"+allfilenames[k]
            img=cv2.imread(filenames,0)
            first_means = np.mean(img,axis=1)
            first_means = np.reshape(first_means,(1,-1))
            first_means = first_means.flatten()
            labels.append(i)
            list_means.append(first_means.tolist())
    hmeans = np.array(list_means)
    labels = np.array(labels)
    return hmeans,labels

x,y = grey_values()
# x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1)
clf = LinearSVC(C=10)
score = cross_val_score(clf,x,y,cv=10)
# joblib.dump(clf, "train_model.m")



# def statistic_value(root):
#     allfilenames = getfilenames(root)
#     list_mean = []
#     for i in range(len(allfilenames)):
#         filenames = root+"\\"+allfilenames[i]
#         img=cv2.imread(filenames,0)
#         first_means = np.mean(img,axis=1)
#         final_mean = np.mean(first_means,axis=0)
#         list_mean.append(final_mean)
#     std = np.std(np.reshape(list_mean,(1,-1)))
#     mean = np.mean(np.reshape(list_mean,(1,-1)))
#     return std,mean


# a = 'D:\\zyk\\1'
# b = 'D:\\zyk\\0'
# c = 'D:\\zyk\\2'
# std_1,mean_1 = statistic_value(a)
# std_0,mean_0 = statistic_value(b)
# list_test_file = getfilenames(c)
# for i in range(len(list_test_file)):
#     filenames = c + "\\" + list_test_file[i]
#     img = cv2.imread(filenames,0)
#     first_means = np.mean(img, axis=1)
#     final_mean = np.mean(first_means, axis=0)
#     if mean_1-1.5*std_1 < final_mean <mean_1+1.5*std_1:
#         print("1")
#     else:
#         print("0")
