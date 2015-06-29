import matplotlib.pyplot as plt

def plot_data(L_min_list, branch_list):

    plt.figure(1)
    plt.subplot(121)
    plt.plot(L_min_list)
    plt.title('Min Path Length')
    plt.axis([0,len(L_min_list),400,600])

    plt.subplot(122)
    plt.plot(branch_list)
    plt.title('Avg Node Branch Cnt')
    plt.axis([0,len(branch_list),0,30])

    plt.show()