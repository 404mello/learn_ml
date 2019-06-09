#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:37:49 2019

@author: prawigya
"""

from sklearn.svm import SVC
import mglearn
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
cancer = load_breast_cancer()
X,Y = mglearn.tools.make_handcrafted_dataset()
print(X, Y)
svm = SVC(kernel='rbf', C=10, gamma = 0.1).fit(X,Y)
mglearn.plots.plot_2d_separator(svm, X, eps=0.5)
plt.scatter(X[:,0],X[:,1],s=60, c=Y, cmap=mglearn.cm3)
sv = svm.support_vectors_
print(sv)
plt.scatter(sv[:,0], sv[:,1],s=200, facecolors='none', zorder = 10, linewidths = 3)
plt.show()
fig, axes = plt.subplots(3,3, figsize = (15,10))
for ax, C in zip(axes, [-1, 0, 3]):
    for a, gamma in zip(ax, range(-1, 2)):
        mglearn.plots.plot_svm(log_C=C, log_gamma=gamma, ax=a)
plt.show()

x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
svc = SVC()

svc.fit(x_train, y_train)
plt.plot(x_train.min(axis=0), 'o', label="min")
plt.plot(x_train.max(axis=0), 'o', label="max")
plt.legend(loc='best')
plt.yscale('log')
plt.show()
