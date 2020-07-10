import astropy.units as u
from astropy.coordinates.sky_coordinate import SkyCoord
from astropy.units import Quantity
from astroquery.gaia import Gaia
import matplotlib.pyplot as plt
import numpy
import numpy as np
#import warnings
#warnings.filterwarnings('ignore')

from astroquery.gaia import Gaia


#This program reads in star position datafiles from the Prism astronomy software (or something of your choice), then plots a color magnitude diagram.
#Overlaid on top of that is a CMD generated from GAIA along with the locations of known variable stars from Christine Clement's catalog (not done yet).
#Taken together, this allows you to pick out blue stragglers in that cluster.

def dataread(filename,xCol,yCol,magCol): #input the name of the file and columns for x, y, and magnitude
    x, y, mag = numpy.loadtxt(filename, usecols = (xCol, yCol, magCol), unpack = True)
    return x,y,mag

def match(blist, vlist, maglist, error): #input the dataread file for b and v, along with the list you want to output to and the error for the x and y values
    for i in range(0,len(blist[2])-1):
        for j in range(0,len(blist[2])-1):
            if (blist[0][i] < ((vlist[0][j]) + error)) and (blist[0][i] > ((vlist[0][j])-error)) and (blist[1][i] < ((vlist[1][j]) + error)) and (blist[1][i] > ((vlist[1][j])-error)):
                maglist[0][i] = blist[2][i]
                maglist[1][i] = vlist[2][j]

b = dataread("./data/Messier 12 B Band - Copy.txt",1,2,6)
v = dataread("./data/Messier 12 V Band - Copy.txt",1,2,6)
magnitude = np.zeros((2,len(b[2])))

match(b,v,magnitude,0.5)
bMinusV = np.zeros(len(magnitude[0]))
justV = np.zeros(len(magnitude[0]))
for i in range(0,len(magnitude[0])):
    bMinusV[i] = magnitude[0][i] - magnitude[1][i]
    justV[i] = magnitude[1][i]


job4 = Gaia.launch_job_async("SELECT * FROM gaiadr2.gaia_source WHERE CONTAINS(POINT('ICRS',gaiadr2.gaia_source.ra,gaiadr2.gaia_source.dec),CIRCLE('ICRS',251.809,-1.948,.3))=1 \
AND pmra BETWEEN -2 AND 2 \
AND pmdec BETWEEN -7 AND -6;", dump_to_file=True)

"""
Gaia.launch_job_async("SELECT * \
FROM gaiadr2.gaia_source AS g, gaiadr2.urat1_best_neighbour AS tbest \
WHERE g.source_id = tbest.source_id \
AND CONTAINS(POINT('ICRS',g.ra,g.dec),CIRCLE('ICRS',251.809,-1.022,1))=1 \
AND abs(pmra_error/pmra)<0.10 \
AND abs(pmdec_error/pmdec)<0.10 \
AND pmra BETWEEN -2 AND 2 \
AND pmdec BETWEEN -8 AND -5;", dump_to_file=False)
"""
p = job4.get_results()

#p.pprint()
#for column in (m.columns):
    #print(column)
print(p['phot_bp_mean_mag','phot_g_mean_mag','phot_rp_mean_mag','bp_rp'])
#plt.scatter(p['bp_rp'],p['phot_bp_mean_mag'],s=1)
#plt.show()


fig, ax = plt.subplots()
ax.scatter(bMinusV,justV,s=1)
#ax.scatter(m['j_m'] - m['ks_m'],m['ks_m'])
#ax.scatter(p['bp_rp']-1.40,p['phot_bp_mean_mag']+4,s=1)
ax.scatter(p['bp_rp'],p['phot_bp_mean_mag'],s=1)
ax.set_xlim([-1.5,1.5])
ax.set_ylim([13,25])
plt.gca().invert_yaxis()
plt.show()
