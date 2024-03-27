import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data/merged_df.csv")

CPI_states = data.iloc[:, 3:]

correlations = CPI_states.corr() #Compute correlations

#The top 10 states are Alaska, Wyoming, South Dakota, Louisiana, Vermont, the District of Columbia, Oklahoma, Iowa, Hawaii

high_mask = correlations[correlations >= 0.5] #High Correlation Mask
low_mask = correlations[correlations < 0.5] #Low Correlation Mask

fig = plt.figure(figsize = (18, 12))
sns.heatmap(correlations, cmap = "YlOrBr", xticklabels= True, yticklabels=True) # Total heat map
plt.title("All States, Correlation to CPI")
fig.savefig("Visuals/Heatmap.png")

fig1 = plt.figure(figsize = (18, 12))
sns.heatmap(low_mask, cmap = "YlOrBr", xticklabels= True, yticklabels=True) #We see that Florida, New Jersey, Illinois, Arizona, Nevada, Michigan, Rhode Island and Connecticut don't correlate well to CPI
plt.title("Heatmap showing States with below 0.5 correlation to CPI")
fig1.savefig("Visuals/Low_heatmap.png")

data = pd.read_csv("data/dummiable_data.csv")

sort_data = data.sort_values(by = ['Year', 'Month', 'Day', 'ZHVI'], ascending = False)
top_15_states = list(sort_data.head(15)['State'])

filtered_df = data[data['State'].isin(top_15_states)]

fig = plt.figure(figsize = (18, 12))
sns.lineplot(data = filtered_df, x = 'CPI', y = 'ZHVI', hue = 'State')
plt.show()


