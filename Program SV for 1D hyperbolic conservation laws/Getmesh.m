function mesh=Getmesh(S,C,T)
%==========================================================================
%               Struct of mesh, 2021.03
%
% S: Spectrol volumn, size 1*(N+1)
% C: Control volumn, size N*(k+2)
% T: Time 
%==========================================================================
T_num=length(T);
U=zeros(size(C,1),size(C,2)-1,T_num);
mesh=struct('S',S,'C',C,'T',T,'U',U);