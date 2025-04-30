"""
This file has functions for data access from the NOAA Physical Science Laboratory THREDDS Server. 

This file is written by: Eric J. Drewitz
"""

import xarray as xr
import requests
import sys

from datetime import datetime, timedelta

def shift_longitude(ds, lon_name='lon'):
    """
    Shifts longitude values to ensure continuity across the Prime Meridian.
    """
    lon = ds[lon_name].values
    lon_shifted = (lon + 180) % 360 - 180
    ds = ds.assign_coords({lon_name: lon_shifted})
    ds = ds.sortby(lon_name)
    return ds

def get_variable_paths(variable, level_type):

    """
    This function returns the OPENDAP path for each variable
    """

    if level_type == 'pressure' or level_type == 'pressure level':
        var_paths = {
        'air':['pressure', 'air.nc'],
        'hgt':['pressure', 'hgt.nc'],
        'rhum':['pressure', 'rhum.nc'],
        'shum':['pressure', 'shum.nc'],
        'omega':['pressure', 'omega.nc'],
        'uwnd':['pressure', 'uwnd.nc'],
        'vwnd':['pressure', 'vwnd.nc']
        }
    
    if level_type == 'surface gauss' or level_type == 'sfc gauss':
        var_paths = {
        'air':['surface_gauss', 'air.2m.gauss.nc'],
        'skt':['surface_gauss', 'skt.sfc.gauss.nc'],
        'prate':['surface_gauss', 'prate.sfc.gauss.nc'],
        'lhtfl':['surface_gauss', 'lhtfl.sfc.gauss.nc'],
        'shtfl':['surface_gauss', 'shtfl.sfc.gauss.nc'],
        'uwnd':['surface_gauss', 'uwnd.10m.gauss.nc'],
        'vwnd':['surface_gauss', 'vwnd.10m.gauss.nc'],
        'cfnlf':['surface_gauss', 'cfnlf.sfc.gauss.nc'],
        'pevpr':['surface_gauss', 'pevpr.sfc.gauss.nc']
        }

    if level_type == 'surface' or level_type == 'surface data':
        var_paths = {
        'pr_wtr':['surface', 'pr_wtr.eatm.nc'],
        'slp':['surface', 'slp.nc'],
        'pres':['surface', 'pres.sfc.nc'],
        'air':['surface', 'air.sig995.nc'],
        'omega':['surface', 'omega.sig995.nc'],
        'pottmp':['surface', 'pottmp.sig995.nc'],
        'rhum':['surface', 'rhum.sig995.nc'],
        'uwnd':['surface', 'uwnd.sig995.nc'],
        'vwnd':['surface', 'vwnd.sig995.nc'],
        'lftx':['surface', 'lftx.sfc.nc'],
        }

    return var_paths[variable][0], var_paths[variable][1]

