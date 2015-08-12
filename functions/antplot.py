import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plotFitnessMat(fitness_mat):
    plt.imshow(fitness_mat, interpolation = 'none', cmap = cm.Greys_r)
    #plt.imshow(fitness_mat, interpolation = 'none')
    plt.xlabel('Colony')
    plt.ylabel('Time [evolutions] starting at top')
    plt.title('Fitness (intensity) for colonies through evolutionary time')
    plt.show()

def plotAlphaDist(alphaBestMin):
    evos = len(alphaBestMin)
    fig, axes = plt.subplots(nrows=evos, ncols=1)
    
    for idx, axis in enumerate(axes):
        axis.hist(alphaBestMin[idx])

    plt.show()

def plotLBox(l_mat, flag):
    plt.boxplot(l_mat.transpose())
    if flag==0:
        plt.ylabel('Minimum Path Length of Colony')
        plt.xlabel('Evolution Cycle')
        plt.title('L_min of Colonies through Evolutionary Cycles')
    if flag==1:
        plt.ylabel('Average Path Length of Colony')
        plt.xlabel('Evolution Cycle')
        plt.title('L_Avg of Colonies through Evolutionary Cycles')
    plt.show()
