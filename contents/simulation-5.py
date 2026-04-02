"""
ENEL445 Power System Optimisation project
Code by: Lucas Trickett, based on MATLAB code by Jeremy Watson
Date: 2025-1-21
Description: Function simulated energy generation market over a year
             in 1 hour time intervals
             * Sets up the random market conditions at the beginning of the year
             * Uses build_plants to choose how much to invest into each
             * Simulates market changes for each hour (for-loop), using get_generation  
               to set generation outputs at each hour
             * See documentation on Learn for further details.
"""

import random
from build_plants import build_plants
from operate_plants import get_generation

def evaluate_year():
    initial_funds = 10e9  # starting funds
    time_period = 365 * 24  # simulation is hourly for a year
    penalty_cost = 1000  # $ / MWh not supplied

    # Simulation setup
    # Load average and standard deviation for the year 
    load_average = 1000 + 1000 * random.random()  # MW
    load_std = 250  # MW

    # Costing
    external_MWs_average = 750  # MW which can be sourced at market price

    base_price_average = 150 * random.gauss(1, 0.1)  # $ / MWh
    priceCoefficient1 = 0.075 * random.gauss(1, 0.1)  # Random for each year
    priceCoefficient2 = 150 * random.gauss(1, 0.1)  # Random for each year

    # Wind power
    cost_wind = 1.1e6 * random.gauss(1, 0.1)  # dollars per MWh
    cap_factor_wind_avg = 0.25  # 25% average, but randomized

    # Hydro power
    cost_hydro = 2.8e6 * random.gauss(1, 0.1) # dollars per MWh
    cap_factor_hydro = 0.45 * random.gauss(1, 0.1)  # i.e., 45% with randomness

    # Geothermal power
    cost_geothermal = 4.8e6 * random.gauss(1, 0.1)
    # Assume a 100% capacity factor

    # Solar power
    cost_solar = 8e5 * random.gauss(1, 0.1) # dollars per MWh
    # Solar_capacity: fraction of potential energy for each hour of the day (0 at night)
    solar_capacity = [0.0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.7, 0.8, 0.8, 0.7, 0.5, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0]

    # Batteries
    cost_battery = 1.5e5 * random.gauss(1, 0.1)  # dollars per MWh
    battery_efficiency = 0.975  # one-way efficiency in supplying energy (storing not considered)

    # Initialization
    starting_funds = initial_funds
    power_plants = [0, 0, 0, 0, 0] # AMount funded into each power plant
    # | 0 - Wind | 1 - Hydro | 2 - Geothermal | 3 - Solar | 4 - Battery |
    
    
    # First decision: how much to invest into each generation type
    wind_build_MW, hydro_build_MW, geo_build_MW, solar_build_MW, battery_build_MW = build_plants(
        load_average, load_std, cost_wind, cap_factor_wind_avg, cost_hydro, cap_factor_hydro,
        cost_geothermal, solar_capacity, cost_solar, cost_battery, battery_efficiency,
        base_price_average, external_MWs_average, penalty_cost, priceCoefficient1,
        priceCoefficient2, starting_funds
    )

    # Check if build is valid
    total_cost = (wind_build_MW * cost_wind + 
                  hydro_build_MW * cost_hydro +
                  geo_build_MW * cost_geothermal + 
                  solar_build_MW * cost_solar +
                  battery_build_MW * cost_battery) # How much we have invested
    
    # If you try invest more than you have, we will do nothing
    if total_cost <= starting_funds and wind_build_MW >= 0 and hydro_build_MW >= 0 and geo_build_MW >= 0 and solar_build_MW >= 0 and battery_build_MW >= 0: # fixed 09/04/25
        power_plants = [wind_build_MW, hydro_build_MW, geo_build_MW, solar_build_MW, battery_build_MW]
        starting_funds -= total_cost

    ############ Create arrays to store hourly data throughout year progression ############
    # Initialize for simulation
    cash = [0] * (time_period + 1)
    cash[0] = starting_funds # Cash at start of year - leftovers from investment

    battery_SoC = [0] * (time_period + 1)
    battery_SoC[0] = power_plants[4] # Assume batteries start completely full
    
    shortfall = [0] * time_period # Cash shortfall at each hour of year
    wind_capacity_factor = [0] * time_period # Wind capacity (limit) at each hour of year
    solar_capacity_factor = [0] * time_period # Solar capacity (limit) at each hour of year
    load = [0] * time_period # Load at each hour of year
    price = [0] * time_period # How much you earn for supplying each MWh
    external_MWs = [0] * time_period

    wind_MWh = [0] * time_period  # Wind generation at each hour of year
    hydro_MWh = [0] * time_period # Hydro generation at each hour of year
    geo_MWh = [0] * time_period # Geo generation at each hour of year
    solar_MWh = [0] * time_period # Solar generation at each hour of year
    battery_MWh = [0] * time_period # Battery generation at each hour of year
    energy_supplied = [0] * time_period # Total generation at each hour of year

    hydro_MWh_sum = 0 # Only so much water in the hydro dam (if sum exceeds)
    
    ############ Simulate annual market change ############
    # Second decision: how much power to supply at each time step
    for t in range(time_period):  # 8760 hours
        
        # Randomised at each hour
        wind_capacity_factor[t] = cap_factor_wind_avg + cap_factor_wind_avg * (random.random() - 0.5) # Random in 50-150%
        solar_capacity_factor[t] = solar_capacity[t % 24] * (0.8 + 0.4 * random.random()) # Random in 80-120%

        load[t] = load_average + load_std * random.gauss(0, 1)
        price[t] = base_price_average + base_price_average/10 * random.gauss(0, 1) + load[t] * priceCoefficient1 - wind_capacity_factor[t] * priceCoefficient2
        external_MWs[t] = external_MWs_average * random.gauss(1, 0.1)

        # Second decision: decide how much to supply
        wind_MWh[t], hydro_MWh[t], geo_MWh[t], solar_MWh[t], battery_MWh[t] = get_generation(
            power_plants[0], wind_capacity_factor[t], power_plants[1], cap_factor_hydro,
            hydro_MWh, power_plants[2], power_plants[3], solar_capacity_factor[t],
            power_plants[4], battery_efficiency, battery_SoC[t], load[t], price, external_MWs[t],
            penalty_cost, cash[t], shortfall, t
        )

        ############ Check if the proposed generation is valid ############
        # Caped based on initial investments and current wind levels
        if wind_MWh[t] > wind_capacity_factor[t] * power_plants[0]:
            wind_MWh[t] = wind_capacity_factor[t] * power_plants[0]

        # Capped based on initial investments
        if hydro_MWh[t] > power_plants[1]:
            hydro_MWh[t] = power_plants[1]
        if hydro_MWh_sum + hydro_MWh[t] > cap_factor_hydro * power_plants[1] * time_period:  # all the water is used, fixed 09/04/25
            hydro_MWh[t] = hydro_MWh[t] = max(0, cap_factor_hydro * power_plants[1] * time_period - hydro_MWh_sum) # use any remaining water (if any)
        hydro_MWh_sum += hydro_MWh[t] # Always increase the sum (= decrement the water) with hydro_MWh[t]. Fixed 24/04/25
        
        # Capped based on initial investments
        if geo_MWh[t] > power_plants[2]:
            geo_MWh[t] = power_plants[2]

        # Capped based on initial investments and current sunlight
        if solar_MWh[t] > solar_capacity_factor[t] * power_plants[3]:
            solar_MWh[t] = solar_capacity_factor[t] * power_plants[3]

        # Cap battery generation to storage + outgoing efficiency
        if battery_MWh[t] > battery_SoC[t] * battery_efficiency:
            battery_MWh[t] = battery_SoC[t] * battery_efficiency
        elif battery_MWh[t] < -(power_plants[4] - battery_SoC[t]):
            # Cant absorb more than batteries can handle (determined by initial investment)
            battery_MWh[t] = -(power_plants[4] - battery_SoC[t])

        # Resolve market
        energy_supplied[t] = wind_MWh[t] + hydro_MWh[t] + geo_MWh[t] + solar_MWh[t] + battery_MWh[t]
        shortfall[t] = load[t] - energy_supplied[t]
        
        if energy_supplied[t] >= load[t]:  # excess energy is dumped for free
            cash[t + 1] = cash[t] + load[t] * price[t] # New cash = old cash + earnings
        else:
            # We didnt supply enough power to cover loads :(
            if shortfall[t] <= external_MWs[t]: # fixed 09/04/25
                #
                cash[t + 1] = cash[t] + energy_supplied[t] * price[t] - shortfall[t] * price[t]
            else:
                # Have to purchase energy externally + we get penalised for being short
                cash[t + 1] = cash[t] + energy_supplied[t] * price[t] - external_MWs[t] * price[t] - (shortfall[t] - external_MWs[t]) * penalty_cost

        # Update battery SOC
        if battery_MWh[t] < 0: # if storing, increase SoC by battery_MWh * efficency (caped at limit = power_plants[4]) 
            battery_SoC[t + 1] = min(power_plants[4], battery_SoC[t] - battery_efficiency * battery_MWh[t])  # battery_MWh is negative so ' - battery_efficiency * battery_MWh[t]' is positive
        else: # if supplying, decrease SoC (batt/efficnecy as SoC loses more due to ineffiency)
            battery_SoC[t + 1] = max(battery_SoC[t] - battery_MWh[t] / battery_efficiency, 0)  # Storage cant be negative

    return cash[-1]


if __name__ == "__main__":
    # Initialize random number generator
    random.seed(1)  # Use system time as the seed for randomness

    # Since each year is random, we take an average to get a reliable measure of quality
    total_simulations = 100 # Number of years to simulate
    total_cash = 0          # Total sum across each year (to take an average of)
    
    for i in range(total_simulations):
        total_cash += evaluate_year()
    
    print(f'Average Annual Profit: {total_cash/(1e9*total_simulations):.5g} billion')
