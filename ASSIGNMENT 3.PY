def calculate_porosity(bulk_volume, grain_volume):
    """Calculates porosity from bulk and grain volumes."""
    try:
        if bulk_volume <= 0 or grain_volume < 0 or grain_volume > bulk_volume:
            raise ValueError("Invalid volume values.")
        pore_volume = bulk_volume - grain_volume
        porosity = pore_volume / bulk_volume
        return porosity
    except ValueError as e:
        return f"Error: {e}"

def calculate_permeability(viscosity, flow_rate, length, area, pressure_drop):
    """Calculates permeability using Darcy's law."""
    try:
        if area <= 0 or length <= 0 or viscosity <= 0 or pressure_drop <= 0:
            raise ValueError("Invalid parameter value for permeability.")
        permeability = (viscosity * flow_rate * length) / (area * pressure_drop)
        return permeability
    except ValueError as e:
        return f"Error: {e}"

def calculate_oil_formation_volume_factor(dissolved_gas, oil_volume_stc, oil_volume_reservoir):
    """Calculates Oil Formation Volume Factor (Boi)"""
    try:
        if oil_volume_stc <= 0 or oil_volume_reservoir <= 0:
            raise ValueError("Invalid parameter value for oil formation volume factor")
        boi = (oil_volume_reservoir + dissolved_gas) / oil_volume_stc
        return boi
    except ValueError as e:
        return f"Error: {e}"

def calculate_water_saturation(porosity, water_resistivity, formation_resistivity):
    """Calculates Water Saturation (Sw)"""
    try:
        if formation_resistivity <= 0 or water_resistivity <= 0 or porosity <= 0:
            raise ValueError("Invalid parameter value for water saturation calculation")
        sw = (water_resistivity/(porosity**2 * formation_resistivity))**0.5
        return sw
    except ValueError as e:
        return f"Error: {e}"

def calculate_reynolds_number(density, velocity, diameter, viscosity):
    """Calculates Reynolds Number (Re)"""
    try:
        if density <= 0 or diameter <= 0 or viscosity <= 0 or velocity <= 0:
            raise ValueError("Invalid parameter value for Reynolds number calculation")
        re = (density*velocity*diameter)/viscosity
        return re
    except ValueError as e:
        return f"Error: {e}"

def calculate_productivity_index(flow_rate, flowing_pressure, static_pressure):
    """Calculates Productivity Index (J)"""
    try:
        if flowing_pressure < 0 or static_pressure <= 0 or flowing_pressure >= static_pressure:
            raise ValueError("Invalid parameter value for Productivity Index calculation")
        j = flow_rate/(static_pressure - flowing_pressure)
        return j
    except ValueError as e:
        return f"Error: {e}"

# Example Usage (Functional)
print(f"Porosity: {calculate_porosity(bulk_volume=100, grain_volume=70)}")
print(f"Permeability: {calculate_permeability(viscosity=1, flow_rate=10, length=100, area=1, pressure_drop=1)}")
print(f"Oil Formation Volume Factor: {calculate_oil_formation_volume_factor(dissolved_gas = 500, oil_volume_stc = 10, oil_volume_reservoir = 15)}")
print(f"Water Saturation: {calculate_water_saturation(porosity = 0.3, water_resistivity = 1, formation_resistivity = 10)}")
print(f"Reynolds Number: {calculate_reynolds_number(density = 50, velocity = 3, diameter = 0.1, viscosity = 1)}")
print(f"Productivity Index: {calculate_productivity_index(flow_rate = 20, flowing_pressure = 1000, static_pressure = 3000)}")

