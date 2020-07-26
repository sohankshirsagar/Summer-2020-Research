import math
import re
import json
import numpy
import matplotlib.pyplot as plt

"""
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


def plotVBV(gaiaData):
    v, err_V, b_v, err_BV = numpy.loadtxt("./data/m3.txt", usecols = (3, 4, 5, 6), unpack = True)

    xAxisArray = []
    yAxisArray = []

    for i in range(len(b_v)):
        if b_v[i] > 1.2:
            continue
        if err_V[i] > 0.05 or err_BV[i] > 0.05:
            continue
        xAxisArray.append(b_v[i])
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
            if ((round((b_vMag), 3) == round((xValue)), 3) and (round((vMag), 3) == round((yValue), 3))):
                matchingGaiaValuesX.append(xValue)
                matchingGaiaValuesY.append(yValue)


    plt.scatter(matchingGaiaValuesX, matchingGaiaValuesY, color = "red")
    plt.gca().invert_yaxis()
    plt.ylabel('V')
    plt.xlabel('B-V')
    plt.title("M3")

    loga, logl, logte = numpy.loadtxt("./data/isoc_z008m.dat", usecols = (0, 3, 4), unpack = True)

    w7 = numpy.where(loga == 10.00)
    w8 = numpy.where(loga == 10.05)

    plt.plot(-logte[w7] + 4.3 , -logl[w7] + 19.4,label= "141 Myr")
    plt.plot(-logte[w8] + 4.3, -logl[w8] + 19.4,label= "159 Gyr")


    plt.legend(loc= "lower left")

    plt.show()

def main():
    gaiaData = readData("./data/m3_gaia_data.txt")
    plotVBV(gaiaData)



main()

"""


v, err_V, b_v, err_BV = numpy.loadtxt("./data/m3.txt", usecols = (3, 4, 5, 6), unpack = True)

xAxisArray = []
yAxisArray = []

for i in range(len(b_v)):
    if b_v[i] > 1.2:
        continue
    if err_V[i] > 0.05 or err_BV[i] > 0.05:
        continue
    xAxisArray.append(b_v[i])
    yAxisArray.append(v[i])

plt.scatter(xAxisArray, yAxisArray, color = "red")
plt.gca().invert_yaxis()
plt.ylabel('V')
plt.xlabel('B-V')
plt.title("M3")

# loga, logl, logte = numpy.loadtxt("./data/isoc_z008m.dat", usecols = (0, 3, 4), unpack = True)
#
# w7 = numpy.where(loga == 10.00)
# w8 = numpy.where(loga == 10.05)
#
# plt.plot(-logte[w7] + 4.25, -logl[w7] + 19.3,label= "141 Myr")
# plt.plot(-logte[w8] + 4.25, -logl[w8] + 19.3,label= "159 Gyr")
#
#
# plt.legend(loc= "lower left")

plt.show()
