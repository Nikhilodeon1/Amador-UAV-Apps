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
            #for reference on how i got these equations, go here: https://www.desmos.com/calculator/9gtrrft4ug
            xlist.append(((((2.703853047*(10**-7))/float(maindata[0]))*elm[0])+((1.00001*(float(maindata[1])))-0.000624082)))
            ylist.append(((((6.9855*(10**-8))/float(maindata[0]))*elm[1])+((1.00001*(float(maindata[2])))-0.000624082)))
        for elm in range(0, int(maindata[-1])):
            out_file.write(str(round(xlist[elm], 6)) + " " + str(round(ylist[elm], 6)) + "\n")
#coords may be slighly offset due to rounding errors
