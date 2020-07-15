import numpy
import matplotlib.pyplot as plt


v, bv = numpy.loadtxt("./data/m45.txt", usecols = (2, 3), unpack = True)

plt.scatter(bv, v)
plt.gca().invert_yaxis()
plt.ylabel('V')
plt.xlabel('B-V')
plt.show()
