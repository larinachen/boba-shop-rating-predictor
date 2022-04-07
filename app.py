import pickle

# reading in clusters and their average ratings
dbfile = open('kmeans_results', 'rb')     
clusters = pickle.load(dbfile)
dbfile.close()

# get cluster centers
centers = []
for item in clusters:
    centers.append(item[2])

# user input coordinate [address, review count]
address = int(input("input address: "))
rc = int(input("input review count: "))
coord = [address, rc]

# calculate distance to cluster center to find which cluster
min_d = 2**20
closest_cluster = 0
rating = ''
for i in range(len(centers)):
    center = centers[i]
    d = ((center[0] - coord[0])**2 + (center[1] - coord[1])**2) ** 0.5
    if d<min_d :
        min_d = d
        closest_cluster = clusters[i][0]
        rating = clusters[i][3]

print([min_d,closest_cluster,rating])
# print(all_d,min_d)
#
# 
