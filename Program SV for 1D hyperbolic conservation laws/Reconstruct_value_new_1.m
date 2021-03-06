function pi_value=Reconstruct_value_new_1(A,C,x,i)
%==========================================================================
%     Derivative approximation polynomial of u(x) in S_i, 2021.03.
%      (same as Reconstruct_value_deri_1.m)
% A: cell-average??matrix (size:N*(k+1)).
% C: control volumes, N*(k+2)
% x: x-value in Si.
% i:the i-th SV, 1<=i<=N.
%==========================================================================
k=size(C,2)-2;      % degree of polynomail in CV
H=diff(C,1,2);      % length of each CV, N*(k+1)
hi=H(i,:);          % size 1*(k+1)
xi=C(i,:);          % size 1*(k+2)

x_num=length(x);
ui_bar=A(i,:);
Lij_bar_1=zeros(x_num,k+1);

for j=1:k+1
    R=zeros(x_num,1);
    for r=j+1:k+2
        S=zeros(x_num,1);
       for s=1:k+2
           if s~=r
               T=zeros(x_num,1);
               for t=1:k+2
                   M=zeros(x_num,1);
                   if (t~=r&&t~=s)
                       seq=sort([r,s,t]);
                       temp=[xi(1:seq(1)-1),xi(seq(1)+1:seq(2)-1),xi(seq(2)+1:seq(3)-1),xi(seq(3)+1:k+2)];
                       for q=1:x_num
                           M(q)=prod(x(q)-temp);
                       end
                       M(:)=M(:)/prod(xi(r)-temp);
                       T(:)=T(:)+M(:)/(xi(r)-xi(t));                     
                   end       
               end
               S(:)=S(:)+T(:)/(xi(r)-xi(s));
           end
       end
       R(:)=R(:)+S(:);
    end
    Lij_bar_1(:,j)=hi(j)*R(:);
end

pi_value=(Lij_bar_1*ui_bar')';