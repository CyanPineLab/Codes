function rate=Error_analysis_super(error,N)
%==========================================================================
%           Calculate the order of superconvergence,2021.03
%
% (Rate of en,ec,ei,edi error)
%==========================================================================
iter_num=length(N); 
if iter_num==1
    error('No convergence order!!!');
end

ru_en=zeros(1,iter_num-1);
ru_ec=zeros(1,iter_num-1); 
ru_ei=zeros(1,iter_num-1); 
ru_edi=zeros(1,iter_num-1);

for iter=1:iter_num-1
    ru_en(iter)=log(error.u_en(iter)/error.u_en(iter+1))/log(N(iter+1)/N(iter));
    ru_ec(iter)=log(error.u_ec(iter)/error.u_ec(iter+1))/log(N(iter+1)/N(iter));
    ru_ei(iter)=log(error.u_ei(iter)/error.u_ei(iter+1))/log(N(iter+1)/N(iter));
    ru_edi(iter)=log(error.u_edi(iter)/error.u_edi(iter+1))/log(N(iter+1)/N(iter));
end

rate=struct('ru_en',ru_en,'ru_ec',ru_ec,'ru_ei',ru_ei,'ru_edi',ru_edi);