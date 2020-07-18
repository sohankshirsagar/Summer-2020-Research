import math
import re
import json
import numpy
import matplotlib.pyplot as plt

def giveGaiaData(fileName):

    gaia_ra, gaia_dec = numpy.loadtxt(fileName, usecols = (1, 3), unpack = True)
    # print(gaia_ra, gaia_dec)
    return gaia_ra, gaia_dec

def plotVBV(gaia_ra, gaia_dec):

    b, v, ra_h, ra_m, ra_s, dec_h, dec_m, dec_s = numpy.loadtxt("./data/m5.txt", usecols = (6, 9, 22, 23, 24, 25, 26, 27), unpack = True)

    xAxisArray = []
    yAxisArray = []
    count = 0
    for i, data_gaia in enumerate(gaia_ra):
        if (i%10000 == 0):
            print("processed {} gaia".format(i))
        for j, data in enumerate(b):
            if (j%10000 == 0):
                print("processed {}:{} actual".format(i,j))
            if ((round(gaia_ra[i], 1) == round(HoursToDecimal(ra_h[j], ra_m[j], ra_s[j]), 1)) and (round(gaia_dec[i], 1) == round(HoursToDecimal(dec_h[j], dec_m[j], dec_s[j]), 1))):
                count = count + 1
                print("found " + count + " pairs")
                xAxisArray.append(b[j]-v[j])
                yAxisArray.append(v[j])

    plt.scatter(xAxisArray, yAxisArray)
    plt.gca().invert_yaxis()
    plt.ylabel('V')
    plt.xlabel('B-V')
    plt.show()

def myround(x, base=5):
    return base * round(x/base)

def HoursToDecimal(hoursInput,minutesInput,secondsInput):
    decimalRA = (hoursInput + (minutesInput/60) + (secondsInput/3600))*15
    return decimalRA

def main():
    gaia_ra, gaia_dec = giveGaiaData("./data/gaia_data_m5.txt")
    plotVBV(gaia_ra, gaia_dec)


main()
