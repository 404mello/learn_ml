#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:13:58 2019

@author: prawigya
"""
import pandas as pd

index = ['Moviename', 'Kicks', 'Kisses', 'Movietype']
movienames = ['California Man', 'He\'s not really into dudes', 'Beautiful woman', 'Kevin Longblade', 'Robo Slayer', 'Amped II']
kicks = [3,2,1,101,99,98]
kisses = [104, 100, 81, 10, 5, 2]
movietype = ['Romance', 'Romance', 'Romance', 'Acton', 'Action', 'Action']
#data = {'eid': [101,102,103,104], 'Name':['A','B','C','D'], 'sal':[1000,2000,3000,4000]}
data = {'Moviename':movienames, 'Kicks':kicks, 'Kisses':kisses, 'Movietype':movietype}
df = pd.DataFrame(data)
df.drop('Moviename')