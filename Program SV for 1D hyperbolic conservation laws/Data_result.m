function Data_result(error,rate,N,k,type)
%==========================================================================
% Save error data and convergence rate in file "Results.xls" ,2021.03
%==========================================================================
headline={'N','&','Max error(h)','&','Order','&','L1 error(h)','&','Order',...
    '&','L2 error(h)','&','Order','\\'};
M=ones(1,length(N));
data=[N',M',error.u_max',M',[0,rate.ru_max]',M',error.u_l1',M',[0,rate.ru_l1]',...
    M',error.u_l2',M',[0,rate.ru_l2]',M'];

xls_name='Results of Error and Rate.xls';
if type==1
    sheet=['Equidistant(k=',num2str(k),')'];
elseif type==2
    sheet=['Gauss(k=',num2str(k),')'];
elseif type==3
    sheet=['Lobatto(k=',num2str(k),')'];
elseif type==4
    sheet=['Radau_left(k=',num2str(k),')'];
else%(type==5)
    sheet=['Radau_right(k=',num2str(k),')'];
end

xlswrite(xls_name,headline,sheet,'A1');
xlswrite(xls_name,data,sheet,'A2');
 
for i=1:length(N)
    Mark1(i)='&';
end
xlswrite(xls_name,Mark1',sheet,'B2');
xlswrite(xls_name,Mark1',sheet,'D2');
xlswrite(xls_name,Mark1',sheet,'F2');
xlswrite(xls_name,Mark1',sheet,'H2');
xlswrite(xls_name,Mark1',sheet,'J2');
xlswrite(xls_name,Mark1',sheet,'L2');
