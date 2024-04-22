import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

pca_data = pd.read_csv("data\pca_Data.csv")

just_data = pca_data.iloc[:, 1:]

# wcss = [] 
# for i in range(1, 11): 
#     kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 21)
#     kmeans.fit(just_data) 
#     wcss.append(kmeans.inertia_)

# plt.plot(range(1, 11), wcss) #Looks like 3 clusters will do
# plt.show()

cluster_3 = KMeans(n_clusters = 3, init = 'k-means++', random_state = 21)
cluster_3.fit(just_data)

pca_data['cluster'] = cluster_3.labels_

# p1 = sns.scatterplot(x = "Dimension1", y = "Dimension2", data = pca_data, s = 65, hue = "cluster")
# plt.title("KMeans Clustered Plot of PCA Data")
# plt.savefig("Visuals/pca_clustered_plots.png")
# plt.show()

zero_cluster = pca_data[pca_data['cluster'] == 0] #Biggest cluster, seems to be homes that aren't affected as much
first_cluster = pca_data[pca_data['cluster'] == 1] # Most expensive states
second_cluster = pca_data[pca_data['cluster'] == 2] # Middle of the road states

print(zero_cluster['States'])
print(first_cluster['States'])
print(second_cluster['States'])