# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir('/home/acorrea/Dropbox/2020.1/ML/Machine Learning A-Z/Part 1 - Data Preprocessing')

# Read a dataset from a csv file
data = pd.read_csv('Data.csv')

# iloc select a submatrix (it's a method in a pandas class)
X = data.iloc[:,:-1].values
Y = data.iloc[:,-1].values

#print(data)
#print (X)
#print (Y)

# Taking care of missing data
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values=np.nan, strategy="mean", axis=0)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

print(X)

