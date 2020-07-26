import numpy
import matplotlib.pyplot as plt


v, err_V, b_v, err_BV = numpy.loadtxt("./data/m13.txt", usecols = (3, 4, 5, 6), unpack = True)

xAxisArray = []
yAxisArray = []

for i in range(len(b_v)):
    if b_v[i] > 1.2:
        continue
    if err_V[i] > 0.010 or err_BV[i] > 0.010:
        continue
    xAxisArray.append(b_v[i])
    yAxisArray.append(v[i])
plt.scatter(xAxisArray, yAxisArray)
plt.gca().invert_yaxis()
plt.ylabel('V')
plt.xlabel('B-V')

# loga, logl, logte = numpy.loadtxt("./data/iso_jc_z070s.dat", usecols = (0, 3, 4), unpack = True)
#
# w7 = numpy.where(loga == 8.15)
# w8 = numpy.where(loga == 8.2)
#
# plt.plot(-logte[w7] + 4.4 , -logl[w7] + 17.5,label= "141 Myr")
# plt.plot(-logte[w8] + 4.4, -logl[w8] + 17.5,label= "159 Gyr")
#
# # plt.xlabel("Log(Teff)")
# # plt.ylabel("Log L")
# # plt.axis([-0.5, 2.5, 25, 0])
# plt.legend(loc= "lower left")

plt.show()
