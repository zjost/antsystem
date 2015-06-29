import numpy as np
from functions.prob_city import prob_city
from functions.choose_city import choose_city


class Ant():
    def __init__(self, city_count,alpha, beta, Q, init_city):
        self.alpha = alpha # conformity
        self.beta = beta # greediness
        self.q = Q # pheromone density
        self.dtau = np.zeros((city_count,city_count)) # delta for next round pheromone trail
        self.L = 0 # total path length
        self.tab = [init_city] # city tab
        self.city = init_city # current city

    def move_city(self,tau_global, visib_mat):
        # Determine the next city
        N = len(tau_global[0,:])
        if len(self.tab) < N:
            #print(self.tab)
            prob_list = prob_city(tau_global, visib_mat, self.alpha, self.beta, self.tab, self.city)
            new_city = choose_city(prob_list)
            # add new city to city tab
            self.tab.append(new_city)
        else:
            new_city = self.tab[0]
        # update delta pheromone trail (both directions)
        self.dtau[self.city, new_city] = self.q
        self.dtau[new_city, self.city] = self.q
        # Update the total distance
        self.L = self.L + 1/visib_mat[self.city,new_city]
        # update current city
        self.city = new_city
    
    def scale_tau(self):
        # Scale tau by total path length, once known
        self.dtau = self.dtau/self.L
        
