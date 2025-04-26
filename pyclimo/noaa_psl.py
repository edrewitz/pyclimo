import xeofs as xe
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as md
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import cmaps

from dateutil import tz
from time_funcs import get_timezone_abbreviation, get_timezone, plot_creation_time
from noaa_psl_data import get_psl_netcdf
from calc import celsius_to_fahrenheit, roundup, rounddown, mm_to_in
from file_funcs import noaa_psl_directory

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

def plot_titles(variable, level_type):

    if level_type == 'surface gauss' or level_type == 'sfc gauss':
        titles = {
            'air':'2-METER TEMPERATURE',
    
        }
    return titles


def plot_period_mean_eof1_eof2(variable, level_type, western_bound, eastern_bound, southern_bound, northern_bound, start_date, end_date, globe=False, to_fahrenheit=True, shrink=1):


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
    
    path, path_print = noaa_psl_directory(variable, level_type, western_bound, eastern_bound, southern_bound, northern_bound, start_date, end_date)

    ds = get_psl_netcdf(variable, level_type, western_bound, eastern_bound, southern_bound, northern_bound, start_date, end_date)

    model = xe.single.EOF(use_coslat=True)
    model.fit(ds, dim="time")
    model.explained_variance_ratio()
    components = model.components()
    scores = model.scores()
    avg = ds.mean(dim='time')

    if variable == 'air':
        avg[variable] = avg[variable] - 273.15
        #mean_levels = np.arange(np.nanmin(avg[variable]), (np.nanmax(avg[variable])+0.5), 0.5)
        #eof_levels = np.arange(np.nanmin(components[variable]), (np.nanmax(components[variable])+1), 1)
        #mean_ticks = mean_levels[::5]
        #eof_ticks = eof_levels[::5]
        mean_cmap = cmaps.temperature_colormap()
        eof_cmap = cmaps.temperature_change_colormap()
        if to_fahrenheit == True:
            avg[variable] = celsius_to_fahrenheit(avg[variable])
            mean_levels = np.arange(np.nanmin(avg[variable]), (np.nanmax(avg[variable])+1), 1)
            unit = '[°F]'
        else:
            unit = '[°C]'
    else:
        pass

    title = plot_titles(variable, level_type)
    title = title[variable]

    for i in range(0, (len(components['mode'])+1)):
        
        fig = plt.figure(figsize=(12,12))
        fig.set_facecolor('aliceblue')
        ax = fig.add_subplot(1, 1, 1, projection=mapcrs)
        ax.set_extent([western_bound, eastern_bound, southern_bound, northern_bound], datacrs)
        ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
        ax.add_feature(cfeature.LAND, color='beige', zorder=1)
        ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
        ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
        ax.add_feature(provinces, linewidth=1, zorder=1)   
        ax.add_feature(cfeature.STATES, linewidth=0.25, zorder=6)
    
        if i == 0:
            fname = f"MEAN {title} {unit}"
            plt.title(f"MEAN {title} {unit}", fontsize=8, fontweight='bold', loc='left')
            plt.title(f"PERIOD OF RECORD: {start_date} - {end_date}", fontsize=7, fontweight='bold', loc='right')
            cs = ax.contourf(avg['lon'], avg['lat'], avg[variable][:, :], transform=datacrs, cmap=mean_cmap)
            cbar = cbar = fig.colorbar(cs, shrink=shrink, pad=0.01, location='right')
            fig.savefig(f"{path}/{fname}", bbox_inches='tight')
            plt.close(fig)
            print(f"Saved {fname} to {path_print}")   
        if i == 1:
            fname = f"EOF1 {title}"
            plt.title(f"EOF1 {title}", fontsize=8, fontweight='bold', loc='left')
            plt.title(f"PERIOD OF RECORD: {start_date} - {end_date}", fontsize=7, fontweight='bold', loc='right')
            cs = ax.contourf(components['lon'], components['lat'], components['air'][0, :, :], transform=datacrs, cmap=eof_cmap)
            cbar = fig.colorbar(cs, shrink=shrink, pad=0.01, location='right')
            fig.savefig(f"{path}/{fname}", bbox_inches='tight')
            plt.close(fig)
            print(f"Saved {fname} to {path_print}")   
        if i == 2:
            fname = f"EOF2 {title}"
            plt.title(f"EOF2 {title}", fontsize=8, fontweight='bold', loc='left')
            plt.title(f"PERIOD OF RECORD: {start_date} - {end_date}", fontsize=7, fontweight='bold', loc='right')
            cs = ax.contourf(components['lon'], components['lat'], components['air'][1, :, :], transform=datacrs, cmap=eof_cmap) 
            cbar = fig.colorbar(cs, shrink=shrink, pad=0.01, location='right')
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

        ax.plot(scores['time'], scores[i, :], color='black')
        ax.fill_between(scores['time'], 0, scores[i, :], color='red', where=(scores[i, :] > 0), alpha=0.3)
        ax.fill_between(scores['time'], scores[i, :], 0, color='blue', where=(scores[i, :] < 0), alpha=0.3)
        fig.savefig(f"{path}/{fname}", bbox_inches='tight')
        plt.close(fig)
        print(f"Saved {fname} to {path_print}")  
        e = e + 1
        

    
