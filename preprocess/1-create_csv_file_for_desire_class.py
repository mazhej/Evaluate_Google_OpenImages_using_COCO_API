import numpy as numpy
import pandas as pd 
import json
import csv
import os
import csv
import os, shutil
os.chdir('/home/maziar/WA/OI/convert_openIm_coco/annotations')

from os import listdir
from os.path import isfile, join

def mapping(class_description,validation_annotation):
    ''' 
    this function read class-description.csv and validation-annotation.csv and create a dictionary of them.
    then it gets the desired class (Fruit, Spoon, Man...) from the user and selects all the images related to that class .
    And save all the desired images names in a .txt file.
    '''
    #create a dictionary from class description file
    class_description = csv.reader(open(class_description, 'r'))
    d_class = {}
    for row in class_description:
        v, k= row
        d_class[k] = v

    #create a dictionary from validation annotations file - (LableName as Key, ImageID as Value)
    validation = csv.reader(open(validation_annotation, 'r'))
    d_valid = {}
    for row in validation:
        if row[2] not in d_valid:
            d_valid[row[2]] = []
        d_valid[row[2]].append(row[0])

    ##get the desired classes
    array = []
    for i in range(2):
        array.append(input("Enter desired class : "))
    ###

    LabelName = []
    for elements in array:
        for k , v in d_class.items():
            if elements == k:
                LabelName.append(d_class[k])

    #images as a list
    images_temp = []
    images = []
    for elements in LabelName:
        for k, v in d_valid.items():
            if elements == k :
                images_temp.append(d_valid[k])

    #add .jpg at the end of each element
    for image in images_temp:
        for jpg in image:
            images.append(str(jpg))



    return LabelName , images

labelname = [f for f in mapping('class-descriptions-boxable.csv','validation-annotations-bbox.csv')]
#imageid = [f[:16] for f in mapping('class-descriptions-boxable.csv','validation-annotations-bbox.csv')]


with open('validation-annotations-bbox.csv', 'r') as f ,open('validation-annotations-bbox-1.csv', 'w') as f_output:
    f.readline()
    reader = csv.reader(f)
    next(reader)
    csv_output = csv.writer(f_output) 
    csv_output.writerow(["ImageID","Source","LabelName","Confidence","XMin","XMax","YMin","YMax","IsOccluded","IsTruncated","IsGroupOf","IsDepiction","IsInside"])
    

    # read file row by row
    f.seek(0)
    for row in reader:
        if row[2] in labelname[0]:
            csv_output.writerow(row)

        # for image_id in labelname[0]:
        #     if image_id == row[2]:
        #         csv_output.writerow(row)

with open('validation-images-with-rotation.csv', 'r') as f ,open('validation-images-with-rotation-2.csv', 'w') as f_output:
    next(f)
    reader = csv.reader(f)
    csv_output = csv.writer(f_output) 
    csv_output.writerow(["ImageID","Subset","OriginalURL","OriginalLandingURL","License","AuthorProfileURL","Author","Title","OriginalSize","OriginalMD5","Thumbnail300KURL","Rotation"])
     
    
    # read file row by row
    f.seek(0)
    for row in reader:
        if row[0] in labelname[1]:
            csv_output.writerow(row)

print(onlyfiles)

