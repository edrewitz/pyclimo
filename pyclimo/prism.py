import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as md
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import pandas as pd
import pyclimo.cmaps as cmaps
import warnings
warnings.filterwarnings('ignore')

from metpy.plots import USCOUNTIES
from datetime import datetime, timedelta
from pyclimo.geometry import get_shapes, get_geo_json 
from pyclimo.file_funcs import prism_file_directory
from dateutil import tz
from pyclimo.time_funcs import get_timezone_abbreviation, get_timezone, plot_creation_time
from pyclimo.coords import get_cwa_coords, get_region_info
from pyclimo.prism_data import get_geotiff_data
from pyclimo.calc import roundup, rounddown, round_to_quarter

mpl.rcParams['font.weight'] = 'bold'
props = dict(boxstyle='round', facecolor='wheat', alpha=1)

mpl.rcParams['xtick.labelsize'] = 9
mpl.rcParams['ytick.labelsize'] = 9

provinces = cfeature.NaturalEarthFeature(category='cultural', 
    name='admin_1_states_provinces_lines', scale='50m', facecolor='none', edgecolor='k')

datacrs = ccrs.PlateCarree()
mapcrs = ccrs.PlateCarree()

local_time, utc_time = plot_creation_time()
timezone = get_timezone_abbreviation()
tzone = get_timezone()
from_zone = tz.tzutc()
to_zone = tz.tzlocal()


