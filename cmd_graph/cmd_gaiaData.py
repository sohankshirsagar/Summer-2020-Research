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

def plotVBV(recordListV, recordListB, gaiaData):

    xAxisArray = []
    yAxisArray = []
    for recordB in recordListB:
        # print("{} Adding:{}".format(index, json.dumps(record, indent = 4)))
        for recordV in recordListV:
            if (math.floor(float(recordB['X'])) == math.floor(float(recordV['X'])) and math.floor(float(recordB['Y'])) == math.floor(float(recordV['Y']))):
                xValue = (float(recordB['Mag'])) - (float(recordV['Mag']))
                yValue = (float(recordV['Mag']))
                xAxisArray.append(xValue)
                yAxisArray.append(yValue)
        # rounding to the nearest 5 for the x and y coordinates
        # for recordV in recordListV:
        #     if (myround(recordB['X']) == myround(recordV['X']) and myround(recordB['Y']) == myround(recordV['Y'])):
        #         xAxisArray.append((recordB['Mag']) - (recordV['Mag']))
        #         yAxisArray.append((recordV['Mag']))
    # print(xAxisArray)
    # print(yAxisArray)
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
            if ((round((b_vMag), 3) == round((xValue)), 3) and (round((vMag), 3) == round((yValue), 3))):
                matchingGaiaValuesX.append(xValue)
                matchingGaiaValuesY.append(yValue)
    #print(removeValuesX)
    #print(removeValuesY)

    plt.scatter(matchingGaiaValuesX, matchingGaiaValuesY)
    plt.gca().invert_yaxis()
    plt.ylabel('V')
    plt.xlabel('B-V')
    plt.show()

def myround(x, base=5):
    return base * round(x/base)


def main():
    recordListB = readData("./data/M12_B.txt")
    recordListV = readData("./data/M12_V.txt")
    gaiaData = readData("./data/gaia_data_m12.txt")
    #print(gaiaData)
    plotVBV(recordListV, recordListB, gaiaData)


main()
