import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("merged_df.csv")

CPI_states = data.iloc[:, 3:]

correlations = CPI_states.corr() #Compute correlations
just_cpi = correlations.sort_values(by = "CPI", ascending = False)['CPI']
print(just_cpi.head(10))

#The top 10 states are Alaska, Wyoming, South Dakota, Louisiana, Vermont, the District of Columbia, Oklahoma, Iowa, Hawaii

high_mask = correlations[correlations >= 0.5] #High Correlation Mask
low_mask = correlations[correlations < 0.5] #Low Correlation Mask

fig = plt.figure(figsize = (18, 12))
sns.heatmap(correlations, cmap = "YlOrBr", xticklabels= True, yticklabels=True) # Total heat map
plt.title("All States, Correlation to CPI")
fig.savefig("Heatmap.png")

fig1 = plt.figure(figsize = (18, 12))
sns.heatmap(low_mask, cmap = "YlOrBr", xticklabels= True, yticklabels=True) #We see that Florida, New Jersey, Illinois, Arizona, Nevada, Michigan, Rhode Island and Connecticut don't correlate well to CPI
plt.title("Heatmap showing States with below 0.5 correlation to CPI")
fig1.savefig("Low_heatmap.png")