def get_psl_netcdf(variable, level_type, western_bound, eastern_bound, southern_bound, northern_bound, start_date, end_date):

    """
    This function will retrieve NCAR Reanalysis data from the NOAA Physical Science Laboratory's OPENDAP. 

    Required Arguments:

    1) variable (String) - The variable name.
    
        Variable Names:
        
       'air' - Temperature
       'hgt' - Geopotential Height
       'rhum' - Relative Humidity
       'shum' - Specific Humidity
       'omega' - Vertical Velocity
       'uwnd' - U-Component of Wind
       'vwnd' - V-Component of Wind
       'skt' - Skin Temperature
       'pres' - Surface Pressure
       'slp' - Mean Sea Level Pressure
       'prate' - Precipitation Rate
       'lhtfl' - Latent Heat Flux
       'shtfl' - Sensible Heat Flux
       'cfnlf' - Cloud Forcing Net Longwave Flux
       'pevpr' - Surface Potential Evaporation Rate
       'pr_wtr' - Precipitable Water
       'pottmp' - Potential Temperature
       'lftx' - Surface Lifting Index

    2) level_type (String) - This determines the directory at which the data is pulled from on the PSL OPENDAP.

        Level Types:

        i) 'pressure' or 'pressure level'

        This type looks at a variable on a certain pressure level. 
        Available Variables for 'pressure' include:
        
        'air' - Temperature at a specific level
        'hgt' - Geopotential Height at a specific level
        'rhum' - Relative Humidity at a specific level
        'shum' - Specific Humidity at a specific level
        'omega' - Vertical Velocity at a specific level
        'uwnd' - U-Component of wind at a specific level
        'vwnd' - V-Component of wind at a specific level
        
        ii) 'surface gauss' or 'sfc gauss'

        This type looks at a variable at the surface level. 
        Available Variables for 'surface gauss' include:
        
        'air' - 2-Meter Temperature
        'skt' - Skin Temperature 
        'prate' - Precipitation Rate
        'lhtfl' - Latent Heat Flux
        'shtfl' - Sensible Heat Flux
        'uwnd' - 10-Meter U-Component of Wind
        'vwnd' - 10-Meter V-Component of Wind
        'cfnlf' - Cloud Forcing Net Longwave Flux
        'pevpr' - Surface Potential Evaporation Rate

        iii) 'surface' or 'surface data'
        
        This type looks at a variable at the surface level. 
        Available Variables for 'surface' include:

        'pr_wtr' - Precipitation Rate
        'slp' - Mean Sea Level Pressure
        'pres' - Surface Pressure
        'air' - 0.995 Sigma Temperature
        'omega' - 0.995 Sigma Vertical Velocity
        'pottmp' - 0.995 Sigma Potential Temperature
        'rhum' - 0.995 Sigma Relative Humidity
        'uwnd' - 0.995 Sigma U-Component of Wind
        'vwnd' - 0.995 Sigma V-Component of Wind
        'lftx' - Surface Lifting Index

    3) western_bound (Float or Integer) - The western bound for the plot in decimal degrees.
        Negative Values = Western Hemisphere
        Positive Values = Eastern Hemisphere

    4) eastern_bound (Float or Integer) - The eastern bound for the plot in decimal degrees.
        Negative Values = Western Hemisphere
        Positive Values = Eastern Hemisphere
        
    5) southern_bound (Float or Integer) - The southern bound for the plot in decimal degrees.
        Negative Values = Southern Hemisphere
        Positive Values = Northern Hemisphere

    6) northern_bound (Float or Integer) - The northern bound for the plot in decimal degrees.
        Negative Values = Southern Hemisphere
        Positive Values = Northern Hemisphere

    7) start_date (String) - The start date of the analysis period in the 'YYYY-mm-dd' format. 

    8) end_date (String) - The end date of the analysis period in the 'YYYY-mm-dd' format. 

    Returns
    -------

    1) An xarray data array for the variable, area and time period.

    OR

    2) An error message if psl.noaa.gov/thredds is down. 
    """

    directory, file = get_variable_paths(variable, level_type)
    
    start_year = int(f"{start_date[0]}{start_date[1]}{start_date[2]}{start_date[3]}")
    start_month = int(f"{start_date[5]}{start_date[6]}")
    start_day = int(f"{start_date[8]}{start_date[9]}")
    
    end_year = int(f"{end_date[0]}{end_date[1]}{end_date[2]}{end_date[3]}")
    end_month = int(f"{end_date[5]}{end_date[6]}")
    end_day = int(f"{end_date[8]}{end_date[9]}")
    
    start = datetime(start_year, start_month, start_day)
    end = datetime(end_year, end_month, end_day)

    western_bound = western_bound - 2
    eastern_bound = eastern_bound + 2
    southern_bound = southern_bound - 2
    northern_bound = northern_bound + 2

    response = requests.get(f"http://psl.noaa.gov/thredds/dodsC/Aggregations/ncep.reanalysis/{directory}/{file}")

    if response.status_code == 200:
        ds = xr.open_dataset(f"http://psl.noaa.gov/thredds/dodsC/Aggregations/ncep.reanalysis/{directory}/{file}", engine='netcdf4')
        ds = shift_longitude(ds)
        ds = ds.sel(lon=slice(western_bound, eastern_bound, 1), lat=slice(northern_bound, southern_bound, 1), time=slice(start, end))
        
        return ds
    else:
        print(f"NOAA PSL THREDDS Server is currently down. Please try again later or contact: psl.data@noaa.gov")
        sys.exit()

    
