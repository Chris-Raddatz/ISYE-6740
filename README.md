# ISYE-6740-
Repo for final project


# Project Timeline

1) First we will load the data and combine the two dataframes, while cleaning out states that have many null values and cleaning up the date format. 

2) Secondly, we can do some data exploration with histograms, barcharts, correlation heatmaps, any sort of visual representation of the data. 
- Just plotted top, bottom and all states ZHVI values across the timeline of the project. You can see the canyon around the 2008 crash, and from 2020 onward there's almost an exponential growth curve. One thing I was thinking of fixing was to get the date to look like a whole number and remove the .0, but I'd like to do some stuff later on it might not be a big deal.

So I found that dummying the data didn't do anything, probably because the values were already separated easily. So a slight overcalculation on my part. 

3) First I want to try building models out of the original data, but we can then look into performing PCA and finding some similarities across that as well. 
- I think we should look into gathering metrics for these models: R^2, RMSE, things of that nature. 
- We've looked at linear regression, we should try our SVM, and look into transforming the ZHVI values into log values, it could help.
