# PyClimo

<img width="200" height="150" alt="climate" src="https://github.com/edrewitz/PyClimo/blob/main/climate.jpg?raw=true"> ![image](https://github.com/user-attachments/assets/da1b43c0-2b6a-4a5c-9eb4-f08b30cab42b)

An open source climate data analysis and visualization package. 

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pyclimo.svg)](https://anaconda.org/conda-forge/pyclimo)  ![PyPI](https://img.shields.io/pypi/v/pyclimo?label=pypi%20pyclimo) [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/pyclimo.svg)](https://anaconda.org/conda-forge/pyclimo) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/pyclimo/badges/latest_release_date.svg)](https://anaconda.org/conda-forge/pyclimo) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/pyclimo/badges/latest_release_relative_date.svg)](https://anaconda.org/conda-forge/pyclimo)  [![Anaconda-Server Badge](https://anaconda.org/conda-forge/pyclimo/badges/license.svg)](https://anaconda.org/conda-forge/pyclimo) 

[![Conda Recipe](https://img.shields.io/badge/recipe-pyclimo-green.svg)](https://anaconda.org/conda-forge/pyclimo) 
      <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=25671&branchName=main">
        <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/pyclimo-feedstock?branchName=main">


Anaconda Downloads:

[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pyclimo.svg)](https://anaconda.org/conda-forge/pyclimo)

 PIP Downloads:

 ![PyPI - Downloads](https://img.shields.io/pypi/dm/pyclimo)

# Table of Contents

[Documentation](https://github.com/edrewitz/pyclimo/blob/main/README.md#documentation)

[Jupyter Lab Examples](https://github.com/edrewitz/pyclimo/blob/main/README.md#jupyter-lab-examples)

[Citations](https://github.com/edrewitz/pyclimo/blob/main/README.md#citations)

# Jupyter Lab Examples

1) **Winter 2024-2025 500 MB Geopotential Height Analysis**

   A first time user setup with analyzing NCAR Reanalysis data for 500mb geopotential heights for DJF 2024-2025 (Winter 2024-2025).
   
   In this example we will create 5 graphics showing the following:
   
   i) Mean 500 MB Geopotential Height for the period
   
   ii) EOF1 (1st Principle Component/1st Empirical Orthogonal Function) for the period
   
   iii) EOF2 (2nd Principle Component/2nd Empirical Orthogonal Function) for the period
   
   iv) EOF1 Scores for the period
   
   v) EOF2 Scores for the period

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/Examples/Winter_2024_2025_Analysis.ipynb) to view Example 1.
   
   Example 1 Graphics:

   1) [Mean 500mb Geopotential Height](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%201/MEAN%20500%20MB%20GEOPOTENTIAL%20HEIGHT%20%5BDM%5D.png)
   2) [EOF1 500mb Geopotential Height](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%201/EOF1%20500%20MB%20GEOPOTENTIAL%20HEIGHT.png)
   3) [EOF2 500mb Geopotential Height](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%201/EOF2%20500%20MB%20GEOPOTENTIAL%20HEIGHT.png)
   4) [EOF1 Scores](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%201/EOF1%20Scores.png)
   5) [EOF2 Scores](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%201/EOF2%20Scores.png)
  
2) **Plotting the Daily Normal Maximum Temperature for July 4th**

   In this example we will plot the daily normal for the maximum temperature for July 4th using the data from PRISM Climate Group.

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/Examples/July_4_prism_normals.ipynb) to view Example 2

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%202/TMAX.png) to view the graphic created in Example 2. 

3) **Plotting the Monthly Normal Maximum Vapor Pressure Deficit for August using the Geographic Area Coordination Center/Predictive Services Areas Reference System**

   In this example we will plot the monthly normal for the maximum vapor pressure Deficit for August using the 'GACC & PSA' reference system.

   This data is from PRISM Climate Group. 

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/Examples/August_prism_normals.ipynb) to view Example 3.

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%203/VPDMAX.png) to view the graphic created in Example 3. 

