import numpy as np
from scipy import integrate
from RK_solution import RK_solution

#==========================================================================
#     Spectral Volume Method for 1D conservation law
#  mesh: current mesh
#  u_init(x): initial function of u.
#==========================================================================
def SepctrlVolume_1D(mesh, u_init):
    N = len(mesh['C'])         # size of spectral volumes
    k = len(mesh['C'][0])-2    # degree of polynomail in each SV
    H = np.diff(mesh['C'])     # length of each CV, N*(k+1)
    T_num = len(mesh['T'])     # size of time
    
    #--------- Initialization(t=0)------
    # use the direct integral as the inital value
    A = np.zeros([N, k+1])
    for i in range(N):
        for j in range(k+1):
            A[i,j], err = integrate.quad(u_init, mesh['C'][i,j], mesh['C'][i,j+1])
    mesh['U'][0] = A/H

    #--------- Solving (Time discretization) -------
    for iter_t in range(1, T_num):
        mesh = RK_solution(mesh, iter_t) 
    return mesh