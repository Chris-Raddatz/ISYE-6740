import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data\merged_df.csv")
conn = data[['Connecticut', 'CPI']]
sns.lineplot(conn, x = "CPI", y = "Connecticut")
plt.show()