import numpy as np

def tau_branch(tau,epp):
    N = len(tau[0,:])
    branch_cnt = []
    for i in range(N):
        branch_cnt.append(np.sum(tau[i,:]>epp))
    
    return branch_cnt