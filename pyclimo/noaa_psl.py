"""
This file has functions that plot the netCDF4 data from the NOAA Physical Sciences Laboratory.

This file is written by: Eric J. Drewitz
"""

import xeofs as xe
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as md
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import pyclimo.cmaps as cmaps
import warnings
warnings.filterwarnings('ignore')

from dateutil import tz
from cartopy.util import add_cyclic_point
from pyclimo.time_funcs import get_timezone_abbreviation, get_timezone, plot_creation_time
from pyclimo.noaa_psl_data import get_psl_netcdf
from pyclimo.calc import celsius_to_fahrenheit, roundup, rounddown, mm_to_in
from pyclimo.file_funcs import noaa_psl_directory

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

def get_level_index(level):

    """
    This function returns the index for a specific pressure level
    """

    index = {

        '1000':0,
        '925':1,
        '850':2,
        '700':3,
        '600':4,
        '500':5,
        '400':6,
        '300':7,
        '250':8,
        '200':9,
        '150':10,
        '100':11,
        '70':12,
        '50':13,
        '30':14,
        '20':15,
        '10':16

    }

    return index


def plot_titles(variable, level_type):

    """
    This function returns the plot title corresponding to the variable. 
    """

    if level_type == 'pressure' or level_type == 'pressure level':
        titles = {
            'air':'TEMPERATURE',
            'hgt':'GEOPOTENTIAL HEIGHT',
            'rhum':'RELATIVE HUMIDITY',
            'omega':'VERTICAL VELOCITY',
            'uwnd':'U-WIND',
            'vwnd':'V-WIND'

        }

    if level_type == 'surface gauss' or level_type == 'sfc gauss':
        titles = {
            'air':'2-METER TEMPERATURE',
            'skt':'SKIN TEMPERATURE',
            'prate':'PRECIPITATION RATE',
            'lhtfl':'LATENT HEAT FLUX',
            'shtfl':'SENSIBLE HEAT FLUX',
            'uwnd':'10-METER U-WIND',
            'vwnd':'10-METER V-WIND',
            'cfnlf':'CLOUD FORCING NET LONGWAVE FLUX',   
        }

    if level_type == 'surface' or level_type == 'surface data':
        titles = {
        'pr_wtr':'PRECIPITABLE WATER',
        'slp':'SEA LEVEL PRESSURE',
        'pres':'SURFACE PRESSURE',
        'air':'0.995 SIGMA TEMPERATURE',
        'omega':'0.995 SIGMA VERTICAL VELOCITY',
        'pottmp':'0.995 SIGMA POTENTIAL TEMPERATURE',
        'rhum':'0.995 SIGMA RELATIVE HUMIDITY',
        'uwnd':'0.995 SIGMA U-WIND',
        'vwnd':'0.995 SIGMA V-WIND',
        'lftx':'SURFACE LIFTING INDEX'
        }
        
    return titles


