import numpy as np

bp = np.array([-0.906179845938664, -0.5384693101056831, 0.0, 0.5384693101056831, 0.906179845938664])
wf = np.array([0.23692688505618834, 0.47862867049936664, 0.5688888888888889, 0.47862867049936664, 0.23692688505618834])

#==========================================================================
#                   Coputer the L operator
# A: cell-average at time t, matrix(size:N*(k+1)).
# S: spectral volumes(partion of the domain [a,b]), N points.
# C: control volumes, N*(k+2).
#==========================================================================
def L_operator(A, C1, C2, H):
    M = len(C1)
    N = len(C2)         # size of spectral volumes
    k = len(C1[0])-2    # degree of polynomail in CV

    f = lambda u:u
    F = np.zeros([M, N, k+1, k+1])
    T = np.zeros([M, N, k+2, k+2])
    Hx = np.diff(C1)    # length x
    Hy = np.diff(C2)    # length y
    for i in range(M):
        for j in range(N):
            x = Reconstruct_value(C1, C1[i], i)
            y = Reconstruct_value(C2, C2[j], j)
            for p in range(k+2):
                for q in range(k+2):
                    T[i,j,p,q] = sum(sum(np.outer(x[p], y[q])*A[i,j]))
            for p in range(k+1):
                for q in range(k+1):
                    F[i,j,p,q] = (T[i,j,p,q]+T[i,j,p+1,q]+T[i,j,p,q+1]+T[i,j,p+1,q+1])*(Hx[i,p]+Hy[j,q])/2
    for i in range(M):
        for j in range(N):
        # used the upwind flux
        # periodic boundary condition
            for p in range(k+1):
                F[i,j,p,0] = F[i,j,p,0] - (T[i,j,p,0]+T[i,j,p+1,0])*Hx[i,p]/2 + (T[i,(j-1)%N,p,k+1]+T[i,(j-1)%N,p+1,k+1])*Hx[i,p]/2
            for q in range(k+1):
                F[i,j,0,q] = F[i,j,0,q] - (T[i,j,0,q]+T[i,j,0,q+1])*Hy[j,q]/2 + (T[(i-1)%M,j,k+1,q]+T[(i-1)%M,j,k+1,q+1])*Hy[j,q]/2
    L = -F/H
    return L


#==========================================================================
# pi_vaule=p_i(x), p_i is the approximation polynomial of u(x) in S_i
# C: control volumes, N*(k+2)
# x: x-value in Si.
# i:the i-th SV, 1<=i<=N.
#==========================================================================
def Reconstruct_value(C, x, i):
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
    return Phi