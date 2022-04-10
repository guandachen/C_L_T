# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:38:00 2022

@author: User
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from statsmodels.distributions.empirical_distribution import ECDF
# example of a bimodal data sample
from matplotlib import pyplot
from numpy.random import normal
from numpy import hstack
from scipy import stats
import scipy
# from scipy.stats.sampling import NumericalInverseHermite
from scipy.stats import norm, genexpon
from scipy.special import ndtr


# Make up some random data
def normal_kernel(x):
    return 1 / np.sqrt((2 * np.pi)) * np.exp(-0.5 * x ** 2)


# olp:out loop run 100 times

olp = 0
k = np.zeros([1, 100])
# var2
while olp < 100:
    s = np.zeros([1, 100])  # save an empty list
    i = 0
    b = 0
    while i < 100:
        g = np.random.uniform(0, 10, 100)  # fist input
        a = 0
        b = 0
        # do average and sort it
        while a < 100:
            b = b + g[a]
            a = a + 1
            # print(i)
            c = b / 100
            # print(c)
            s[0, i] = c

        i = i + 1
    d = np.reshape(s, (100,))  # set the data to 1-dimension array
    ecdf = ECDF(d)  # find ECDF

    inv_cdf = interp1d(ecdf.y, ecdf.x, bounds_error=False, assume_sorted=True)  # INV CDF

    r = np.random.uniform(0, 1, 100)
    ys = inv_cdf(r)
    where_are_inf = np.isinf(ys)
    ys[where_are_inf] = 0
    print(ys)

    k[0, olp] = np.sum(ys) / 100;
    olp = olp + 1;
    ys = 0;

fin_val = np.reshape(k, (100,))
ecdf = ECDF(fin_val);
inv_cdf = interp1d(ecdf.y, ecdf.x, bounds_error=False, assume_sorted=True)

fin_r = np.random.uniform(0, 1, 100)
fin_ys = inv_cdf(fin_r)
where_are_inf = np.isinf(fin_ys)
fin_ys[where_are_inf] = 5
# print(fin_ys)
plt.hist(fin_ys, 25)  # histtype='step', color='blue', linewidth=1);
plt.show()
pdf = 0
total_fin_ys = [i for i in range(0, 10, 1)]
total_pdf = []
for x in total_fin_ys:
    for i in fin_ys:
        pdf += normal_kernel(x - i)
    pdf = pdf / len(fin_ys)
    total_pdf.append(pdf)
plt.plot(total_fin_ys, total_pdf)
plt.show()
