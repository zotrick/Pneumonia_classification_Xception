import os
import sys
import numpy as np
import cv2
from glob import glob

def create_folder(folder):
    try:
        os.makedirs(folder)
    except OSError:
        print("Created")
#        print ("Creation of the directory %s failed" % path)
    else:
        print("Error: Non Created")
#        print ("Successfully created the directory %s " % path)

def remove_border(img, threshold=0):
    "Crop image, throwing away the border below the threshold"
    mask = img > threshold
    return img[np.ix_(mask.any(1), mask.any(0))]

def crop_center(img, size):
    "Crop center sizexsize of the image"
    y, x = img.shape
    startx = (x - size) // 2 
    starty = (y - size) // 2
    return img[starty:starty+size, startx:startx+size]

def bigger_edge(img):
    y, x = img.shape
    return y if y < x else x


def preprocess(path, save_path, size=512):
    files = glob(path+"*.jpg")
    num = len(files)
    for ix, i in enumerate(files):
        
        filename = os.path.basename(i)
        print('Preprocessing {} - {} %'.format(filename, int(ix / num * 100)), end='\r')
        
        img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
        
        # Remove black border (sometimes there is a black band)
        img_noborder = remove_border(img)
        # Find bigger edge
        edge = bigger_edge(img_noborder)
        # Crop center
        img_cropped = crop_center(img_noborder, edge)
        # Resize to final size
        img_final = cv2.resize(img_cropped, (size, size), interpolation = cv2.INTER_AREA)
        # Save preproccesed image        
        cv2.imwrite(save_path+filename, img_final, [int(cv2.IMWRITE_PNG_COMPRESSION), 1])
        
    
#path = os.getcwd()
SIZE = 299
path = "C:\\Users\\Eduardo\\Documents\\Datasets\\Pneumonia\\" 

inDir= path+"\\training\\NORMAL\\"
outDir= path+"\\prep\\training\\NORMAL\\"
create_folder(outDir)
preprocess(inDir, outDir, SIZE)

inDir= path+"\\training\\PNEUMONIA\\"
outDir= path+"\\prep\\training\\PNEUMONIA\\"
create_folder(outDir)
preprocess(inDir, outDir, SIZE)

inDir= path+"\\validation\\NORMAL\\"
outDir= path+"\\prep\\validation\\NORMAL\\"
create_folder(outDir)
preprocess(inDir, outDir, SIZE)

inDir= path+"\\validation\\PNEUMONIA\\"
outDir= path+"\\prep\\validation\\PNEUMONIA\\"
create_folder(outDir)
preprocess(inDir, outDir, SIZE)

inDir= path+"\\testing\\NORMAL\\"
outDir= path+"\\prep\\testing\\NORMAL\\"
create_folder(outDir)
preprocess(inDir, outDir, SIZE)

inDir= path+"\\testing\\PNEUMONIA\\"
outDir= path+"\\prep\\testing\\PNEUMONIA\\"
create_folder(outDir)
preprocess(inDir, outDir, SIZE)