### Introduction
The main purpose of this repo is to convert the Google Open Images' annotation files to COCO format, so we can use coco evaluator.
There are 4 scripts here. The first one let you choose your desired classes for transfer learning. If you only want to select some of Open Images' classes and evaluate your model, first you need to create a csv file for them. The script asks you to put the classes name( it should be the classes that exist in open images).
Second script creates a coco format json file from the csv file that was created before. The third one convert the hexadecimal to integer since there was an issue, and uses the int as a key. After this process, you can use the 4th script which is coco evaluator.
### Future work
Since the number of classes in OpenImages is different from coco, we cannot trust the accuracy. The number of classes needs to be compatible.
