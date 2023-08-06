# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


dataset = pd.read_csv("forestfires.csv")

x = dataset[["month","day"]].values

# =============================================================================
# dataset.drop(columns=(['month','day']),axis=1)
# ds = dataset.drop((['month','day']),axis=1)
# from sklearn.model_selection import train_test_split
# train, test = train_test_split(ds,train_size=.3,test_size=.7)
# train_X = train.drop("area",axis=1).copy()
# train_Y=pd.DataFrame()
# train_Y['area']=train['area'].copy()
# dataset['output']=dataset['area'].copy()
# 
# test_X = test.drop("area",axis=1).copy()
# test_Y=pd.DataFrame()
# test_Y['area']=test['area'].copy()
# 
# from sklearn.neural_network import MLPRegressor
# 
# ann_model = MLPRegressor(random_state=1, max_iter=500).fit(train_X, train_Y)
# predication = ann_model.predict(test_X)
# predication_df = pd.DataFrame(predication)
# predication_df.to_csv("predicate.csv")
# =============================================================================
