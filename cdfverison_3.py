# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:38:00 2022

@author: User
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from statsmodels.distributions.empirical_distribution import ECDF
# np.random.seed( 10 )
# number of random variable && iteration
num_x = 100
num_y = 100
iteration = 100

# Set an empty list
k = np.zeros([1, 100])
rv_x = np.zeros(num_x)
rv_y = np.zeros([1, num_y])

# Initial value of x and y (uniform distribution)
for i in range(num_y):
    rv_x = np.random.uniform(0, 10, num_x)
    rv_y[0, i] = np.mean(rv_x)

#
for num_iter in range(iteration):
    d = np.reshape(rv_y, (num_y,))
    ecdf = ECDF(d)
    inv_cdf = interp1d(ecdf.y, ecdf.x, bounds_error=False, assume_sorted=True)  # INV CDF
    for i in range(num_y):
        rv_idx = np.random.uniform(0, 1, num_x)  # determined number of new random variable

        rv_x = inv_cdf(rv_idx)
        #print(rv_x)
    # find out where is i-inf and change it t
    for find_inf in range(len(rv_x)):
        if -np.inf == rv_x[find_inf]:
            rv_x[find_inf] = np.random.uniform(0,1,1)
        #print(rv_idx[np.where(rv_x == -np.inf)[0][0]])  # check the index of -inf from which one
    print(rv_x)
    rv_y[0, i] = np.mean(rv_x)

plt.hist(rv_y, histtype='step', bins=25, density=True, stacked=True)
plt.show()





