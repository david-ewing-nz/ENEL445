function phi = HammersleySeq(N, b)
% This function generates a N-point Hammersley sequence matrix.

M = numel(b);

phi = zeros(N, M+1);
phi(:, 1) = (1:N)'/N;
for  m = 1 : M
      for n = 1 : N
            phi(n, m+1) = RadicalInverseFun(n, b(m));
      end;
end;