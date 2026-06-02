
"""DBSCAN MASTERCLASS"""

import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

def explain():
    print("""
DBSCAN = Density Based Spatial Clustering

Concepts:
- Core Points
- Border Points
- Noise Points

Parameters:
- eps
- min_samples

Advantages:
- No need for K
- Finds irregular clusters
- Detects outliers
""")

def dbscan_demo():
    X,_ = make_moons(n_samples=500, noise=0.08)
    model = DBSCAN(eps=0.2, min_samples=5)
    labels = model.fit_predict(X)

    plt.figure(figsize=(6,4))
    plt.scatter(X[:,0], X[:,1], c=labels)
    plt.show()

if __name__ == '__main__':
    explain()
