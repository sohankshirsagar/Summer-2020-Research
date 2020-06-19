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
        fields = re.split("\s\s+", line.strip())
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
            record[field.strip()] = value
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
            if (recordB['X'] == recordV ['X'] and recordB['Y'] == recordV['Y']):
                xAxisArray.append(float(recordB['Mag']) - float(recordV['Mag']))
                yAxisArray.append(float(recordV['Mag']))
    # print(xAxisArray)
    # print(yAxisArray)
    plt.scatter(xAxisArray, yAxisArray)
    plt.ylabel('V')
    plt.xlabel('B-V')
    plt.show()


def main():
    recordListB = readData("./data/439Points.txt")
    recordListV = readData("./data/555Points.txt")
    plotVBV(recordListV, recordListB)

main()
