from numpy import double
from scipy.misc import face

paths = [
    ["./room.stl",[212,210,254],[0,0,-0.2]],
    ["./hand1.stl",[210,140,50],[0,-5,1]],
    ["./icosphere.stl",[255,160,30],[0,0,1]],
    ["./human.stl",[200,200,200],[5,5,0]],
    ["./whatisthis.stl",[200,210,210],[5,-5,2.2]],
    ["./saturn.stl",[230,160,50],[-5,0,1]],
]

lt = "scene = {};\n"

lt += "scene['home'] = "
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

lt += "]];\n"

paths = [
    ["./truck.stl",[212,210,254],[0,0,-0.2]],
]

lt += "scene['truck'] = "
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

lt += "]];\n"

paths = [
   ["./cubes.stl",[250,255,254],[0,0,30]],
]

lt += "scene['blocks'] = "
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

lt += "]];\n"

paths = [
   ["./triangle.stl",[250,255,254],[0,0,0]],
]

lt += "scene['triangle'] = "
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

lt += "]];\n"

paths = [
    ["./tdbgtitle.stl",[250,150,80],[-5,-10,1]],
    ["./human.stl",[220,200,200],[-4,-10,1]],
]

lt += "scene['tdbgtitle'] = "
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

lt += "]];\n"

path_w = './object.js'

wf = open(path_w, mode='w')
wf.write(lt)

lt = ""
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
        lt += 'new Polygon() {'
        lt += " pos = new double[][] {"
        lt += "new double[] {"+fctl[i][0]+","+fctl[i][1]+","+fctl[i][2]+"},new double[] {"+fctl[i][3]+","+fctl[i][4]+","+fctl[i][5]+"},new double[] {"+fctl[i][6]+","+fctl[i][7]+","+fctl[i][8]+"},"
        # lt += color
        lt += "},"
        lt += '},'


path_w = './object.cs'

wf = open(path_w, mode='w')
wf.write(lt)