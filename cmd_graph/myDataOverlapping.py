import math
import re
import json
import numpy
import matplotlib.pyplot as plt

def readData(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()
    fieldNames = []
    recordList = []
    for index, line in enumerate(lines):
        fields = re.split("\s+", line.strip())
        if (index == 0):
            fieldNames = fields
            # print(fieldNames)
            continue
        if (len(fields) < len(fieldNames)-1):
            # print("Skipping Line: {}".format(line))
            continue
        # if (len(fields) != len(fieldNames)):
        #     fields.append("")
        record = {}
        for field, value in zip(fieldNames, fields):
            record[field.strip()] = float(value)
        recordList.append(record)
        # print(json.dumps(recordList, indent = 4))
        # if (index > 5):
        #     break
    return recordList

def plotVBV(title, recordListB, recordListV, fileIso, age1, age1String, age2, age2String, age1X, age1Y, age2X, age2Y, outImageFileName):

    xAxisArray = []
    yAxisArray = []
    for recordB in recordListB:
        # print("{} Adding:{}".format(index, json.dumps(record, indent = 4)))
        for recordV in recordListV:
            if (math.floor(recordB['X']) == math.floor(recordV['X']) and math.floor(recordB['Y']) == math.floor(recordV['Y'])):
                xAxisArray.append((recordB['Mag']) - (recordV['Mag']))
                yAxisArray.append((recordV['Mag']))
    # print(xAxisArray)
    # print(yAxisArray)
    plt.scatter(xAxisArray, yAxisArray, color = "red")
    plt.gca().invert_yaxis()
    plt.ylabel('V')
    plt.xlabel('B-V')
    plt.title(title)

    loga, logl, logte = numpy.loadtxt(fileIso, usecols = (0, 3, 4), unpack = True)

    w7 = numpy.where(loga == age1)
    w8 = numpy.where(loga == age2)

    plt.plot(-logte[w7] + age1X, -logl[w7] + age1Y, label= age1String)
    plt.plot(-logte[w8] + age2X, -logl[w8] + age2Y, label= age2String)

    # plt.xlabel("Log(Teff)")
    # plt.ylabel("Log L")
    # plt.axis([5.0, 3.5, 0, 6])
    plt.legend(loc= "lower left")

    plt.show()

def main():
    recordListB = readData("./data/M12_B.txt")
    recordListV = readData("./data/M12_V.txt")
    plotVBV("M12", recordListB, recordListV, "./data/iso_jc_z070s.dat", 10.1, "12.6 Gyr", 10.15, "14.1 Gyr", 3.28, 18, 3.28, 18, "./outputGraphs/M12_Iso.jpg")

main()
