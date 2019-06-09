#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:32:04 2019

@author: prawigya
"""

import scikitplot as skplt
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

file_name = 'fruit_data_with_colors.txt'
name = ['mass', 'width', 'height', 'color_score']
fdata = pd.read_table(file_name)
X = fdata[name]
Y = fdata['fruit_label']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
ypredict = knn.predict(x_test)
prob = knn.predict_proba(x_test)
print(prob)
skplt.metrics.plot_roc(y_test, prob)
plt.show()
print("Confusion Matrix")
print(confusion_matrix(y_test, ypredict))
print("Classification Report")
print(classification_report(y_test, ypredict))
