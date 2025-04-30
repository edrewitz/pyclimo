import os

def noaa_psl_directory(variable, level_type, western_bound, eastern_bound, southern_bound, northern_bound, start_date, end_date):


    variable = variable.upper()
    level_type = level_type.upper()
    
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

    path = f"Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}"
    path_print = f"f:Climate Analysis Graphics/NOAA PSL/{variable}/{level_type}/{western_bound}{wsym}_{eastern_bound}{esym}_{northern_bound}{nsym}_{southern_bound}{ssym}/{start_year}_{start_month}_{start_day}_to_{end_year}_{end_month}_{end_day}"

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

    Returns: The file path where the graphics will save to. 
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



























