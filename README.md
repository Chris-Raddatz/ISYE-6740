# ISYE-6740-
Repo for final project


# Project Timeline

1) First we will load the data and combine the two dataframes, while cleaning out states that have many null values and cleaning up the date format. 

2) Secondly, we can do some data exploration with histograms, barcharts, correlation heatmaps, any sort of visual representation of the data. 
- Just plotted top, bottom and all states ZHVI values across the timeline of the project. You can see the canyon around the 2008 crash, and from 2020 onward there's almost an exponential growth curve. One thing I was thinking of fixing was to get the date to look like a whole number and remove the .0, but I'd like to do some stuff later on it might not be a big deal.

So I found that dummying the data didn't do anything, probably because the values were already separated easily. So a slight overcalculation on my part. 

3) First I want to try building models out of the original data, but we can then look into performing PCA and finding some similarities across that as well. 
- I think we should look into gathering metrics for these models: R^2, RMSE, things of that nature. 
- Taking the log value of the ZVHI values reduced the test score to -65.72, but the RMSE was reduced to 0.51 lol. Also R^2 is the same as model.score(ytest, y_pred)

4) Perform Clustering to identify similar house markets. 

5) GMM Possibly

6) Look into the difference in values between 2001 and 2007, see how they compare from 2020 onward. Could be interesting to see if there's a difference. 

### What I've Done:
- Loaded Data and looked into initial data exploration: Correlation Maps, simple linear plots, can think of more as we go on
- Performed Linear Regression, identifying what states have the highest coefficients for CPI when regressed - meaning they have higher house prices as they CPI goes up
- Looked into SVM slightly, but didn't spend too much time on it. 
- Now done PCA, most of the variation was within Dimension 1, Dimension 2 offers variability but because it doesn't explain much variance I pay little attention to it. 
- Plotted percent increase in ZHVI values across the timeline, to get another visual on which states are at the high and bottom of this spectrum. 


### Doing Currently
- Look into clustering of the PCA data, can also try to do GMM between CPI and each state