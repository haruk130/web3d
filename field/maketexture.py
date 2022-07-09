import cv2
import numpy
import copy
import math
import os
from PIL import Image

path = os.path.dirname(os.path.abspath(__file__))

ifile = "texture/stone.jpg"
ofile = "texture/img.js"

image = numpy.asarray(Image.open(ifile))
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("original size: "+str(image.shape)) # show original size

#size = input("input size: ")
size = 128
#image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE) # rotate image
image = cv2.resize(image,(int(size),int(size))) # resize image
image = cv2.blur(image,(2,2))
#cv2.imwrite("a.png",image)
print("size: "+str(image.shape)) # show resized size

message = """"""
if image.shape[2]==4:
    rt = ""
    rt += message
    rt += "[\n"
    for y in range(image.shape[0]-1):
        rt += "    ["
        for x in range(image.shape[1]-1):
            rt += "["+str(image[y,x][0])+","+str(image[y,x][1])+","+str(image[y,x][2])+","+str(image[y,x][3])+"],"
        rt += "],"
    rt += "\n],"
else:
    rt = ""
    rt += message
    rt += "[\n  "
    for y in range(image.shape[0]-1):
        rt += "["
        for x in range(image.shape[1]-1):
            rt += "["+str(image[y,x][0])+","+str(image[y,x][1])+","+str(image[y,x][2])+",255"+"],"
        rt += "],"
    rt += "\n],"



#print(rt)
with open(ofile, mode='w') as f:
    f.write(rt)