from numpy import double
from scipy.misc import face


path = "./whatisthis.stl"

with open(path) as f:
    data = f.readlines()


fctl = []
lfctl = []
c = 0

for l in data:
    if (l.startswith("vertex")):
        c+=1
        ld = l.replace("\n","").split(" ")
        lfctl.append(str(double(ld[1])))
        lfctl.append(str(double(ld[2])))
        lfctl.append(str(double(ld[3])))
        if (c%3==0):
            fctl.append(lfctl)
            # print(lfctl)
            lfctl = []

lt = "cube = "
lt += "[ [0],"
lt += "["

for i in range(len(fctl)):
    lt += '['
    lt += "["+fctl[i][0]+","+fctl[i][1]+","+fctl[i][2]+"],["+fctl[i][3]+","+fctl[i][4]+","+fctl[i][5]+"],["+fctl[i][6]+","+fctl[i][7]+","+fctl[i][8]+"],"
    lt += "[100000],[0,0],[0,128],[128,128]"
    lt += '],'

lt += "]]"

# print(lt)

path_w = './object.txt'

wf = open(path_w, mode='w')
wf.write(lt)