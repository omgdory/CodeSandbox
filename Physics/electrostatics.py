# Derived equations for electrostatics
from math import *

# epsilon naught (Farads per Meter)
EPSILON_NAUGHT = 8.854*pow(10,-12)

# Capacitance (Coulombs/Volts => Farads)
def capacitance(charge: float, voltage: float) -> float:
    return charge/voltage

# Electric Field due to sphere
# Newtons/Coulomb
def EFsphere(charge: float, radius: float) -> float:
    k = 1/(4*pi*EPSILON_NAUGHT)
    return k * charge / (radius*radius)

# Energy Density at "r" for spherical capacitor
def ED_capacitor_sphere(innerRadius: float, outerRadius: float, voltage: float, r: float) -> float:
    ep = EPSILON_NAUGHT/2
    rdiff = (innerRadius*outerRadius)/(outerRadius-innerRadius)
    return ep * pow((voltage/(r*r)) * rdiff, 2)

def ED_capacitor_parallel(voltage: float, distance: float) -> float:
    return voltage/distance

# Energy Density for parallel plate capacitor
def ED(capacitance: float, voltage: float):
    return (1/2)*capacitance*(voltage*voltage)

if __name__ == "__main__":
    print(str())
    
# def foo(req, *args, **kwargs):
#     print(req)
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)

# foo('hello', 1, 7, 1231, rad=99, kwarg2='nog')