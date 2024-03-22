from sklearn.linear_model import LinearRegression
import pandas as pd

file = pd.read_csv("merged_df.csv")
# print(file.head())

states = list(file.columns)[4:]

model = LinearRegression()
x = file[['CPI']]
y = file[states]


model.fit(x, y)

print(model.intercept_)
cdf = pd.DataFrame(model.coef_, states, columns=['Coefficients'])
print(cdf)