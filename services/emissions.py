def calculate_emissions(distance, vehicle_type, fuel_type, fuel_efficiency):
    """
    Calculate vehicle emissions based on distance, fuel type, and fuel efficiency.
    """
    # Define emissions factors (kg CO2 per liter of fuel)
    EMISSIONS_FACTORS = {
        "petrol": 2.31,  # Petrol: 2.31 kg CO2 per liter
        "diesel": 2.68,  # Diesel: 2.68 kg CO2 per liter
        "electric": 0.0  # Electric vehicles have no direct emissions
    }

    # Validate inputs
    if fuel_efficiency <= 0:
        raise ValueError("Fuel efficiency must be greater than zero.")
    if distance <= 0:
        raise ValueError("Distance must be greater than zero.")
    
    # Convert distance to kilometers (assuming it is provided in meters)
    distance_km = distance / 1000  # Convert from meters to kilometers

    # Calculate fuel consumed (in liters)
    fuel_consumed = distance_km / fuel_efficiency  # Liters of fuel consumed

    # Get the emissions factor for the given fuel type
    emissions_factor = EMISSIONS_FACTORS.get(fuel_type)

    if emissions_factor is None:
        raise ValueError("Invalid fuel type provided. Valid options: petrol, diesel, electric.")
    
    # Calculate total emissions (in kg CO2)
    emissions = fuel_consumed * emissions_factor

    return {
        "fuel_consumed": fuel_consumed,
        "emissions": emissions,
        "unit": "kg CO2"
    }
