function L=L_operator(A,C)
%==========================================================================
%                   Coputer the L operator. 2021.03.
% A: cell-average at time t, matrix(size:N*(k+1)).
% S: spectral volumes(partion of the domain [a,b]), N points.
% C: control volumes, N*(k+2).
%==========================================================================
N=size(C,1);        % size of spectral volumes
k=size(C,2)-2;      % degree of polynomail in CV
H=diff(C,1,2);      % length of each CV, N*(k+1)
f = @(u)u.^2/2;
F=zeros(N,k+2);
for i=1:N
%    F(i,:)=Reconstruct_value(A,C,C(i,:),i);
    F(i,:)=( Reconstruct_value(A,C,C(i,:),i) ).^2/2;
    
    
    % used the upwind flux
   if i==1 % periodic boundary condition
       i_left=N;
   else
       i_left=i-1;
   end
%    F(i,1)=Reconstruct_value(A,C,C(i_left,k+2),i_left);
    u=Reconstruct_value(A,C,C(i,1),i);
    u_left=Reconstruct_value(A,C,C(i_left,k+2),i_left);
    F(i,1)=0.5*(0.5*u_left^2+0.5*u^2-1*(u-u_left));
end

L=-diff(F,1,2)./H;