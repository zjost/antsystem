''' This defines the calculation for fitness of a colony '''

def fitness(colony, c0, c1):
    # This function calculates the fitness of the colony
    totL = colony.L
    avgL = totL/colony.N
    minL = colony.minL

    # Dorigo's best:  423.741
    # Dorigo's avg:  424.250

    #return c0/(avgL-415.) + c1/(minL-415.)
    return c0/(avgL-430)**2 + c1/(minL-415)**2
    
