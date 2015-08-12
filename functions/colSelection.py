from functions.fitness import fitness
import random
import numpy as np

def colSelection(col_list, c0, c1):
    nCols = len(col_list)
    fitness_list = []
    for colony in col_list:
        fitness_list.append(fitness(colony, c0, c1))

    totFit = sum(fitness_list)
    # This array holds votes for each colony in col_list
    colonyVotes = np.zeros(nCols)
    # Iterate over the total number of new colonies to be created
    for j in range(nCols):
        # Assign random number over size of total fitness
        temp1 = random.uniform(0, totFit)
        # Initialize an accumulator
        tot = 0
        # Get cumulative sum of fitnesses to decide on colony
        for i in range(nCols):
            # Update cumulative sum
            tot = tot + fitness_list[i]
            # If less than the random number, increase vote
            if temp1<tot:
                colonyVotes[i] = colonyVotes[i] + 1
                break

    return colonyVotes        
        
