import numpy as np

#can put global params here


def fed_batch_kuhlman(t, ind_vars, params):
    #ind_vars:    [X, Y, V]
    #params:
    Sf, Y, mu_max, K = params
    
    #X = biomass concentration
    #S = substrate concentration
    #V = volume
    X, S, V = ind_vars
    
    mu = mu_max*S/(K+S+S**2/2.0)
    
    #Flow rate equation: can be optimized as a control parameter
    F = 0.2+2*t
    
    Xdot = (mu - F/V)*X
    
    Sdot = - mu/Y*X + (Sf-S)*F/V
    
    Vdot = F
    
    return np.r_[Xdot, Sdot, Vdot]