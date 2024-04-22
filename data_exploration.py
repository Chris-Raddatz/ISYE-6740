import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data/merged_df.csv")

plt.style.use("ggplot")

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

# fig = plt.figure(figsize = (18, 12))
# sns.lineplot(data = filtered_top_10, x = 'Year', y = 'ZHVI', hue = 'State')
# plt.title("Top 10 Highest State Prices on Zillow")
# plt.savefig("Visuals/Top_10_States_ZVHI.png")
# plt.show()

fig = plt.figure(figsize = (18, 12))
sns.lineplot(data = filtered_bottom_10, x = 'Year', y = 'ZHVI', hue = 'State')
plt.title("Lowest 10 State Prices on Zillow")
plt.savefig("Visuals/Bottom_10_States_ZVHI.png")
plt.show()

# plt.clf()
# fig = plt.figure(figsize = (18, 12))
# sns.lineplot(data = data, x = "Year", y = "ZHVI")
# plt.title("Zillow House Evaluations Across 20 Years")
# plt.savefig("Visuals/Total_House_Prices.png")
# plt.show()

#Calculate minimum, maximum, standard deviation and % increase
minimums = []
maximums = []
percent_increases = []
stdevs = []

states = data['State'].unique()

for i in states:
    filtered_df = data[data['State'] == i]
    max = round(np.max(filtered_df['ZHVI']))
    min = round(np.min(filtered_df['ZHVI']))
    stdev = round(np.std(filtered_df['ZHVI']), 2)
    start = filtered_df.loc[filtered_df.index[0], "ZHVI"]
    finish = filtered_df.loc[filtered_df.index[-1], "ZHVI"]

    percent_increase = round((finish - start) / start * 100, 2)

    minimums.append(min)
    maximums.append(max)
    stdevs.append(stdev)
    percent_increases.append(percent_increase)

stats = pd.DataFrame({"State" : states,"Minimum" : minimums, "Maximum" : maximums, "Standard Deviation" : stdevs, "Percent Increase" : percent_increases})

order_stats = stats[['State', 'Percent Increase']].sort_values(by = "Percent Increase", ascending = False).reset_index(drop = True)

head_order = order_stats.head(5)
tail_order = order_stats.tail(5)

merged_orders = pd.concat([head_order, tail_order], axis = 0)

print(merged_orders)

plt.figure(figsize = (14,8))
sns.barplot(order_stats, y = "Percent Increase", x = "State")
plt.xticks(rotation = 90)
plt.title("Percent Increase in ZHVI (2002 - 2021)")
plt.xlabel("States")
plt.ylabel("Percent Increase")
plt.savefig("Visuals/Percent_Increase.png")
plt.show()


