from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(21)

file = pd.read_csv("data/merged_df.csv")

states = list(file.columns)[4:]

x = file[['CPI']]
y = file[states]

# params = {"fit_intercept" : [True, False], "n_jobs" : [None, 1, -1], "fit_intercept" : [True, False],
#            "positive" : [True, False]}

# model = LinearRegression()

# gridsearch = GridSearchCV(model, param_grid= params)

# gridsearch.fit(x, y)
# print(gridsearch.best_params_)


xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.20, train_size = .80, random_state = 21)
model = LinearRegression(fit_intercept=False, n_jobs=None, positive=False)
model.fit(xtrain, ytrain)
y_pred = model.predict(xtest)

cdf = pd.DataFrame(model.coef_, states, columns=['Coefficients'])

ordered_by_coef = cdf.sort_values(by = "Coefficients", ascending = False)

plt.figure(figsize = (14,8))
sns.barplot(ordered_by_coef.T)
plt.xticks(rotation = 90)
plt.title("State coefficients for Regressing on CPI")
plt.xlabel("States")
plt.ylabel("Coefficients")
plt.savefig("Visuals/Coefficient_states.png")
plt.show()
print("Model Training Score: {:.2f}".format(model.score(xtrain, ytrain)))
print("Model Test Score: {:.2f}".format(model.score(xtest, ytest)))
print("MSE {:.2f}".format(mean_squared_error(ytest, y_pred, squared = False)))
print("R^Squared Score: {:.2f}".format(r2_score(ytest, y_pred)))