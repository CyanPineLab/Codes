function Rate_show_super(error,N,k,division_type)
%==========================================================================
%        Show the super convergence(loglog figure),2021.03
%
% error: the error of h and q
% N:the subdivision number for space
% k: the degree of approximation polynamation
%==========================================================================
if length(N)<2
    error('No convergence rate to be showed');
end

figure
loglog(N,error.u_en,'b-.*',N,error.u_ec,'m-.s',N,error.u_ei,'g:o',N,error.u_edi,'r-+',N,5*N.^(-(2*k)),'k-+',N,5*N.^(-(k+1)),'k-+')
legend('e_n','e_c','e_i','e_{di}','2k','k+1')
title(['Error analysis with k=',num2str(k)])

