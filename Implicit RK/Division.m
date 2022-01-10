function c=Division(k,type)
%==========================================================================
%                    division [-1,1] with k+2 points, 2021.03
%type:  1=Equidistant; 
%       2=Gauss points;
%       3=Gauss-Lobatto points;
%       4=Gauss-Radau points(left);
%       5=Gauss-Radau points(right)
%==========================================================================
c=zeros(1,k);
%--- control points on [-1,1]
if type==1  % Equidistant 
    c=linspace(-1,1,k);
elseif type==2  % Gauss points
    c=legs(k);
elseif type==3  % Gauss-Lobatto points
    c=legslb(k);
elseif type==4  % Gauss-Radau points(left)
    c=legsrd(k);
elseif type==5  % Gauss-Radau points(right)
    c_temp=legsrd(k);
    c=fliplr(-c_temp);
else
    error("No such division now!!")
end

c(:)=(c(:)+1)/2.;