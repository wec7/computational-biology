load 1d3z.txt;
N = 75;
A = X1d3z(1:N,:);
p = A';
plot3(p(1,:),p(2,:),p(3,:),'r*-');
c = zeros(N,N);
M = 10;
sig = 10;
for i = 1 : N
    for j = 1 : N
        if (i~=j) 
            c(i,j) = M / norm(p(:,i)-p(:,j), 'fro');%+randn();
        end
    end
end
Y = lle_eval('origin.pdb','eval.pdb', c, p, 7);