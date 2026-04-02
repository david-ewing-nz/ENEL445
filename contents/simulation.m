%% ENEL445 Power generation optimisation project
% Jeremy Watson, 2024

clear 
close all
clc

%% Objective
% End the year with the most cash!
% You are given initial_funds of $10 billion to build and oeprate a power system
% Your goal is to have the most cash in hand at the end of one year (365*24
% hourly time periods). if you fail to supply electricity, you will be charged 
% a penalty_cost for each MWh not supplied.
initial_funds = 10e9; % starting funds
time_period = 365*24; % simulation is hourly for a year
penalty_cost = 1000; % $ / MWh not supplied

%% Randomness etc.
rng(1) % This will be changed (randomly) for the final evaluation
totalSimulations = 100; % This will be set to 100 for the final evaluation

%% Run trials
final_score = zeros(totalSimulations,1);
for n = 1:totalSimulations
    %% Simulation setup
    % Unless otherwise stated, all parameters with randomness have 10% std
    load_average = 1000 + 1000 * rand(); % MW
    load_std = 250; % MW

    %% Costing
    external_MWs_average = 750; % MW which can be sourced at market price
    external_MWs_std = 75; 

    base_price_average = 15 * randn + 150; % $ / MWh
    priceCoefficient1 = 0.0075*randn + 0.075; % will be randomly chosen for each year
    priceCoefficient2 = 15*randn + 150; % will be randomly chosen for each year

    %% Wind power
    % Your max power will be randomized with a _uniform_ distribution from 0% to
    % 50% capacity
    cost_wind = 1.1e5*randn + 1.1e6; % dollars per MW
    cap_factor_wind_avg = 0.25; % i.e. 25% average, but will be uniformally distributed between 0 and 2*avg%

    %% Hydro power
    % Your total energy over the month will be limited to 40% capacity factor
    cost_hydro = 2.8e5*randn + 2.8e6; % dollars per MW
    cap_factor_hydro = 0.45 + 0.045 * randn; % i.e. 45% with randomness

    %% Geothermal power
    cost_geothermal = 4.8e5*randn + 4.8e6;
    % We will assume a 100% capacity factor!!

    %% Solar power
    cost_solar = 8e4*randn + 8e5;
    % Capacity factor for each of 24 hours per day
    % Will be 20% randomized at each time step, uniform distribution
    % midnight - 1am, 1am - 2am, etc
    solar_capacity = [...
        0.0 0 0 0 0 0 ...
        0.1 0.2 0.3 0.5 0.7 0.7 ...
        0.8 0.8 0.7 0.5 0.3 0.2 ...
        0.1 0.0 0.0 0.0 0.0 0.0];

    %% Batteries
    % Batteries start fully charged
    cost_battery = 1.5e4*randn + 1.5e5; % $ / MWh
    battery_efficiency = 0.975; % one way efficiency

    %% Initilization
    power_plants = zeros(5,1);
    starting_funds = initial_funds;

    %% First decision: how much to build
    % Note, you do not need to spend all your money building stuff!
    [wind_build_MW, hydro_build_MW, geo_build_MW, solar_build_MW, battery_build_MW] ...
        = build_plants(load_average, load_std, cost_wind, cap_factor_wind_avg, ...
        cost_hydro, cap_factor_hydro, cost_geothermal, solar_capacity, cost_solar, ...
        cost_battery, battery_efficiency, base_price_average, external_MWs_average, ...
        penalty_cost, priceCoefficient1, priceCoefficient2, ...
        starting_funds);

    %% Check if build is valid
    % Invalid builds are not built at all... make sure your program doesn't
    % do this!
    total_cost = wind_build_MW*cost_wind + hydro_build_MW*cost_hydro + geo_build_MW*cost_geothermal + solar_build_MW*cost_solar + battery_build_MW*cost_battery;
    if  total_cost <= starting_funds && all([wind_build_MW hydro_build_MW geo_build_MW solar_build_MW battery_build_MW] >= 0) % fixed 09/04/25: no negative MW builds
        power_plants(1) = wind_build_MW;
        power_plants(2) = hydro_build_MW;
        power_plants(3) = geo_build_MW;
        power_plants(4) = solar_build_MW;
        power_plants(5) = battery_build_MW;

        starting_funds = starting_funds - total_cost;
    end
    
    %% Initialize for simulation
    cash = zeros(time_period+1,1);
    cash(1) = starting_funds;
    
    battery_SoC = zeros(time_period+1,1);
    battery_SoC(1) = power_plants(5);

    shortfall = zeros(time_period,1);
   
    wind_capacity_factor  = zeros(time_period,1);
    solar_capacity_factor = zeros(time_period,1);
    load = zeros(time_period,1);
    price = zeros(time_period,1);
    external_MWs = zeros(time_period,1);

    wind_MWh = zeros(time_period,1);
    hydro_MWh = zeros(time_period,1);
    geo_MWh = zeros(time_period,1);
    solar_MWh = zeros(time_period,1);
    battery_MWh = zeros(time_period,1);

    energy_supplied = zeros(time_period,1);
    %% Second decision: how much power to supply from where at each time step
    for t = 1:time_period

        %% Wind, solar power, load, pricing etc.
        wind_capacity_factor(t) = cap_factor_wind_avg + cap_factor_wind_avg * (rand() - 0.5);
        solar_capacity_factor(t) = solar_capacity(mod(t,24) + 1) * (0.8 + 0.4*rand());
        load(t) = load_average + load_std*randn;
        price(t) = base_price_average + base_price_average/10*randn + load(t)*priceCoefficient1 - wind_capacity_factor(t)*priceCoefficient2;
        external_MWs(t) = external_MWs_average + external_MWs_std * randn;
        
        %% Second decision: decide how much to supply
        [wind_MWh(t), hydro_MWh(t), geo_MWh(t), solar_MWh(t), battery_MWh(t)] = ...
            operate_plants(power_plants(1), wind_capacity_factor(t), power_plants(2), ...
            cap_factor_hydro, hydro_MWh, power_plants(3), power_plants(4), solar_capacity_factor(t), ...
            power_plants(5), battery_efficiency, battery_SoC(t), load(t),  price, external_MWs(t), ...
            penalty_cost, cash(t), shortfall, t);

        %% Check if the proposed generation is valid 
        % if not, the proposed MWs will be capped
        if wind_MWh(t) > wind_capacity_factor(t)*power_plants(1)
            wind_MWh(t) = wind_capacity_factor(t)*power_plants(1);
        end

        if hydro_MWh(t) > power_plants(2)
            hydro_MWh(t) = power_plants(2);
        end
        if sum(hydro_MWh) > cap_factor_hydro * power_plants(2) * time_period % already used all the water!! Fixed 09/04/25 - don't allow too-large hydro_MWh to skip this check
            hydro_MWh(t) = 0;
        end

        if geo_MWh(t) > power_plants(3)
            geo_MWh(t) = power_plants(3);
        end

        if solar_MWh(t) > solar_capacity_factor(t)*power_plants(4)
            solar_MWh(t) = solar_capacity_factor(t)*power_plants(4);
        end

        if battery_MWh(t) > battery_SoC(t) * battery_efficiency
            battery_MWh(t) = battery_SoC(t)  * battery_efficiency;
        elseif battery_MWh(t) < -(power_plants(5) - battery_SoC(t))
            battery_MWh(t) = -(power_plants(5) - battery_SoC(t));
        end

        %% Resolve market
        energy_supplied(t) = wind_MWh(t) + hydro_MWh(t) + geo_MWh(t) + solar_MWh(t) + battery_MWh(t);
        shortfall(t) = load(t) - energy_supplied(t);
        if energy_supplied(t) >= load(t) % excess energy is dumped for free
            cash(t+1) = cash(t) + load(t) * price(t);
        else
            if shortfall(t) <= external_MWs(t) % fixed 09/04/25
                cash(t+1) = cash(t) + energy_supplied(t) * price(t) - shortfall (t) * price(t);
            else
                cash(t+1) = cash(t) + energy_supplied(t) * price(t) - external_MWs(t) * price(t) - (shortfall(t) - external_MWs(t)) * penalty_cost;
            end
        end

        %% Update battery SOC
        if battery_MWh(t) < 0
            battery_SoC(t+1) = min(power_plants(5), battery_SoC(t) - battery_efficiency*battery_MWh(t)); % don't overcharge
        else
            battery_SoC(t+1) = max(battery_SoC(t) - battery_MWh(t)/battery_efficiency, 0); % don't undercharge
        end

    end
    final_score(n) = cash(t+1);
end

%% Result
% This is what we need to maximize
% The given start functions achieve around $3 billion cash at the end of 
% the year, on average.
% It is definitely possible to more than double this by using
% optimization techniques.
score = mean(final_score); 
fprintf('After 1 year, you have funds of $ %d on average!\n', score)

%% Figures
% Uncomment/modify if you want to plot stuff
% figure(1)
% plot(1:time_period, load)
% ylabel('Load (MW)')
% xlabel('Time')
% 
% figure(2)
% plot(1:time_period, wind_MWh, 1:time_period, hydro_MWh, 1:time_period, geo_MWh, 1:time_period, solar_MWh, 1:time_period, battery_MWh)
% legend('Wind', 'Hydro', 'Geothermal', 'Solar', 'Battery')
% ylabel('MW')
% xlabel('Time')
% 
% figure(3)
% plot(1:time_period+1, cash)
% ylabel('Funds ($)')
% 
% figure(4)
% plot(1:time_period, shortfall)
% ylabel('Shortfall (MWh)')
% 
% figure(5)
% plot(1:time_period+1, battery_SoC)
% ylabel('Battery SoC (MWh)')