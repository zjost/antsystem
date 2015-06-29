import random as rand

def choose_city(p_list):
    die = rand.random()
    temp = 0
    N = len(p_list)
    #print(p_list)
    for i in range(N):
        temp = temp + p_list[i]
        if die < temp:
            return i