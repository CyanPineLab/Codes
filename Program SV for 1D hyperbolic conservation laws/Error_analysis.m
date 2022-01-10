function rate=Error_analysis(error,N)
%==========================================================================
%           Calculate the order of convergence,2021.03
%
% (Rate of Max error, L1 error, L2 error)
%==========================================================================
iter_num=length(N); 
if iter_num==1
    error('No convergence order!!!');
end

ru_max=zeros(1,iter_num-1);
ru_l1=zeros(1,iter_num-1);
ru_l2=zeros(1,iter_num-1);


for iter=1:iter_num-1
    ru_max(iter)=log(error.u_max(iter)/error.u_max(iter+1))/log(N(iter+1)/N(iter));
    ru_l1(iter)=log(error.u_l1(iter)/error.u_l1(iter+1))/log(N(iter+1)/N(iter));
    ru_l2(iter)=log(error.u_l2(iter)/error.u_l2(iter+1))/log(N(iter+1)/N(iter));
end

rate=struct('ru_max',ru_max,'ru_l1',ru_l1,'ru_l2',ru_l2);