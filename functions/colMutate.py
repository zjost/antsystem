''' This function will reproduce a colony with mutated individuals.
It will merely copy each ant and shift the alpha by a number from
a uniform distribution centered at zero and between a specific
max distance'''
import random

def colMutate(colony, d_alpha_max):
    for ant in colony.ants:
        old_alpha = ant.alpha
        new_alpha = old_alpha + random.uniform(-d_alpha_max/2, d_alpha_max/2)
        ant.alphaUpdate(new_alpha)

    return colony
