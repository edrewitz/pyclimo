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
        print(f"NOAA PSL THREDDS Server is currently down. Please try again later...")
        sys.exit()

    