4) **Plotting the Daily Precipitation for October 30th, 2012**

   In this example, we will plot the daily precipitation for October 30th, 2012. This was the day Super Storm Sandy hit Long Island and New York City.

   This data is from PRISM Climate Group.

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/Examples/Sandy.ipynb) to view Example 4.

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%204/PPT.png) to view the graphic created in Example 4.

5) **Plotting the Mean Monthly Minimum Temperature for December 2017**

   In this example, we will plot the mean monthly minimum temperature for December 2017 using the data from PRISM Climate Group.

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/Examples/Dec2017.ipynb) to view Example 5.

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%205/TMIN.png) to view the graphic created in Example 5.

6) **Winter 2024-2025 Sea-Level Pressure Analysis Northern Hemispheric View**

   In this example we will create 5 graphics showing the following:
   
   i) Mean Sea-Level Pressure for the period
   
   ii) EOF1 (1st Principle Component/1st Empirical Orthogonal Function) for the period
   
   iii) EOF2 (2nd Principle Component/2nd Empirical Orthogonal Function) for the period
   
   iv) EOF1 Scores for the period
   
   v) EOF2 Scores for the period

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/Examples/Winter_2024_2025_Analysis_NH.ipynb) to view Example 6.

   Example 6 Graphics:

   1) [Mean Sea Level Pressure](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%206/MEAN%20SEA%20LEVEL%20PRESSURE%20%5BhPa%5D.png)
   2) [EOF1 Sea Level Pressure](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%206/EOF1%20SEA%20LEVEL%20PRESSURE.png)
   3) [EOF2 Sea Level Pressure](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%206/EOF2%20SEA%20LEVEL%20PRESSURE.png)
   4) [EOF1 Scores](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%206/EOF1%20Scores.png)
   5) [EOF2 Scores](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%206/EOF2%20Scores.png)
  
7) **Plotting the Monthly Normal Maximum Vapor Pressure Deficit for July using a Custom Reference System and Importing a Locally Hosted GeoJSON File**

   In this example we will plot the monthly normal for the maximum vapor pressure Deficit for July and use a custom reference system and give it a name for the image.

   We will also import a locally hosted GeoJSON file that has the geometry for the Southern California Edison (SCE) service area and overlay the SCE service area with counties. 

   This data is from PRISM Climate Group. 

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/Examples/July_prism_normals.ipynb) to view Example 7.

   [click here](https://github.com/edrewitz/PyClimo-Jupyter-Lab-Examples/blob/main/graphics/Example%207/VPDMAX.png) to view the graphic created in Example 7. 

# Documentation

1) [plot_ncar_reanalysis_data_period_mean_eof1_eof2()](https://github.com/edrewitz/pyclimo/blob/main/README.md#plot_ncar_reanalysis_data_period_mean_eof1_eof2)
2) [plot_prism_data()](https://github.com/edrewitz/pyclimo/blob/main/README.md#plot_prism_data)


### plot_ncar_reanalysis_data_period_mean_eof1_eof2()

This function plots NCAR Reanalysis netCDF4 data from the NOAA Physical Science Laboratory. 

The series of plots include:

i) Period Mean

ii) Spatial EOF1 

iii) Spatial EOF2

iv) EOF1 Scores

v) EOF2 Scores

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

Optional Arguments:

1) globe (Boolean) - Default = False. When set to True, the plot will be for the entire globe. 

2) to_fahrenheit (Boolean) - Default = True. When set to True, the air temperature (not potential temperature!!) will be convered to Fahrenheit. 
   When set to False, the air temperature will be in Celsius. 

3) shrink (Float) - Default = 1. This is how the colorbar is sized to the figure. 
   This is a feature of matplotlib, as per their definition, the shrink is:
   "Fraction by which to multiply the size of the colorbar." 
   This should only be changed if the user wishes to make a custom plot. 
   Preset values are called from the settings module for each region. 

4) x1 (Float) - Default = 0.01. The x-position of the signature text box with respect to the axis of the image. 

5) y1 (Float) - Default = -0.03. The y-position of the signature text box with respect to the axis of the image. 

