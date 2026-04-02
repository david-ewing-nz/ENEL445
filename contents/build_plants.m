function [wind_build_MW, hydro_build_MW, geo_build_MW, solar_build_MW, battery_build_MW] = build_plants(...
    load_average, load_std, cost_wind, cap_factor_wind_avg, ...
    cost_hydro, cap_factor_hydro, cost_geothermal, solar_capacity, cost_solar, ...
    cost_battery, battery_efficiency, base_price, external_MWs_average, ...
    penalty_cost, priceCoefficient1, priceCoefficient2, ...
    funds)

%% ENEL445 Power generation optimisation project
% Jeremy Watson, 2024
% This function determines how much generation to build

%% Inputs:
% See simulation.m for more details, these are the parameters of the
% year-long simulation which might be useful to optimize your power plant
% build.

%% Outputs
% How much capacity of each type to build (MW)

wind_build_MW = 0.2*funds/cost_wind;
hydro_build_MW = 0.2*funds/cost_hydro;
geo_build_MW = 0.2*funds/cost_geothermal;
solar_build_MW = 0.2*funds/cost_solar;
battery_build_MW = 0.2*funds/cost_battery;

end

