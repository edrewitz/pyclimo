# PyClimo

<img width="200" height="150" alt="climate" src="https://github.com/edrewitz/PyClimo/blob/main/climate.jpg?raw=true"> ![image](https://github.com/user-attachments/assets/da1b43c0-2b6a-4a5c-9eb4-f08b30cab42b)

A climate data analysis data visualization package. 

# Table of Contents

[Documentation](https://github.com/edrewitz/pyclimo/blob/main/README.md#documentation)

[Jupyter Lab Examples]()

[Citations](https://github.com/edrewitz/pyclimo/blob/main/README.md#citations)

# Documentation

1) [plot_ncar_reanalysis_data_period_mean_eof1_eof2()]()


### plot_ncar_reanalysis_data_period_mean_eof1_eof2()

This function plots NCAR Reanalysis netCDF4 data from the NOAA Physical Science Laboratory. 

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

Returns
1) A plot of the mean value for the variable for the period. 
2) A plot showing EOF1 for the variable for the period. 
3) A plot showing EOF2 for the variable for the period. 
4) A plot showing EOF1 score time series for the variable for the period.
5) A plot showing EOF2 score time series for the variable for the period.



### Citations

MetPy: May, R. M., Goebbert, K. H., Thielen, J. E., Leeman, J. R., Camron, M. D., Bruick, Z., Bruning, E. C., Manser, R. P., Arms, S. C., and Marsh, P. T., 2022: MetPy: A Meteorological Python Library for Data Analysis and Visualization. Bull. Amer. Meteor. Soc., 103, E2273-E2284, https://doi.org/10.1175/BAMS-D-21-0125.1.

xarray: Hoyer, S., Hamman, J. (In revision). Xarray: N-D labeled arrays and datasets in Python. Journal of Open Research Software.

cartopy: Phil Elson, Elliott Sales de Andrade, Greg Lucas, Ryan May, Richard Hattersley, Ed Campbell, Andrew Dawson, Bill Little, Stephane Raynaud, scmc72, Alan D. Snow, Ruth Comer, Kevin Donkers, Byron Blay, Peter Killick, Nat Wilson, Patrick Peglar, lgolston, lbdreyer, … Chris Havlin. (2023). SciTools/cartopy: v0.22.0 (v0.22.0). Zenodo. https://doi.org/10.5281/zenodo.8216315

NumPy: Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2. (Publisher link).

Pandas: McKinney, W., & others. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51–56).

xeofs: Rieger, N. & Levang, S. J. (2024). xeofs: Comprehensive EOF analysis in Python with xarray. Journal of Open Source Software, 9(93), 6060. DOI: https://doi.org/10.21105/joss.06060

georasters: Ozak, E. (2021). georasters: Geographic Raster functionality for Python using osgeo and GDAL (Version 0.5.29) 