def plot_prism_data(dtype, variable, year, month, day, normal_type, clear_data_in_folder=True, to_fahrenheit=True, to_inches=True, western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=1, county_border_linewidth=0.25, gacc_border_linewidth=1, psa_border_linewidth=0.5, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.25, nws_public_zones_linewidth=0.25, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', region='conus', x1=0.01, y1=-0.03, x2=0.725, y2=-0.025, x3=0.01, y3=0.01, cwa=None, signature_fontsize=6, stamp_fontsize=5, shrink=0.7, custom_geojson=False, geojson_path=None, reference_system_label=None, custom_border_color='black', custom_border_linewidth=1):

    """
    This function downloads and plots PRISM Climate Data and saves the graphics to a folder. 
    If the folder does not exist, the function will build the new directory. 

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
       
       Additional Variables For Normals Only at 800m resolution:
       - solclear = Total daily global shortwave solar radiation received on a horizontal surface under clear sky conditions [averaged over all days in the month] 
       - solslope = Total daily global shortwave solar radiation received on a sloped surface [averaged over all days in the month] 
       - soltotal = Total daily global shortwave solar radiation received on a horizontal surface [averaged over all days in the month] 
       - soltrans = Atmospheric transmittance (cloudiness) [monthly average daily soltotal/monthly average daily solclear]

    3) year (String) - Year
       Daily Data goes back to 1981
       Monthly Data goes back to 1895

    4) month (String) - 2 digit abbreviation for month (MM)

    5) day (String) - For daily data only - 2 digit abbreviation for day (DD)
       If the user wants to use monthly data instead of daily data, pass a value of None for the variable day. 

    6) normal_type (String) - Daily or Monthly normals.

    Optional Arguments:

    1) clear_data_in_folder (Boolean) - Default=True - When set to True, the user will clear all old data in the f:PRISM Data folder. 
       When set to False, the old data will remain un-touched and archived in the f:PRISM Data folder. 

    2) to_fahrenheit (Boolean) - Default = True. When set to True, if the user is plotting a temperature based parameter, the values will convert to Fahrenheit. 
       When set to False, the values will remain in Celsius. 

    3) to_inches (Boolean) - Default = True. When set to True, if the user is plotting precipitation, the values will convert to inches. 
       When set to False, the values will remain in mm. 

    4) western_bound (Integer or Float) - Default = None. Western extent of the plot in decimal degrees. 
       The default setting is None. If set to None, the user must select a state or gacc_region. 
       This setting should be changed from None to an integer or float value if the user wishes to
       have a custom area selected. Negative values denote the western hemisphere and positive 
       values denote the eastern hemisphere. 

    5) eastern_bound (Integer or Float) - Default = None. Eastern extent of the plot in decimal degrees. 
       The default setting is None. If set to None, the user must select a state or gacc_region. 
       This setting should be changed from None to an integer or float value if the user wishes to
       have a custom area selected. Negative values denote the western hemisphere and positive 
       values denote the eastern hemisphere. 

    6) southern_bound (Integer or Float) - Default = None. Southern extent of the plot in decimal degrees. 
       The default setting is None. If set to None, the user must select a state or gacc_region. 
       This setting should be changed from None to an integer or float value if the user wishes to
       have a custom area selected. Positive values denote the northern hemisphere and negative 
       values denote the southern hemisphere. 

    7) northern_bound (Integer or Float) - Default = None. Northern extent of the plot in decimal degrees. 
       The default setting is None. If set to None, the user must select a state or gacc_region. 
       This setting should be changed from None to an integer or float value if the user wishes to
       have a custom area selected. Positive values denote the northern hemisphere and negative 
       values denote the southern hemisphere.

    8) reference_system (String) - Default = 'States & Counties'. The georgraphical reference system with respect to the borders on the map. If the user
        wishes to use a reference system not on this list, please see items 8-14. 
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
                           

    9) show_state_borders (Boolean) - If set to True, state borders will display. If set to False, state borders will not display. 
        Default setting is False. Users should change this value to False if they wish to hide state borders. 

    10) show_county_borders (Boolean) - If set to True, county borders will display. If set to False, county borders will not display. 
        Default setting is False. Users should change this value to False if they wish to hide county borders. 

    11) show_gacc_borders (Boolean) - If set to True, GACC (Geographic Area Coordination Center) borders will display. If set to False, GACC borders will not display. 
        Default setting is False. Users should change this value to True if they wish to display GACC borders. 

    12) show_psa_borders (Boolean) - If set to True, PSA (Predictive Services Area) borders will display. If set to False, PSA borders will not display. 
        Default setting is False. Users should change this value to True if they wish to display PSA borders.

    13) show_cwa_borders (Boolean) - If set to True, CWA borders will display. If set to False, CWA borders will not display. 
        Default setting is False. Users should change this value to True if they wish to display CWA borders.

    14) show_nws_firewx_zones (Boolean) - If set to True, NWS FWZ borders will display. If set to False, NWS FWZ borders will not display. 
        Default setting is False. Users should change this value to True if they wish to display NWS FWZ borders.

    15) show_nws_public_zones (Boolean) - If set to True, NWS Public Zone borders will display. If set to False, NWS Public Zone borders will not display. 
        Default setting is False. Users should change this value to True if they wish to display NWS Public Zone borders.

    16) state_border_linewidth (Integer) - Linewidth (thickness) of the state borders. Default setting is 2. 

    17) county_border_linewidth (Integer) - Linewidth (thickness) of the county borders. Default setting is 1. 

    18) gacc_border_linewidth (Integer) - Linewidth (thickness) of the GACC borders. Default setting is 2. 

    19) psa_border_linewidth (Integer) - Linewidth (thickness) of the PSA borders. Default setting is 1. 

    20) state_border_linestyle (String) - Linestyle of the state borders. Default is a solid line. 
        To change to a dashed line, users should set state_border_linestyle='--'. 

    21) county_border_linestyle (String) - Linestyle of the county borders. Default is a solid line. 
        To change to a dashed line, users should set county_border_linestyle='--'. 

    22) gacc_border_linestyle (String) - Linestyle of the GACC borders. Default is a solid line. 
        To change to a dashed line, users should set gacc_border_linestyle='--'. 

    23) psa_border_linestyle (String) - Linestyle of the PSA borders. Default is a solid line. 
        To change to a dashed line, users should set psa_border_linestyle='--'. 

    24) cwa_border_linestyle (String) - Linestyle of the CWA borders. Default is a solid line. 
        To change to a dashed line, users should set psa_border_linestyle='--'. 

    25) nws_firewx_zones_linestyle (String) - Linestyle of the NWS FWZ borders. Default is a solid line. 
        To change to a dashed line, users should set psa_border_linestyle='--'. 

    26) nws_public_zones_linestyle (String) - Linestyle of the NWS Public Zone borders. Default is a solid line. 
        To change to a dashed line, users should set psa_border_linestyle='--'. 

    27) region (String) - The two letter state abbreviation or four letter GACC Region abbreviation for the region the user wishes to make the graphic for. 
        If the user wishes to make a graphic for the entire CONUS, there are 4 acceptable abbreviations: 'US' or 'us'
        or 'USA' or 'usa'. Example: If the user wishes to make a plot for the state of California both 'CA' or 'ca' are
        acceptable. Default setting is 'us'. If the user wishes to make a plot based on gacc_region, this value must be 
        changed to None. 

        Here is a list of acceptable GACC Regions abbreviations:

        South Ops: 'OSCC' or 'oscc' or 'SOPS' or 'sops'
        
        North Ops: 'ONCC' or 'oncc' or 'NOPS' or 'nops'
        
        Great Basin: 'GBCC' or 'gbcc' or 'GB' or 'gb'
        
        Northern Rockies: 'NRCC' or 'nrcc' or 'NR' or 'nr'
        
        Rocky Mountain: 'RMCC' or 'rmcc' or 'RM' or 'rm'
        
        Southwest: 'SWCC' or 'swcc' or 'SW' or 'sw'
        
        Southern: 'SACC' or 'sacc' or 'SE' or 'se'
        
        Eastern: 'EACC' or 'eacc' or 'E' or 'e'
        
        Pacific Northwest: 'PNW' or 'pnw' or 'NWCC' or 'nwcc' or 'NW' or 'nw'
        
        Alaska: Setting state='AK' or state='ak' suffices here. Leave gacc_region=None and set the state variable as shown. 

    28) x1 (Float) - Default = 0.01. The x-position of the signature text box with respect to the axis of the image. 

    29) y1 (Float) - Default = -0.03. The y-position of the signature text box with respect to the axis of the image. 

    30) x2 (Float) - Default = 0.725. The x-position of the timestamp text box with respect to the axis of the image.

    31) y2 (Float) - Default = -0.025. The y-position of the timestamp text box with respect to the axis of the image.

    32) x3 (Float) - Default = 0.01. The x-position of the reference system text box with respect to the axis of the image.

    33) y3 (Float) - Default = 0.01. The y-position of the reference system text box with respect to the axis of the image.

    34) cwa (String) - *For Alaska only* - The 3-letter abbreviation for the National Weather Service CWA. 
        For a view of the entire state - set cwa=None. 

        NWS CWA Abbreviations:

        1) AER - NWS Anchorage East Domain
        
        2) ALU - NWS Anchorage West Domain
        
        3) AJK - NWS Juneau
        
        4) AFG - NWS Fairbanks        

    35) signature_fontsize (Integer) - Default = 6. The fontsize of the signature. This is only to be changed when making a custom plot. 

    36) stamp_fontsize (Integer) - Default = 5. The fontsize of the timestamp and reference system text. This is only to be changed when making a custom plot. 

    37) shrink (Integer or Float) - Default = 0.7. This is how the colorbar is sized to the figure. 
            This is a feature of matplotlib, as per their definition, the shrink is:
            "Fraction by which to multiply the size of the colorbar." 
            This should only be changed if the user wishes to change the size of the colorbar. 
            Preset values are called from the settings module for each state and/or gacc_region.

    38) custom_geojson (Boolean) - Default = False. When set to True, the user can import a geojson file locally hosted on their PC. This is used when
        the user wants to use custom boundaries not found in pyclimo or geometries hosted in a geojson file that the user wishes to remain internal. 

    39) geojson_path (String) - Default = None. The complete path to the geojson file on the user's computer. 

    40) reference_system_label (String) - Default = None. The name of the reference system if the user wishes to use a custom reference system. 

    41) custom_border_color (String) - Default='black'. The color of the border of the custom boundaries (the geometries in the locally hosted geojson).

    42) custom_border_linewidth (Integer) - Default = 1. The linewidth of the border of the custom boundaries (the geometries in the locally hosted geojson).
    

    Returns
    -------

    An graphic showing the analysis of PRISM Data saved to a path. 
    
    If the user is plotting monthly data, the path will be:

    f:Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{resolution}/{normal_type}/{reference_system}

    If the user is plotting daily data, the path will be:

    f:Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{day}/{resolution}/{normal_type}/{reference_system}    
    """

    PSAs = get_shapes(f"PSA Shapefiles/National_PSA_Current.shp")
    
    GACC = get_shapes(f"GACC Boundaries Shapefiles/National_GACC_Current.shp")
    
    CWAs = get_shapes(f"NWS CWA Boundaries/w_05mr24.shp")
    
    FWZs = get_shapes(f"NWS Fire Weather Zones/fz05mr24.shp")
    
    PZs = get_shapes(f"NWS Public Zones/z_05mr24.shp")

    if month == '01':
        mon = 'JAN'
    if month == '02':
        mon = 'FEB'
    if month == '03':
        mon = 'MAR'
    if month == '04':
        mon = 'APR'
    if month == '05':
        mon = 'MAY'
    if month == '06':
        mon = 'JUN'
    if month == '07':
        mon = 'JUL'
    if month == '08':
        mon = 'AUG'
    if month == '09':
        mon = 'SEP'
    if month == '10':
        mon = 'OCT'
    if month == '11':
        mon = 'NOV'
    if month == '12':
        mon = 'DEC'

    if custom_geojson == True:
        shapes = get_geo_json(geojson_path)
    else:
        pass
    

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':

        reference_system_label = reference_system
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if region == 'CONUS' or region == 'conus':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if region == 'CONUS' or region == 'conus':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if region == 'CONUS' or region == 'conus':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if region == 'CONUS' or region == 'conus':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if region == 'CONUS' or region == 'conus':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if region == 'CONUS' or region == 'conus':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if region == 'CONUS' or region == 'conus':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if region == 'CONUS' or region == 'conus':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if region == 'CONUS' or region == 'conus':
                county_border_linewidth=0.25   

    path, path_print = prism_file_directory(dtype, 'us', variable, year, month, day, '4km', normal_type, reference_system_label)

    fname = f"{variable.upper()}.png"

    try:
        western_bound, eastern_bound, southern_bound, northern_bound, x1, y1, x2, y2, x3, y3, signature_fontsize, stamp_fontsize, shrink = get_region_info(region)
        if region == 'NH' or region == 'nh' or region == 'VT' or region == 'vt' or region == 'NJ' or region == 'nj' or region == 'IN' or region == 'in' or region == 'IL' or region == 'il' or region == 'ID' or region == 'id' or region == 'AL' or region == 'al' or region == 'MS' or region == 'ms':
            western_bound = western_bound - 0.5
            eastern_bound = eastern_bound + 0.5
        if cwa != None:
            western_bound, eastern_bound, southern_bound, northern_bound = get_cwa_coords(cwa)
        else:
            pass

    except Exception as e:
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        x1=x1
        y1=y1
        x2=x2
        y2=y2
        x3=x3
        y3=y3
        shrink=shrink

    df = get_geotiff_data(dtype, variable, year, month, day, normal_type, clear_data_in_folder, to_fahrenheit, to_inches)

    df = df[df['longitude'] <= eastern_bound] 
    df = df[df['longitude'] >= western_bound] 
    df = df[df['latitude'] >= southern_bound]
    df = df[df['latitude'] <= northern_bound]
        
    lon = df['longitude']
    lat = df['latitude']
    var = df[variable]

    if variable == 'tmax' or variable == 'tmean' or variable == 'tmin':
        cmap = cmaps.temperature_colormap()
        vmin = int(round(np.nanmin(var),0))
        vmax = int(round(np.nanmax(var),0))
        levels = np.arange(rounddown(vmin), (roundup(vmax) + 1), 1)
        if vmin >= 0:
            variance = vmax - vmin
        else:
            variance = vmax + vmin
        if variance >= 30:
            ticks = levels[::5]
        elif variance >= 15 and variance < 30:
            ticks = levels[::5]
        else:
            ticks = levels[::5]

        if variable == 'tmax':
            title_var = 'Maximum Temperature'
        if variable == 'tmean':
            title_var = 'Mean Temperature'
        if variable == 'tmin':
            title_var = 'Minimum Temperature'
        if dtype == 'Normals' or dtype == 'normals':
            if to_fahrenheit == True:
                title_left = f"{normal_type.upper()} {title_var.upper()} [°F] 30-Year (1991-2020) Normal"
            else:
                title_left = f"{normal_type.upper()} {title_var.upper()} [°C] 30-Year (1991-2020) Normal"
            if normal_type == 'Daily' or normal_type == 'daily':
                title_right = f"Valid: {mon}-{day}"
            if normal_type == 'Monthly' or normal_type == 'monthly':
                title_right = f"Valid: {mon}"
        if dtype == 'Daily' or dtype == 'daily':
            if to_fahrenheit == True:
                title_left = f"{title_var.upper()} [°F]"
            else:
                title_left = f"{title_var.upper()} [°C]"
            title_right = f"Valid: {year}-{mon}-{day}"              
        if dtype == 'Monthly' or dtype == 'monthly':
            if to_fahrenheit == True:
                title_left = f"{title_var.upper()} [°F]"
            else:
                title_left = f"{title_var.upper()} [°C]"
            title_right = f"Valid: {year}-{mon}" 
                
    elif variable == 'tdmean':
        var = celsius_to_fahrenheit(var)
        cmap = cmaps.dew_point_colormap()
        vmin = int(round(np.nanmin(var),0))
        vmax = int(round(np.nanmax(var),0))
        levels = np.arange(rounddown(vmin), (roundup(vmax) + 1), 1)
        variance = vmax - vmin
        if variance > 30:
            ticks = levels[::5]
        else:
            ticks = levels[::1]
        title_var = 'Mean Dew Point Temperature'
        if dtype == 'Daily' or dtype == 'daily':
            if to_fahrenheit == True:
                title_left = f"{title_var.upper()} [°F]"
            else:
                title_left = f"{title_var.upper()} [°C]"
            title_right = f"Valid: {year}-{mon}-{day}"               
        if dtype == 'Monthly' or dtype == 'monthly':
            if to_fahrenheit == True:
                title_left = f"{title_var.upper()} [°F]"
            else:
                title_left = f"{title_var.upper()} [°C]"
            title_right = f"Valid: {year}-{mon}" 
        if dtype == 'Normals' or dtype == 'normals':
            if to_fahrenheit == True:
                title_left = f"{normal_type.upper()} {title_var.upper()} [°F] 30-Year (1991-2020) Normal"
            else:
                title_left = f"{normal_type.upper()} {title_var.upper()} [°C] 30-Year (1991-2020) Normal"
            if normal_type == 'Daily' or normal_type == 'daily':
                title_right = f"Valid: {mon}-{day}"
            if normal_type == 'Monthly' or normal_type == 'monthly':
                title_right = f"Valid: {mon}"

    elif variable == 'ppt':
        cmap = cmaps.precipitation_colormap()
        vmin = 0
        vmax = int(round_to_quarter(np.nanmax(var)))
        levels = np.arange(vmin, (vmax + 0.01), 0.01)
        ticks = levels[::100]
        title_var = 'Total Precipitation'
        if dtype == 'Daily' or dtype == 'daily':
            if to_inches == True:
                title_left = f"{title_var.upper()} [IN]"
            else:
                title_left = f"{title_var.upper()} [MM]"
            title_right = f"Valid: {year}-{mon}-{day}"               
        if dtype == 'Monthly' or dtype == 'monthly':
            if to_inches == True:
                title_left = f"{title_var.upper()} [IN]"
            else:
                title_left = f"{title_var.upper()} [MM]"
            title_right = f"Valid: {year}-{mon}" 
        if dtype == 'Normals' or dtype == 'normals':
            if to_inches == True:
                title_left = f"{normal_type.upper()} {title_var.upper()} [IN] 30-Year (1991-2020) Normal"
            else:
                title_left = f"{normal_type.upper()} {title_var.upper()} [MM] 30-Year (1991-2020) Normal"
            if normal_type == 'Daily' or normal_type == 'daily':
                title_right = f"Valid: {mon}-{day}"
            if normal_type == 'Monthly' or normal_type == 'monthly':
                title_right = f"Valid: {mon}"

    elif variable == 'vpdmax' or variable == 'vpdmin':
        cmap = cmaps.vapor_pressure_deficit_colormap()
        vmin = int(round(np.nanmin(var),0))
        vmax = int(round(np.nanmax(var),0))
        levels = np.arange(vmin, (vmax + 1), 1)
        ticks = levels[::10]
        if variable == 'vpdmax':
            title_var = 'Maximum Vapor Pressure Deficit'
        if variable == 'vpdmin':
            title_var = 'Minimum Vapor Pressure Deficit'
        if dtype == 'Daily' or dtype == 'daily':
            title_left = f"{title_var.upper()} [hPa]"
            title_right = f"Valid: {year}-{mon}-{day}"               
        if dtype == 'Monthly' or dtype == 'monthly':
            title_left = f"{title_var.upper()} [hPa]"
            title_right = f"Valid: {year}-{mon}" 
        if dtype == 'Normals' or dtype == 'normals':
            title_left = f"{normal_type.upper()} {title_var.upper()} [hPa] 30-Year (1991-2020) Normal"
            if normal_type == 'Daily' or normal_type == 'daily':
                title_right = f"Valid: {mon}-{day}"
            if normal_type == 'Monthly' or normal_type == 'monthly':
                title_right = f"Valid: {mon}"

    fig = plt.figure(figsize=(12,12))
    fig.set_facecolor('aliceblue')
    ax = fig.add_subplot(1, 1, 1, projection=mapcrs)
    ax.set_extent([western_bound, eastern_bound, southern_bound, northern_bound], datacrs)
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    ax.add_feature(provinces, linewidth=1, zorder=1)

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass  
    if custom_geojson == True:
        ax.add_geometries(shapes, crs=datacrs, facecolor='none', edgecolor=custom_border_color, linewidth=custom_border_linewidth)

    plt.title(f"{title_left}", fontsize=8, fontweight='bold', loc='left')
    
    plt.title(f"{title_right}", fontsize=7, fontweight='bold', loc='right')

    ax.text(x1, y1, "Plot Created With PyClimo (C) Eric J. Drewitz " +utc_time.strftime('%Y')+" | Data Source: PRISM Climate Group: prism.oregonstate.edu", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', bbox=props)
    ax.text(x2, y2, "Image Created: " + local_time.strftime(f'%m/%d/%Y %H:%M {timezone}') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=stamp_fontsize, fontweight='bold', bbox=props)
    ax.text(x3, y3, "Reference System: "+reference_system_label, transform=ax.transAxes, fontsize=stamp_fontsize, fontweight='bold', bbox=props, zorder=11)  

    cs = ax.scatter(lon, lat, c=var, cmap=cmap, alpha=0.5, transform=datacrs, vmin=vmin, vmax=vmax)

    cbar = fig.colorbar(cs, shrink=shrink, pad=0.01, location='right', ticks=ticks)

    fig.savefig(f"{path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {path_print}")  









