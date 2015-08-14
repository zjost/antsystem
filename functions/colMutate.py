''' This function will reproduce a colony with mutated individuals.
It will generate a shifted alpha_weight array and assign new alpha
values to the ants based on these probabilities'''
import random
from functions.alphaWeightMutate import alphaWeightMutate
from functions.alphaAssign import alphaAssign

def colMutate(colony, alpha_min, alpha_max, max_mutation):
    # Mutate the alpha_weights of the colony
    alphaWeightMutate(colony.alphaWeights, max_mutation)
    # Assign new alpha values based on these mutated weights
    alphaAssign(colony, alpha_min, alpha_max)

    return colony
