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
from calc import relative_humidity_from_temperature_and_dewpoint, celsius_to_fahrenheit

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


def get_geotiff_data(dtype, region, variable, year, month, day, resolution, normal_type, clear_data_in_folder, plot_anomaly):

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

    2) region (String) - Either 'us' for the CONUS or 'ak' for Alaska

    3) variable (String) - The variable to analyze. 
    
       Universal Variables:
       - ppt = Daily [monthly] total precipitation (rain+melted snow) 
       - tdmean = Daily mean dew point temperature [averaged over all days in the month]
       - tmax = Daily maximum temperature [averaged over all days in the month]
       - tmean = Daily mean temperature, calculated as (tmax+tmin)/2
       - tmin = Daily minimum temperature [averaged over all days in the month]
       - vpdmax = Daily maximum vapor pressure deficit [averaged over all days in the month] 
       - vpdmin = Daily minimum vapor pressure deficit [averaged over all days in the month] 
       - rhmean = Mean Relative Humidity calculated from tmean and tdmean
       
       Additional Variables For Normals Only at 800m resolution:
       - solclear = Total daily global shortwave solar radiation received on a horizontal surface under clear sky conditions [averaged over all days in the month] 
       - solslope = Total daily global shortwave solar radiation received on a sloped surface [averaged over all days in the month] 
       - soltotal = Total daily global shortwave solar radiation received on a horizontal surface [averaged over all days in the month] 
       - soltrans = Atmospheric transmittance (cloudiness) [monthly average daily soltotal/monthly average daily solclear]

    4) year (String) - Year
       Daily Data goes back to 1981
       Monthly Data goes back to 1895

    5) month (String) - 2 digit abbreviation for month (MM)

    6) day (String) - For daily data only - 2 digit abbreviation for day (DD)

    7) resolution (String) - 4km or 800m. 800m takes much longer to convert to a Pandas DataFrame due to a much larger file size.
       However, there is a large increase in resolution. 

    8) normal_type (String) - Daily or Monthly normals. 

    9) clear_data_in_folder (Boolean) - When set to True, the user will clear all old data in the f:PRISM Data folder. 
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
        if variable == 'rhmean':
            url_tmean_norm = f"https://data.prism.oregonstate.edu/normals/{region.lower()}/4km/tmean/daily"
            url_tdmean_norm = f"https://data.prism.oregonstate.edu/normals/{region.lower()}/4km/tdmean/daily"
            url_tmean_data = f"https://data.prism.oregonstate.edu/daily/tmean/{year}"
            url_tdmean_data = f"https://data.prism.oregonstate.edu/daily/tdmean/{year}"
    
            fname_tmean_norm = f"prism_tmean_{region.lower()}_25m_2020{month}{day}_avg_30y.zip"
            geotif_tmean_norm = f"prism_tmean_{region.lower()}_25m_2020{month}{day}_avg_30y.tif"
            fname_tdmean_norm = f"prism_tdmean_{region.lower()}_25m_2020{month}{day}_avg_30y.zip"
            geotif_tdmean_norm = f"prism_tdmean_{region.lower()}_25m_2020{month}{day}_avg_30y.tif"
            fname_tmean_data = f"PRISM_tmean_stable_4kmD2_{year}{month}{day}_bil.zip"
            fname_tdmean_data = f"PRISM_tdmean_stable_4kmD2_{year}{month}{day}_bil.zip"
            geotif_tmean_data = f"PRISM_tmean_stable_4kmD2_{year}{month}{day}_bil.bil"
            geotif_tdmean_data = f"PRISM_tdmean_stable_4kmD2_{year}{month}{day}_bil.bil"
    
            urllib.request.urlretrieve(f"{url_tmean_norm}/{fname_tmean_norm}", f"{fname_tmean_norm}")
            urllib.request.urlretrieve(f"{url_tdmean_norm}/{fname_tdmean_norm}", f"{fname_tdmean_norm}")
            urllib.request.urlretrieve(f"{url_tmean_data}/{fname_tmean_data}", f"{fname_tmean_data}")
            urllib.request.urlretrieve(f"{url_tdmean_data}/{fname_tdmean_data}", f"{fname_tdmean_data}")
        
            extract_zipped_files(f"{fname_tmean_norm}", f"PRISM Data/{fname_tmean_norm}")
            os.remove(f"{fname_tmean_norm}")
            extract_zipped_files(f"{fname_tdmean_norm}", f"PRISM Data/{fname_tdmean_norm}")
            os.remove(f"{fname_tdmean_norm}")
            extract_zipped_files(f"{fname_tmean_data}", f"PRISM Data/{fname_tmean_data}")
            os.remove(f"{fname_tmean_data}")
            extract_zipped_files(f"{fname_tdmean_data}", f"PRISM Data/{fname_tdmean_data}")
            os.remove(f"{fname_tdmean_data}")
        
            tmean_norm = gr.from_file(f"PRISM Data/{fname_tmean_norm}/{geotif_tmean_norm}")
            tdmean_norm = gr.from_file(f"PRISM Data/{fname_tdmean_norm}/{geotif_tdmean_norm}")
            tmean_data = gr.from_file(f"PRISM Data/{fname_tmean_data}/{geotif_tmean_data}")
            tdmean_data = gr.from_file(f"PRISM Data/{fname_tdmean_data}/{geotif_tdmean_data}")
    
            df_tmean_norm = tmean_norm.to_pandas()
            df_tdmean_norm = tdmean_norm.to_pandas()
            df_tmean_data = tmean_data.to_pandas()
            df_tdmean_data = tdmean_data.to_pandas()
    
            df_tmean_norm = df_tmean_norm.loc[:,['value', 'x', 'y']]
            df_tmean_norm = df_tmean_norm.rename(columns={f'value':f'tmean', f'x':f'longitude', f'y':f'latitude'})

            df_tdmean_norm = df_tdmean_norm.loc[:,['value', 'x', 'y']]
            df_tdmean_norm = df_tdmean_norm.rename(columns={f'value':f'tdmean', f'x':f'longitude', f'y':f'latitude'})

            df_tmean_data = df_tmean_data.loc[:,['value', 'x', 'y']]
            df_tmean_data = df_tmean_data.rename(columns={f'value':f'tmean', f'x':f'longitude', f'y':f'latitude'})

            df_tdmean_data = df_tdmean_data.loc[:,['value', 'x', 'y']]
            df_tdmean_data = df_tdmean_data.rename(columns={f'value':f'tdmean', f'x':f'longitude', f'y':f'latitude'})

            if plot_anomaly == False:
                df = pd.DataFrame()
                df['latitude'] = df_tmean_data['latitude']
                df['longitude'] = df_tmean_data['longitude']
                df[variable] = relative_humidity_from_temperature_and_dewpoint(celsius_to_fahrenheit(df_tmean_data['tmean']), celsius_to_fahrenheit(df_tdmean_data['tdmean']))    
            else:
                df = pd.DataFrame()
                df['latitude'] = df_tmean_data['latitude']
                df['longitude'] = df_tmean_data['longitude']
                df['rh'] = relative_humidity_from_temperature_and_dewpoint(celsius_to_fahrenheit(df_tmean_data['tmean']), celsius_to_fahrenheit(df_tdmean_data['tdmean']))
                df['norm'] = relative_humidity_from_temperature_and_dewpoint(celsius_to_fahrenheit(df_tmean_norm['tmean']), celsius_to_fahrenheit(df_tdmean_norm['tdmean']))
                df[variable] = df['rh'] - df['norm']

        else:
            url_norm = f"https://data.prism.oregonstate.edu/normals/{region.lower()}/{resolution.lower()}/{variable.lower()}/daily"
            url_data = f"https://data.prism.oregonstate.edu/daily/{variable.lower()}/{year}"
    
            fname_norm = f"prism_{variable.lower()}_{region.lower()}_25m_2020{month}{day}_avg_30y.zip"
            geotif_norm = f"prism_{variable.lower()}_{region.lower()}_25m_2020{month}{day}_avg_30y.tif"
            fname_data = f"PRISM_{variable.lower()}_stable_{resolution.lower()}D2_{year}{month}{day}_bil.zip"
            geotif_data = f"PRISM_{variable.lower()}_stable_{resolution.lower()}D2_{year}{month}{day}_bil.bil"
    
            urllib.request.urlretrieve(f"{url_norm}/{fname_norm}", f"{fname_norm}")
            urllib.request.urlretrieve(f"{url_data}/{fname_data}", f"{fname_data}")
        
            extract_zipped_files(f"{fname_norm}", f"PRISM Data/{fname_norm}")
            os.remove(f"{fname_norm}")
            extract_zipped_files(f"{fname_data}", f"PRISM Data/{fname_data}")
            os.remove(f"{fname_data}")
        
            norm = gr.from_file(f"PRISM Data/{fname_norm}/{geotif_norm}")
            data = gr.from_file(f"PRISM Data/{fname_data}/{geotif_data}")
    
            df_norm = norm.to_pandas()
            df_data = data.to_pandas()
    
            df_norm = df_norm.loc[:,['value', 'x', 'y']]
            df_norm = df_norm.rename(columns={f'value':f'{variable.lower()}', f'x':f'longitude', f'y':f'latitude'})

            df_data = df_data.loc[:,['value', 'x', 'y']]
            df_data = df_data.rename(columns={f'value':f'{variable.lower()}', f'x':f'longitude', f'y':f'latitude'})

            if plot_anomaly == False:
                df = pd.DataFrame()
                df = df_data
            else:
                df = pd.DataFrame()
                df['latitude'] = df_data['latitude']
                df['longitude'] = df_data['longitude']
                df[variable] = df_data[variable.lower()] - df_norm[variable.lower()]

    if dtype == 'Monthly' or dtype == 'monthly':
        if variable == 'rhmean':
            url_tmean_norm = f"https://data.prism.oregonstate.edu/normals/{region.lower()}/4km/tmean/monthly"
            url_tdmean_norm = f"https://data.prism.oregonstate.edu/normals/{region.lower()}/4km/tdmean/monthly"
            url_tmean_data = f"https://data.prism.oregonstate.edu/monthly/tmean/{year}"
            url_tdmean_data = f"https://data.prism.oregonstate.edu/monthly/tdmean/{year}"
    
            fname_tmean_norm = f"prism_tmean_{region.lower()}_25m_2020{month}_avg_30y.zip"
            geotif_tmean_norm = f"prism_tmean_{region.lower()}_25m_2020{month}_avg_30y.tif"
            fname_tdmean_norm = f"prism_tdmean_{region.lower()}_25m_2020{month}_avg_30y.zip"
            geotif_tdmean_norm = f"prism_tdmean_{region.lower()}_25m_2020{month}_avg_30y.tif"
            fname_tmean_data = f"PRISM_tmean_stable_4kmM3_{year}{month}_bil.zip"
            fname_tdmean_data = f"PRISM_tdmean_stable_4kmM3_{year}{month}_bil.zip"
            geotif_tmean_data = f"PRISM_tmean_stable_4kmM3_{year}{month}_bil.bil"
            geotif_tdmean_data = f"PRISM_tdmean_stable_4kmM3_{year}{month}_bil.bil"
    
            urllib.request.urlretrieve(f"{url_tmean_norm}/{fname_tmean_norm}", f"{fname_tmean_norm}")
            urllib.request.urlretrieve(f"{url_tdmean_norm}/{fname_tdmean_norm}", f"{fname_tdmean_norm}")
            urllib.request.urlretrieve(f"{url_tmean_data}/{fname_tmean_data}", f"{fname_tmean_data}")
            urllib.request.urlretrieve(f"{url_tdmean_data}/{fname_tdmean_data}", f"{fname_tdmean_data}")
        
            extract_zipped_files(f"{fname_tmean_norm}", f"PRISM Data/{fname_tmean_norm}")
            os.remove(f"{fname_tmean_norm}")
            extract_zipped_files(f"{fname_tdmean_norm}", f"PRISM Data/{fname_tdmean_norm}")
            os.remove(f"{fname_tdmean_norm}")
            extract_zipped_files(f"{fname_tmean_data}", f"PRISM Data/{fname_tmean_data}")
            os.remove(f"{fname_tmean_data}")
            extract_zipped_files(f"{fname_tdmean_data}", f"PRISM Data/{fname_tdmean_data}")
            os.remove(f"{fname_tdmean_data}")
        
            tmean_norm = gr.from_file(f"PRISM Data/{fname_tmean_norm}/{geotif_tmean_norm}")
            tdmean_norm = gr.from_file(f"PRISM Data/{fname_tdmean_norm}/{geotif_tdmean_norm}")
            tmean_data = gr.from_file(f"PRISM Data/{fname_tmean_data}/{geotif_tmean_data}")
            tdmean_data = gr.from_file(f"PRISM Data/{fname_tdmean_data}/{geotif_tdmean_data}")
    
            df_tmean_norm = tmean_norm.to_pandas()
            df_tdmean_norm = tdmean_norm.to_pandas()
            df_tmean_data = tmean_data.to_pandas()
            df_tdmean_data = tdmean_data.to_pandas()
    
            df_tmean_norm = df_tmean_norm.loc[:,['value', 'x', 'y']]
            df_tmean_norm = df_tmean_norm.rename(columns={f'value':f'tmean', f'x':f'longitude', f'y':f'latitude'})

            df_tdmean_norm = df_tdmean_norm.loc[:,['value', 'x', 'y']]
            df_tdmean_norm = df_tdmean_norm.rename(columns={f'value':f'tdmean', f'x':f'longitude', f'y':f'latitude'})

            df_tmean_data = df_tmean_data.loc[:,['value', 'x', 'y']]
            df_tmean_data = df_tmean_data.rename(columns={f'value':f'tmean', f'x':f'longitude', f'y':f'latitude'})

            df_tdmean_data = df_tdmean_data.loc[:,['value', 'x', 'y']]
            df_tdmean_data = df_tdmean_data.rename(columns={f'value':f'tdmean', f'x':f'longitude', f'y':f'latitude'})

            if plot_anomaly == False:
                df = pd.DataFrame()
                df['latitude'] = df_tmean_data['latitude']
                df['longitude'] = df_tmean_data['longitude']
                df[variable] = relative_humidity_from_temperature_and_dewpoint(celsius_to_fahrenheit(df_tmean_data['tmean']), celsius_to_fahrenheit(df_tdmean_data['tdmean']))    
            else:
                df = pd.DataFrame()
                df['latitude'] = df_tmean_data['latitude']
                df['longitude'] = df_tmean_data['longitude']
                df['rh'] = relative_humidity_from_temperature_and_dewpoint(celsius_to_fahrenheit(df_tmean_data['tmean']), celsius_to_fahrenheit(df_tdmean_data['tdmean']))
                df['norm'] = relative_humidity_from_temperature_and_dewpoint(celsius_to_fahrenheit(df_tmean_norm['tmean']), celsius_to_fahrenheit(df_tdmean_norm['tdmean']))
                df[variable] = df['rh'] - df['norm']

        else:
            url_norm = f"https://data.prism.oregonstate.edu/normals/{region.lower()}/{resolution.lower()}/{variable.lower()}/monthly"
            url_data = f"https://data.prism.oregonstate.edu/time_series/{region.lower()}/an/{resolution.lower()}/{variable.lower()}/monthly/{year}/"
            
    
            fname_norm = f"prism_{variable.lower()}_{region.lower()}_25m_2020{month}_avg_30y.zip"
            geotif_norm = f"prism_{variable.lower()}_{region.lower()}_25m_2020{month}_avg_30y.tif"
            fname_data = f"prism_{variable.lower()}_{region.lower()}_25m_{year}{month}.zip"
            geotif_data = f"prism_{variable.lower()}_{region.lower()}_25m_{year}{month}.tif"
            
            
    
            urllib.request.urlretrieve(f"{url_norm}/{fname_norm}", f"{fname_norm}")
            urllib.request.urlretrieve(f"{url_data}/{fname_data}", f"{fname_data}")
        
            extract_zipped_files(f"{fname_norm}", f"PRISM Data/{fname_norm}")
            os.remove(f"{fname_norm}")
            extract_zipped_files(f"{fname_data}", f"PRISM Data/{fname_data}")
            os.remove(f"{fname_data}")
        
            norm = gr.from_file(f"PRISM Data/{fname_norm}/{geotif_norm}")
            data = gr.from_file(f"PRISM Data/{fname_data}/{geotif_data}")
    
            df_norm = norm.to_pandas()
            df_data = data.to_pandas()
    
            df_norm = df_norm.loc[:,['value', 'x', 'y']]
            df_norm = df_norm.rename(columns={f'value':f'{variable.lower()}', f'x':f'longitude', f'y':f'latitude'})

            df_data = df_data.loc[:,['value', 'x', 'y']]
            df_data = df_data.rename(columns={f'value':f'{variable.lower()}', f'x':f'longitude', f'y':f'latitude'})

            if plot_anomaly == False:
                df = pd.DataFrame()
                df = df_data
            else:
                variable = variable.lower()
                if variable == 'ppt':
                    df = pd.DataFrame()
                    df['latitude'] = df_data['latitude']
                    df['longitude'] = df_data['longitude']
                    df[variable] = (df_data[variable]/df_norm[variable]) * 100

                else:
                    df = pd.DataFrame()
                    df['latitude'] = df_data['latitude']
                    df['longitude'] = df_data['longitude']
                    df[variable] = df_data[variable.lower()] - df_norm[variable.lower()]
    
    if dtype == 'Normals' or dtype == 'normals':
        if variable == 'rhmean':
            url_tmean = f"https://data.prism.oregonstate.edu/normals/{region.lower()}/{resolution.lower()}/tmean/{normal_type.lower()}"
            url_tdmean = f"https://data.prism.oregonstate.edu/normals/{region.lower()}/{resolution.lower()}/tdmean/{normal_type.lower()}"
    
            if normal_type == 'Monthly' or normal_type == 'monthly':
                fname_tmean = f"prism_tmean_{region.lower()}_25m_2020{month}_avg_30y.zip"
                geotif_tmean = f"prism_tmean_{region.lower()}_25m_2020{month}_avg_30y.tif"
                fname_tdmean = f"prism_tdmean_{region.lower()}_25m_2020{month}_avg_30y.zip"
                geotif_tdmean = f"prism_tdmean_{region.lower()}_25m_2020{month}_avg_30y.tif"
            if normal_type == 'Daily' or normal_type == 'daily':
                fname_tmean = f"prism_tmean_{region.lower()}_25m_2020{month}{day}_avg_30y.zip"
                geotif_tmean = f"prism_tmean_{region.lower()}_25m_2020{month}{day}_avg_30y.tif"
                fname_tdmean = f"prism_tdmean_{region.lower()}_25m_2020{month}{day}_avg_30y.zip"
                geotif_tdmean = f"prism_tdmean_{region.lower()}_25m_2020{month}{day}_avg_30y.tif"
    
            urllib.request.urlretrieve(f"{url_tmean}/{fname_tmean}", f"{fname_tmean}")
            urllib.request.urlretrieve(f"{url_tdmean}/{fname_tdmean}", f"{fname_tdmean}")
        
            extract_zipped_files(f"{fname_tmean}", f"PRISM Data/{fname_tmean}")
            os.remove(f"{fname_tmean}")
            extract_zipped_files(f"{fname_tdmean}", f"PRISM Data/{fname_tdmean}")
            os.remove(f"{fname_tdmean}")
        
            tmean = gr.from_file(f"PRISM Data/{fname_tmean}/{geotif_tmean}")
            tdmean = gr.from_file(f"PRISM Data/{fname_tdmean}/{geotif_tdmean}")
    
            df_tmean = tmean.to_pandas()
            df_tdmean = tdmean.to_pandas()
    
            df_tmean = df_tmean.loc[:,['value', 'x', 'y']]
            df_tmean = df_tmean.rename(columns={f'value':f'tmean', f'x':f'longitude', f'y':f'latitude'})

            df_tdmean = df_tdmean.loc[:,['value', 'x', 'y']]
            df_tdmean = df_tdmean.rename(columns={f'value':f'tdmean', f'x':f'longitude', f'y':f'latitude'})

            df = pd.DataFrame()
            df['latitude'] = df_tmean['latitude']
            df['longitude'] = df_tmean['longitude']
            df[variable] = relative_humidity_from_temperature_and_dewpoint(celsius_to_fahrenheit(df_tmean['tmean']), celsius_to_fahrenheit(df_tdmean['tdmean']))

        else: 
            url = f"https://data.prism.oregonstate.edu/normals/{region.lower()}/{resolution.lower()}/{variable.lower()}/{normal_type.lower()}"
    
            if normal_type == 'Monthly' or normal_type == 'monthly':
                fname = f"prism_{variable.lower()}_{region.lower()}_25m_2020{month}_avg_30y.zip"
                geotif = f"prism_{variable.lower()}_{region.lower()}_25m_2020{month}_avg_30y.tif"
            if normal_type == 'Daily' or normal_type == 'daily':
                fname = f"prism_{variable.lower()}_{region.lower()}_25m_2020{month}{day}_avg_30y.zip"
                geotif = f"prism_{variable.lower()}_{region.lower()}_25m_2020{month}{day}_avg_30y.tif"
    
            urllib.request.urlretrieve(f"{url}/{fname}", f"{fname}")
        
            extract_zipped_files(f"{fname}", f"PRISM Data/{fname}")
            os.remove(f"{fname}")
        
            var = gr.from_file(f"PRISM Data/{fname}/{geotif}")
    
            df = var.to_pandas()
    
            df = df.loc[:,['value', 'x', 'y']]
    
            df = df.rename(columns={f'value':f'{variable.lower()}', f'x':f'longitude', f'y':f'latitude'})

    return df






























            
