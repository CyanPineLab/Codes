import numpy as np
from scipy import integrate
from RK_solution import RK_solution

def u_init(x,y):
    return np.sin(x+y)

#==========================================================================
#     Spectral Volume Method for 2D conservation law
#  mesh: current mesh
#  u_init(x,y): initial function of u.
#==========================================================================
def SepctrlVolume_2D(mesh, u_init):
    M = len(mesh['C1']) 
    N = len(mesh['C2'])         # size of spectral volumes
    k = len(mesh['C1'][0])-2    # degree of polynomail in each SV

    Hx = np.diff(mesh['C1'])    # length x
    Hy = np.diff(mesh['C2'])    # length y

    T_num = len(mesh['T'])     # size of time
    
    #--------- Initialization(t=0)------
    # use the direct integral as the inital value
    A = np.zeros([M, N, k+1, k+1])
    for i in range(M):
        for j in range(N):
            for p in range(k+1):
                for q in range(k+1):
                    A[i,j,p,q], err = integrate.dblquad(u_init, mesh['C1'][i,p], mesh['C1'][i,p+1], 
                                    lambda g:mesh['C2'][j,q], lambda h:mesh['C2'][j,q+1])

    V = np.zeros([M, N, k+1, k+1])
    for i in range(M):
        for j in range(N):
            V[i,j] = np.outer(Hx[i], Hy[j])
    mesh['U'] = A/V

    #--------- Solving (Time discretization) -------
    for iter_t in range(1, T_num):
        mesh = RK_solution(mesh, iter_t, V) 
    return mesh