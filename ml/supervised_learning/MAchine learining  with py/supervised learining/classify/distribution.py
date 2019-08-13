import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
from collections import Counter
# img = cv2.imread('D:\\zyk\\zyk\\1\\1.2.840.887072.1.9.1.1.20140827083819.54.17216126.png',0)
# a = img.flatten()
# a = a.tolist()

def listdir(file,allfilenames):
    list_dirs = os.listdir(file)
    for list_dir in list_dirs:
        file_name = os.path.join(file,list_dir)
        if os.path.isdir(file_name):
            listdir(file_name,allfilenames)
        else:
            allfilenames.append(file_name)
    return allfilenames

# def getfilenames(file):
#     second_file_name = os.listdir(file)
#     all_filenames = []
#     labels = []
#     for i in range(len(second_file_name)):
#         file_names = os.listdir(file + '\\'+ second_file_name[i])
#         for file_name in file_names:
#             a = file + '\\' +second_file_name[i] + '\\' +file_name
#             all_filenames.append(a)
#             labels.append(i)
#     return all_filenames,labels

def get_grey_values(filenames,allfilenames):
    # all_filenames,labels = getfilenames(filenames)
    all_filenames = listdir(filenames,allfilenames)
    classify = []
    for i in range(len(all_filenames)):
        img = cv2.imread(all_filenames[i], 0)
        greyvalues = img.flatten()
        greyvalues = greyvalues.tolist()
        greyvalues = sorted(greyvalues)
        frequency = Counter(greyvalues)
        keys = []
        values = []
        for key, value in dict(frequency).items():
            keys.append(key)
            values.append(value)
        keys = np.array(keys)
        values = np.array(values)
        if values[-1] > 40000:
            classify.append(0)
        else:
            classify.append(1)
    return classify
allfilenames = []
classifys = get_grey_values('D:\\zyk\\zyk\\3',allfilenames)
print(classifys)
# img = cv2.imread()
# greyvalues = img.flatten()
# greyvalues = greyvalues.tolist()
# greyvalues = sorted(greyvalues)
# frequency = Counter(greyvalues)
# keys = []
# values = []
# for key, value in dict(frequency).items():
# keys.append(key)
# values.append(value)
# keys = np.array(keys)
# values = np.array(values)