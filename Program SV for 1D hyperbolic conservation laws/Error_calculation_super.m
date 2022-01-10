function error_super=Error_calculation_super(error_super,mesh,u_exact,u_exact_x,iter)
%==========================================================================
%         Calculate various errors without exact solution, 2021.03
% (en, ec, ei, edi error)
%==========================================================================

N=size(mesh.C,1);         % size of element
k=size(mesh.C,2)-2;       % degree
h=diff(mesh.S);           % length of element
T_num=length(mesh.T);     % size of time
T_end=mesh.T(T_num);

n=5;    % Gauss points for integral
[bp,wf]=legs(n);
%===== The en error.
u_en=0;
for i=1:N
    uN=Reconstruct_value(mesh.U(:,:,T_num),mesh.C,mesh.S(i+1),i);
    u=u_exact(mesh.S(i+1),T_end);
    u_en=u_en+(u-uN).^2;
end
error_super.u_en(iter)=sqrt(u_en/(N));

%===== The ec error.
u_ec=0;
for i=1:N
    v(:)=h(i)/2*bp(:)+mesh.S(i)+h(i)/2;
    u=u_exact(v,T_end);
    uN=Reconstruct_value(mesh.U(:,:,T_num),mesh.C,v,i);
    value=wf*( u-uN )';
    u_ec=u_ec+(value/2).^2;
end
error_super.u_ec(iter)=sqrt(u_ec/(N));

%===== The ei error.
u_ei=0;
for i=1:N
    uN=Reconstruct_value(mesh.U(:,:,T_num),mesh.C,mesh.C(i,2:k+1),i);
    u=u_exact(mesh.C(i,2:k+1),T_end);
    u_ei=u_ei+sum((u-uN).^2);
end
error_super.u_ei(iter)=sqrt(u_ei/(N));

%===== The edi error.
u_edi=0;
for i=1:N
    uN_d=Reconstruct_value_deri_1(mesh.U(:,:,T_num),mesh.C,mesh.C(i,2:k+1),i);
    u_d=u_exact_x(mesh.C(i,2:k+1),T_end);
    u_edi=u_edi+sum((u_d-uN_d).^2);
end
error_super.u_edi(iter)=sqrt(u_edi/(N));