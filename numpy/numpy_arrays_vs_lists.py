# setting the enviornments in Visual Code first: https://code.visualstudio.com/docs/python/environments
# https://colab.research.google.com/drive/1VdLyfnop7Tt4wx4BmS6WHSSQg3n5wXrX
# arrays vs lists.

import numpy as np
import pandas as pd


L = [1,2,3] # standard non-numpy list
A = np.array([1,2,3]) # numpy-array


for e in L:
    print (e)

for e in A:
    print (e)

print (A)

L.append(5)
L
A+np.array([4])
x = A+np.array([4,5,6])
x
