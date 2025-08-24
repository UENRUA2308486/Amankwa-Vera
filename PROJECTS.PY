# 00P PRINCIPAL
class PetroleumEngineeringCalculations:  # Base class

    def __init__(self, name="Base Calculation"):
        self.name = name

    def calculate(self):
        raise NotImplementedError("Subclasses must implement the calculate method.") # Enforce implementation

    def description(self):
        return f"Calculation: {self.name}"

class Porosity(PetroleumEngineeringCalculations):
    def __init__(self, bulk_volume, grain_volume):
        super().__init__(name="Porosity Calculation")
        self.bulk_volume = bulk_volume
        self.grain_volume = grain_volume

    def calculate(self):
        try:
            if self.bulk_volume <= 0 or self.grain_volume < 0 or self.grain_volume > self.bulk_volume:
                raise ValueError("Invalid volume values.")
            pore_volume = self.bulk_volume - self.grain_volume
            porosity = pore_volume / self.bulk_volume
            return porosity
        except ValueError as e:
            return f"Error: {e}"

    def description(self): # Polymorphism
        return "Calculates porosity from bulk and grain volumes."

class Permeability(PetroleumEngineeringCalculations):
    def __init__(self, viscosity, flow_rate, length, area, pressure_drop):
        super().__init__(name="Permeability Calculation")
        self.viscosity = viscosity  # cp
        self.flow_rate = flow_rate  # cm3/s
        self.length = length  # cm
        self.area = area  # cm2
        self.pressure_drop = pressure_drop  # atm

    def calculate(self):
        try:
            if self.area <= 0 or self.length <= 0 or self.viscosity <= 0 or self.pressure_drop <= 0:
                raise ValueError("Invalid parameter value for permeability.")
            permeability = (self.viscosity * self.flow_rate * self.length) / (self.area * self.pressure_drop) #Darcy's law
            return permeability
        except ValueError as e:
            return f"Error: {e}"

    def description(self):  # Polymorphism
        return "Calculates permeability using Darcy's law."

class OilFormationVolumeFactor(PetroleumEngineeringCalculations):
    def __init__(self, dissolved_gas, oil_volume_stc, oil_volume_reservoir):
        super().__init__(name = "Oil Formation Volume Factor Calculation")
        self.dissolved_gas = dissolved_gas
        self.oil_volume_stc = oil_volume_stc
        self.oil_volume_reservoir = oil_volume_reservoir

    def calculate(self):
        try:
            if self.oil_volume_stc <= 0 or self.oil_volume_reservoir <= 0:
                raise ValueError("Invalid parameter value for oil formation volume factor")
            boi = (self.oil_volume_reservoir + self.dissolved_gas) / self.oil_volume_stc
            return boi
        except ValueError as e:
            return f"Error: {e}"

    def description(self):  # Polymorphism
        return "Calculates oil formation volume factor (Boi)"

class WaterSaturation(PetroleumEngineeringCalculations):
    def __init__(self, porosity, water_resistivity, formation_resistivity):
        super().__init__(name = "Water saturation calculation")
        self.porosity = porosity
        self.water_resistivity = water_resistivity
        self.formation_resistivity = formation_resistivity

    def calculate(self):
        try:
            if self.formation_resistivity <= 0 or self.water_resistivity <= 0 or self.porosity <= 0:
                raise ValueError("Invalid parameter value for water saturation calculation")
            sw = (self.water_resistivity/(self.porosity**2 * self.formation_resistivity))**0.5
            return sw
        except ValueError as e:
            return f"Error: {e}"

    def description(self):  # Polymorphism
        return "Calculates Water Saturation (Sw)"

class ReynoldsNumber(PetroleumEngineeringCalculations):
  def __init__(self, density, velocity, diameter, viscosity):
    super().__init__(name = "Reynolds Number Calculation")
    self.density = density
    self.velocity = velocity
    self.diameter = diameter
    self.viscosity = viscosity

  def calculate(self):
    try:
        if self.density <= 0 or self.diameter <= 0 or self.viscosity <= 0 or self.velocity <= 0:
            raise ValueError("Invalid parameter value for Reynolds number calculation")
        re = (self.density*self.velocity*self.diameter)/self.viscosity
        return re
    except ValueError as e:
        return f"Error: {e}"

  def description(self):  # Polymorphism
        return "Calculates Reynolds Number (Re)"

class ProductivityIndex(PetroleumEngineeringCalculations):
    def __init__(self, flow_rate, flowing_pressure, static_pressure):
        super().__init__(name = "Productivity Index Calculation")
        self.flow_rate = flow_rate
        self.flowing_pressure = flowing_pressure
        self.static_pressure = static_pressure

    def calculate(self):
        try:
            if self.flowing_pressure < 0 or self.static_pressure <= 0 or self.flowing_pressure >= self.static_pressure:
                raise ValueError("Invalid parameter value for Productivity Index calculation")
            j = self.flow_rate/(self.static_pressure - self.flowing_pressure)
            return j
        except ValueError as e:
            return f"Error: {e}"

    def description(self):  # Polymorphism
        return "Calculates Productivity Index (J)"

# Example Usage
porosity_calc = Porosity(bulk_volume=100, grain_volume=70)
print(porosity_calc.description()) # Polymorphism in action
print(f"Porosity: {porosity_calc.calculate()}")

permeability_calc = Permeability(viscosity=1, flow_rate=10, length=100, area=1, pressure_drop=1)
print(permeability_calc.description())
print(f"Permeability: {permeability_calc.calculate()}")

Boi = OilFormationVolumeFactor(dissolved_gas = 500, oil_volume_stc = 10, oil_volume_reservoir = 15)
print(Boi.description())
print(f"Oil Formation Volume Factor: {Boi.calculate()}")

Sw = WaterSaturation(porosity = 0.3, water_resistivity = 1, formation_resistivity = 10)
print(Sw.description())
print(f"Water Saturation: {Sw.calculate()}")

Re = ReynoldsNumber(density = 50, velocity = 3, diameter = 0.1, viscosity = 1)
print(Re.description())
print(f"Reynolds Number: {Re.calculate()}")

J = ProductivityIndex(flow_rate = 20, flowing_pressure = 1000, static_pressure = 3000)
print(J.description())
print(f"Productivity Index: {J.calculate()}")