6) x2 (Float) - Default = 0.725. The x-position of the timestamp text box with respect to the axis of the image.

7) y2 (Float) - Default = -0.025. The y-position of the timestamp text box with respect to the axis of the image.

8) y3 (Float) - Default = 0.01. The y-position of the reference system text box with respect to the axis of the image for the EOF Scores plots.

9) signature_fontsize (Integer) - Default = 6. The fontsize of the signature. This is only to be changed when making a custom plot. 

10) stamp_fontsize (Integer) - Default = 5. The fontsize of the timestamp and reference system text. This is only to be changed when making a custom plot. 

11) level (String) - Default = '500'. The pressure level in hPa. 
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

12) hemispheric_view (Boolean) - Default = False. When set to True, the view will be a Polar Stereographic of either the Northern or Southern Hemisphere.

13) hemisphere (String) - Default = 'N'. When set to 'N' the hemispheric view will be that of the Northern Hemisphere. Set to 'S' for Southern Hemisphere. 

Returns

1) A plot of the mean value for the variable for the period.

2) A plot showing EOF1 for the variable for the period. 

3) A plot showing EOF2 for the variable for the period. 

4) A plot showing EOF1 score time series for the variable for the period.

5) A plot showing EOF2 score time series for the variable for the period.


### plot_prism_data()

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

An graphic showing the analysis of PRISM Data saved to a path. 

If the user is plotting monthly data, the path will be:

f:Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{resolution}/{normal_type}/{reference_system}

If the user is plotting daily data, the path will be:

f:Climate Analysis Graphics/PRISM/{dtype}/{region}/{variable}/{year}/{month}/{day}/{resolution}/{normal_type}/{reference_system}    



### Citations

**MetPy**: May, R. M., Goebbert, K. H., Thielen, J. E., Leeman, J. R., Camron, M. D., Bruick, Z., Bruning, E. C., Manser, R. P., Arms, S. C., and Marsh, P. T., 2022: MetPy: A Meteorological Python Library for Data Analysis and Visualization. Bull. Amer. Meteor. Soc., 103, E2273-E2284, https://doi.org/10.1175/BAMS-D-21-0125.1.

**xarray**: Hoyer, S., Hamman, J. (In revision). Xarray: N-D labeled arrays and datasets in Python. Journal of Open Research Software.

**cartopy**: Phil Elson, Elliott Sales de Andrade, Greg Lucas, Ryan May, Richard Hattersley, Ed Campbell, Andrew Dawson, Bill Little, Stephane Raynaud, scmc72, Alan D. Snow, Ruth Comer, Kevin Donkers, Byron Blay, Peter Killick, Nat Wilson, Patrick Peglar, lgolston, lbdreyer, … Chris Havlin. (2023). SciTools/cartopy: v0.22.0 (v0.22.0). Zenodo. https://doi.org/10.5281/zenodo.8216315

**NumPy**: Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2. (Publisher link).

**Pandas**: McKinney, W., & others. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51–56).

**xeofs**: Rieger, N. & Levang, S. J. (2024). xeofs: Comprehensive EOF analysis in Python with xarray. Journal of Open Source Software, 9(93), 6060. DOI: https://doi.org/10.21105/joss.06060

**rasterio**: @software{gillies_2019,
  author =    {Sean Gillies and others},
  organization = {Mapbox},
  title =     {Rasterio: geospatial raster I/O for {Python} programmers},
  year =      {2013--},
  url = "https://github.com/rasterio/rasterio"
}

**geopandas**: Kelsey Jordahl, Joris Van den Bossche, Martin Fleischmann, Jacob Wasserman, James McBride, Jeffrey Gerard, … François Leblanc. (2020, July 15). geopandas/geopandas: v0.8.1 (Version v0.8.1). Zenodo. http://doi.org/10.5281/zenodo.3946761

**FireWxPy**: Eric J. Drewitz. (2025). edrewitz/firewxpy: FireWxPy v1.6.2 (FireWxPy1.6.2). Zenodo. https://doi.org/10.5281/zenodo.15620392
