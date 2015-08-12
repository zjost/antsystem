import numpy as np
import random
import matplotlib.pyplot as plt
from functions.plot_data import plot_data
from functions.visib import visib
from functions.prob_city import prob_city
from functions.tau_branch import tau_branch
from functions.tau_prune import tau_prune
from Ant import Ant

# Get visibility matrix
n = visib()

# Get the number of cities
N = len(n[0,:])

''' Ants '''
# Define number of ants and list object that will hold them
number_of_ants = N
#number_of_ants = 1
my_ants = []

# Define global ants characteristics
alpha = 1 # Pheromone effect
beta = 5 # Greed
Q = 100
init_city = 0

''' Stochastic Options'''
# Define random characteristics
#random.seed(1)

''' Initialization '''
tau = np.ones((30,30)) # initial trail
epp = 0.0001 # Minimum branch level
evap = 0.5 # evaporation constant
iters = 100 # Number of ant cycles
L_list = [] # list of global path lengths
L_list_a1 = [] # list of ant 1 path lengths
L_min = 100000 # Variable to hold minimum path
L_min_list = [] # List holding minimum path lengths
path_min = []
branch_list = [] # Record number of branches

# Getting the clock object
clock = 0

''' Run simulation '''
# Start the travels
for j in range(iters):
    
    ##################
    # Re-initialize
    ##################
    # clear delta_tau
    delta_tau = np.zeros((N,N))
    # clear ant list
    my_ants = []

    # Create new ants
    for i in range(number_of_ants):
        init_city = random.randint(0, N-1)
        my_ants.append( Ant(N,alpha, beta, Q, init_city) )


    ##################
    # Iterate over all cities
    ##################
    for i in range (N):
        # Move all the ants to a new city
        for ant in my_ants:
            ant.move_city(tau, n)
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
        L_list.append(ant.L)
        if ant.L < L_min:
            L_min = ant.L
            path_min = ant.tab
    L_list_a1.append(my_ants[0].L)
    L_min_list.append(L_min)

    # Update the global tau
    #print(delta_tau)
    tau = evap*tau+delta_tau
    #print(tau)
    # Prune to get rid of super small numbers
    tau = tau_prune(tau,epp)
    # Calculate branching
    branch_list.append(np.average(tau_branch(tau,epp)))

#L_list = np.array(L_list)
print(L_min)
print(path_min)

# Plot output
plot_data(L_min_list, branch_list)
