import numpy as np
import matplotlib.pyplot as plt
import h5py

snap = h5py.File('examples/DM-L50-N128/output/snapshot_002.hdf5','r')
pos = np.array(snap['PartType1']['Coordinates'])

fig = plt.scatter(pos[:,0],pos[:,1],s=0.0001)
fig = plt.savefig('scatter_plot.png')
