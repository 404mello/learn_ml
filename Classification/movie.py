#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:42:43 2019

@author: prawigya
"""
#from numpy import *
import numpy
from operator import itemgetter
from sklearn.metrics.pairwise import euclidean_distances

def CreateDataset(): 
    group = numpy.array([[1,1.1],[1,1],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify(p_data, dataset, labels, k):
    """
    dataSetSize = dataset.shape[0]
    diffmat = tile(p_data, (dataSetSize, 1)) - dataset
    sqDifMat = diffmat ** 2
    sqDistance = sqDifMat.sum(axis=1)
    distance = sqDistance**0.5
    """
    distance = euclidean_distances(dataset, p_data)
    #print(distance)
    sortMatDistance = distance[:,0].argsort()
    classcount = {}
    for i in range(k):
        v = labels[sortMatDistance[i]]
        classcount[v] = classcount.get(v,0)+1
        sortClassCount = sorted(classcount.items(), key = itemgetter(1), reverse=True)
    return sortClassCount[0][0]
    