% This is the main function for developing an iterative solution for 
% frequency difference of arrival (FDOA)-only source geolocation 
% based on the BFGS algorithm with line search. Developed by 
% Le Yang, Xi Li and Yi Liu in April 2023.

% Program initialization
clc;                                   % Clear command window.
close all;                          % Close all figures.
clear all;                          % Clear workspace.

% Constants
c = 299792458;            % Speed of light.
 
deg2rad = pi/180;        % Degree to radian conversion.
rad2deg = 180/pi;        % Radian to degree conversion.

f0 = 1e9;                        % Carrier frequency of the source signal.
wavelength = c/f0;       % Wavelength of the source signal.

% Source position
Lt = 10 * deg2rad;        % Source longitude.
Bt =   5 * deg2rad;        % Source latitude.
Ht = 0;
uo = sphere_LLA2ECEF(Lt, Bt, Ht);

% Sensor location
Ls1 =  0 * deg2rad;
Bs1 =  0 * deg2rad;
Hs1 = 1000e3; 
s1 = sphere_LLA2ECEF(Ls1, Bs1, Hs1);

distance = 100e3;
Ls2 = Ls1 + distance/norm(s1);
Bs2 = Bs1;
Hs2 = Hs1;
s2 = sphere_LLA2ECEF(Ls2, Bs2, Hs2);

Ls3 = Ls1 - distance/norm(s1);
Bs3 = Bs1;
Hs3 = Hs1;
s3 = sphere_LLA2ECEF(Ls3, Bs3, Hs3);

Ls4 = Ls1;
Bs4 = Bs1 + distance/norm(s1);
Hs4 = Hs1;
s4 = sphere_LLA2ECEF(Ls4, Bs4, Hs4);

speed1 = 7e3;
heading1 = 40 * deg2rad;
ENUVec1 = speed1 * [sin(heading1), cos(heading1), 0]';
s1dot = sphere_ENU2ECEF(Ls1, Bs1, ENUVec1);

speed2 = 7e3;
heading2 = 45 * deg2rad;
ENUVec2 = speed2 * [sin(heading2), cos(heading2), 0]';
s2dot = sphere_ENU2ECEF(Ls2, Bs2, ENUVec2);

speed3 = 7e3;
heading3 = 40 * deg2rad;
ENUVec3 = speed3 * [sin(heading3), cos(heading3), 0]';
s3dot = sphere_ENU2ECEF(Ls3, Bs3, ENUVec3);

speed4 = 7e3;
heading4 = 35 * deg2rad;
ENUVec4 = speed4 * [sin(heading4), cos(heading4), 0]';
s4dot = sphere_ENU2ECEF(Ls4, Bs4, ENUVec4);

s = [s1, s2, s3, s4];                                           % Sensor position matrix.
sdot = [s1dot, s2dot, s3dot, s4dot];              % Sensor velocity matrix.
 
M = size(s,2);                                                    % Number of sensors.                             

% Geolocation scenario visualization
figure(1)
plot(Lt * rad2deg, Bt * rad2deg, '^', 'MarkerSize', 12);

hold on;     grid on;
box on;
title('Geolocation scenario');

plot(Ls1 * rad2deg, Bs1 * rad2deg, 'o', 'MarkerSize', 12);
plot(Ls2 * rad2deg, Bs2 * rad2deg, 'o', 'MarkerSize', 12);
plot(Ls3 * rad2deg, Bs3 * rad2deg, 'o', 'MarkerSize', 12);
plot(Ls4 * rad2deg, Bs4 * rad2deg, 'o', 'MarkerSize', 12);

xlabel('Longitude (degree)');
ylabel('Latitude (degree)');
axis([-5, 15, -5, 15]);

% True FDOAs
fdoa = zeros(M-1, 1);

for m = 2 : M
      fdoa(m-1) = FDOAGen(uo, zeros(3,1), s(:, 1), sdot(:, 1), s(:, m), sdot(:, m));
end;
fdoa = fdoa/wavelength;                                % m/s to Hz.

% Noise statistics
sigma_f = 16;                                                      % Noise standard deviation (Hz).

Q = (eye(M-1) + ones(M-1))/2;
Q = sigma_f^2 * Q;                                          % Noise covariance.

% Range for source-reference sensor distance
L_range = 40 * deg2rad;
B_range = 40 * deg2rad;

[r1_lb, r1_ub] = sphere_r1_range(s(:, 1), L_range, B_range);

% Range for source orientation angle
theta_lb  = -pi/2;
theta_ub = pi/2;

% Monte Carlo simulation
scaling = 1000e3;                                            % Scaling factor for distance.   

N = 20;                                                              % Number of initial solution guesses.
b = 2;                                                                 % Base for the Hammersley sequence. 

delta = 0.05;

delta_r1 = (r1_ub - r1_lb) * delta;
delta_theta = (theta_ub - theta_lb) * delta;

ensembleRun = 1e2;                                        % Number of ensemble runs.
rmse = zeros(ensembleRun, 1);
for k = 1 : ensembleRun
      fdoa_noise = chol(Q)' * randn(M-1, 1);
      FDOA = fdoa + fdoa_noise;               
      
      % Multistart search initialization
      phi = HammersleySeq(N, b);    
        
      r1 = r1_lb + delta_r1 + phi(:, 1) * (r1_ub - r1_lb - 2 * delta_r1);
      theta = theta_lb + delta_theta + phi(:, 2) * (theta_ub - theta_lb - 2 * delta_theta);
      
      if (k == 1)        
         figure(2);
         polar(pi/2 - theta, r1/scaling, '.');
         
         CostfunContour(r1_lb, r1_ub, theta_lb, theta_ub, s, sdot, Ls1, Bs1, FDOA, wavelength, Q, scaling);
         
         figure(4);
         hold on;
         
         plot(theta * rad2deg, r1/scaling, '.', 'MarkerSize',12);
      end;
      
      u = zeros(3, N);                                          % FDOA geolocation results from different initial solution guesses.
      C = zeros(N, 1);                                          % Cost function values from different initial solution guesses.   
      
      for n = 1 : N                                                % BFGS algorithm with bisection-based pinpointing for line search.
            [u(:, n), C(n)] = BFGS_Bisection(FDOA, Q, wavelength, s, sdot, r1(n), r1_lb, r1_ub, theta(n), theta_lb, theta_ub, Ls1, Bs1, scaling);
      end;
      
      [~, index] = min(C);
      
      u_est = u(:, index);
      rmse(k) = norm(u_est - uo)^2;
      
      if mod(k, 100) == 0
         k
      end;
end;

rmse = sqrt(mean(rmse))/1e3


            
