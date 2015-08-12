import numpy as np
import random
from Colony import Colony
from functions.prob_city import prob_city
from functions.tau_branch import tau_branch
from functions.tau_prune import tau_prune

def tsp(colony, iters, n_mat):
    '''
    This function will cycle a colony through the cities
    for a given number of iterations.  It will return the updated
    colony
    Args:  colony is a colony of ants; iters is number of iterations
    to cycle through the TSP; n_mat is the visibility matrix of
    the current city configuration
    '''

    # Initialization
    N = len(n_mat[0,:]) # Number of cities
    tau = np.ones((30,30)) # initial trail
    epp = 0.0001 # Minimum branch level
    evap = 0.5 # evaporation constant
    my_ants = colony.ants
    clock = 0
    
    ''' Run simulation '''
    # Start the travels
    for j in range(iters):
        
        ##################
        # Re-initialize
        ##################
        # clear global delta_tau
        delta_tau = np.zeros((N,N))

        # Reset ants for next tour
        for ant in my_ants:
            init_city = random.randint(0, N-1)
            ant.reset(init_city)

        ##################
        # Iterate over all cities
        ##################
        for i in range (N):
            # Move all the ants to a new city
            for ant in my_ants:
                ant.move_city(tau, n_mat)
            # Increment the clock
            clock = clock + 1


        ##################
        # Have global path information
        ##################    
        # Scale individual tau's with inverse of ant's path length
        # and add to delta tau
        for ant in my_ants:
            ant.scale_tau()
            delta_tau = delta_tau + ant.dtau

        # Update colony with new, travelled ants 
        colony.updateAnts(my_ants)

        # Update the global tau
        tau = evap*tau+delta_tau

        # Prune to get rid of super small numbers
        tau = tau_prune(tau,epp)

    return colony

