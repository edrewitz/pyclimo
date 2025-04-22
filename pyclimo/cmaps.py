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


