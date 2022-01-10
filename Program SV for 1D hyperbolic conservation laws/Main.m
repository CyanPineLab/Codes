
function Main
%========================================================================== 
%           SV for Solving 1D hyperbolic conservation laws
%         u_t+u_x=0,u(x,0)=u0 with periodic boundary condition
%==========================================================================

%===== 1、initial Information =====
a=0;b=2*pi;     % Domain [a,b]
T_num=50;       % Time step

N=[4,8,16,32,64,128,256];
iter_num=length(N);

degree_k=4;      % Degree of the polynomail on each SV(>=0)
type=5;          % Division points at [-1,1] 
                 %   1=Equidistant; 2=Gauss points; 3=Gauss-Lobatto points;
                 %   4=Gauss-Radau points(left); 5=Gauss-Radau points(right)

error=struct_error(iter_num);            % Struct to stroe error data
%error_super=struct_error_super(iter_num);% Struct to stroe error_super data  
%===== 2、Solving SWE =====
for iter=1:iter_num
    %---1��、Initialize spectral volume and time.--------------------------
     S=linspace(a,b,N(iter)+1)  % Spectrol volumes
%     T=linspace(0,T_end,T_num);  % Time
    delta_T=0.0002*min(diff(S))^4; %Space time ratio
    T=0:delta_T:(T_num-1)*delta_T;
    C=Division(S,degree_k,type); % Control volumes,size N*(k+2)
    mesh=Getmesh(S,C,T);
    
    %---2)、SD Solution ----- ---------------------------------------------
    tic
    mesh=SepctrlVolume_1D(mesh,@u_init);    
    disp(['Solution is finished for N=',num2str(N(iter))]);
    toc
    
    %---3、Error calculation. ---------------------------------------------
    tic
    error=Error_calculation(error,mesh,@u_exact,iter);
%     error_super=Error_calculation_super(error_super,mesh,@u_exact,@u_exact_x,iter);
    disp(['Error calculation is finished for N=',num2str(N(iter))]);
    toc
    
end

%===== 3、Error Analysis and Data processing=====
tic
rate=Error_analysis(error,N);
% Rate_show(error,N,degree_k);   % draw the rate in figure
% Data_result(error,rate,N,degree_k,type);         % Store data(error and rate) in xls files
disp('Error analysis(convergence) and date store are finished');
toc
rate.ru_max
rate.ru_l1
rate.ru_l2

% tic
% rate_super=Error_analysis_super(error_super,N);
% Rate_show_super(error_super,N,degree_k) % draw the rate in figure
% Data_result_super(error_super,rate_super,N,degree_k,type);  % Store data(error and rate) in xls files
% disp('Error analysis(supconvergence) and date store are finished');
% toc


Pic_show(mesh,@u_exact);
disp(['The results is for k=',num2str(degree_k)]);

function u=u_exact(x,t)
u=sin(x+t)+1/2;

function u=u_init(x)
u=sin(x)+1/2;

% function u=u_exact(x,t)
% u=sin(x-t);
% function u=u_exact_x(x,t)
% u=sin(x);
% function u=u_init(x)
% u=sin(x);