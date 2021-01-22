# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:02:09 2019

@author: Eduardo
"""
import os
import random
from shutil import copyfile

def create_folders(TR_1, VAL_1, TR_2, VAL_2):
    try:
        os.makedirs(TR_1)
        os.makedirs(TR_2)
        
        os.makedirs(VAL_1)
        os.makedirs(VAL_2)
        
    except OSError:
        print("Created")
#        print ("Creation of the directory %s failed" % path)
    else:
        print("Error: Non Created")
#        print ("Successfully created the directory %s " % path)
        
def split_data(SOURCE, TRAINING, VALIDATION, SPLIT_SIZE):
    filenames =os.listdir(SOURCE)
    filenames.sort()
    random.seed(55)
    random.shuffle(filenames)
    
    
    split_1 = int(SPLIT_SIZE[0] * len(filenames))
    train_filenames = filenames[:split_1]
    valid_filenames = filenames[split_1:]
    for num, file in enumerate(train_filenames):
        if os.path.getsize(SOURCE  + file) != 0:
            copyfile(SOURCE +  file, TRAINING + "\\" + file)
    for num, file in enumerate(valid_filenames):
        if os.path.getsize(SOURCE  + file) != 0:
            copyfile(SOURCE +  file, VALIDATION + "\\" + file)
        

path = "C:\\Users\\Eduardo\\Datasets\\Pneumonia\\Original\\" 
DIP_SOURCE_DIR = path+"\\PNEUMONIA\\"
TRAINING_DIP_DIR = path+"\\training\\PNEUMONIA\\"
VALIDATION_DIP_DIR = path+"\\validation\\PNEUMONIA\\"
NONDI_SOURCE_DIR = path+"\\NORMAL\\"
TRAINING_NONDI_DIR = path+"\\training\\NORMAL\\"
VALIDATION_NONDI_DIR = path+"\\validation\\NORMAL\\"

TRAINING_DIR = path+"\\training"
VALIDATION_DIR = path+"\\validation"
# %%
#Split dataset
split_size = [0.8,0.2]
create_folders(TRAINING_DIP_DIR, VALIDATION_DIP_DIR, TRAINING_NONDI_DIR, VALIDATION_NONDI_DIR)

split_data(DIP_SOURCE_DIR, TRAINING_DIP_DIR, VALIDATION_DIP_DIR, split_size)
split_data(NONDI_SOURCE_DIR, TRAINING_NONDI_DIR, VALIDATION_NONDI_DIR, split_size)