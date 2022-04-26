# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:14:04 2022

@author: Eduin Hernandez
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from statsmodels.distributions.empirical_distribution import ECDF

num_x = 100
num_y = 100
iteration = 20

rv_x = np.random.uniform(0, 10, (num_x, num_y))
rv_y = rv_x.mean(axis=0)
    
d = rv_y.flatten()

ecdf = ECDF(d)
inv_cdf = interp1d(ecdf.y, ecdf.x, bounds_error=False, assume_sorted=True)  # INV CDF

rv_idx = np.random.uniform(inv_cdf.x[1], inv_cdf.x[-1], (iteration, num_x, num_y))
rv_x_new = inv_cdf(rv_idx)
rv_y_new = rv_x_new.mean(axis=1)

plt.hist(rv_y_new.flatten(), histtype='step', bins=25, density=True, stacked=True)
plt.show()