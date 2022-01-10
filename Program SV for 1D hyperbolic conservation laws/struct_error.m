function error=struct_error(iter_num)
%==========================================================================
%            Struct of error at the end time, 2021.03
%==========================================================================
u_max=zeros(1,iter_num);
u_l1=zeros(1,iter_num);
u_l2=zeros(1,iter_num);

error=struct('u_max',u_max,'u_l1',u_l1,'u_l2',u_l2);