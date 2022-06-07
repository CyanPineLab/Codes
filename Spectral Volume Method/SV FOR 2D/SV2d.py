#========================================================================== 
#           SV for Solving 2D hyperbolic conservation laws
#     u_t+u_x+u_y=0, u(x,y,0)=u0 with periodic boundary condition
#==========================================================================
import math
import numpy as np
# import matplotlib.pyplot as plt
import time
import Division
from SepctrlVolume_2D import SepctrlVolume_2D
from scipy import integrate
# import L_operator
# from Error_calculation import Error_calculation

#==========================================================================
#               Struct of mesh
# S: Spectrol volumn, size (N+1)*(N+1)
# C: Control volumn, size N*N*(k+2)*(k+2)
# T: Time 
#==========================================================================
def Getmesh(S1, S2, C1, C2, T):
    T_num = len(T)
    U = np.zeros([len(C1), len(C2), len(C1[0])-1, len(C2[0])-1])
    mesh = {'S1':S1, 'S2':S2, 'C1':C1, 'C2':C2, 'T':T, 'U':U}
    return mesh

def u_init(x,y):
    return np.sin(x+y)

def u_exact(x,y):
    return np.sin(x+y-2)


def SV2d(): # a = 0, b = 2*math.pi, N = 4, degree_k = 3):
    #===== 1、initial Information =====
    a, b = 0, 2*np.pi     # domain [a, b]
    c, d = 0, 2*np.pi     # domain [c, d]

    N = [4,8,16,32]                 # [4,8,16,32,64,128,256]
    iter_num = len(N)
    degree_k = 2            # Degree of the polynomail on each SV(>=0)
    type = 5                # Division points at [-1,1] 
                            #   1=Equidistant; 2=Gauss points; 3=Gauss-Lobatto points;
                            #   4=Gauss-Radau points(left); 5=Gauss-Radau points(right);
                            #   6=Chebyshev points

    #===== 2、Solving PDE =====
    for iter in range(iter_num):
        # 1) Initialize spectral volume and time.--------------------------
        S1 = np.linspace(a, b, N[iter]+1)   # Spectrol volumes
        S2 = np.linspace(c, d, N[iter]+1)
        delta_T = 0.002*min(np.diff(S1))     # Space time ratio
        T_num = int(1/delta_T)
        T = np.linspace(0, 1, T_num)
        C1 = Division.Division(S1, degree_k, type)  # Control volumes,size N*(k+2)
        C2 = Division.Division(S2, degree_k, type)  # Control volumes,size N*(k+2)
        mesh = Getmesh(S1, S2, C1, C2, T)
    
        print(T_num, N[iter], degree_k)
        # 2) SD Solution ----- ---------------------------------------------
        tic = time.time()
        mesh = SepctrlVolume_2D(mesh, u_init)  
        print('Solution is finished for N =', N[iter])
        toc = time.time()
        print("Costs", toc-tic, "s")
        # print(mesh['U'])

        mmm = 0
        TTT = np.zeros([N[iter], N[iter], degree_k+1, degree_k+1])
        for i in range(N[iter]):
            for j in range(N[iter]):
                for p in range(degree_k+1):
                    for q in range(degree_k+1):
                        TTT[i,j,p,q], err = integrate.dblquad(u_exact, mesh['C1'][i,p], mesh['C1'][i,p+1], 
                                        lambda g:mesh['C2'][j,q], lambda h:mesh['C2'][j,q+1])
                        TTT[i,j,p,q] = TTT[i,j,p,q]/( (mesh['C1'][i,p+1]-mesh['C1'][i,p])*(mesh['C2'][j,q+1]-mesh['C2'][j,q]) )
                        mmm = max(mmm, abs(mesh['U'][i,j,p,q]-TTT[i,j,p,q]))
        print(mmm)
        
        # 3) Error calculation. ---------------------------------------------
        # error = Error_calculation(mesh, u_exact, iter)
        # print(error)
        # print('Error calculation is finished for N=', N[iter])

    #===== 3、Error Analysis and Data processing=====
    # rate = Error_analysis(error, N)

    # return Pic_show(mesh, u_exat, exp = 2)


if __name__ == '__main__':
    SV2d()