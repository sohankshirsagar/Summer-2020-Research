import math
import re
import json
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

def plot(recordList):
    xAxisArray = []
    yAxisArray = []
    for data in recordList:
        # print("proccessing: {} {}".format(data['Bmag'],data['Vmag']))
        b_vMag = data['B_V']
        vMag = data['V']

        if (data['B_V'] == 0.0):
            continue

        xAxisArray.append(b_vMag)
        yAxisArray.append(vMag)

    plt.scatter(xAxisArray, yAxisArray)
    plt.gca().invert_yaxis()
    plt.ylabel('V')
    plt.xlabel('B-V')
    plt.show()

def main():
    recordList = readData("./data/m55.txt")
    plot(recordList)

main()
