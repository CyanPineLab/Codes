function Data_result_super(error,rate,N,k,type)
%==========================================================================
% Save error data and superconvergence rate in file "Results_super.xls"
% ,2021.03
%==========================================================================

headline={'N','&','en error(h)','&','Order','&','ec error(h)','&','Order',...
    '&','ei error(h)','&','Order', '&','edi error(h)','&','Order','\\'};
M=ones(1,length(N));
data=[N',M',error.u_en',M',[0,rate.ru_en]',M',error.u_ec',M',[0,rate.ru_ec]',...
    M',error.u_ei',M',[0,rate.ru_ei]',M',error.u_edi',M',[0,rate.ru_edi]',M'];

xls_name='Results_super of Error and Rate.xls';
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
xlswrite(xls_name,Mark1',sheet,'N2');
xlswrite(xls_name,Mark1',sheet,'P2');