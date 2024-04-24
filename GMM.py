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

# Used https://towardsdatascience.com/simple-example-of-2d-density-plots-in-python-83b83b934f67

def plot_kernel(data, state):
    x = np.array(data['CPI'])
    y = np.array(data[state])
    deltaX = (max(x) - min(x))/10
    deltaY = (max(y) - min(y))/10
    xmin = min(x) - deltaX
    xmax = max(x) + deltaX
    ymin = min(y) - deltaY
    ymax = max(y) + deltaY

    # Peform the kernel density estimate
    xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = stats.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)

    fig = plt.figure(figsize = (12,8))
    ax = fig.gca()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    # Contourf plot
    cfset = ax.contourf(xx, yy, f, cmap='coolwarm')
    ## Or kernel density estimate plot instead of the contourf plot
    #ax.imshow(np.rot90(f), cmap='Blues', extent=[xmin, xmax, ymin, ymax])
    # Contour plot
    cset = ax.contour(xx, yy, f, colors='k')
    # Label plot
    ax.clabel(cset, inline=1, fontsize=10)
    ax.set_xlabel('CPI')
    ax.set_ylabel('State ZHVI Values')
    plt.title('2D Gaussian Kernel density estimation for {}'.format(state))
    plt.show()
    return None

for state in states:
    plot_kernel(data, state)