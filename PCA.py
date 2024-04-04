import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

np.random.seed(21)

file = pd.read_csv("data/merged_df.csv").T

states = file.index[4:]
state_values = file.iloc[4:, 1:]

scaler = StandardScaler()

scaled_df=state_values.copy()

scaled_df=pd.DataFrame(scaler.fit_transform(scaled_df), columns=scaled_df.columns)

# print(state_values)
# print(states)

# plt.plot(x, y)
# plt.title("What we are trying to decompose")
# plt.xlabel("CPI")
# plt.ylabel("State (ZHVI) Values")
# plt.savefig("Visuals/Pre-PCA_Figure.png")
# plt.show()

#-------Performing PCA-------
pca_data = PCA(n_components=2).fit_transform(scaled_df) #1 Component has the whole variance

dim1 = pca_data[:, 0]
dim2 = pca_data[:, 1]

pca_df = pd.DataFrame({"States" : states, "Dimension1" : dim1, "Dimension2" : dim2})


ax = plt.figure(figsize=(12,8))
p1 = sns.scatterplot(x = "Dimension1", y = "Dimension2", data = pca_df, s = 65)
plt.title("PCA Reduced ZHVI Values")

for line in range(0,pca_df.shape[0]):
     p1.text(pca_df.Dimension1[line], pca_df.Dimension2[line], pca_df.States[line], 
             horizontalalignment='right', size='medium', color='black', weight='semibold')
     
plt.savefig("Visuals/PCA_reduced_state_representation.png")
plt.show()


