import math
import re
import json
import numpy
import matplotlib.pyplot as plt

# def readData(fileName):
#     file = open(fileName, "r")
#     lines = file.readlines()
#     file.close()
#     fieldNames = []
#     recordList = []
#     for index, line in enumerate(lines):
#         fields = re.split("\s+", line.strip())
#         if (index == 0):
#             fieldNames = fields
#             # print(fieldNames)
#             continue
#         if (len(fields) < len(fieldNames)-1):
#             # print("Skipping Line: {}".format(line))
#             continue
#         # if (len(fields) != len(fieldNames)):
#         #     fields.append("")
#         record = {}
#         for field, value in zip(fieldNames, fields):
#             record[field.strip()] = (value)
#         recordList.append(record)
#         # print(json.dumps(recordList, indent = 4))
#         # if (index > 5):
#         #     break
#     return recordList
#
#
#
# def plotVBV(gaiaData):
#     b ,b_err, v, v_err = numpy.loadtxt("./data/m14.txt", usecols = (7, 8, 9, 10), unpack = True)
#
#     xAxisArray = []
#     yAxisArray = []
#     for i, data in enumerate(b):
#         xPoint = b[i]-v[i]
#         if xPoint > 1.6 and v[i] > 19:
#             continue
#         if xPoint < 1.25 and v[i] < 16:
#             continue
#         if b_err[i] < 0.05 and v_err[i] < 0.05:
#             xAxisArray.append(xPoint)
#             yAxisArray.append(v[i])
#
#
#     matchingGaiaValuesX = []
#     matchingGaiaValuesY = []
#
#     for data in gaiaData:
#         # print("proccessing: {} {}".format(data['Bmag'],data['Vmag']))
#         try:
#             b_vMag = float(data['BP-RP'].strip())
#         except ValueError:
#             # print("Error while converting Bmag: {}".format(data['Bmag']))
#             continue
#         try:
#             vMag = float(data['RPmag'].strip())
#         except ValueError:
#             # print("Error while converting Vmag: {}".format(data['Vmag']))
#             continue
#         for xValue, yValue in zip(xAxisArray, yAxisArray):
#             if ((round((b_vMag), 3) == round((xValue)), 3) and (round((vMag), 3) == round((yValue), 3))):
#                 matchingGaiaValuesX.append(xValue)
#                 matchingGaiaValuesY.append(yValue)
#
#
#     plt.scatter(matchingGaiaValuesX, matchingGaiaValuesY, color = "red")
#     plt.gca().invert_yaxis()
#     plt.ylabel('V')
#     plt.xlabel('B-V')
#     plt.title("M14")
#
#     iso_y, iso_x = numpy.loadtxt("./data/m14_iso.txt", usecols = (0, 1), unpack = True)
#
#     plt.plot(iso_x, iso_y, label = "13 Gyr")
#
#     plt.legend(loc= "lower left")
#
#     plt.show()
#
# def main():
#     gaiaData = readData("./data/m14_gaia_data.txt")
#     plotVBV(gaiaData)
#
#
#
# main()



b ,b_err, v, v_err = numpy.loadtxt("./data/m14.txt", usecols = (7, 8, 9, 10), unpack = True)

xAxisArray = []
yAxisArray = []
for i, data in enumerate(b):
    xPoint = b[i]-v[i]
    if xPoint > 1.6 and v[i] > 19:
        continue
    if xPoint < 1.25 and v[i] < 16:
        continue
    if b_err[i] < 0.05 and v_err[i] < 0.05:
        xAxisArray.append(xPoint)
        yAxisArray.append(v[i])


plt.scatter(xAxisArray, yAxisArray, color = "red")
plt.gca().invert_yaxis()
plt.ylabel('V')
plt.xlabel('B-V')
plt.title("M14")

iso_y, iso_x = numpy.loadtxt("./data/m14_iso.txt", usecols = (0, 1), unpack = True)

plt.plot(iso_x, iso_y, label = "13 Gyr")
# loga, logl, logte = numpy.loadtxt("./data/isoc_z030.dat", usecols = (0, 3, 4), unpack = True)
#
# w7 = numpy.where(loga == 10.15)
# w8 = numpy.where(loga == 10.20)
#
# plt.plot(-logte[w7] + 4.9, -logl[w7] + 20, label= "14.1 Gyr")
# plt.plot(-logte[w8] + 4.9, -logl[w8] + 20, label= "15.9 Gyr")
#
plt.legend(loc= "lower left")

plt.show()
