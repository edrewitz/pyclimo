import os
import warnings
warnings.filterwarnings('ignore')

def noaa_psl_directory(variable, level_type, western_bound, eastern_bound, southern_bound, northern_bound, start_date, end_date, dataset_type, level):

    """
    This function builds the file directory for the NOAA PSL Graphics. 
    
    Required Arguments:

    1) variable (String) - The variable name.
    
        Variable Names:
        
       'air' - Temperature
       'hgt' - Geopotential Height
       'rhum' - Relative Humidity
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

    9) dataset_type (String) - The type of dataset (i.e. NCAR Reanalysis)

    10) level (String) - Default = '500'. The pressure level in hPa. 
        Valid levels:

        '1000'
        '925'
        '850'
        '700'
        '600'
        '500'
        '400'
        '300'
        '250'
        '200'
        '150'
        '100'
        '70'
        '50'
        '30'
        '20'
        '10'

    Returns
    -------

    1) A path where the NOAA PSL Graphics will be stored
    2) An abbreviation of the path to be printed to the user
    """

    variable = variable.upper()
    level_type = level_type.upper()
    dataset_type = dataset_type.upper()
    
    start_year = f"{start_date[0]}{start_date[1]}{start_date[2]}{start_date[3]}"
    start_month = f"{start_date[5]}{start_date[6]}"
    start_day = f"{start_date[8]}{start_date[9]}"
    
    end_year = f"{end_date[0]}{end_date[1]}{end_date[2]}{end_date[3]}"
    end_month = f"{end_date[5]}{end_date[6]}"
    end_day = f"{end_date[8]}{end_date[9]}"

    if western_bound <= 0:
        wsym = 'W'
    if western_bound > 0:
        wsym = 'E'
    if eastern_bound <= 0:
        esym = 'W'
    if eastern_bound > 0:
        esym = 'E'  
    if southern_bound >= 0:
        ssym = 'N'
    if southern_bound < 0:
        ssym = 'S'
    if northern_bound >= 0:
        nsym = 'N'
    if northern_bound < 0:
        nsym = 'S'

    western_bound = abs(western_bound)
    eastern_bound = abs(eastern_bound)
    southern_bound = abs(southern_bound)
    northern_bound = abs(northern_bound)

    if level_type == 'SURFACE GAUSS' or level_type == 'SFC GAUSS' or level_type == 'SURFACE' or level_type == 'SURFACE DATA':

        if os.path.exists(f"Climate Analysis Graphics"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}"):
            pass
    
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}/{dataset_type}"):
            pass
    
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}/{dataset_type}")
    
        path = f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}/{dataset_type}"
        path_print = f"f:Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}/{dataset_type}"

    else:

        if os.path.exists(f"Climate Analysis Graphics"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}"):
            pass
    
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}")
    
        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}/{dataset_type}"):
            pass
    
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}/{dataset_type}")

        if os.path.exists(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}/{dataset_type}/{level}"):
            pass
    
        else:
            os.mkdir(f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}/{dataset_type}/{level}")
    
        path = f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}/{dataset_type}/{level}"
        path_print = f"f:Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}/{dataset_type}/{level}"

    return path, path_print


def prism_file_directory(dtype, region, variable, year, month, day, resolution, normal_type, reference_system):

    """
    This function builds the file structure for the PRISM Climate Data Graphics

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

    7) resolution (String) - 4km or 800m. 

    8) normal_type (String) - Daily or Monthly normals. 

    9) reference_system (String) - Default = 'States & Counties'. The georgraphical reference system with respect to the borders on the map. 
        
        Reference Systems:

        1) 'States & Counties'
        2) 'States Only'
        3) 'GACC Only'
        4) 'GACC & PSA'
        5) 'CWA Only'
        6) 'NWS CWAs & NWS Public Zones'
        7) 'NWS CWAs & NWS Fire Weather Zones'
        8) 'NWS CWAs & Counties'
        9) 'GACC & PSA & NWS Fire Weather Zones'
        10) 'GACC & PSA & NWS Public Zones'
        11) 'GACC & PSA & NWS CWA'
        12) 'GACC & PSA & Counties'
        13) 'GACC & Counties'

    Returns 
    -------
    
    1) The file path where the graphics will save to. 
    """

    dtype = dtype.upper()
    region = region.upper()
    variable = variable.upper()
    resolution = resolution.upper() 
    normal_type = normal_type.upper()
    reference_system = reference_system.upper()

    if os.path.exists(f"Climate Analysis Graphics"):
        pass
    else:
        os.mkdir(f"Climate Analysis Graphics")

    if os.path.exists(f"Climate Analysis Graphics/PRISM"):
        pass
    else:
        os.mkdir(f"Climate Analysis Graphics/PRISM")

    if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}"):
        pass
    else:
        os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}")

    if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}"):
        pass
    else:
        os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}")

    if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}"):
        pass
    else:
        os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}")

    if dtype == 'DAILY':

        if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}")

        if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}")

        if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{day}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{day}")

        if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{day}/{resolution}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{day}/{resolution}")

        if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{day}/{resolution}/{reference_system}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{day}/{resolution}/{reference_system}")

        path = f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{day}/{resolution}/{reference_system}"
        path_print = f"f:Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{day}/{resolution}/{reference_system}"

    if dtype == 'MONTHLY':

        if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}")

        if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}")

        if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{resolution}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{resolution}")

        if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{resolution}/{reference_system}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{resolution}/{reference_system}")

        path = f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{resolution}/{reference_system}"
        path_print = f"f:Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{resolution}/{reference_system}"

    if dtype == 'NORMALS':

        if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}"):
            pass
        else:
            os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}")

        if normal_type == 'MONTHLY':
        
            if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{resolution}"):
                pass
            else:
                os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{resolution}")
        
            if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{resolution}/{normal_type}"):
                pass
            else:
                os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{resolution}/{normal_type}")
    
            if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{resolution}/{normal_type}/{reference_system}"):
                pass
            else:
                os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{resolution}/{normal_type}/{reference_system}")
    
            path = f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{resolution}/{normal_type}/{reference_system}"
            path_print = f"f:Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{resolution}/{normal_type}/{reference_system}"

        if normal_type == 'DAILY':
            if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{day}"):
                pass
            else:
                os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{day}") 

            if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{day}/{resolution}"):
                pass
            else:
                os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{day}/{resolution}")

            if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{day}/{resolution}/{normal_type}"):
                pass
            else:
                os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{day}/{resolution}/{normal_type}")

            if os.path.exists(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{day}/{resolution}/{normal_type}/{reference_system}"):
                pass
            else:
                os.mkdir(f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{day}/{resolution}/{normal_type}/{reference_system}")

            path = f"Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{day}/{resolution}/{normal_type}/{reference_system}"
            path_print = f"f:Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{month}/{day}/{resolution}/{normal_type}/{reference_system}"
            

    return path, path_print



























