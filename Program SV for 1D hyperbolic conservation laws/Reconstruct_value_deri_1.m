function pi_value=Reconstruct_value_deri_1(A,C,x,i)
%==========================================================================
% pi_vaule=p_i'(x), p_i is the derivative approximation polynomial of u(x) in S_i,
% 2021.03.

% A: cell-average£¬matrix(size:N*(k+1)).
% C: control volumes, N*(k+2)
% x: x-value in Si.
% i:the i-th SV, 1<=i<=N.
%==========================================================================

ui_bar=A(i,:);
xi=C(i,:);
hi=diff(xi);
k=length(xi)-2;

omega_bar_der=zeros(1,k+2);
for i=1:k+2
    xi_temp=[xi(1:i-1),xi(i+1:k+2)];
    omega_bar_der(i)=prod(xi(i)-xi_temp);
end
x_num=length(x);
Phi=zeros(x_num,k+1);

for l=1:k+1
    R=zeros(x_num,1);
    for r=l+1:k+2
        M=zeros(x_num,1);
        for m=1:k+2              
            if (m~=r)  
                S=zeros(x_num,1);
                for s=1:k+2                  
                    if (s~=r&&s~=m)
                        seq=sort([r,m,s]);               
                        xi_temp=[xi(1:seq(1)-1),xi(seq(1)+1:seq(2)-1),xi(seq(2)+1:seq(3)-1),xi(seq(3)+1:k+2)];
                        for q=1:x_num
                            S(q)=S(q)+prod(x(q)-xi_temp);
                        end
                    end                    
                end
                M(:)=M(:)+S(:);
            end
        end
        R(:)=R(:)+M(:)/omega_bar_der(r);
    end
    Phi(:,l)=hi(l)*R(:);
end

pi_value=(Phi*ui_bar')';