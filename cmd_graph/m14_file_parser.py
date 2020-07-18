import numpy
import matplotlib.pyplot as plt


b ,b_err, v, v_err = numpy.loadtxt("./data/m14.txt", usecols = (7, 8, 9, 10), unpack = True)

xAxisArray = []
yAxisArray = []
for i, data in enumerate(b):
    if b_err[i] < 0.05 and v_err[i] < 0.05:
        xAxisArray.append(b[i]-v[i])
        yAxisArray.append(v[i])


plt.scatter(xAxisArray, yAxisArray)
plt.gca().invert_yaxis()
plt.ylabel('V')
plt.xlabel('B-V')
plt.show()