def plot_ncar_reanalysis_data_period_mean_eof1_eof2(variable, level_type, western_bound, eastern_bound, southern_bound, northern_bound, start_date, end_date, globe=False, to_fahrenheit=True, shrink=1, x1=0.01, y1=-0.03, x2=0.725, y2=-0.025, y3=-0.05, signature_fontsize=6, stamp_fontsize=5, level='500', hemispheric_view=False, hemisphere='N'):

    """
    This function plots NCAR Reanalysis netCDF4 data from the NOAA Physical Science Laboratory. 

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
    -------
    1) A plot of the mean value for the variable for the period. 
    2) A plot showing EOF1 for the variable for the period. 
    3) A plot showing EOF2 for the variable for the period. 
    4) A plot showing EOF1 score time series for the variable for the period.
    5) A plot showing EOF2 score time series for the variable for the period. 
    """

    if globe == True:
        western_bound = -180
        eastern_bound = 180
        southern_bound = -90
        northern_bound = 90
    else:
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound

    if hemispheric_view == True:

        if hemisphere == 'N':
            mapcrs = ccrs.NorthPolarStereo()
            western_bound = -180
            eastern_bound = 180
            southern_bound = 25
            northern_bound = 90
            shrink = 0.85
        
        if hemisphere == 'S':
            mapcrs = ccrs.SouthPolarStereo()
            western_bound = -180
            eastern_bound = 180
            southern_bound = -90
            northern_bound = -25
            shrink = 0.85
    else:
        mapcrs = ccrs.PlateCarree()
    
    path, path_print = noaa_psl_directory(variable, level_type, western_bound, eastern_bound, southern_bound, northern_bound, start_date, end_date, 'NCAR Reanalysis', level)

    ds = get_psl_netcdf(variable, level_type, western_bound, eastern_bound, southern_bound, northern_bound, start_date, end_date)

    level_idx = get_level_index(level)
    level_idx = level_idx[level]

    model = xe.single.EOF(use_coslat=True)
    model.fit(ds[variable], dim="time")
    model.explained_variance_ratio()
    components = model.components()
    scores = model.scores()
    avg = ds[variable].mean(dim='time')      
    
    eof_cmap = cmaps.eof_colormap_1()

    if variable == 'air' or variable == 'skt':
        avg = avg - 273.15
        mean_cmap = cmaps.temperature_colormap()
        extend = 'both'
        if to_fahrenheit == True:
            avg = celsius_to_fahrenheit(avg)
            minima = int(round(np.nanmin(avg), -1))
            maxima = int(round(np.nanmax(avg), -1))
            mean_levels = np.arange(minima, (maxima + 1), 1)
            mean_ticks = mean_levels[::5]
            unit = '[°F]'
            funit = '[°F]'
        else:
            unit = '[°C]'
            funit = '[°C]'
            mean_levels = np.arange(np.nanmin(avg), (np.nanmax(avg)+0.5), 0.5)
            mean_ticks = mean_levels[::5]
    else:
        pass

    if variable == 'pottmp':
        mean_cmap = cmaps.temperature_colormap()
        minima = np.nanmin(avg)
        maxima = np.nanmax(avg)
        top = maxima + 1
        mean_levels = np.arange(minima, top, 1)
        mean_ticks = mean_levels[::5]
        extend = 'both'
        unit = '[K]'
        funit = '[K]'

    if variable == 'lftx':
        mean_cmap = cmaps.vertical_velocity_colormap()
        minima = int(round(np.nanmin(avg),0))
        maxima = int(round(np.nanmax(avg),0))
        top = maxima + 1
        mean_levels = np.arange(minima, top, 1)
        mean_ticks = mean_levels[::5]
        extend = 'both'
        unit = '[Value]'
        funit = '[Value]'

    if variable == 'rhum':
        mean_cmap = cmaps.relative_humidity_colormap()
        eof_cmap = cmaps.eof_colormap_2()
        mean_levels = np.arange(0, 101, 1)
        mean_ticks = mean_levels[::5]
        extend = 'neither'
        unit = '[%]'
        funit = '[%]'

    if variable == 'prate':
        mean_cmap = cmaps.relative_humidity_colormap()
        eof_cmap = cmaps.eof_colormap_2()
        avg = avg * 3600
        maxima = np.nanmax(avg)
        top = maxima + 0.01
        mean_levels = np.arange(0, top, 0.01)
        mean_ticks = mean_levels[::5]
        extend = 'max'
        unit = '[mm*hr^-1]'
        funit = '[mmhr^-1]'

    if variable == 'pr_wtr':
        mean_cmap = cmaps.relative_humidity_colormap()
        eof_cmap = cmaps.eof_colormap_2()
        maxima = np.nanmax(avg)
        top = maxima + 1
        mean_levels = np.arange(0, top, 1)
        mean_ticks = mean_levels[::5]
        extend = 'max'
        unit = '[mm]'
        funit = '[mm]'

    if variable == 'slp' or variable == 'pres':
        avg = avg/100
        mean_cmap = cmaps.temperature_colormap()
        minima = int(round(np.nanmin(avg), -1))
        maxima = int(round(np.nanmax(avg), -1))
        mean_levels = np.arange(minima, (maxima + 1), 1)
        mean_ticks = mean_levels[::5] 
        unit = '[hPa]'
        funit = '[hPa]'
        extend = 'both'

    if variable == 'omega':
        mean_cmap = cmaps.vertical_velocity_colormap()
        minima = round(np.nanmin(avg), 2)
        maxima = round(np.nanmax(avg), 2)
        mean_levels = np.arange(minima, (maxima + 0.01), 0.01)
        mean_ticks = mean_levels[::5]
        unit = '[Pa*s^-1]'
        funit = '[Pas^-1]'
        extend = 'both'

    if variable == 'lhtfl' or variable == 'shtfl' or variable == 'cfnlf':
        mean_cmap = cmaps.vertical_velocity_colormap()
        minima = int(round(np.nanmin(avg), 0))
        maxima = int(round(np.nanmax(avg), 0))
        mean_levels = np.arange(minima, (maxima + 1), 1)
        if variable == 'lhtfl':
            mean_ticks = mean_levels[::10]
        elif variable == 'shtfl':
            mean_ticks = mean_levels[::20]
        else:
            mean_ticks = mean_levels[::5]
        unit = '[W*m^-2]'
        funit = '[Wm^-1]'
        extend = 'both'

    if variable == 'uwnd' or variable == 'vwnd':
        mean_cmap = cmaps.vertical_velocity_colormap()
        minima = int(round(np.nanmin(avg), 0))
        maxima = int(round(np.nanmax(avg), 0))
        mean_levels = np.arange(minima, (maxima + 1), 1)
        mean_ticks = mean_levels[::5]
        unit = '[m*s^-1]'
        funit = '[ms^-1]'
        extend = 'both'

    if variable == 'hgt':
        avg = (avg[level_idx, :, :])/10
        mean_cmap = cmaps.temperature_colormap()
        minima = int(round(np.nanmin(avg), -1))
        maxima = int(round(np.nanmax(avg), -1))
        mean_levels = np.arange(minima, (maxima + 1), 1)
        mean_ticks = mean_levels[::5] 
        unit = '[DM]'
        funit = '[DM]'
        extend = 'both'

    avg_lon = avg['lon']
    avg_lon_idx = avg.dims.index('lon')
    cyclic_avg, cyclic_avg_lon = add_cyclic_point(avg.values, coord=avg_lon, axis=avg_lon_idx)

    eofs_lon = components['lon']
    eofs_lon_idx = components.dims.index('lon')
    cyclic_eof, cyclic_eof_lon = add_cyclic_point(components, coord=eofs_lon, axis=eofs_lon_idx)

    title = plot_titles(variable, level_type)
    title = title[variable]

    for i in range(0, (len(components['mode'])+1)):
        
        fig = plt.figure(figsize=(12,12))
        fig.set_facecolor('aliceblue')
        ax = fig.add_subplot(1, 1, 1, projection=mapcrs)
        ax.set_extent([western_bound, eastern_bound, southern_bound, northern_bound], datacrs)
        ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
        ax.add_feature(cfeature.LAND, color='beige', zorder=1)
        ax.add_feature(cfeature.BORDERS, linestyle='-', zorder=2)
        ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
        ax.add_feature(cfeature.LAKES, color='black', zorder=1)
        ax.add_feature(provinces, linewidth=1, zorder=2)   
        ax.add_feature(cfeature.STATES, linewidth=0.25, zorder=2)
    
        if i == 0:
            if level_type == 'pressure' or level_type == 'pressure level':
                fname = f"MEAN {level} MB {title} {funit}.png"
                plt.title(f"MEAN {level} MB {title} {unit}", fontsize=8, fontweight='bold', loc='left')
            else:
                fname = f"MEAN {title} {funit}.png"
                plt.title(f"MEAN {title} {unit}", fontsize=8, fontweight='bold', loc='left')
            plt.title(f"PERIOD OF RECORD: {start_date} - {end_date}", fontsize=7, fontweight='bold', loc='right')
            ax.text(x1, y1, "Plot Created With PyClimo (C) Eric J. Drewitz " +utc_time.strftime('%Y')+" | Data Source: NOAA PSL: psl.noaa.gov", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', bbox=props)
            ax.text(x2, y2, "Image Created: " + local_time.strftime(f'%m/%d/%Y %H:%M {timezone}') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=stamp_fontsize, fontweight='bold', bbox=props)
            try:
                cs = ax.contourf(cyclic_avg_lon, avg['lat'], cyclic_avg[:, :], levels=mean_levels, transform=datacrs, cmap=mean_cmap, extend=extend)
            except Exception as e:
                cs = ax.contourf(cyclic_avg_lon, avg['lat'], cyclic_avg[level_idx, :, :], levels=mean_levels, transform=datacrs, cmap=mean_cmap, extend=extend)
            cbar = cbar = fig.colorbar(cs, shrink=shrink, pad=0.01, location='right', ticks=mean_ticks)
            fig.savefig(f"{path}/{fname}", bbox_inches='tight')
            plt.close(fig)
            print(f"Saved {fname} to {path_print}")   
        if i == 1:
            if level_type == 'pressure' or level_type == 'pressure level':
                fname = f"EOF1 {level} MB {title}.png"
                plt.title(f"EOF1 {level} MB {title}", fontsize=8, fontweight='bold', loc='left')
            else:
                fname = f"EOF1 {title}.png"
                plt.title(f"EOF1 {title}", fontsize=8, fontweight='bold', loc='left')
            plt.title(f"PERIOD OF RECORD: {start_date} - {end_date}", fontsize=7, fontweight='bold', loc='right')
            ax.text(x1, y1, "Plot Created With PyClimo (C) Eric J. Drewitz " +utc_time.strftime('%Y')+" | Data Source: NOAA PSL: psl.noaa.gov", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', bbox=props)
            ax.text(x2, y2, "Image Created: " + local_time.strftime(f'%m/%d/%Y %H:%M {timezone}') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=stamp_fontsize, fontweight='bold', bbox=props)
            try:
                cs = ax.contourf(cyclic_eof_lon, components['lat'], cyclic_eof[0, :, :], transform=datacrs, cmap=eof_cmap, extend='both')
            except Exception as e:
                cs = ax.contourf(cyclic_eof_lon, components['lat'], cyclic_eof[0, level_idx, :, :], transform=datacrs, cmap=eof_cmap, extend='both')
            fig.savefig(f"{path}/{fname}", bbox_inches='tight')
            plt.close(fig)
            print(f"Saved {fname} to {path_print}")   
        if i == 2:
            if level_type == 'pressure' or level_type == 'pressure level':
                fname = f"EOF2 {level} MB {title}.png"
                plt.title(f"EOF2 {level} MB {title}", fontsize=8, fontweight='bold', loc='left')
            else:
                fname = f"EOF2 {title}.png"
                plt.title(f"EOF2 {title}", fontsize=8, fontweight='bold', loc='left')
            plt.title(f"PERIOD OF RECORD: {start_date} - {end_date}", fontsize=7, fontweight='bold', loc='right')
            ax.text(x1, y1, "Plot Created With PyClimo (C) Eric J. Drewitz " +utc_time.strftime('%Y')+" | Data Source: NOAA PSL: psl.noaa.gov", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', bbox=props)
            ax.text(x2, y2, "Image Created: " + local_time.strftime(f'%m/%d/%Y %H:%M {timezone}') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=stamp_fontsize, fontweight='bold', bbox=props)
            try:
                cs = ax.contourf(cyclic_eof_lon, components['lat'], cyclic_eof[1, :, :], transform=datacrs, cmap=eof_cmap, extend='both')
            except Exception as e:
                cs = ax.contourf(cyclic_eof_lon, components['lat'], cyclic_eof[1, level_idx, :, :], transform=datacrs, cmap=eof_cmap, extend='both')
            fig.savefig(f"{path}/{fname}", bbox_inches='tight')
            plt.close(fig)
            print(f"Saved {fname} to {path_print}")   

    e = 1
    for i in range(0, len(scores['mode'])):

        fname = f"EOF{e} Scores.png"
        fig = plt.figure(figsize=(12,12))
        ax = fig.add_subplot(1, 1, 1)
        ax.xaxis.set_major_formatter(md.DateFormatter('%m-%d'))
        fig.set_facecolor('aliceblue')

        plt.title(f"EOF{e} SCORES", fontsize=12, fontweight='bold', loc='left')
        plt.title(f"PERIOD OF RECORD: {start_date} - {end_date}", fontsize=10, fontweight='bold', loc='right')
        ax.text(x1, y3, "Plot Created With PyClimo (C) Eric J. Drewitz " +utc_time.strftime('%Y')+" | Data Source: NOAA PSL: psl.noaa.gov", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', bbox=props)
        ax.text(x2, y3, "Image Created: " + local_time.strftime(f'%m/%d/%Y %H:%M {timezone}') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=stamp_fontsize, fontweight='bold', bbox=props)

        ax.plot(scores['time'], scores[i, :], color='black')

        if variable == 'rhum' or variable == 'prate' or variable == 'pr_wtr':
            c1 = 'lime'
            c2 = 'saddlebrown'
        else:
            c1 = 'red'
            c2 = 'blue'
        
        ax.fill_between(scores['time'], 0, scores[i, :], color=c1, where=(scores[i, :] > 0), alpha=0.3)
        ax.fill_between(scores['time'], scores[i, :], 0, color=c2, where=(scores[i, :] < 0), alpha=0.3)
        fig.savefig(f"{path}/{fname}", bbox_inches='tight')
        plt.close(fig)
        print(f"Saved {fname} to {path_print}")  
        e = e + 1
        
        

    
