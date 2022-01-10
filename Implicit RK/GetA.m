function A=GetA(C,k)
%==========================================================================
%                    get coefficient A, 2022.01
%==========================================================================
A=zeros(k,k);

for i=1:k 
   K=zeros(k,1);
   for j=1:k
       K(j)=C(j+1,i)/j;
   end
   A(i,:)=linsolve(C(1:k,:),K);
end