import math
with open("input.in", "r") as file:
    inputList = (str(file.read())).split("\n")
    maindata = inputList[0].split(" ")
    inputList.pop(0)
    ulist = []
    for elm in inputList:
        wlist = elm.split(" ")
        e = []
        for elm2 in wlist:
            e.append(int(elm2))
        ulist.append(e)
    with open ('out.out', 'w') as out_file:
        xlist = []
        ylist = []
        for elm in ulist:
            xlist.append(float(maindata[1]) - (((-2.7038*(10**-7))*elm[0])+0.000737717))
            ylist.append(float(maindata[2]) - (((-6.9855*(10**-8))*elm[1])+0.000139849))
        for elm in range(0, int(maindata[-1])):
            out_file.write(str(round(xlist[elm], 5)) + " " + str(round(ylist[elm], 5)) + "\n")