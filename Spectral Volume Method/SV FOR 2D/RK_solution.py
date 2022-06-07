import numpy as np
from L_operator import L_operator

#==========================================================================
#                 Runge-Kutta scheme
# mesh: current mesh
# iter_t: time interval point
#==========================================================================
def RK_solution(mesh, iter_t, V):
    #----- Initial Information ----
    M = len(mesh['C1']) 
    N = len(mesh['C2'])         # size of spectral volumes
    k = len(mesh['C1'][0])-2    # degree of polynomail in each SV
    delta_t = mesh['T'][iter_t] - mesh['T'][iter_t-1]   # time interval

    A = np.zeros([M, N, k+1, k+1])
    A = mesh['U']
    
    #------ Runge-Kutta scheme( Second-order scheme) -----
    L0 = L_operator(A, mesh['C1'], mesh['C2'], V)
    A1 = A + delta_t*L0
    L1 = L_operator(A1, mesh['C1'], mesh['C2'], V)
    B = 1/2*(A + A1 + delta_t*L1)
    #------ Runge-Kutta scheme( Third-order scheme) -----
    # L0 = L_operator(A, mesh['C1'], mesh['C2'], V)
    # A1 = A + delta_t*L0
    # L1 = L_operator(A, mesh['C1'], mesh['C2'], V)
    # A2 = 3/4*A + 1/4*A1 + 1/4*delta_t*L1
    # L2 = L_operator(A, mesh['C1'], mesh['C2'], V)
    # B = 1/3*A + 2/3*A2 + 2/3*delta_t*L2
    #------ Runge-Kutta scheme( Fourth-order scheme) -----
    # L0 = L_operator(A, mesh['C'])
    # A1 = A + 0.391752226571890*delta_t*L0
    # L1 = L_operator(A1, mesh['C'])
    # A2 = 0.444370493651235*A + 0.555629506348765*A1 + 0.368410593050371*delta_t*L1
    # L2 = L_operator(A2, mesh['C'])
    # A3 = 0.620101851488403*A + 0.379898148511597*A2 + 0.251891774271694*delta_t*L2
    # L3 = L_operator(A3, mesh['C'])
    # A4 = 0.178079954393132*A + 0.821920045606868*A3 + 0.544974750228521*delta_t*L3
    # L4 = L_operator(A4, mesh['C'])
    # B = 0.517231671970585*A2 + 0.096059710526147*A3 + 0.063692468666290*delta_t*L3 + 0.386708617503269*A4 + 0.226007483236906*delta_t*L4

    mesh['U'] = B
    return mesh