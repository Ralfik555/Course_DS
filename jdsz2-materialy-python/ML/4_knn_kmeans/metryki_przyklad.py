# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:45:19 2019

@author: krzys
"""

from sklearn.neighbors import DistanceMetric
from matplotlib import pyplot as plt
import numpy as np

####------------------ rozkład kadegorii, sredni oraz z dwch przykladowych dniach ---
avg_dist =  [ 0.2, 0.15, 0.12, 0.10, 0.09, 0.09, 0.07, 0.05, 0.04, 0.03, 0.03, 0.02, 0.01]
day1 =      [ 0.18, 0.16, 0.13, 0.11, 0.08, 0.08, 0.08, 0.04, 0.05, 0.02, 0.04, 0.01, 0.02]
day2 =      [ 0.2, 0.15, 0.12, 0.10, 0.09, 0.09, 0.04, 0.08, 0.04, 0.03, 0.03, 0.02, 0.01]
sum(day2)

##------- nadanie labeli (do wykresu)
label = [ 'l_'+ str(i+1) for i in range(len(avg_dist))]
x = np.arange(len(avg_dist))

####--------- wykresy kategori ------
plt.figure(figsize=(15,10))
plt.bar(x,avg_dist)
plt.xticks(x,label)
plt.show()

plt.figure(figsize=(15,10))
plt.bar(x,day1)
plt.xticks(x,label)
plt.show()

plt.figure(figsize=(15,10))
plt.bar(x,day2)
plt.xticks(x,label)
plt.show()

##--------- rozkłady po dniach w licie, by policzyć macierz odległoci ---
X = [avg_dist,day1,day2 ]

##-------- wybranie metryki i policzenie wg niej odległosci ----------
dist = DistanceMetric.get_metric('euclidean')
d = dist.pairwise(X)
print('euclidean\n',d)
print('difference:', d[0][2]/d[0][1])

dist = DistanceMetric.get_metric('chebyshev')
d = dist.pairwise(X)
print('chebyshev\n',d)
print('difference:', d[0][2]/d[0][1])