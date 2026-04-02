function [u, C] = BFGS_Bisection(fdoa, Q, wavelength, s, sdot, r1, r1_lb, r1_ub, theta, theta_lb, theta_ub, L, B, scaling)
% This function finds the FDOA-only geolocation result using the BFGS
% algorithm with bisection-based pinpointing for line search.

R = 6378.137e3;                                              % Earth radius.

R = R/scaling;                                                   % Scaled Earth radius.
s = s/scaling;                                                    % Scaled sensor positions.

r1 = r1/scaling;                                                % Scaled source-reference sensor distance.
r1_lb = r1_lb/scaling;                                      % Scaled lower bound of the source-reference sensor distance.
r1_ub = r1_ub/scaling;                                    % Scaled upper bound of the source-reference sensor distance.

% M = size(s, 2);                                                   % Number of sensors.

[g, p, ~] = MLCost(theta, r1, fdoa, Q, s, sdot, L, B, R, wavelength, scaling);

tolerance = 1e-6;                                             % Stop tolerance.
MaxIter = 20;                                                    % Maximum number of iterations.   

phi0 = g;                                                           % Logarithm of the ML cost function at the initial solution guess.
phi0dot = p' * (-p);                                          % Initial gradient of line search along the gradient descent.

if max(abs(p)) > tolerance                              % BFGS algorithm.
   [a, flag] = LineSearch_Bisection(phi0, phi0dot, -p, theta, theta_lb, theta_ub, r1,  r1_lb, r1_ub, fdoa, Q, s, sdot, L, B, R, wavelength, scaling);
   
   theta = theta - a * p(1);                                % Search direction = -p.
   r1 = r1 - a * p(2);
   
   [g1, p1, u1] = MLCost(theta, r1, fdoa, Q, s, sdot, L, B, R, wavelength, scaling);

   iter = 1;                                                           % Iteration counter.
   V = eye(2);                                                
   
   dp = p;                                                            % Gradient at the previous solution.  
   dp1 = p1;                                                       % Gradient at the current solution.
   
   g0 = g1;                                                          % ML cost at the previous solution.
   u0 = u1;
   
   if (~flag)
      while (iter <= MaxIter)
          d = - a * p;                                              % Update in the solution.
          y = dp1 - dp;                                          % Difference in gradient.
          sigma = 1/(d' * y + sqrt(eps));
          
          V = (eye(2) - sigma * d * y') * V * (eye(2) - sigma * d * y')' + sigma * (d * d');
          V = (V + V')/2;
          
          p = V * dp1;                                            % Line search direction (-p).
          if dp1'*(-p) > 0                                       % Increase in cost function.
             p = dp1;                                               % Gradient descent.
             V = eye(2);                                           % Reset the inverse of the estimated Hessian.
          end;
          
          phi0 = g1;
          phi0dot = dp1' * (-p);
          
          [a, flag] = LineSearch_Bisection(phi0, phi0dot, -p, theta, theta_lb, theta_ub, r1,  r1_lb, r1_ub, fdoa, Q, s, sdot, L, B, R, wavelength, scaling);
          
          theta = theta - a * p(1);                         % Solution update.
          r1 = r1 - a * p(2);
   
          dp = dp1;                                                % Gradient at the previous solution.
          
          [g1, dp1, u1] = MLCost(theta, r1, fdoa, Q, s, sdot, L, B, R, wavelength, scaling);              % Gradient at the current solution.
          
          iter = iter + 1;
          
          if (flag == 1)                                           % Solution at the boundary.
              break;
          
          elseif max(abs(dp1)) < tolerance          
              break;
              
          elseif abs(g1 - g0) < tolerance * (1 + abs(g0))  
              break;
              
          elseif norm(u1 - u0) < tolerance * (1+norm(u0))
              break;
              
          end;          
          g0 = g1;                                                  % Logarithm of the ML cost function at the previous solution. 
          u0 = u1;                                                  % Previous solution.
          
      end;
   end;
end;

u = u1*scaling;                                                 % FDOA-only geolocation result.
C = g1;                                                              % Logarithm of the ML cost function.