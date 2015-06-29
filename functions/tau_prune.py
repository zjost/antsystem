

def tau_prune(tau, epp):
    N = len(tau[0,:])
    for i in range(N):
        for j in range(i,N):
            if tau[i,j] < epp:
                tau[i,j] = tau[j,i] = .00000001
             
    return tau