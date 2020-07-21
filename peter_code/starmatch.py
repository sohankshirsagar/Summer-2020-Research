import matplotlib.pyplot as plt
import numpy as np
import math

def dataread(filename,xCol,yCol,bCol,vCol,hours,minutes,seconds,deg,arcmin,arcsec):
    with open(filename) as f:
        lines = f.readlines()
        x = [float(line.split()[xCol]) for line in lines]
        y = [float(line.split()[yCol]) for line in lines]
        bMag = [float(line.split()[bCol]) for line in lines]
        vMag = [float(line.split()[vCol]) for line in lines]
        ra = [((float(line.split()[hours])) + ((float(line.split()[minutes]))/(60)) + ((float(line.split()[seconds]))/ 3600))*15 for line in lines]
        dec = [float(line.split()[deg]) + (float(line.split()[arcmin]))/(60) + (float(line.split()[arcsec]))/(3600)  for line in lines]
    return x,y,bMag,vMag,ra,dec

def RaDecRead(filename,raCol,decCol):
    with open(filename) as f:
        lines = f.readlines()
        ra = [float(line.split()[raCol]) for line in lines]
        dec = [float(line.split()[decCol]) for line in lines]
    return ra,dec

def starMatch(gaiaResultsRA,gaiaResultsDEC,photometryRA,photometryDEC,photometryB,photometryV,starlistB,starlistV,error):
    for i in range(0, len(photometryRA)-1): #the big list
        for j in range(0, len(gaiaResultsRA)-1): #the small list
            if (photometryRA[i] < ((gaiaResultsRA[j]) + error)) and (photometryRA[i] > ((gaiaResultsRA[j])-error)) and (photometryDEC[i] < ((gaiaResultsDEC[j]) + error)) and (photometryDEC[i] > ((gaiaResultsDEC[j])-error)):
                starlistB[i] = photometryB[i]
                starlistV[i] = photometryV[i]

gaiaRADEC = RaDecRead('gaiaOmegaCenRaDecEpoch2000.txt',0,1) #reads in gaia data from a table taken out of topcat
testArray = dataread('stetsonSmallCut.txt',1,2,6,9,22,23,24,25,26,27) #reads in photometry from P.B. Stetson's catalog
clusterMembersB = np.zeros(len(gaiaRADEC[1]))
clusterMembersV = np.zeros(len(gaiaRADEC[1]))
bMinusV = np.zeros(len(clusterMembersB)-1)
justV = np.zeros(len(clusterMembersV)-1)

starMatch(gaiaRADEC[0],gaiaRADEC[1],testArray[4],testArray[5],testArray[2],testArray[3],clusterMembersB,clusterMembersV,.9)

for i in range(0,len(clusterMembersV)-1):
    bMinusV[i] = clusterMembersB[i] - clusterMembersV[i]
    justV[i] = clusterMembersV[i]

fig, ax = plt.subplots()
ax.scatter(bMinusV,justV,s=1)
ax.scatter
ax.set_xlim([-1.5,1.5])
ax.set_ylim([13,27])
plt.gca().invert_yaxis()
plt.show()
