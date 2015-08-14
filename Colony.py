import numpy as np
from functions.prob_city import prob_city
from functions.choose_city import choose_city
from Ant import Ant
import random


class Colony():
    def __init__(self, ant_list):
        self.ants = ant_list # list of ants from Ant class
        self.N = len(ant_list) # number of ants in colony
        self.L = 1e5 # total path length
        self.minL = 1e5 # minimum L
        self.alphaWeights = []

    def getAlphaDist(self):
        # This method returns an array of alpha values for the population
        alphaList = []
        for ant in self.ants:
            alphaList.append(ant.alpha)
        return np.asarray(alphaList)

    def getMinL(self):
        # This function returns the minimum path length
        minL = self.minL
        for ant in self.ants:
            l = ant.L
            if (l<minL):
                minL = l
                
        self.minL = minL
    
    def getTotL(self):
        # This function compares the so-far best total path
        # and the current one and stores the better of the two
        # into self.L
        totL = 0
        for ant in self.ants:
            l = ant.L
            totL = totL + l
                
        if totL < self.L:
            self.L = totL

    def mutate(self, d_alpha_max):
        # Copy ant list
        ant_list = self.ants
        # Mutate each ant in colony
        for ant in ant_list:
            old_alpha = ant.alpha
            new_alpha = old_alpha + random.uniform(-d_alpha_max/2, d_alpha_max/2)
            ant.alphaUpdate(new_alpha)
            
        new_colony = Colony(ant_list)
        return new_colony

    def updateAnts(self, ant_list):
        # This method updates values of the colony based on
        # the details of the population from TSP iterations
        # Add new ant list
        self.ants = ant_list
        # Update minimum L and total L
        self.getMinL()
        self.getTotL()

    def setAlphaWeights(self, alpha_weights):
        # This method sets the alpha_weights array of the colony
        self.alphaWeights = alpha_weights

        
