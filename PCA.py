import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

np.random.seed(21)

file = pd.read_csv("data/merged_df.csv").T

print(file)

states = file.index[4:].to_numpy()
state_values = file.iloc[4:, 1:].to_numpy()

print(state_values)
print(states)

# plt.plot(x, y)
# plt.title("What we are trying to decompose")
# plt.xlabel("CPI")
# plt.ylabel("State (ZHVI) Values")
# plt.savefig("Visuals/Pre-PCA_Figure.png")
# plt.show()

#-------Performing PCA-------
pca = PCA(n_components = 2)


