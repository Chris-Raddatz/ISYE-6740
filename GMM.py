import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
import math
import numpy as np
from sklearn.neighbors import KernelDensity
import statistics as st
from matplotlib.pyplot import plot
import scipy.stats as stats


data = pd.read_csv("data/merged_df.csv")

states = data.columns[4:]

m = data.shape[0]

# Used https://towardsdatascience.com/simple-example-of-2d-density-plots-in-python-83b83b934f67

def plot_kernel(data, state):
    x = np.log(np.array(data['CPI']))
    y = np.log(np.array(data[state]))
    deltaX = (max(x) - min(x))/10
    deltaY = (max(y) - min(y))/10
    xmin = min(x) - deltaX
    xmax = max(x) + deltaX
    ymin = min(y) - deltaY
    ymax = max(y) + deltaY
# Create meshgrid
    xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j] # 100 Values from xmin to xmax and from ymin to ymax


    positions = np.vstack([xx.ravel(), yy.ravel()]) #Ravel flattens, then we stack onto each other
    values = np.vstack([x, y])
    kernel = stats.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)

    fig = plt.figure(figsize=(12,8))
    ax = fig.gca() #Gets axis
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    cfset = ax.contourf(xx, yy, f, cmap='coolwarm') #Color levels
    ax.imshow(f, cmap='coolwarm')
    cset = ax.contour(xx, yy, f, colors='k') #Plots the lines
    ax.clabel(cset, fontsize=10) #Provides labels for each contour 
    ax.set_xlabel('CPI (Log Transformed)')
    ax.set_ylabel('State ZHVI (Log Transformed)')
    plt.title('2D Gaussian Kernel density estimation for {}'.format(state))
    plt.show()
    return None
for state in states:
    plot_kernel(data, state)