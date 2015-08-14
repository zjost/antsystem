''' This function will create a list of colonies where each ant
selects its alpha parameter from one of two values '''

import random
from Ant import Ant
from Colony import Colony
from functions.alphaAssign import alphaAssign
from functions.alphaWeightInit import alphaWeightInit

# This version will assign each ant one of two alpha values (min or max)
# The variation in colony will come from the relative frequency of the two


def colCreate(colCreateParms):

    ''' colCreateParms list:
    nColonies, nAnts, nCities are number of each.
    alpha_min, alpha_max are alpha parameter constraints
    beta and Q are ant parameters
    initMethodFlag controls the alpha weight calculation method used
    in alphaWeightInit function.
    nBins is the number of bins created for alpha assignments
    '''

    (nColonies, nAnts, nCities, alpha_min, alpha_max,
         beta, Q, initMethodFlag, nBins) = colCreateParms

    # Initialize list of colonies
    col_list = []

    
    for i in range(nColonies):
        # Initialize ant list
        my_ants = []

        # Create new ants
        for j in range(nAnts):
            # Determine the initial city
            init_city = random.randint(0, nCities-1)
            # Define dummy alpha for the individual
            alpha = 0
            my_ants.append( Ant(nCities,alpha, beta, Q, init_city) )

        # Create colony class
        newColony = Colony(my_ants)
        # Set alpha_weights
        alpha_weights = alphaWeightInit(nBins, initMethodFlag)
        newColony.setAlphaWeights(alpha_weights)
        # Assign real alpha values
        alphaAssign(newColony, alpha_min, alpha_max)

        col_list.append(newColony)


    return col_list
