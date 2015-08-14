import numpy as np
import random
import matplotlib.pyplot as plt
from time import time
from functions.plot_data import plot_data
from functions.visib import visib
from functions.prob_city import prob_city
from Ant import Ant
from Colony import Colony
from functions.colCreate import colCreate
from functions.colEvo import colEvo
from functions.tsp import tsp
from functions.fitness import fitness
from functions.antplot import plotFitnessMat
from functions.antplot import plotAlphaDist
from functions.antplot import plotLBox
from functions.saveFiles import saveFiles

# Get visibility matrix
n_mat = visib()

# Get the number of cities
N = len(n_mat[0,:])

''' Ants '''
# Define number of ants and list object that will hold them
number_of_ants = N


# Define global ants characteristics
beta = 5 # Greed
Q = 100
init_city = 0

''' Stochastic Options'''
# Define random characteristics
#random.seed(1)

''' Cycle Parameters '''
iters = 50 # Number of ant cycles
#d_alpha_max = 0.01 # Max evo shift in alpha
evo_cycles = 100

# Colony evolution parms
c0 = 0 # weight for Lavg
c1 = 2000 # weight for Lmin
alpha_min = 0
alpha_max = 10
max_mutation = 0.05
evoParms = (c0, c1, alpha_min, alpha_max, max_mutation)

# Colony create parms
nColonies = 100
initMethodFlag = 1
nBins = 10
colCreateParms = (nColonies, number_of_ants, N, alpha_min,
                  alpha_max, beta, Q, initMethodFlag, nBins)


# Saved files params
params = (nColonies, iters, evo_cycles, alpha_min, alpha_max,
          max_mutation, c0, c1)

# Variable initialization
fitness_mat = np.zeros((evo_cycles, nColonies))
lMin_mat = np.zeros((evo_cycles, nColonies))
lAvg_mat = np.zeros((evo_cycles, nColonies))
# Will hold the best alpha distribution for each evo cycle
alphaBestMin = []

# Initialize a list of ant colonies
colony_list = colCreate(colCreateParms)

for i in range(evo_cycles):
    # create a colony index
    j = 0
    # Initialize minimum to a high number
    tempMin = 1e5
    # Cycle each colony through TSP 'iters' times
    for colony in colony_list:
        # Submit to TSP cycling
        colony = tsp(colony, iters, n_mat)
        # Display update and store fitness of current colony/evo
        print("evo= " + str(i) + " , colony= "+str(j))
        fitness_mat[i,j]=fitness(colony, c0, c1)
        # Get colony minimum for this evo and store it
        iterMin = colony.minL
        lMin_mat[i,j]=iterMin
        lAvg_mat[i,j]=colony.L/colony.N
        # Check if it's best so far from all colonies
        # If so, store the index of the colony
        if iterMin<tempMin:
            tempMin = iterMin
            bestIdx = j
        # Increment colony index    
        j = j+1

    # Store the alpha dist. for the best L_min
    alphaBestMin.append(colony_list[bestIdx].getAlphaDist())

    # Evolve the colony list for the next iteration
    colony_list, offspring_list = colEvo(colony_list, evoParms)
    print(fitness_mat[i,:])
    print(offspring_list)


saveFiles(fitness_mat, alphaBestMin, lMin_mat, lAvg_mat, params, int(time()))
#plotFitnessMat(fitness_mat)
#plotAlphaDist(alphaBestMin[0:evo_cycles:int(evo_cycles/10)])
#plotLBox(lMin_mat, 0)
#plotLBox(lAvg_mat, 1)

