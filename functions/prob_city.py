import numpy as np

def prob_city(tau, n, alpha, beta, city_tab, city):
    N = len(tau[0,:])
    p = np.zeros(N) # initialize probability matrix
    for i in range(N):
        if (i not in city_tab): # only make non-zero if not visited before
            #print("city %d i %d" % (city,i))
            prob = (tau[city,i]**alpha)*(n[city,i]**beta)
            #print(n[city,i])
            #print(i)
            p[i] = prob
            
    #print(p)    
    norm = np.sum(p)
        
    # normalize the probabilities
    p = p/norm
    
    return p
            
            