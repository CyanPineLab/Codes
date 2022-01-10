function C=Division(S,k,type)
%==========================================================================
%                    division [-1,1] with k+2 points, 2021.03
%type:  1=Equidistant; 
%       2=Gauss points;
%       3=Gauss-Lobatto points;
%       4=Gauss-Radau points(left);
%       5=Gauss-Radau points(right)
%==========================================================================
h=diff(S);  % Length of each S ,size 1*N
N=length(S)-1;  % size of SV
C=zeros(N,k+2);
%--- control points on [-1,1]
if type==1  % Equidistant 
    c=linspace(-1,1,k+2);
elseif type==2  % Gauss points
    c_temp=legs(k);
    c=[-1,c_temp,1];
elseif type==3  % Gauss-Lobatto points
    c=legslb(k+2);
elseif type==4  % Gauss-Radau points(left)
    c_temp=legsrd(k+1);
    c=[c_temp,1];
elseif type==5  % Gauss-Radau points(right)
    c_temp=legsrd(k+1);
    c_temp=fliplr(-c_temp);
    c=[-1,c_temp];
else
    error("No such division now!!")
end

for i=1:N 
   C(i,:)=h(i)/2*c(:)+S(i)+h(i)/2; 
end