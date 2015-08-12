''' This function will create a list of colonies where each ant
selects its alpha parameter from a uniform distribution '''

import random
from Ant import Ant
from Colony import Colony

def colCreatev2(nColonies, nAnts, nCities, alpha_min, alpha_max, beta, Q):
    # Initialize list of colonies
    col_list = []

    # The change to alpha between colonies
    alpha_delta = (float(alpha_max)-alpha_min)/nColonies
    # Initialize a_min and a_max for the colonies
    a_min = alpha_min
    a_max = alpha_min + alpha_delta
    
    for i in range(nColonies):
        # Initialize ant list
        my_ants = []

        # Create new ants
        for j in range(nAnts):
            # Determine the initial city
            init_city = random.randint(0, nCities-1)
            # Define alpha for the individual
            #alpha = random.uniform(alpha_min, alpha_max)
            alpha = random.uniform(a_min, a_max)
            my_ants.append( Ant(nCities,alpha, beta, Q, init_city) )

        col_list.append(Colony(my_ants))

        # Update a_min and a_max
        a_min = a_min + alpha_delta
        a_max = a_max + alpha_delta

    return col_list
