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
            record[field.strip()] = (value)
        recordList.append(record)
        # print(json.dumps(recordList, indent = 4))
        # if (index > 5):
        #     break
    return recordList

def matching(gaiaData):
    b, v = numpy.loadtxt("./data/m5.txt", usecols = (6, 9), unpack = True)

    xAxisArray = []
    yAxisArray = []

    for i, value in enumerate(b):
        if (b[i]-v[i] < 50):
            xAxisArray.append(b[i]-v[i])
            yAxisArray.append(v[i])

    matchingGaiaValuesX = []
    matchingGaiaValuesY = []

    for data in gaiaData:
        # print("proccessing: {} {}".format(data['Bmag'],data['Vmag']))
        try:
            b_vMag = float(data['BP-RP'].strip())
        except ValueError:
            # print("Error while converting Bmag: {}".format(data['Bmag']))
            continue
        try:
            vMag = float(data['RPmag'].strip())
        except ValueError:
            # print("Error while converting Vmag: {}".format(data['Vmag']))
            continue
        for xValue, yValue in zip(xAxisArray, yAxisArray):
            if ((round((b_vMag), 0) == round((xValue)), 0) and (round((vMag), 0) == round((yValue), 0))):
                matchingGaiaValuesX.append(xValue)
                matchingGaiaValuesY.append(yValue)

    plt.scatter(matchingGaiaValuesX, matchingGaiaValuesY)
    plt.gca().invert_yaxis()
    plt.ylabel('V')
    plt.xlabel('B-V')

    plt.show()

def main():
    gaiaData = readData("./data/gaia_data_m5.txt")
    matching(gaiaData)


main()
