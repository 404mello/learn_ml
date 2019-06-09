#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:16:20 2019

@author: prawigya
"""

#Feature selection
#Used to tackle overfitting, underfitting, time consumption and accuracy
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
filename = 'winequality-red.csv'
data = pd.read_csv(filename)
data = data.values
X=data[:,0:11]
Y=data[:,11]

#SelectKBest, chi2
np.set_printoptions(precision=3)
fs = SelectKBest(score_func=chi2, k=4) #No of features used=4
fitdata = fs.fit(X,Y)
print("Score", fitdata.scores_)
tdata = fitdata.transform(X)
print(tdata[0:5,])

"""
model = LogisticRegression()
rfe = RFE(model, n_features_to_select=3)
fit = rfe.fit(X,Y)
print("Number of features used", fit.n_features_)
print("Features selected", fit.support_)
print("Rank of features",fit.ranking_)
"""
