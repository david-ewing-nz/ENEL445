"""
Lucas Trickett
Date: 2025-1-21
Description: Function chooses how much to output from each 
             generation type (solar, wind...etc)
"""

def get_generation(wind_capacity, cap_factor_wind, hydro_capacity, cap_factor_hydro, 
                   hydro_MWh_history, geo_capacity, solar_capacity, cap_factor_solar, 
                   battery_capacity, battery_efficiency, battery_SoC, load, price_history, 
                   external_MWs, penalty_cost, cash, shortfall_history, T):
    """
    Simulates power generation over a given timestep for different energy sources.
    
    Args:
        wind_capacity, cap_factor_wind, hydro_capacity, cap_factor_hydro, 
        hydro_MWh_history, geo_capacity, solar_capacity, cap_factor_solar, 
        battery_capacity, battery_efficiency, battery_SoC, load, price_history, 
        external_MWs, penalty_cost, cash, shortfall_history, T: Various input parameters 
        related to power generation and system operation.
    
    Returns:
        tuple: wind_MWh, hydro_MWh, geo_MWh, solar_MWh, battery_MWh
    """
    
    # Wind: always use full amount (curtailment is free)
    wind_MWh = wind_capacity * cap_factor_wind
    
    # Geothermal: always use full amount (curtailment is free)
    geo_MWh = geo_capacity
    
    # Solar: always use full amount(curtailment is free)
    solar_MWh = solar_capacity * cap_factor_solar
    
    # Hydro: Supply shortfall if possible to avoid penalty costs, but don't overuse
    shortfall = load - geo_MWh - wind_MWh - solar_MWh # How much load left
    hydro_MWh = 10*min(hydro_capacity, max(0, shortfall)) # Caped at capacity 
    
    # Battery: Supply shortfall if possible to avoid penalty, else charge
    shortfall = load - geo_MWh - wind_MWh - solar_MWh - hydro_MWh # How much load left
    
    if shortfall > 0:
        battery_MWh = min(battery_SoC * battery_efficiency, shortfall) # Caped at SoC * efficiency
    else:
        battery_MWh = shortfall  # If shortfall negative, absorb excess into batteries for later
    
    return wind_MWh, hydro_MWh, geo_MWh, solar_MWh, battery_MWh
