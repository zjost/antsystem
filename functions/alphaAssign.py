''' This function will assign alpha values to a colony.  It will be
passed a colony, alpha_min, alpha_max, and an array of weights for
each alpha bucket.  It will then generate alpha values according to these
weights for all of the ants and update the values'''

import random

def alphaAssign(colony, alpha_min, alpha_max):
    alpha_weights = colony.alphaWeights
    # Get a list of alpha bins
    nBins = len(alpha_weights)
    d_alpha = (alpha_max-alpha_min)/(nBins-1)
    alpha_list = [alpha_min+i*d_alpha for i in range(nBins)]

    # Cycle through all ants in colony and assign alpha values
    for ant in colony.ants:
        # Generate a random number
        temp = random.random()
        # Keep a cumulative sum of probabilities
        tot = 0
        for idx, w in enumerate(alpha_weights):
            tot = tot + w
            # If in the cumulative probability range, assign the alpha
            if temp < tot:
                alpha = alpha_list[idx]
                ant.alphaUpdate(alpha)
                break

