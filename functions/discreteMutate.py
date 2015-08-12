''' This function will mutate a colony of ants that have alpha's from one
of two possible values.  It will calculate a relative frequency and then
generate random numbers using that frequency measure '''

import random

def discreteMutate(colony):
    
    alphaDist = colony.getAlphaDist()
    alpha_min = alphaDist.min()
    alpha_max = alphaDist.max()
    N = len(alphaDist)
    # Get number of ants with alpha = alpha_max
    Nalpha2 = sum(x==alpha_max for x in alphaDist)
    # Calculate the probability of assigning alpha = alpha_max
    f = Nalpha2/N
    for ant in colony.ants:
        temp = random.random()
        if temp < f:
            ant.alphaUpdate(alpha_max)
        else:
            ant.alphaUpdate(alpha_min)


    # Return updated colony list
    return colony
