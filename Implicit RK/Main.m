
function Main
%========================================================================== 
%           Implicit RK Method
%==========================================================================

%===== 1¡¢initial Information =====
a=0; b=1;           % Domain[0,1]
y0=1;               %
N=10;               % 
degree_k=3;         % Degree of the polynomail on each SV(>=0)
type=2;             % Division points at [-1,1] 
                    %   1=Equidistant; 2=Gauss points; 3=Gauss-Lobatto points;
                    %   4=Gauss-Radau points(left); 5=Gauss-Radau points(right)
               
%===== 2¡¢get Coefficients =====                    
c = Division(degree_k, type);
C = ones(degree_k+1, degree_k);
for i=2:degree_k+1
    C(i,:)=C(i-1,:).*c;
end
B = Getb(C,degree_k);
A = GetA(C,degree_k);

%===== 3¡¢calculate =====   
tic
t=linspace(a,b,N+1);
h=diff(t);
y=zeros(N+1,1);
y(1)=y0;
for i=1:N
    y(i+1)=CalY(t(i),y(i),h(i),c,B,A);
end
y
plot(t,y,t,u_exact(t))
toc

end

function u=u_exact(t)
u=exp(t);
end

