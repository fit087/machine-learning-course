# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read a dataset from a csv file
data = pd.read_csv('Data.csv')

# iloc select a submatrix (it's a method in a pandas class)
X = data.iloc[:,:-1].values
Y = data.iloc[:,-1].values

print(data)
print (X)
print (Y)
