''' This function will create a list of colonies where each ant
selects its alpha parameter from one of two values '''

import random
from Ant import Ant
from Colony import Colony

# This version will assign each ant one of two alpha values (min or max)
# The variation in colony will come from the relative frequency of the two


def colCreate(nColonies, nAnts, nCities, alpha_min, alpha_max, beta, Q):
    # Initialize list of colonies
    col_list = []

    
    for i in range(nColonies):
        # Initialize ant list
        my_ants = []

        # Get a relative frequency of alpha_max to alpha_min for colony i
        f = random.random()

        # Create new ants
        for j in range(nAnts):
            # Determine the initial city
            init_city = random.randint(0, nCities-1)
            # Define alpha for the individual
            #alpha = random.uniform(alpha_min, alpha_max)
            #alpha = random.uniform(a_min, a_max)
            temp = random.random()
            if temp < f:
                alpha = alpha_max
            else:
                alpha = alpha_min
            my_ants.append( Ant(nCities,alpha, beta, Q, init_city) )

        col_list.append(Colony(my_ants))


    return col_list
