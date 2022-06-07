#==========================================================================
#                    division [-1,1] with k+2 points
# type:  1=Equidistant; 
#        2=Gauss points;
#        3=Gauss-Lobatto points;
#        4=Gauss-Radau points(left);
#        5=Gauss-Radau points(right);
#        6=Gauss-Chebyshev points.
#==========================================================================
import numpy as np
import math


# return k+2 division of S
def Division(S, k, type):
    h = np.diff(S)      # Length of each S ,size 1*N
    N = len(S)-1        # size of SV
    C = np.zeros([N,k+2])
    # control points on [-1,1]
    if type==1:     # Equidistant
        c = np.linspace(-1,1,k+2)
    elif type==2:   # Gauss points
        c_temp = legs(k)
        c = [-1]+c_temp+[1]
    elif type==3:   # Gauss-Lobatto points
        c = legslb(k+2)
    elif type==4:   # Gauss-Radau points(left)
        c_temp = legsrd(k+1)
        c = c_temp+[1]
    elif type==5:   # Gauss-Radau points(right)
        c_temp = legsrd(k+1)
        c_temp = [-c_temp[k-i] for i in range(k+1)]
        c = [-1]+list(c_temp)
    elif type==6:   # Chebyshev points
        c_temp = cheby(k)
        c = [-1]+c_temp+[1]
    else:
        raise Exception("No such division now!!", type)

    for i in range(N):
        C[i] = [h[i]/2*c[j]+S[i]+h[i]/2 for j  in range(k+2)]
    return C


# lepoly: Legendre polynomial of degree n
def lepoly(n, x):
    if n == 0:
        return np.ones(len(x)), np.zeros(len(x))
    elif n == 1:
        return [t for t in x], np.ones(len(x))
    polylst, pderlst = np.ones(len(x)), np.zeros(len(x))
    poly, pder = [t for t in x], np.ones(len(x))     # L_0=1, L_0'=0, L_1=x, L_1'=1

    for k in range(2,n+1):                          # Three-term recurrence relation
        # kL_k(x)=(2k-1)xL_{k-1}(x)-(k-1)L_{k-2}(x)
        polyn = [((2*k-1)*x[i]*poly[i]-(k-1)*polylst[i])/k for i in range(len(x))]
        # L_k'(x)=L_{k-2}'(x)+(2k-1)L_{k-1}(x)
        pdern = [pderlst[i]+(2*k-1)*poly[i] for i in range(len(x))]
        polylst = [t for t in poly]
        poly = [t for t in polyn]
        pderlst = [t for t in pder]
        pder = [t for t in pdern]
    return pdern, polyn


# x=legs(n) returns n Legendre-Gauss points arranged in ascending order
# [x,w]= legs(n) returns n Legendre-Gauss points and weights
# Newton iteration method is used for computing nodes
def legs(n):
    theta_k = [(4*i-1)*math.pi/(4*n+2) for i in range(1,n+1)]
    ze = [-(1.0-(n-1)/(8*n**3)-(39-28/math.sin(theta_k[i])**2)/(384*n**4))*math.cos(theta_k[i]) for i in range(n)]
    ep = np.spacing(1)*10
    ze1 = ze+ep+1
    while max([abs(ze1[i]-ze[i]) for i in range(n)]) >= ep:
        ze1 = [t for t in ze]
        dy, y = lepoly(n, ze)
        ze = [ze[i] - y[i]/dy[i] for i in range(n)]
    return ze


# x=legslb(n) returns n Legendre-Gauss-Lobatto points with x[0]=-1, x[n-1]=1
# [x,w]= legslb(n) returns n Legendre-Gauss-Lobatto points and weights
# Newton iteration method is used for computing nodes
def legslb(n):
    # Compute the initial guess of the interior LGL points
    nn = n-1
    theta_k =[(4*i-1)*math.pi/(4*nn+2) for i in range(1,n+1)]
    sigmak = [-(1.0-(nn-1)/(8*nn**3)-(39-28/math.sin(theta_k[i])**2)/(384*nn**4))*math.cos(theta_k[i]) for i in range(n)]
    ze = [(sigmak[i]+sigmak[i+1])/2 for i in range(nn-1)]
    ep = np.spacing(1)*10
    ze1 = ze+ep+1
    while max([abs(ze1[i]-ze[i]) for i in range(len(ze))]) >= ep:
        ze1 = [t for t in ze]
        dy, y = lepoly(nn, ze)
        ze = [ze[i]-(1-ze[i]*ze[i])*dy[i]/(2*ze[i]*dy[i]-nn*(nn+1)*y[i]) for i in range(len(ze))]
    return [-1]+ze+[1]


# x=legsrd(n) returns n Legendre-Gauss-Radau points with x[0]=-1.
# [x,w]= legsrd(n) returns n Legendre-Gauss-Radau points and weights
# Eigen method is used for computing nodes.
def legsrd(n):
    j = np.array(range(n-1))
    A = np.diag(1/((2*j+1)*(2*j+3)))
    j = np.array(range(1,n-1))
    A = A + np.diag(np.sqrt(j*(j+1))/(2*j+1),1) + np.diag(np.sqrt(j*(j+1))/(2*j+1),-1)
    x, X = np.linalg.eig(A)
    return [-1] + list(np.sort(x))


# x=cheby(n) returns n Gauss-Chebyshev points.
# [x,w]= legsrd(n) returns n Legendre-Gauss-Radau points and weights
def cheby(n):
    x = np.sort([np.cos((2*i+1)*np.pi/(2*n)) for i in range(n)])
    return x.tolist()
