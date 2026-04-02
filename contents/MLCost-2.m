function [g, p, u] = MLCost(theta, r1, fdoa, Q, s, sdot, L, B, R, wavelength, scaling)
% This function computes the maximum likelihood cost function 
% and its gradient at the given source-reference distance, r1, and 
% orientation angle w.r.t. the east, theta.

a = (R^2 - r1^2 + s(:, 1)'*s(:, 1))/(2*norm(s(:, 1)));     % Source x-coordinate in ENU.
h = sqrt(max([0, R^2 - a^2]) + 1/scaling^2);

T = ENU2ECEF_Matrix(L, B, 1);

u = [h * sin(theta), h*cos(theta), a]';
u = T *u;

M = size(s, 2);                                                   % Number of sensors.
FDOA = zeros(M-1, 1);                                    % Reproduced FDOA.

for m = 2 : M
      FDOA(m-1) = FDOAGen(u, zeros(3, 1), s(:, 1), sdot(:, 1), s(:, m), sdot(:, m));
end;
FDOA = FDOA/wavelength;                             % m/s to Hz.

g = 1/2*(fdoa - FDOA)' * inv(Q) * (fdoa - FDOA);         % ML cost function value at u.

df_du = zeros(M-1, 3);
du_dp = zeros(3, 2);

for m = 2 : M
      df_du(m-1, :) = drdot_du(u, zeros(3, 1), s(:, m), sdot(:, m));
      df_du(m-1, :) = df_du(m-1, :) - drdot_du(u, zeros(3, 1), s(:, 1), sdot(:, 1))';
end;

p = -1/wavelength * (fdoa - FDOA)' * inv(Q) * df_du;

du_dp = [h*cos(theta),     r1 * a/(h*norm(s(:, 1))) * sin(theta);   
               -h*sin(theta),      r1 * a/(h*norm(s(:, 1))) * cos(theta);
                 0,                      -r1/norm(s(:, 1))];

du_dp = T * du_dp;
 
p = (p * du_dp)';
p = p/(g+1/scaling);                                       % Gradient of the logarithm of the ML cost function at [theta, r1]'.

g = log(g);                                                         % Logarithm of the ML cost function.

% figure(4)
% quiver(theta*180/pi, r1, p(1)/norm(p)*180/pi, p(2)/norm(p), 0, 'MaxHeadSize', 0.005);







