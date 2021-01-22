# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:10:43 2019

@author: Eduardo
"""

# Open all data set and save it like numpy array

import numpy as np
from glob import glob
import cv2
import os
from tempfile import TemporaryFile
# %%
def get_label(path, CLASSES_NAME):
    parts =  path.split('\\')
    l = parts[-2] == CLASSES_NAME
    label = np.argwhere(l)
    return label

def load_dataset(path, TRAINING_DIR):

    CLASSES_NAME = np.array(os.listdir(TRAINING_DIR))
    filenames_train = glob(TRAINING_DIR+"*\\*")
    
    x = []
    y = []
    for ix, i in enumerate(filenames_train):
        im = np.array(cv2.imread(i))
        im = np.reshape(im, (299,299,3))
        x.append(im)
        y.append(get_label(i, CLASSES_NAME))
        #print(ix)

    
    X_train = np.array(x)
    Y_train = y
    
    
    return X_train, Y_train


def save_numpyz(X_train, Y_train, X_val, Y_val, X_test, Y_test):
    
    np.savez('pneumonia_undersampling_xc_dataset.npz', x_train=X_train, y_train=Y_train,
             x_val=X_val, y_val=Y_val, x_test=X_test, y_test=Y_test )
    
    
path = "C:\\Users\\Eduardo\\Documents\\Datasets\\Pneumonia\\prep\\" 

TRAINING_DIR = path+"\\training\\"
VALIDATION_DIR = path+"\\validation\\"
TESTING_DIR = path+"\\testing\\"

print("Loading images and labels to numpy...")
X_train, Y_train = load_dataset(path, TRAINING_DIR)
X_val, Y_val = load_dataset(path, VALIDATION_DIR)
X_test, Y_test = load_dataset(path, TESTING_DIR)
#print("Saving dataset in numpy format...")
#np.save('x_train', X_train)
#np.save('x_val', X_val)
#np.save('x_test', X_test)
print("Reshape of labels...")
Y_train = np.reshape(Y_train, (len(Y_train),1))
Y_val = np.reshape(Y_val, (len(Y_val),1))
Y_test = np.reshape(Y_test, (len(Y_test),1))
#print("Saving Y to numpy...")
#np.save('y_train', Y_train)
#np.save('y_val', Y_val)
#np.save('y_test', Y_test)
print("Saving dataset in numpyz format...")
save_numpyz(X_train, Y_train, X_val, Y_val, X_test, Y_test)   

