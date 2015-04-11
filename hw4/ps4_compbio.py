import numpy as np
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection

from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA

# read file and save info at following lists
ls_no = []
ls_x = []
ls_y = []
ls_z = []
file = open('1ubq.pdb', 'r')
s_line = file.readline()
while (s_line != 'END\r\n'):
	ls_words = s_line.split()
	if ls_words[2] == 'CA':
		ls_no.append(int(ls_words[1]))
		ls_x.append(float(ls_words[5]))
		ls_y.append(float(ls_words[6]))
		ls_z.append(float(ls_words[7]))
	s_line = file.readline()

# construct dataframe to save position info
d_atom = {'x':pd.Series(ls_x,index=ls_no),
          'y':pd.Series(ls_y,index=ls_no),
          'z':pd.Series(ls_z,index=ls_no)}
df_atom = pd.DataFrame(d_atom)
i_len_atom = len(df_atom.index)

'''
# search pairs with distance within 6A, and delete atoms never in a pair
df_atom['legal'] = False
for i, i_no in enumerate(df_atom.index):
	for j, j_no in enumerate(df_atom.index[i+1:]):
		f_dis_sqr = (df_atom['x'][i_no]-df_atom['x'][j_no])**2 
		+ (df_atom['y'][i_no]-df_atom['y'][j_no])**2
		+ (df_atom['z'][i_no]-df_atom['z'][j_no])**2
		if f_dis_sqr <= 36:
			df_atom['legal'][i_no] = True
			df_atom['legal'][j_no] = True
print df_atom
exit()
# since all atoms are labeled with 'True', so I commented the step above.
'''

X_true = df_atom.values
n_samples = len(X_true)
# Center the data
X_true -= X_true.mean()

similarities = euclidean_distances(X_true)


# Add noise to the similarities
noise = np.random.rand(n_samples, n_samples)
noise = noise + noise.T
noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
similarities += noise

seed = np.random.RandomState(seed=3)
mds = manifold.MDS(n_components=3, max_iter=3000, eps=1e-9, random_state=seed,
                   dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(similarities).embedding_

# Rescale the data
pos *= np.sqrt((X_true ** 2).sum()) / np.sqrt((pos ** 2).sum())

# Rotate the data
clf = PCA(n_components=3)
X_true = clf.fit_transform(X_true)
pos = clf.fit_transform(pos)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X_true[:, 0], X_true[:, 1], X_true[:, 2], c='r', s=n_samples)
ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c='g', s=n_samples)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

# Calculate RMSD
RMSD = np.sqrt(((X_true - pos)**2).sum() / n_samples)
print RMSD