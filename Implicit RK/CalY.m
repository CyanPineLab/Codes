function y=CalY(tn,yn,h,c,b,A)
%==========================================================================
%                    Calculate yn+1, 2022.01
%==========================================================================
s=length(c);
Y=zeros(s,1);
Y_new=ones(s,1);
while max(abs(Y-Y_new)) > 1e-10
    for i=1:s
        Y(i)=Y_new(i);
    end
    for i=1:s
        tmp=0;
        for j=1:s
            tmp=tmp+A(i,j)*f(tn+c(j)*h,Y(j));
        end
        Y_new(i)=yn+h*tmp;
    end
end

tmp=0;
for i=1:s
    tmp=tmp+b(i)*f(tn+c(i)*h,Y_new(i));
end
y=yn+h*tmp;
