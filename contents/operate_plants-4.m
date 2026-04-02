function [wind_MWh, hydro_MWh, geo_MWh, solar_MWh, battery_MWh] = ...
    get_generation(wind_capacity, cap_factor_wind, hydro_capacity, ...
    cap_factor_hydro, hydro_MWh_history, geo_capacity, solar_capacity, cap_factor_solar, ...
    battery_capacity, battery_efficiency, battery_SoC, load, price_history, external_MWs, ...
    penalty_cost, cash, shortfall_history, T)

%% ENEL445 Power generation optimisation project
% Jeremy Watson, 2024
% This is the file that operates your power plants throughout the year.

%% Inputs
% wind_capacity - installed wind capacity (MW)
% cap_factor_wind - wind capacity factor for that time period
% hydro_capacity - installed hydro capacity (MW)
% cap_factor_hydro - hydro capacity factor for the year
% geo_capacity - installed geothermal capacity (MW)
% solar_capacity - installed solar capacity (MW)
% cap_factor_solar - solar capacity factor for that time period
% battery_capacity - installed battery capacity (MWh)
% battery_efficiency - battery one-way efficiency (assumed same for charge
%   and discharge)
% battery_SoC - battery state-of-charge (MWh). The usual SoC is battery_SoC
%   / battery_capacity
% load - load (MW) for current time period
% price_history - history of electricity price (only needed for more
%   advanced strategies)
% external_MWs - how many external MWhs can be purchased at market price to
%   avoid the penalty cost
% penalty_cost - if load is not supplied, this is the penalty per MWh
% cash - what are our current funds?
% shortfall_history - history of energy shortfalls (only needed for more
%   advanced strategies)
% T - current timestep

%% Outputs
% How much each type of generation is going to contribute for the current
% time period T. For batteries, a positive MWh means supplying the system,
% a negative MWh means the battery is charging. 
% 
% The programme checks for illegal / impossible results (more error
% checking is likely to be added). 

%% Wind: always use (curtailment is free)
wind_MWh = wind_capacity * cap_factor_wind;

%% Geothermal: always use (curtailment is free)
geo_MWh = geo_capacity;

%% Solar: always use (curtailment is free)
solar_MWh = solar_capacity * cap_factor_solar;

%% Hydro:
% Always supply shortfall if possible to avoid penalty rates
% Don't over-use as water will run out
shortfall = load - geo_MWh - wind_MWh - solar_MWh;
hydro_MWh = min(hydro_capacity, max(0, shortfall));

%% Battery:
% Simple logic (can be improved): always supply shortfall if possible to 
% avoid penalty rates
shortfall = load - geo_MWh - wind_MWh - solar_MWh - hydro_MWh;

if shortfall > 0
    battery_MWh = min(battery_SoC * battery_efficiency, shortfall);
else % always charge when having excess energy
    battery_MWh = shortfall;
end









