import re
import json
import matplotlib.pyplot as plt

MAX_COLUMN_CHAR_LENGTH = [13, 11, 10, 8, 9, 20, 11, 6, 10, 9, 9, 17]
# test comment

def readData():
    file = open("313 brightest stars.txt", "r")
    lines = file.readlines()
    file.close()
    fieldNames = []
    recordList = []
    # for index, line in enumerate(lines):
    #     fields = re.split("\s\s+", line.strip())
    #     if (index == 0):
    #         fieldNames = fields
        #         print(fieldNames)
    #         continue
    #     if (len(fields) < len(fieldNames)-1):
    #         # print("Skipping Line: {}".format(line))
    #         continue
    #     if (len(fields) != len(fieldNames)):
    #         fields.append("")
    #     record = {}
    #     for field, value in zip(fieldNames, fields):
    #         record[field.strip()] = value
    #     recordList.append(record)
    # # print(json.dumps(recordList, indent = 4))
    #     if (index > 5):
    #         break
    for index, line in enumerate(lines):
        if (index == 0):
            fieldNames = re.split("\s\s+", line.strip())
            # print('fieldnames:{} line:{}'.format(fieldNames, line))
            continue
        fields = []
        for char_length in MAX_COLUMN_CHAR_LENGTH:
            if line:
                substring, line = line[:char_length], line[char_length:]
                stripped_substring = substring.strip()
                if stripped_substring:
                    fields.append(stripped_substring)
        if (len(fields) < len(fieldNames)-1):
            # print("Skipping Line: {}".format(line))
            continue

        if (len(fields) != len(fieldNames)):
            fields.append("")

        record = {}
        for field, value in zip(fieldNames, fields):
            record[field.strip()] = value
        recordList.append(record)
    # print(json.dumps(recordList, indent = 4))

    return recordList

def plotVBV(recordList):
    xAxisArray = []
    yAxisArray = []
    for index,record in enumerate(recordList):
        # print("{} Adding:{}".format(index, json.dumps(record, indent = 4)))
        xAxisArray.append(float(record['B-V']))
        yAxisArray.append(float(record['V']))
    # print(xAxisArray)
    # print(yAxisArray)
    plt.scatter(xAxisArray, yAxisArray)
    plt.ylabel('V')
    plt.xlabel('B-V')
    plt.show()

def main():
    recordList = readData()
    plotVBV(recordList)

main()
