import numpy as np

#==========================================================================
#                   Coputer the L operator
# A: cell-average at time t, matrix(size:N*(k+1)).
# S: spectral volumes(partion of the domain [a,b]), N points.
# C: control volumes, N*(k+2).
#==========================================================================
def L_operator(A, C):
    N = len(C)          # size of spectral volumes
    k = len(C[0])-2     # degree of polynomail in CV
    H = np.diff(C)      # length of each CV, N*(k+1)
    f = lambda u:u**2/2
    F = np.zeros([N, k+2])
    for i in range(N):
        F[i] = Reconstruct_value(A, C, C[i], i)
        #F[i]= (Reconstruct_value(A, C, C[i], i))**2/2
    # F[0,0] = 0.5*F[0,0] + 0.5*A[0,0]
    for i in range(1,N):
        # used the upwind flux
        # periodic boundary condition
        F[i,0] = F[(i-1)%N,-1]
        # F[i,0] = 0.5*(F[(i-1)%N,-1]+F[i,0]-0*(F[i,0]-F[(i-1)%N,-1]))
    L = -np.diff(F)/H
    return L


#==========================================================================
# pi_vaule=p_i(x), p_i is the approximation polynomial of u(x) in S_i
# A: cell-average，matrix(size:N*(k+1)).
# C: control volumes, N*(k+2)
# x: x-value in Si.
# i:the i-th SV, 1<=i<=N.
#==========================================================================
def Reconstruct_value(A, C, x, i):
    ui_bar = A[i]
    xi = C[i]
    hi = np.diff(xi)
    k = len(xi)-2
    omega_bar_der = np.zeros(k+2)
    for i in range(k+2):
        xi_temp = np.delete(xi, i)
        omega_bar_der[i] = np.prod(xi[i] - xi_temp)
    x_num = len(x)
    Phi = np.zeros([x_num,k+1])

    for l in range(k+1):
        R = np.zeros(x_num)
        for r in range(l+1, k+2):
            M = np.zeros(x_num)
            for m in range(k+2):
                if m != r:
                    xi_temp = np.delete(xi, [m, r])
                    for q in range(x_num):
                        M[q] = M[q] + np.prod(x[q] - xi_temp)
            R = R + M/omega_bar_der[r]
        Phi[:,l] = hi[l]*R

    pi_value = np.matmul(Phi, ui_bar)
    return pi_value