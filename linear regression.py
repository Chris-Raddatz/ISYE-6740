from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(21)

file = pd.read_csv("merged_df.csv")

states = list(file.columns)[4:]

model = LinearRegression(fit_intercept= False, n_jobs = -1)
x = file[['CPI']]
y = file[states]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.15, train_size = .85, random_state = 21)
model.fit(xtrain, ytrain)

# print(model.intercept_) #Have an intercept of 0
cdf = pd.DataFrame(model.coef_, states, columns=['Coefficients'])
print(cdf)

sns.barplot(cdf.T)
plt.xticks(rotation = 90)
plt.title("State coefficients for Regressing on CPI")
plt.xlabel("States")
plt.ylabel("Coefficients")
plt.savefig("Coefficient_states.png")
plt.show()
# print(model.score(xtest, ytest))