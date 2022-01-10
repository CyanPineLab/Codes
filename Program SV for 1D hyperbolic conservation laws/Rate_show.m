function Rate_show(error,N,k)
%==========================================================================
%           Show convergence(loglog figure),2021.03
%
% error: the error(Max,L1,L2) of h and q
% N:the subdivision number for space
% k: the degree of approximation polynamation
%==========================================================================
if length(N)<2
    error('No convergence rate to be showed');
end

figure
loglog(N,error.u_max,'b-.*',N,error.u_l1,'m-.s',N,error.u_l2,'g:o',N,5*N.^(-(k+1)),'k-+')
legend('Max error','L1 error','L2 error','k+1')
title(['Error analysis with k=',num2str(k)])

