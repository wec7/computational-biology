% load 1d3z.txt;
% load 1ubq.txt;
% s = 2;
% t = 70;
% A = X1d3z(s:t,:);
% B = X1ubq(s:t,:);
    A = 5.9*Y';
    B = p';
    s = 1;
    t = 75;
    uA = mean(A);
    uB = mean(B);
    A = A - ones(t-s+1,1)*uA;
    B = B - ones(t-s+1,1)*uB;
    A = A';
    B = B';
    C=A*B';
    [U, D, V] = svd(C);
    if det(C)>0
        S = diag([1,1,1]);
    else
        S = diag([1,1,-1]);
    end
    R = U*S*V';
    A = R'*A;
    M = A-B;
    rmsd = norm(M, 'fro')/sqrt(t-s+1)
    plot3(A(1,:),A(2,:),A(3,:),'r*-');
    hold on;
    plot3(B(1,:),B(2,:),B(3,:),'bo-')

