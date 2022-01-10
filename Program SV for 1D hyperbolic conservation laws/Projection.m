function pu_value=Projection(u,base_x,x,a,b)
%==========================================================================
%       A special projection(degree of k polynomail) of u satisfying 
%   \int_a^b (Pu-u)v=0 and Pu(b)=u(a) with v is degree of k-1 polynomail,
%   2020.03
% u: Mapping function 
% base_x: Interpolation points, size 1*(k+1), with x(k+1)=b,i.e. right radau
%    points
% x: The points which value we want to obtain
% pu_value: projection value at interpolation points x
%==========================================================================
k=length(base_x)-1;  % degree of the polynomail
base_u=zeros(1,k+1);
base_u(k+1)=u(base_x(k+1));

A=zeros(k,k);
B=zeros(k,1);
for i=1:k
    for j=1:k
        A(i,j)=Quad_base(base_x,j,i,a,b);
    end
    B(i,1)=Quad_u(u,i,a,b)-base_u(k+1)*Quad_base(base_x,k+1,i,a,b);
end
base_u(1:k)=A\B;

x_num=length(x);
L=ones(x_num,k+1);
for j=1:k+1
    for s=1:k+1
        if s~=j
            L(:,j)=L(:,j).*(x(:)-base_x(s))/(base_x(j)-base_x(s));
        end
    end
end
pu_value=(L*base_u')';


function value=Quad_base(base_x,j,i,a,b)
n=5;    % Gauss points for integral
[bp,wf]=legs(n);
v(:)=(b-a)/2*bp(:)+(a+b)/2;

k=length(base_x)-1;
Lj=ones(1,n);
for s=1:k+1
    if s~=j
        Lj=Lj.*((v-base_x(s))/(base_x(j)-base_x(s)));
    end
end
vi=v.^(i-1);
value=wf*(Lj.*vi)';
value=value*(b-a)/2;

function value=Quad_u(u,i,a,b)
n=5;    % Gauss points for integral
[bp,wf]=legs(n);
v(:)=(b-a)/2*bp(:)+(a+b)/2;
vi=v.^(i-1);
value=wf*(u(v).*vi)';
value=value*(b-a)/2;