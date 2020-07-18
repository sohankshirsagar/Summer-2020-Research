import numpy
import matplotlib.pyplot as plt


v, err_v, b, err_b = numpy.loadtxt("./data/ngc3201.txt", usecols = (3, 4, 5, 6), unpack = True)

# wV = numpy.where(err_V <= 0.001)
# wB = numpy.where(err_B <= 0.001)

xAxisArray = []
yAxisArray = []

for i, data in enumerate(v):
    if err_b[i] <= 1 and err_v[i] <= 1:
        if (b[i]-v[i] < 0 or b[i]-v[i] > 2):
            continue
        xAxisArray.append(b[i]-v[i])
        yAxisArray.append(v[i])


plt.scatter(xAxisArray, yAxisArray)
plt.gca().invert_yaxis()
plt.ylabel('V')
plt.xlabel('B-V')
plt.show()


"""
Our data extend from the tip of the red giant branch (RGB) to below the main-sequence turnoff (MSTO) and sample the horizontal branch (HB) very well.
The broad RGB is consistent with the variable reddening across the face of NGC 3201 noted by several authors (von Braun & Mateo 2001, and references therein).
A population of blue straggler stars is seen above and blueward of the MSTO.
"""
