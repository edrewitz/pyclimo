"""
This file hosts all the colormaps used to plot data. 

(C) Meteorologist Eric J. Drewitz
"""
import matplotlib.colors
import warnings
warnings.filterwarnings('ignore')

def temperature_colormap():
    temperature_colormap = matplotlib.colors.LinearSegmentedColormap.from_list("temperature", ["darkviolet", "blue", "deepskyblue", "springgreen", "green", "gold", "orange", "pink", "darkred", "deeppink"])

    return temperature_colormap

def dew_point_colormap():
    dew_point_colormap = matplotlib.colors.LinearSegmentedColormap.from_list("dew point", ["darkorange", "orange", "darkkhaki", "forestgreen", "lime", "aqua"])

    return dew_point_colormap

def relative_humidity_colormap():
    relative_humidity_colormap = matplotlib.colors.LinearSegmentedColormap.from_list("relative humidity", ["saddlebrown", "darkorange", "gold", "lightgoldenrodyellow", "yellowgreen", "lawngreen", "springgreen", "lime"])
    
    return relative_humidity_colormap

def temperature_change_colormap():
    temperature_change_colormap = matplotlib.colors.LinearSegmentedColormap.from_list("temperature change", ["darkblue", "blue", "deepskyblue", "lightgrey", "lightgrey", "orangered", "red", "darkred"])

    return temperature_change_colormap

def dew_point_change_colormap():
    dew_point_change_colormap = matplotlib.colors.LinearSegmentedColormap.from_list("dew point change", ["darkorange", "darkkhaki", "lightgrey", "forestgreen", "aqua"])

    return dew_point_change_colormap

def precipitation_colormap():
    precipitation_colormap = matplotlib.colors.LinearSegmentedColormap.from_list("precipitation", ["magenta", "blue", "cyan", "lime", "darkgreen", "gold", "orange", "red", "darkred", "maroon", "dimgrey"])

    return precipitation_colormap

def precipitation_anomaly_colormap():
    precipitation_anomaly_colormap = matplotlib.colors.LinearSegmentedColormap.from_list("precipitation anomaly", ["saddlebrown", "peru", "orange", "gold", "lightgrey", "lime", "darkgreen", "blue", "navy" ])

    return precipitation_anomaly_colormap

def relative_humidity_change_colormap():
    relative_humidity_change_colormap = matplotlib.colors.LinearSegmentedColormap.from_list("relative humidity", ["saddlebrown", "peru", "orange", "gold", "lightgrey", "yellowgreen", "lawngreen", "springgreen", "lime"])
    
    return relative_humidity_change_colormap

def vapor_pressure_deficit_colormap():
    
    vapor_pressure_deficit_colormap = matplotlib.colors.LinearSegmentedColormap.from_list("vpd", ["indigo", "purple", "magenta", "lightgrey", "gold", "darkorange", "saddlebrown"])
    
    return vapor_pressure_deficit_colormap
