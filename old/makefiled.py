import cv2
import numpy
import copy
import math
import os
from PIL import Image

blocks = [
    [1000,[135,125,123]], # 道
    [200 ,[185,122,87]], # 土
    [300 ,[181,230,29]], # 草
    [301 ,[34,177,76]], # 草
    [302 ,[68,223,9]], # 草
    [400 ,[200,191,231]], # 花
    [500 ,[65,90,70]], # 石
]


def length3d_s(pos) :
    return (pos[0][0]-pos[1][0])**2+(pos[0][1]-pos[1][1])**2+(pos[0][2]-pos[1][2])**2

path = os.path.dirname(os.path.abspath(__file__))

ifile = "field/field.png"
ifileb = "field/fieldblock.png"
ofile = "field/field.js"

image = cv2.imread(ifile)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageb = cv2.imread(ifileb)
imageb = cv2.cvtColor(imageb, cv2.COLOR_BGR2RGB)
print("original size: "+str(image.shape)) # show original size

size = input("input size: ").split(" ")
image = cv2.blur(image,(80,80))
image = cv2.resize(image,(int(size[0]),int(size[1]))) # resize image
imageb = cv2.resize(imageb,(int(size[0]),int(size[1]))) # resize image
# cv2.imwrite("a.png",image)
# cv2.imwrite("b.png",imageb)
print("size: "+str(image.shape)) # show resized size

min = image.min()
max = image.max()

max_elev = 255*0.5*0.3

scale = (max_elev/(max-min))

message = """"""
rt = ""
rt += message

f= "\nfield = [\n"
b= "\nfieldblock = [\n"
for y in range(image.shape[0]-1):
    f += "    ["
    b += "    ["
    for x in range(image.shape[1]-1):
        f += '{:5.2f}'.format((max_elev-(image[y,x]*scale-min*scale)+5)) + ','

        px = imageb[y,x]
        lengt = 255**3
        block = 0
        for bl in blocks:
            l = length3d_s([px.tolist(),bl[1]])
            # print (([l,px.tolist(),bl[1]]))
            if l<lengt:
                lengt = l
                block = bl[0]
        b += str(block)+","

    f += "],\n"
    b += "],\n"
f += "]"
b += "]"
rt += f
rt += b

#print(rt)
with open(ofile, mode='w') as f:
    f.write(rt)