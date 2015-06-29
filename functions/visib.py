import csv
import numpy as np

def visib():
    # read in list of names
    city_list = []
    with open('oliver30.csv', newline='') as csvfile:
        coords = csv.reader(csvfile, dialect = 'excel')
        for coord in coords:
            city_list.append(coord)

    city_list = np.asarray(city_list, dtype = np.float)

    N = len(city_list)

    d = np.zeros((N,N))

    for i in range(N):
        for j in range(i,N):
            x1 = city_list[i,0]
            x2 = city_list[j,0]
            y1 = city_list[i,1]
            y2 = city_list[j,1]
            if(i==j):
                d[i,j]= d[j,i] = 10000
            else:
                d[i,j]= d[j,i]=1/np.sqrt((x1-x2)**2 + (y1-y2)**2)
        
    return d