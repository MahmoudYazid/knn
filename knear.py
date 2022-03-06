from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import numpy as np
A = np.array([[3.1, 2.3], [2.3, 4.2], [3.9, 3.5], [3.7, 6.4], [4.8, 1.9],[8.3, 3.1], [5.2, 7.5], [4.8, 4.7], [3.5, 5.1], [4.4, 2.9],])

y=[4,3]

model = NearestNeighbors(n_neighbors=3, algorithm='auto')
model.fit(A)
indices = model.kneighbors([y])
 
print(A[indices[1][:,0]][0],[0])
print(A[indices[1][:, 0]][0][1])
"""
plt.scatter(A[:, 0], A[:, 1], marker='o', s=100, color='k')
plt.scatter(A[indices[1][:, 0]][0][0], A[indices[1][:, 0]][0][1],
            marker='o', s=250, color='k', facecolors='none')
plt.scatter(y[0], y[1],
            marker='x', s=100, color='k')
plt.show()
"""