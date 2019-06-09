#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:47:06 2019

@author: prawigya
"""

import pandas as pd
#from sklearn.svm import
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import mglearn
import numpy as np
from mpl_toolkits.mplot3d import Axes3D, axes3d

filename = 'Social_Network_Ads.csv'
df = pd.read_csv(filename)
X = df[['Age','EstimatedSalary']].values
Y = df['Purchased'].values

plt.xlabel("Age")
plt.scatter(X[:, 0], X[:, 1], c=Y, s=60, cmap=mglearn.cm2)
plt.ylabel("Estimated Salary")
plt.show()

svm = SVC(kernel='poly', C=10, gamma = 0.1).fit(X,Y)

mglearn.plots.plot_2d_separator(svm, X)
plt.xlabel("Age")
plt.scatter(X[:, 0], X[:, 1], c=Y, s=60, cmap=mglearn.cm2)
plt.ylabel("Estimated Salary")
plt.show()

X_new = np.hstack([X, X[:,1:]**2])
figure = plt.figure()
ax = Axes3D(figure, elev=-152, azim = -26)
ax.scatter(X_new[:,0], X_new[:,1], X_new[:,2], c=Y, cmap = mglearn.cm2, s=60)
ax.set_xlabel("Age")
ax.set_ylabel("EstimatedSalary")
ax.set_zlabel("Age**2")
plt.show()

linear_svm_3d = SVC(kernel='poly', C=10, gamma = 0.1).fit(X_new, Y)
coef, intercept = linear_svm_3d.coef_.ravel(),linear_svm_3d.intercept_
figure = plt.figure()
ax = Axes3D(figure, elev=-152, azim=-26)
xx = np.linspace(X_new[:, 0].min(), X_new[:, 0].max(), 50)
yy = np.linspace(X_new[:, 1].min(), X_new[:, 1].max(), 50)
XX, YY = np.meshgrid(xx, yy)
ZZ = (coef[0] * XX + coef[1] * YY + intercept) / -coef[2]
ax.scatter(X_new[:, 0], X_new[:, 1], X_new[:, 2], c=Y,
           cmap=mglearn.cm2, s=60)
ax.plot_surface(XX, YY, ZZ, rstride=8, cstride=8, alpha=0.3)
ax.set_xlabel("feature1")
ax.set_ylabel("feature2")
ax.set_zlabel("feature1 ** 2")
plt.show()
"""
plt.xlabel("feature1")
plt.scatter(X[:, 0], X[:, 1], c=y, s=60, cmap=mglearn.cm2)
plt.ylabel("feature2")
plt.show()
from sklearn.svm import LinearSVC
linear_svm = LinearSVC().fit(X, y)
mglearn.plots.plot_2d_separator(linear_svm, X)
plt.scatter(X[:, 0], X[:, 1], c=y, s=60, cmap=mglearn.cm2)
plt.xlabel("feature1")
plt.ylabel("feature2")
plt.show()

X_new = np.hstack([X, X[:, 1:] ** 2])
from mpl_toolkits.mplot3d import Axes3D, axes3d
figure = plt.figure()
ax = Axes3D(figure, elev=-152, azim=-26)
ax.scatter(X_new[:, 0], X_new[:, 1], X_new[:, 2],
           c=y, cmap=mglearn.cm2, s=60)
ax.set_xlabel("feature1")
ax.set_ylabel("feature2")
ax.set_zlabel("feature1 ** 2")
plt.show()

linear_svm_3d = LinearSVC().fit(X_new, y)
coef, intercept = linear_svm_3d.coef_.ravel(),linear_svm_3d.intercept_
figure = plt.figure()
ax = Axes3D(figure, elev=-152, azim=-26)
xx = np.linspace(X_new[:, 0].min(), X_new[:, 0].max(), 50)
yy = np.linspace(X_new[:, 1].min(), X_new[:, 1].max(), 50)
XX, YY = np.meshgrid(xx, yy)
ZZ = (coef[0] * XX + coef[1] * YY + intercept) / -coef[2]
ax.scatter(X_new[:, 0], X_new[:, 1], X_new[:, 2], c=y,
           cmap=mglearn.cm2, s=60)
ax.plot_surface(XX, YY, ZZ, rstride=8, cstride=8, alpha=0.3)
ax.set_xlabel("feature1")
ax.set_ylabel("feature2")
ax.set_zlabel("feature1 ** 2")
plt.show()
"""