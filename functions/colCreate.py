''' This function will create a list of colonies where each ant
selects its alpha parameter from a uniform distribution '''

import random
from Ant import Ant
from Colony import Colony

def colCreate(nColonies, nAnts, nCities, alpha_min, alpha_max, beta, Q):
    # Initialize list of colonies
    col_list = []
    
    for i in range(nColonies):
        # Initialize ant list
        my_ants = []
        # Create new ants
        for j in range(nAnts):
            # Determine the initial city
            init_city = random.randint(0, nCities-1)
            # Define alpha for the individual
            alpha = random.uniform(alpha_min, alpha_max)
            my_ants.append( Ant(nCities,alpha, beta, Q, init_city) )

        col_list.append(Colony(my_ants))

    return col_list
