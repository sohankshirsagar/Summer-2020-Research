import numpy
import matplotlib.pyplot as plt


loga, logl, logte = numpy.loadtxt("./data/isoc_z008.dat", usecols = (0, 3, 4), unpack = True)

w7 = numpy.where(loga == 7.0)
w8 = numpy.where(loga == 8.0)

plt.plot(logte[w7], logl[w7],label= "10 Myr")
plt.plot(logte[w8], logl[w8],label= "100 Myr")

plt.xlabel("Log(Teff)")
plt.ylabel("Log L")
plt.axis([5.0, 3.5, 0, 6])
plt.legend(loc= "lower left")
plt.show()
