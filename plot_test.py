import pynbody
import numpy as np
import matplotlib.pyplot as plt

s = pynbody.load('snapshot_010.hdf5')
s.physical_units()
halos = s.halos()
h1 = halos[1]
h1_coords = h1['pos']

# pynbody.analysis.halo.center(halos[1], vel=False)
# fig = pynbody.plot.image(halos[1].d)#, width = '40 kpc', cmap=plt.cm.Greys)#, units = 'Msol kpc^-2')
# fig = plt.hist2d(h1_coords[:,0],h1_coords[:,1],bins=1000)
fig = plt.scatter(h1_coords[:,0],h1_coords[:,1],s=0.1)
fig = plt.xlim((-200,200))
fig = plt.ylim((-200,200))
fig = plt.savefig('Pynbody_test.png')
