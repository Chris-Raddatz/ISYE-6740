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

# fig = plt.figure(figsize = (18, 12))
# sns.heatmap(correlations, cmap = "YlOrBr", xticklabels= True, yticklabels=True) # Total heat map
# plt.title("All States, Correlation to CPI")
# fig.savefig("Visuals/Heatmap.png")

# fig1 = plt.figure(figsize = (18, 12))
# sns.heatmap(low_mask, cmap = "YlOrBr", xticklabels= True, yticklabels=True) #We see that Florida, New Jersey, Illinois, Arizona, Nevada, Michigan, Rhode Island and Connecticut don't correlate well to CPI
# plt.title("Heatmap showing States with below 0.5 correlation to CPI")
# fig1.savefig("Visuals/Low_heatmap.png")

data = pd.read_csv("data/dummiable_data.csv")

sort_data_decreasing = data.sort_values(by = ['Year', 'Month', 'Day', 'ZHVI'], ascending = False) #To find the top house valuations
sort_data_increasing = data.sort_values(by = ['Year', 'Month', 'Day', 'ZHVI'], ascending = [False, False, False, True]) #To find the bottom valuations
top_10_states = list(sort_data_decreasing.head(10)['State'])
bottom_10_states = list(sort_data_increasing.head(10)['State'])

filtered_top_10 = data[data['State'].isin(top_10_states)]
filtered_bottom_10 = data[data['State'].isin(bottom_10_states)]

plt.style.use("ggplot")

fig = plt.figure(figsize = (18, 12))
sns.lineplot(data = filtered_top_10, x = 'Year', y = 'ZHVI', hue = 'State')
plt.title("Top 10 Highest State Prices on Zillow")
plt.savefig("Visuals/Top_10_States_ZVHI.png")
plt.show()

plt.clf()
fig = plt.figure(figsize = (18, 12))
sns.lineplot(data = filtered_bottom_10, x = 'Year', y = 'ZHVI', hue = 'State')
plt.title("Bottom 10 Highest State Prices on Zillow")
plt.savefig("Visuals/Bottom_10_States_ZVHI.png")
plt.show()




plt.clf()
sns.lineplot(data = data, x = "Year", y = "ZHVI")
plt.title("Zillow House Evaluations Across 20 Years")
plt.savefig("Visuals/Total_House_Prices.png")
plt.show()


