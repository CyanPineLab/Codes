function Pic_show(mesh,u)
%==========================================================================
%      Show the approximate solution (and exact solution)
% mesh: current mesh
% u: exact solution without time t (optional)
%==========================================================================
T=mesh.T;
T_num=length(mesh.T);       % size of time
N=length(mesh.S)-1;        % size of spectral volumes


x_value=[];
y_value=[];
for i=1:N
    x_temp=linspace(mesh.S(i)+2*eps,mesh.S(i+1)-2*eps,10);
    y_temp=Reconstruct_value(mesh.U(:,:,T_num),mesh.C,x_temp,i);
    x_value=[x_value,x_temp]; %#ok<AGROW>
    y_value=[y_value,y_temp]; %#ok<AGROW>
end
%=== draw the approximation solution====
if nargin==1
    figure;
    plot(x_value,y_value,'r:o');
    title(['Picture for N=',num2str(N)])
    legend('Approximate solution')
end
%=== draw the approximation solution and the exact solution at the last time===
if nargin==2
    figure;
    y=u(x_value,T(end));
    plot(x_value,y_value,'r:o',x_value,y,'g');
    title(['Picture for N=',num2str(N)])
    legend('Approximate solution','Exact Solution')
end
