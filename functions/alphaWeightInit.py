''' This function will initialize alpha_weights to be passed to
the alphaAssign function for assigning alpha values to individual ants
within a colony.  It will be called by colCreate.py.  The method of assigning
weights is set by the flag variable'''

import numpy as np
import random

def alphaWeightInit(nBins, flag):
    ''' flag methods:
    0 - All weights are equal
    1 - Weights are random
    '''
    
    if flag == 0:
        w = [1/nBins]*nBins
        w = np.array(w)
    else:
        w = []
        for i in range(nBins):
            w.append(random.random())
        w = np.array(w)
        w = w/w.sum()

    return w
        
