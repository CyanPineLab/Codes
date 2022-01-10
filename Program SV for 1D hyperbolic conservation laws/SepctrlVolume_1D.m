function mesh=SepctrlVolume_1D(mesh,u_init)
%==========================================================================
%     Spectral Volume Method for 1D conservation law, 2021.03
%
% mesh: current mesh
% u_init(x): initial function of u.
%==========================================================================

N=size(mesh.C,1);        % size of spectral volumes
k=size(mesh.C,2)-2;      % degree of polynomail in each SV
H=diff(mesh.C,1,2);      % length of each CV, N*(k+1)
T_num=length(mesh.T);    % size of time

%--------- Initialization(t=0)------
% %  use the direct integral as the inital value
A=zeros(N,k+1); 
for i=1:N
    for j=1:k+1
        A(i,j)=integral(u_init,mesh.C(i,j),mesh.C(i,j+1));
    end
end
mesh.U(:,:,1)=A./H;

% use the project as the inital value
% A=zeros(N,k+1);
% n=5;    % Gauss points for integral
% [bp,wf]=legs(n);
% pro_point=legsrd(k+1); % Right Radau for the projection points
% pro_point=fliplr(-pro_point);
% for i=1:N
%     Pro_Point=pro_point*(mesh.S(i+1)-mesh.S(i))/2+(mesh.S(i)+mesh.S(i+1))/2; 
%     for j=1:k+1
%        v=bp*H(i,j)/2+(mesh.C(i,j)+mesh.C(i,j+1))/2;        
%        pu_init=Projection(u_init,Pro_Point,v,mesh.S(i),mesh.S(i+1));
%        A(i,j)=wf*pu_init';
%     end
% end
% mesh.U(:,:,1)=A./2;

%--------- Solving (Time discretization) -------
for iter_t=2:T_num
    mesh=RK_solution(mesh,iter_t);
end