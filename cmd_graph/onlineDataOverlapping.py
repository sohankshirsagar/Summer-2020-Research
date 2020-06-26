import numpy
import matplotlib.pyplot as plt


V, BV = numpy.loadtxt("./data/m45.dat", usecols = (2, 3), unpack = True)


plt.scatter(BV, V)
plt.gca().invert_yaxis()
plt.ylabel('V')
plt.xlabel('B-V')

loga, logl, logte = numpy.loadtxt("./data/isoc_z0001.dat", usecols = (0, 3, 4), unpack = True)

w7 = numpy.where(loga == 6.0)
w8 = numpy.where(loga == 8.0)

plt.plot(logte[w7] - 2, logl[w7] + 4,label= "10 Myr")
plt.plot(logte[w8] - 3.6, logl[w8] + 7,label= "100 Myr")

# plt.xlabel("Log(Teff)")
# plt.ylabel("Log L")
# plt.axis([5.0, 3.5, 0, 6])
plt.legend(loc= "lower left")

plt.show()
