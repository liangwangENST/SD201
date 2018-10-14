from sklearn.cluster import KMeans
import numpy as np
import numpy as np

#create a numpy array
X = np.array([[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]])

#convert a list to a numpy array
a=[]
for i in range(0,10):
    p=[i,2*i]
    a.append(p)

Y=np.array(a, dtype='float32')

kmeans = KMeans(init='random', n_clusters=2, max_iter=10000, n_init=100).fit(X)
print('labels : \n',kmeans.labels_)
print('center : \n ',kmeans.cluster_centers_  )
print('predict :\n',kmeans.predict([[0,0],[3,3]]))

