function error_super=struct_error_super(iter_num)
%==========================================================================
%        Struct of error of superconvergence at the end time, 2021.03
%==========================================================================
u_en=zeros(1,iter_num);
u_ec=zeros(1,iter_num);
u_ei=zeros(1,iter_num);
u_di=zeros(1,iter_num);

error_super=struct('u_en',u_en,'u_ec',u_ec,'u_ei',u_ei,'u_di',u_di);