# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


dataset = pd.read_csv("forestfires.csv")

dataset.drop(columns=(['month','day']),axis=1)
ds = dataset.drop((['month','day']),axis=1)
from sklearn.model_selection import train_test_split
train, test = train_test_split(ds,train_size=.3,test_size=.7)
trin_X = train.drop("area",axis=1).copy()
train_Y=pd.DataFrame()
train_Y['area']=train['area'].copy()
dataset['output']=dataset['area'].copy()
