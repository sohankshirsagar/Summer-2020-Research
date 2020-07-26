import numpy
import matplotlib.pyplot as plt


y, b_y, err = numpy.loadtxt("./data/47tuc.txt", usecols = (3, 4, 7), unpack = True)

w05 = numpy.where(err < 0.05)

#plt.scatter(-0.055+1.707*b_y[w05], y[w05], color = "red")
plt.gca().invert_yaxis()
plt.ylabel('V')
plt.xlabel('B-V')

loga, logl, logte = numpy.loadtxt("./data/isoc_z030.dat", usecols = (0, 3, 4), unpack = True)

w7 = numpy.where(loga == 10.00)
w8 = numpy.where(loga == 10.05)

plt.plot(-logte[w7] + 4.4 , -logl[w7] + 17.5,label= "10 Gyr")
plt.plot(-logte[w8] + 4.4, -logl[w8] + 17.5,label= "11 Gyr")

# plt.xlabel("Log(Teff)")
# plt.ylabel("Log L")
# plt.axis([5.0, 3.5, 0, 6])
plt.legend(loc= "lower left")

plt.show()
