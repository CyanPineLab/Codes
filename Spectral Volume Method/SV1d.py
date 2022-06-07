#========================================================================== 
#           SV for Solving 1D hyperbolic conservation laws
#         u_t+u_x=0, u(x,0)=u0 with periodic boundary condition
#==========================================================================
import math
# from unittest import skip
import numpy as np
import time
import Division
from SepctrlVolume_1D import SepctrlVolume_1D
import L_operator

#==========================================================================
#               Struct of mesh
# S: Spectrol volumn, size 1*(N+1)
# C: Control volumn, size N*(k+2)
# T: Time 
#==========================================================================
def Getmesh(S, C, T):
    T_num = len(T)
    U = np.zeros([T_num, len(C), len(C[0])-1])
    mesh = {'S':S, 'C':C, 'T':T, 'U':U}
    return mesh

def u_init0(x):
    return np.sin(x)

def u_init1(x):
    return np.exp(x)

def result(mesh):
    T = mesh['T']
    T_num = len(T)          # size of time
    N = len(mesh['S'])-1    # size of spectral volumes

    x_value = []
    y_value = []
    for i in range(N):
        x_temp = np.linspace(mesh['S'][i]+2*np.spacing(1), mesh['S'][i+1]-2* np.spacing(1), 10)
        y_temp = L_operator.Reconstruct_value(mesh['U'][T_num-1], mesh['C'], x_temp, i)
        x_value = x_value + x_temp.tolist()
        y_value = y_value + y_temp.tolist()

    return [y_value, x_value]


def SV1d(a = 0, b = 2*math.pi, N = 4, degree_k = 3, t0 = 0, t = 1, style = 0):
    #===== 1、initial Information =====
    type = 5                # Division points at [-1,1] 
                            #   1=Equidistant; 2=Gauss points; 3=Gauss-Lobatto points;
                            #   4=Gauss-Radau points(left); 5=Gauss-Radau points(right);
                            #   6=Chebyshev points

    #===== 2、Solving PDE =====
    # 1) Initialize spectral volume and time.--------------------------
    S = np.linspace(a,b,N+1)                    # Spectrol volumes

    delta_T = 0.02*min(np.diff(S))**2           # 0.05*min(np.diff(S)) # Space time ratio
    T_num = int((t-t0)/delta_T)
    T = np.linspace(t0,t,T_num)

    C = Division.Division(S, degree_k, type)    # Control volumes,size N*(k+2)
    mesh = Getmesh(S,C,T)

    # 2) SD Solution ----- ---------------------------------------------
    tic = time.time()
    if style == 0:
        mesh = SepctrlVolume_1D(mesh, u_init0)  
    else: 
        mesh = SepctrlVolume_1D(mesh, u_init1)  
    print('Solution is finished for N =', N)
    toc = time.time()
    print("Costs", toc-tic, "s")
        
    return result(mesh)
