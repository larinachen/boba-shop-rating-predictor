# import libraries
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
import pickle


# load dataset
bobas = pd.read_csv('merged_data.csv')

# features we will use to do the clustering
features = bobas.iloc[:,[0,2]]

# convert extracted features into numpy array
features = np.array(features)


''' 
------------------------------------------------------------
plot inertia graph to determine number of clusters
uncomment to create and view new inertia graph
------------------------------------------------------------

# delete NaNs and infinites
# features = np.delete(features,[333,0])
#print(features)
print(np.argwhere(np.isnan(features)))
print(np.any(np.isnan(features)))
#print(np.argwhere(np.isfinite(features)))

# find the optimal number of clusters
# Collecting the distortions into list
distortions = []
K = range(1,8)
for k in K:
 kmeanModel = KMeans(n_clusters=k)
 kmeanModel.fit(features)
 distortions.append(kmeanModel.inertia_)
# Plotting the distortions
plt.figure(figsize=(16,8))
plt.plot(K, distortions, "bx-")
plt.xlabel("k")
plt.ylabel("Distortion")
plt.title("The Elbow Method showing the optimal clusters")
plt.show()
'''


#implement kmeans
# Define the model
kmeans_model = KMeans(n_clusters=3, random_state=32932)
# Fit into our dataset fit
kmeans_predict = kmeans_model.fit_predict(features)
# get the coordinates of the cluster centers
centers = kmeans_model.cluster_centers_

# sort boba shops into 3 arrays (1 per cluster)
c0 = []
c1 = []
c2 = []

for i in range(len(kmeans_predict)):
    
    cluster = kmeans_predict[i]
    if cluster==0:
        c0.append(i)
    elif cluster==1:
        c1.append(i)
    elif cluster == 2:
        c2.append(i)
    else:
        print('error')

#print([sum(all_ratings) ,len(all_ratings)])
#print([c0, "\n", c1, '\n',c2])


# find average rating of each cluster 
#
# cluster 0
all_ratings_c0 = []
for i in range(len(c0)):
    index = c0[i]
    rating = bobas.loc[index].at["ratings"]
    all_ratings_c0.append(rating)
avg_rating_c0 = sum(all_ratings_c0) / len(all_ratings_c0)
print('----------')
#print([sum(all_ratings_c0) ,len(all_ratings_c0)])
print(avg_rating_c0)
#
# cluser 1
all_ratings_c1 = []
for i in range(len(c1)):
    index = c1[i]
    rating = bobas.loc[index].at["ratings"]
    all_ratings_c1.append(rating)
avg_rating_c1 = sum(all_ratings_c1) / len(all_ratings_c1)
#print([sum(all_ratings_c1) ,len(all_ratings_c1)])
print(avg_rating_c1)
#
# cluster 2
all_ratings_c2 = []
for i in range(len(c2)):
    index = c2[i]
    rating = bobas.loc[index].at["ratings"]
    all_ratings_c2.append(rating)
avg_rating_c2 = sum(all_ratings_c2) / len(all_ratings_c2)
#print([sum(all_ratings_c2) ,len(all_ratings_c2)])
print(avg_rating_c2)
# print([len(all_ratings), len(all_ratings_c0), len(all_ratings_c1), len(all_ratings_c2)])

# make dictionary of clusters and their ratings
def takeSecond(elem):
    return elem[1]
clusters = [[0,avg_rating_c0, centers[0], 'lowest'], [1, avg_rating_c1,centers[1], 'medium'],[2, avg_rating_c2,centers[2], 'hightest']]
clusters.sort(key=takeSecond)
levels = ['lowest','medium','highest']
for i in range(len(clusters)):
    c = clusters[i]
    c[3]=levels[i]
#print(clusters)


# pickle the cluster centers and the ratings
dbfile = open('kmeans_results', 'wb')
pickle.dump(clusters, dbfile)                     
dbfile.close()
print(clusters)

