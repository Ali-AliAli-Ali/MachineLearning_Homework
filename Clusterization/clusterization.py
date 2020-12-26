import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import pointGenerator


amountPoints = 10000
amountTestPoints = pointGenerator.amountTestDeterminer(amountPoints)

amountClusters = int(input())
steps = 5

Points, testPoints = pointGenerator.usual(amountPoints)
centroids = np.zeros((amountClusters, 2))



plt.figure(figsize=(8, 8))
cluster = AgglomerativeClustering(n_clusters=amountClusters, affinity='euclidean', linkage='ward')
testPointsClusters = np.array(cluster.fit_predict(testPoints))
plt.scatter(testPoints[:,0], testPoints[:,1], c=cluster.labels_, cmap='rainbow')

t = sumX = sumY = kInCluster = 0
while t < amountClusters:
    for i in range(amountTestPoints):
        if testPointsClusters[i] == t:
            sumX += testPoints[i][0]
            sumY += testPoints[i][1]
            kInCluster += 1
    centroids[t][0] = sumX/kInCluster
    centroids[t][1] = sumY/kInCluster
    t += 1
    sumX = sumY = kInCluster = 0
plt.scatter(centroids[:,0], centroids[:,1], c='m', marker='x')

for step in range(steps):
    for point in Points:
        mindist = 1000
        for i in range(amountClusters):
            if np.hypot(abs(centroids[i][0]-point[0]), abs(centroids[i][1]-point[1])) < mindist:
                mindist = np.hypot(abs(centroids[i][0]-point[0]), abs(centroids[i][1]-point[1]))
                point[2] = i
    t = sumX = sumY = kInCluster = 0
    while t < amountClusters:
        for point in Points:
            if point[2] == t:
                sumX += point[0]
                sumY += point[1]
                kInCluster += 1
        centroids[t][0] = sumX/kInCluster
        centroids[t][1] = sumY/kInCluster
        t += 1
        sumX = sumY = kInCluster = 0

plt.scatter(Points[:,0], Points[:,1], c=Points[:,2], cmap='rainbow', s=3)
plt.scatter(centroids[:,0], centroids[:,1], c='r', marker='x', s=100)

plt.show()




#___________________This is a K-Means clustering for comparison___________________
# from sklearn.cluster import KMeans
#
# kmeans = KMeans(n_clusters=amountClusters).fit(Points)
# centroids = kmeans.cluster_centers_
#
# plt.figure(figsize=(8, 8))
# plt.scatter(Points[:, 0], Points[:, 1], c=kmeans.labels_.astype(float), s=3, cmap='rainbow')
# plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50, marker='x')
# plt.show()
