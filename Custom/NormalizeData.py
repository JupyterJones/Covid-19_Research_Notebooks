'''
Ranges any span of numeric data between 0,1
Usage:
from NormalizeData import *
DATA = [1,34,546,3985,857463,49495857]
NormalizeData(DATA)
>>> array([0.00000000e+00, 6.66722483e-07, 1.10110228e-05, 8.04915870e-05,
       1.73239150e-02, 1.00000000e+00])
'''
import numpy as np
def NormalizeData(DATA):
    data = np.asarray(DATA)
    return (data - np.min(data)) / (np.max(data) - np.min(data))
