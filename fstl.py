from numpy import double
from scipy.misc import face

# 150000000000m = 150000000km = 1au
# 1000 = 1km

# 150000 = 1au
paths = [
#    ["./icosphere.stl",[230,160,50],[0,0,0]],
    ["./whatisthis.stl",[200,200,200],[0,0,0]],
    ["./saturn.stl",[230,160,50],[-6,1,-1]],
]

lt = "cube = "
lt += "[ [0],"
lt += "["

for path in paths:
    with open(path[0]) as f:
        data = f.readlines()

    color = "[0],["+str(path[1][0])+"],["+str(path[1][1])+"],["+str(path[1][2])+"],"

    fctl = []
    lfctl = []
    c = 0

    for l in data:
        if (l.startswith("vertex")):
            c+=1
            ld = l.replace("\n","").split(" ")
            lfctl.append(str(double(ld[1])+path[2][0]))
            lfctl.append(str(double(ld[2])+path[2][1]))
            lfctl.append(str(double(ld[3])+path[2][2]))
            if (c%3==0):
                fctl.append(lfctl)
                # print(lfctl)
                lfctl = []
    for i in range(len(fctl)):
        lt += '['
        lt += "["+fctl[i][0]+","+fctl[i][1]+","+fctl[i][2]+"],["+fctl[i][3]+","+fctl[i][4]+","+fctl[i][5]+"],["+fctl[i][6]+","+fctl[i][7]+","+fctl[i][8]+"],"
        lt += color
        lt += "[0],"
        lt += '],'

lt += "]]"

path_w = './object.txt'

wf = open(path_w, mode='w')
wf.write(lt)