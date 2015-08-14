''' This function will mutate alpha_weights based on a max mutation
probability distance.  It takes an alpha_weight vector and mutation
amount and randomly changes the weight of each element +/- a random
number between 0 and the max value.'''

import random

def alphaWeightMutate(alpha_weights, max_mutation):
    nBins = len(alpha_weights)
    for idx, weight in enumerate(alpha_weights):
        # Generate a number beteen +/- max_mutation
        delta = 2*(random.random()-0.5)*max_mutation
        if (weight+delta < 0):
            alpha_weights[idx] = 0
        else:
            alpha_weights[idx] = weight+delta

