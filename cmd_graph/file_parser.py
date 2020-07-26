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

def plotVBV(recordListV, recordListB):

    xAxisArray = []
    yAxisArray = []
    for recordB in recordListB:
        # print("{} Adding:{}".format(index, json.dumps(record, indent = 4)))
        for recordV in recordListV:
            if (math.floor(recordB['X']) == math.floor(recordV['X']) and math.floor(recordB['Y']) == math.floor(recordV['Y'])):
                xAxisArray.append((recordB['Mag']) - (recordV['Mag']))
                yAxisArray.append((recordV['Mag']))
        # rounding to the nearest 5 for the x and y coordinates
        # for recordV in recordListV:
        #     if (myround(recordB['X']) == myround(recordV['X']) and myround(recordB['Y']) == myround(recordV['Y'])):
        #         xAxisArray.append((recordB['Mag']) - (recordV['Mag']))
        #         yAxisArray.append((recordV['Mag']))
    # print(xAxisArray)
    # print(yAxisArray)
    plt.scatter(xAxisArray, yAxisArray)
    plt.gca().invert_yaxis()
    plt.ylabel('V')
    plt.xlabel('B-V')
    #plt.title("M12")
    plt.show()

def myround(x, base=5):
    return base * round(x/base)


def main():
    recordListB = readData("./data/M12_B.txt")
    recordListV = readData("./data/M12_V.txt")
    plotVBV(recordListV, recordListB)


main()
