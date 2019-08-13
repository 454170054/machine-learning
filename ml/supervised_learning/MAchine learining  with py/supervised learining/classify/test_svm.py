# -*- coding: utf-8 -*-
import os
import numpy as np
import cv2
from sklearn.externals import joblib
def listdir(file,allfilenames):
    list_dirs = os.listdir(file)
    for list_dir in list_dirs:
        file_name = os.path.join(file,list_dir)
        if os.path.isdir(file_name):
            listdir(file_name,allfilenames)
        else:
            allfilenames.append(file_name)
    return allfilenames

def grey_values(file,allfilenames):
    list_means =[]
    allfilenames = listdir(file,allfilenames)
    for filename in allfilenames:
        img=cv2.imread(filename,0)
        first_means = np.mean(img,axis=1)
        first_means = np.reshape(first_means,(1,-1))
        first_means = first_means.flatten()
        list_means.append(first_means.tolist())
    hmeans = np.array(list_means)
    return hmeans,allfilenames


def predict(file):
    '''1代表错误分类'''
    list_filenames = []
    test_data,allfilenames = grey_values(file,list_filenames)
    clf = joblib.load("train_model.m")
    classify = clf.predict(test_data)
    with open('classify.txt','w+') as fh:
        for i in range(len(classify)):
            if classify[i] == 1:
                fh.write(allfilenames[i] + '\n')

file = 'D:\\zyk\\zyk\\3'
predict(file)
