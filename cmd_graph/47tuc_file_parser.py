import numpy
import matplotlib.pyplot as plt


y, b_y, err = numpy.loadtxt("./data/47tuc.txt", usecols = (3, 4, 7), unpack = True)

w05 = numpy.where(err < 0.05)

plt.scatter(-0.055+1.707*b_y[w05], y[w05])
plt.gca().invert_yaxis()
plt.ylabel('V')
plt.xlabel('B-V')

plt.show()
