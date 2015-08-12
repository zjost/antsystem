''' This function will run the mutation algorithm on a list of colonies
and return a new list of colonies'''

from functions.colMutate import colMutate
from functions.colSelection import colSelection
from copy import deepcopy

def colEvo(col_list, c0, c1, d_alpha_max):
    nColonies = len(col_list)
    # Get number of offspring for each colony
    offspring_list = colSelection(col_list, c0, c1)


    new_col_list = []
    # Iterate over list of offspring
    for i in range(nColonies):
        # Get number of children for colony i
        children = offspring_list[i]
        if int(children)==0:
            continue
        for j in range(int(children)):
            # Append mutated colony i for each number of children
            # Make a copy so that the original ants are not modified
            temp_col = deepcopy(col_list[i])
            new_col = temp_col.mutate(d_alpha_max)
            new_col_list.append(new_col)

    return new_col_list, offspring_list
        
            
    
