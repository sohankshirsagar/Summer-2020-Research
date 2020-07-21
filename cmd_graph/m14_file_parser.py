import numpy
import matplotlib.pyplot as plt


b ,b_err, v, v_err = numpy.loadtxt("./data/m14.txt", usecols = (7, 8, 9, 10), unpack = True)

xAxisArray = []
yAxisArray = []
for i, data in enumerate(b):
    xPoint = b[i]-v[i]
    if xPoint > 1.6 and v[i] > 19:
        continue
    if xPoint < 1.25 and v[i] < 16:
        continue
    if b_err[i] < 0.05 and v_err[i] < 0.05:
        xAxisArray.append(xPoint)
        yAxisArray.append(v[i])


plt.scatter(xAxisArray, yAxisArray, color = "red")
plt.gca().invert_yaxis()
plt.ylabel('V')
plt.xlabel('B-V')
plt.title("M14")

loga, logl, logte = numpy.loadtxt("./data/isoc_z030.dat", usecols = (0, 3, 4), unpack = True)

w7 = numpy.where(loga == 10.15)
w8 = numpy.where(loga == 10.20)

plt.plot(-logte[w7] + 4.9, -logl[w7] + 20, label= "14.1 Gyr")
plt.plot(-logte[w8] + 4.9, -logl[w8] + 20, label= "15.9 Gyr")

# plt.xlabel("Log(Teff)")
# plt.ylabel("Log L")
# plt.axis([5.0, 3.5, 0, 6])
plt.legend(loc= "lower left")

plt.show()
