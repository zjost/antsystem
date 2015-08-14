import numpy as np


def saveFiles(fitness_mat, alphaBestMin, lMin_mat, lAvg_mat, params, count):

    (nColonies, iters, evo_cycles, alpha_min, alpha_max,
          max_mutation, c0, c1) = params

    #parms = (nColonies, evo_cycles, iters, alpha_min, alpha_max,
    #         d_alpha_max)

    np.savetxt('G:\\Python333\\play\\TSP\\data\\' + str(count) + '-fitness_mat.txt', fitness_mat, fmt='%.3f',
               delimiter=',')

    np.savetxt('G:\\Python333\\play\\TSP\\data\\' + str(count) + '-alphaBestMin.txt', alphaBestMin, fmt='%.3f',
               delimiter=',')

    np.savetxt('G:\\Python333\\play\\TSP\\data\\' + str(count) + '-minLMat.txt', lMin_mat, fmt='%.3f',
               delimiter=',')

    np.savetxt('G:\\Python333\\play\\TSP\\data\\' + str(count) + '-avgLMat.txt', lAvg_mat, fmt='%.3f',
               delimiter=',')


    # Create list of parameter definition strings
    parm_list = []
    parm_list.append('nColonies='+str(nColonies))
    parm_list.append('iters='+str(iters))
    parm_list.append('evo_cycles='+str(evo_cycles))
    parm_list.append('alpha_min='+str(alpha_min))
    parm_list.append('alpha_max='+str(alpha_max))
    parm_list.append('max_mutation='+str(max_mutation))
    parm_list.append('c0='+str(c0))
    parm_list.append('c1='+str(c1))
    # Store into a numpy array
    parm_mat = np.array(parm_list)
    # Save the data
    np.savetxt('G:\\Python333\\play\\TSP\\data\\' + str(count) + '-modelparms.txt', parm_mat, fmt='%s',
               delimiter=',')


    # Load with something like:
    # test_fitness = np.loadtxt('fitness_mat2.txt', delimiter=',', skiprows=1)
