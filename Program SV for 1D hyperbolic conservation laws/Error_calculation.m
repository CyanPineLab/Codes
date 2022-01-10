function error=Error_calculation(error,mesh,u_exact,iter)
%==========================================================================
%                     Calculate various errors, 2021.03
% (Max error, L1 error, L2 error)
%==========================================================================

N=size(mesh.C,1);         % size of element
h=diff(mesh.S);             % length of element
T_num=length(mesh.T);       % size of time
T_end=mesh.T(T_num);


n=5;    % Gauss points for integral
[bp,wf]=legs(n);

%===== The max error.(max(|u-u_h|))
x_value=[];y_value=[];
for i=1:N
    x_temp=linspace(mesh.S(i)+2*eps,mesh.S(i+1)-2*eps,4);
    y_temp=Reconstruct_value(mesh.U(:,:,T_num),mesh.C,x_temp,i);
    x_value=[x_value,x_temp];
    y_value=[y_value,y_temp];
end
error.u_max(iter)=max( abs(u_exact(x_value,T_end) - y_value));

%===== The L1 error.(\int |u-u_h| dx)
u_l1=0;
for i=1:N
    v(:)=h(i)/2*bp(:)+mesh.S(i)+h(i)/2;
    value_u=sum( wf.*( abs( u_exact(v,T_end) - Reconstruct_value(mesh.U(:,:,T_num),mesh.C,v,i) )));
    u_l1=u_l1+h(i)/2*value_u;
end
error.u_l1(iter)=u_l1;

%===== The L2 error.(\sqrt(\int |u-u_h|^2 dx))
u_l2=0;
for i=1:N
    v(:)=h(i)/2*bp(:)+mesh.S(i)+h(i)/2;
    value_u=sum( wf.*( u_exact(v,T_end) - Reconstruct_value(mesh.U(:,:,T_num),mesh.C,v,i) ).^2);
    u_l2=u_l2+h(i)/2*value_u;
end
error.u_l2(iter)=sqrt(u_l2);