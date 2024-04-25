import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data/clean_CPI.csv")

plt.style.use("ggplot")

restricted_data = data[(data['Year'] >= 2002) & (data['Year'] <= 2021)].reset_index(drop = True)

fig = plt.figure(figsize = (18, 12))
sns.lineplot(data = restricted_data, x = 'Year', y = 'CPI')
plt.title("CPI over 2002 - 2021")
plt.savefig("Visuals/CPI_Over_Time.png")
plt.show()