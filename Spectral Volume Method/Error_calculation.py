import numpy as np
from L_operator import Reconstruct_value

#==========================================================================
#                     Calculate various errors
#  (Max error, L1 error, L2 error)
#==========================================================================
def Error_calculation(mesh, u_exact, iter):
    N = len(mesh['C'])          # size of element
    h = np.diff(mesh['S'])          # length of element
    T_num = len(mesh['T'])          # size of time
    T_end = mesh['T'][T_num-1]

    n = 5    # Gauss points for integral
    bp = np.array([-0.906179845938664, -0.5384693101056831, 0.0, 0.5384693101056831, 0.906179845938664])
    wf = np.array([0.23692688505618834, 0.47862867049936664, 0.5688888888888889, 0.47862867049936664, 0.23692688505618834])
    eps = np.spacing(1)

    #===== The max error.(max(|u-u_h|))
    x_value = np.array([])
    y_value = np.array([])
    for i in range(N):
        x_temp = np.linspace(mesh['S'][i]+2*eps, mesh['S'][i+1]-2*eps, 4)
        y_temp = Reconstruct_value(mesh['U'][T_num-1], mesh['C'], x_temp, i)
        x_value = np.hstack((x_value,x_temp))
        y_value = np.hstack((y_value,y_temp))

    u_max = max( abs(u_exact(x_value,T_end) - y_value) )

    #===== The L1 error.(\int |u-u_h| dx)
    u_l1 = 0
    for i in range(N):
        v = h[i]/2*(bp+1) + mesh['S'][i]
        value_u = sum( wf*( abs( u_exact(v, T_end) - Reconstruct_value(mesh['U'][T_num-1],mesh['C'],v,i) )))
        u_l1 = u_l1 + h[i]/2*value_u

    #===== The L2 error.(\sqrt(\int |u-u_h|^2 dx))
    u_l2 = 0
    for i in range(N):
        v = h[i]/2*(bp+1) + mesh['S'][i]
        value_u = sum( wf*( u_exact(v,T_end) - Reconstruct_value(mesh['U'][T_num-1],mesh['C'],v,i) )**2 )
        u_l2 = u_l2 + h[i]/2*value_u
    u_l2 = np.sqrt(u_l2)

    return [u_max, u_l1, u_l2]


def Error_analysis(error, N):
    iter_num = len(N)
    rate = np.zeros([iter_num,3])
    for i in range(1,iter_num):
        rate[i] = -np.log(error[i]/error[i-1])/np.log(N[i]/N[i-1])
    return rate