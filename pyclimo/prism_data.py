"""
This file hosts all the functions responsible for the following:
    1) Downloading the PRISM Climate Data
    2) Extracting the Zipped PRISM Climate Data to a folder
    3) Converting the GeoTiff data into a Pandas DataFrame
    4) Returning the Pandas DataFrame to the user 

    (C) Meteorologist Eric J. Drewitz

"""

import urllib.request
import os
import georasters as gr
import pandas as pd
import shutil
import warnings
warnings.filterwarnings('ignore')

from zipfile import ZipFile
from calc import celsius_to_fahrenheit

def extract_zipped_files(file_path, extraction_folder):

    """
    This function unzips a file in a folder. 

    Required Arguments:

    1) file_path (String) - The path to the file that needs unzipping.

    2) extraction_folder (String) - The folder that the zipped files are located in.

    Returns: The contents in the zipped folder are extracted to the extraction folder
    """

    # Load the zipfile
    with ZipFile(file_path, 'r') as zObject:
        # extract a specific file in the zipped folder
        zObject.extractall(extraction_folder)
    zObject.close()


def get_geotiff_data(dtype, variable, year, month, day, normal_type, clear_data_in_folder):

    """
    This function does the following actions:

    1) Builds the data directory if it does not exist yet. 
    2) Downloads the zipped folder holding climate data from the PRISM Climate Group FTP Server
    3) Unzips the zip file and extracts the contents to an extraction folder
    4) Extracts the data from the GeoTiff (.tif) file and converts the data to a Pandas DataFrame

    Required Arguments:

    1) dtype (String) - Data Type: Daily, Monthly, Normals
       - Daily = Daily Data
       - Monthly = Monthly Data
       - Normals = 30-Year Climate Normals

    2) variable (String) - The variable to analyze. 
    
       Universal Variables:
       - ppt = Daily [monthly] total precipitation (rain+melted snow) 
       - tdmean = Daily mean dew point temperature [averaged over all days in the month]
       - tmax = Daily maximum temperature [averaged over all days in the month]
       - tmean = Daily mean temperature, calculated as (tmax+tmin)/2
       - tmin = Daily minimum temperature [averaged over all days in the month]
       - vpdmax = Daily maximum vapor pressure deficit [averaged over all days in the month] 
       - vpdmin = Daily minimum vapor pressure deficit [averaged over all days in the month] 

    3) year (String) - Year
       Daily Data goes back to 1981
       Monthly Data goes back to 1895

    4) month (String) - 2 digit abbreviation for month (MM)

    5) day (String) - For daily data only - 2 digit abbreviation for day (DD)

    6) normal_type (String) - Daily or Monthly normals. 

    7) clear_data_in_folder (Boolean) - When set to True, the user will clear all old data in the f:PRISM Data folder. 
       When set to False, the old data will remain un-touched and archived in the f:PRISM Data folder. 

    Returns: A Pandas DataFrame of PRISM Climate Data
    """

    if os.path.exists(f"PRISM Data"):
        pass
    else:
        os.mkdir(f"PRISM Data")

    if clear_data_in_folder == True:
        for folder in os.listdir(f"PRISM Data"):
            shutil.rmtree(f"PRISM Data/{folder}")
    else:
        pass

    if dtype == 'Daily' or dtype == 'daily':
        url_data = f"https://data.prism.oregonstate.edu/time_series/us/an/4km/{variable.lower()}/daily/{year}"

        fname_data = f"prism_{variable.lower()}_us_25m_{year}{month}{day}.zip"
        geotif_data = f"prism_{variable.lower()}_us_25m_{year}{month}{day}.tif"

        urllib.request.urlretrieve(f"{url_data}/{fname_data}", f"{fname_data}")
    
        extract_zipped_files(f"{fname_data}", f"PRISM Data/{fname_data}")
        os.remove(f"{fname_data}")
    
        data = gr.from_file(f"PRISM Data/{fname_data}/{geotif_data}")

        df_data = data.to_pandas()

        df_data = df_data.loc[:,['value', 'x', 'y']]
        df_data = df_data.rename(columns={f'value':f'{variable.lower()}', f'x':f'longitude', f'y':f'latitude'})

        df = pd.DataFrame()
        df = df_data

    if dtype == 'Monthly' or dtype == 'monthly':
        url_data = f"https://data.prism.oregonstate.edu/time_series/us/an/4km/{variable.lower()}/monthly/{year}"
        
        fname_data = f"prism_{variable.lower()}_us_25m_{year}{month}.zip"
        geotif_data = f"prism_{variable.lower()}_us_25m_{year}{month}.tif"

        urllib.request.urlretrieve(f"{url_data}/{fname_data}", f"{fname_data}")
    
        extract_zipped_files(f"{fname_data}", f"PRISM Data/{fname_data}")
        os.remove(f"{fname_data}")
    
        data = gr.from_file(f"PRISM Data/{fname_data}/{geotif_data}")

        df_data = data.to_pandas()

        df_data = df_data.loc[:,['value', 'x', 'y']]
        df_data = df_data.rename(columns={f'value':f'{variable.lower()}', f'x':f'longitude', f'y':f'latitude'})

        df = pd.DataFrame()
        df = df_data
    
    if dtype == 'Normals' or dtype == 'normals':
        
        url = f"https://data.prism.oregonstate.edu/normals/us/4km/{variable.lower()}/{normal_type.lower()}"

        if normal_type == 'Monthly' or normal_type == 'monthly':
            fname = f"prism_{variable.lower()}_us_25m_2020{month}_avg_30y.zip"
            geotif = f"prism_{variable.lower()}_us_25m_2020{month}_avg_30y.tif"
        if normal_type == 'Daily' or normal_type == 'daily':
            fname = f"prism_{variable.lower()}_us_25m_2020{month}{day}_avg_30y.zip"
            geotif = f"prism_{variable.lower()}_us_25m_2020{month}{day}_avg_30y.tif"

        urllib.request.urlretrieve(f"{url}/{fname}", f"{fname}")
    
        extract_zipped_files(f"{fname}", f"PRISM Data/{fname}")
        os.remove(f"{fname}")
    
        var = gr.from_file(f"PRISM Data/{fname}/{geotif}")

        df = var.to_pandas()

        df = df.loc[:,['value', 'x', 'y']]

        df = df.rename(columns={f'value':f'{variable.lower()}', f'x':f'longitude', f'y':f'latitude'})

    return df






























            
