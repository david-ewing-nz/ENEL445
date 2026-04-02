"""
Lucas Trickett
Date: 2025-1-21
Description: Function allocates fraction of initial funds to each power plant type
"""


def build_plants(load_average, load_std, cost_wind, cap_factor_wind_avg, 
                 cost_hydro, cap_factor_hydro, cost_geothermal, solar_capacity, 
                 cost_solar, cost_battery, battery_efficiency, base_price, 
                 external_MWs_average, penalty_cost, priceCoefficient1, 
                 priceCoefficient2, funds):
    """
    Determines how much generation to build based on given parameters.
    
    Args:
        load_average, load_std, cost_wind, cap_factor_wind_avg, 
        cost_hydro, cap_factor_hydro, cost_geothermal, solar_capacity, 
        cost_solar, cost_battery, battery_efficiency, base_price, 
        external_MWs_average, penalty_cost, priceCoefficient1, 
        priceCoefficient2, funds: Various input parameters related to load, cost, and power generation.
    
    Returns:
        tuple: wind_build_MW, hydro_build_MW, geo_build_MW, solar_build_MW, battery_build_MW
    """
    
    # Code to replace/optimise: Equal share of spending
    wind_build_frac = 0.2
    hydro_build_frac = 0.2
    geo_build_frac = 0.2
    solar_build_frac = 0.2
    battery_build_frac = 0.2

    wind_build_MW = wind_build_frac * funds / cost_wind
    hydro_build_MW = hydro_build_frac * funds / cost_hydro
    geo_build_MW = geo_build_frac * funds / cost_geothermal
    solar_build_MW = solar_build_frac * funds / cost_solar
    battery_build_MW = battery_build_frac * funds / cost_battery
    
    return wind_build_MW, hydro_build_MW, geo_build_MW, solar_build_MW, battery_build_MW
