"""
This file holds the functions that perform calculations. 

(C) Meteorologist Eric J. Drewitz
"""
import math
import numpy as np

def round_to_quarter(x):
    """
    Round to the nearest 0.25
    """
    return round(x * 4) / 4

def mm_to_in(mm):

    """
    Converts millimeters to inches
    """

    return mm * 0.0393701

def celsius_to_fahrenheit(c):
    
    """
    Converts Celsius to Fahrenheit
    """

    frac = 9/5
    return (c * frac) + 32

def roundup(x):
    """
    Rounds Value Up to the nearest 10
    """
    return int(math.ceil(x / 10.0)) * 10

def rounddown(x):
    """
    Rounds Value Down to the nearest 10
    """
    return int(math.floor(x / 10.0)) * 10

def saturation_vapor_pressure(temperature):

    """
    This function calculates the saturation vapor pressure from temperature.
    This function uses the formula from Bolton 1980.         
    """

    e = 6.112 * np.exp(17.67 * (temperature) / (temperature + 243.5))
    return e

def relative_humidity_from_temperature_and_dewpoint(temperature, dewpoint):

    """
    This function calculates the relative humidity from temperature and dewpoint. 
    """

    e = saturation_vapor_pressure(dewpoint)
    e_s = saturation_vapor_pressure(temperature)
    return (e / e_s) * 100











