"""
This file hosts the coordinates for the different regions in the United States. 

(C) Meteorologist Eric J. Drewitz
"""

import warnings
warnings.filterwarnings('ignore')

def get_cwa_coords(cwa):

    """
    This function returns the coordinate bounds for the Alaska NWS CWAs

    Required Arguments:

    1) cwa (String) **For Alaska Only as of the moment** The NWS CWA abbreviation. 

    Returns: Coordinate boundaries in decimal degrees
    """

    if cwa == None:
        wb, eb, sb, nb = [-170, -128, 50, 75]
    if cwa == 'AER' or cwa == 'aer':
        wb, eb, sb, nb = [-155, -140.75, 55.5, 64.5]
    if cwa == 'ALU' or cwa == 'alu':
        wb, eb, sb, nb = [-170, -151, 52, 62.9]
    if cwa == 'AJK' or cwa == 'ajk':
        wb, eb, sb, nb = [-145, -129.5, 54, 60.75]
    if cwa == 'AFG' or cwa == 'afg':
        wb, eb, sb, nb = [-170, -140.75, 59, 72]

    return wb, eb, sb, nb

def get_region_info(region):

    region = region

    if region == 'CONUS' or region == 'conus':
        western_bound = -126
        eastern_bound = -66
        southern_bound = 24
        northern_bound = 50.5  
        shrink = 0.375
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'CA' or region == 'ca':
        western_bound = -124.61
        eastern_bound = -113.93
        southern_bound = 32.4
        northern_bound = 42.5
        shrink = 0.8
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5


    if region == 'AK' or region == 'ak':
        western_bound = -170
        eastern_bound = -130
        southern_bound = 50
        northern_bound = 75      
        shrink = 0.55
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5


    if region == 'AER' or region == 'aer':
        western_bound = -155
        eastern_bound = -140.75
        southern_bound = 55.5
        northern_bound = 64     
        shrink = 0.5
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5


    if region == 'ALU' or region == 'alu':
        western_bound = -170
        eastern_bound = -151
        southern_bound = 52
        northern_bound = 63      
        shrink = 0.5
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'AJK' or region == 'ajk':
        western_bound = -145
        eastern_bound = -129.5
        southern_bound = 54
        northern_bound = 60.75      
        shrink = 0.375
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'AFG' or region == 'afg':
        western_bound = -170
        eastern_bound = -140.75
        southern_bound = 60
        northern_bound = 75      
        shrink = 0.425
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'HI' or region == 'hi':
        western_bound = -160.3
        eastern_bound = -154.73
        southern_bound = 18.76
        northern_bound = 22.28
        shrink = 0.55
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'ME' or region == 'me':       
        western_bound = -71.2
        eastern_bound = -66.75
        southern_bound = 42.2
        northern_bound = 47.6  
        shrink = 1
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 7
        stamp_fontsize = 6

    if region == 'NH' or region == 'nh':
        western_bound = -72.65
        eastern_bound = -70.60
        southern_bound = 42.35
        northern_bound = 45.36
        shrink = 1
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.725, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'VT' or region == 'vt':
        western_bound = -73.50
        eastern_bound = -71.44
        southern_bound = 42.5
        northern_bound = 45.10
        shrink = 1
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.725, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'MA' or region == 'ma':
        western_bound = -73.55
        eastern_bound = -69.88
        southern_bound = 41.3
        northern_bound = 42.92
        shrink = 0.375
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'RI' or region == 'ri':
        western_bound = -71.86
        eastern_bound = -71.11
        southern_bound = 41.2
        northern_bound = 42.03
        shrink = 0.925
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.725, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'CT' or region == 'ct':
        western_bound = -73.74
        eastern_bound = -71.77
        southern_bound = 40.8
        northern_bound = 42.06
        shrink = 0.55
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'NJ' or region == 'nj':
        western_bound = -75.60
        eastern_bound = -73.5
        southern_bound = 38.45
        northern_bound = 41.37
        shrink = 1
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.725, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'DE' or region == 'de':
        western_bound = -76
        eastern_bound = -74.5
        southern_bound = 38.2
        northern_bound = 39.9
        shrink = 0.925
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.725, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'NY' or region == 'ny':
        western_bound = -79.85
        eastern_bound = -71.85
        southern_bound = 40.3
        northern_bound = 45.08
        shrink = 0.5
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'PA' or region == 'pa':
        western_bound = -80.6
        eastern_bound = -74.6
        southern_bound = 39.25
        northern_bound = 42.32
        shrink = 0.45
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'OH' or region == 'oh':
        western_bound = -84.9
        eastern_bound = -80.4
        southern_bound = 37.75
        northern_bound = 42.0
        shrink = 0.8
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'MI' or region == 'mi':
        western_bound = -90.5
        eastern_bound = -82.31
        southern_bound = 40.6
        northern_bound = 48.26
        shrink = 0.8
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'MN' or region == 'mn':
        western_bound = -97.45
        eastern_bound = -89.28
        southern_bound = 42.85
        northern_bound = 49.45
        shrink = 0.7
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'WI' or region == 'wi':
        western_bound = -93.1
        eastern_bound = -86.68
        southern_bound = 41.8
        northern_bound = 47.11
        shrink = 0.7
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'IA' or region == 'ia':
        western_bound = -96.77
        eastern_bound = -90
        southern_bound = 39.9
        northern_bound = 43.7
        shrink = 0.475
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'IN' or region == 'in':
        western_bound = -88.19
        eastern_bound = -84.69
        southern_bound = 37.1
        northern_bound = 41.79
        shrink = 1
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.715, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'MO' or region == 'mo':
        western_bound = -95.9
        eastern_bound = -88.92
        southern_bound = 35.8
        northern_bound = 40.66
        shrink = 0.6
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'IL' or region == 'il':
        western_bound = -91.67
        eastern_bound = -87.44
        southern_bound = 36.3
        northern_bound = 42.55
        shrink = 1
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.725, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'ND' or region == 'nd':
        western_bound = -104.2
        eastern_bound = -96.47
        southern_bound = 45.3
        northern_bound = 49.1
        shrink = 0.425
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'SD' or region == 'sd':
        western_bound = -104.14
        eastern_bound = -96.3
        southern_bound = 42.12
        northern_bound = 46.15
        shrink = 0.45
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'NE' or region == 'ne':
        western_bound = -104.14
        eastern_bound = -95.25
        southern_bound = 39.3
        northern_bound = 43.1
        shrink = 0.375
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'MD' or region == 'md':
        western_bound = -79.52
        eastern_bound = -74.97
        southern_bound = 37.9
        northern_bound = 39.79
        shrink = 0.365
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'VA' or region == 'va':
        western_bound = -83.77
        eastern_bound = -75.15
        southern_bound = 35.7
        northern_bound = 39.53
        shrink = 0.375
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'SC' or region == 'sc':
        western_bound = -83.46
        eastern_bound = -78.35
        southern_bound = 31.4
        northern_bound = 35.25
        shrink = 0.625
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'KY' or region == 'ky':
        western_bound = -89.64
        eastern_bound = -81.86
        southern_bound = 35.8
        northern_bound = 39.24
        shrink = 0.375
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'WV' or region == 'wv':
        western_bound = -82.68
        eastern_bound = -77.61
        southern_bound = 36.5
        northern_bound = 40.72
        shrink = 0.715
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'NC' or region == 'nc':
        western_bound = -84.4
        eastern_bound = -75.35
        southern_bound = 33
        northern_bound = 37
        shrink = 0.375
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'NV' or region == 'nv':
        western_bound = -120.15
        eastern_bound = -113.92
        southern_bound = 34.91
        northern_bound = 42.09
        shrink = 1
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.725, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'FL' or region == 'fl':
        western_bound = -87.71
        eastern_bound = -79.77
        southern_bound = 24.44
        northern_bound = 31.08
        shrink = 0.715
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5
        
    if region == 'OR' or region == 'or':
        western_bound = -125
        eastern_bound = -116.25
        southern_bound = 41.3
        northern_bound = 46.36
        shrink = 0.5
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'WA' or region == 'wa':
        western_bound = -125
        eastern_bound = -116.9
        southern_bound = 44.8
        northern_bound = 49.1
        shrink = 0.45
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'ID' or region == 'id':
        western_bound = -117.4
        eastern_bound = -110.97
        southern_bound = 41.2
        northern_bound = 49.1
        shrink = 1
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.725, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'GA' or region == 'ga':
        western_bound = -85.8
        eastern_bound = -80.68
        southern_bound = 29.8
        northern_bound = 35.05
        shrink = 0.875
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.725, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'AL' or region == 'al':
        western_bound = -88.75
        eastern_bound = -84.77
        southern_bound = 29.5
        northern_bound = 35.05
        shrink = 1
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.69, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'MS' or region == 'ms':
        western_bound = -91.82
        eastern_bound = -87.95
        southern_bound = 29.65
        northern_bound = 35.05
        shrink = 1
        x1, y1 = 0.01, -0.01
        x2, y2 = 0.69, -0.01
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'LA' or region == 'la':
        western_bound = -94.24
        eastern_bound = -88.85
        southern_bound = 28.4
        northern_bound = 33.13
        shrink = 0.715
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'AR' or region == 'ar':
        western_bound = -94.81
        eastern_bound = -89.48
        southern_bound = 32.4
        northern_bound = 36.58
        shrink = 0.675
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'TX' or region == 'tx':
        western_bound = -106.95
        eastern_bound = -93.28
        southern_bound = 24.9
        northern_bound = 36.71
        shrink = 0.715
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'OK' or region == 'ok':
        western_bound = -103.18
        eastern_bound = -94.26
        southern_bound = 33.5
        northern_bound = 37.2
        shrink = 0.34
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'NM' or region == 'nm':
        western_bound = -109.24
        eastern_bound = -102.89
        southern_bound = 30.3
        northern_bound = 37.1
        shrink = 0.9
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'AZ' or region == 'az':
        western_bound = -115.05
        eastern_bound = -108.94
        southern_bound = 30.7
        northern_bound = 37.1
        shrink = 0.9
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'UT' or region == 'ut':
        western_bound = -114.2
        eastern_bound = -108.97
        southern_bound = 36.2
        northern_bound = 42.1
        shrink = 1
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'CO' or region == 'co':
        western_bound = -109.2
        eastern_bound = -101.93
        southern_bound = 36.4
        northern_bound = 41.1
        shrink = 0.55
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'WY' or region == 'wy':
        western_bound = -111.1
        eastern_bound = -103.95
        southern_bound = 40.4
        northern_bound = 45.07
        shrink = 0.55
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'MT' or region == 'mt':
        western_bound = -116.22
        eastern_bound = -103.93
        southern_bound = 43.4
        northern_bound = 49.1
        shrink = 0.375
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'KS' or region == 'ks':
        western_bound = -102.16
        eastern_bound = -94.51
        southern_bound = 36.3
        northern_bound = 40.11
        shrink = 0.4
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'TN' or region == 'tn':
        western_bound = -90.37
        eastern_bound = -81.57
        southern_bound = 34.2
        northern_bound = 36.75
        shrink = 0.25
        x1, y1 = 0.01, -0.05
        x2, y2 = 0.725, -0.04
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'OSCC' or region == 'oscc' or region == 'SOPS' or region == 'sops':
        western_bound = -122.1
        eastern_bound = -113.93
        southern_bound = 32.4
        northern_bound = 39.06
        shrink = 0.7
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5
        
    if region == 'ONCC' or region == 'oncc' or region == 'NOPS' or region == 'nops':
        western_bound = -124.8
        eastern_bound = -119.1
        southern_bound = 35.9
        northern_bound = 42.15
        shrink = 0.9
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'GBCC' or region == 'gbcc' or region == 'GB' or region == 'gb':
        western_bound = -120.5
        eastern_bound = -107.47
        southern_bound = 33
        northern_bound = 46.4
        shrink = 0.9
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'NRCC' or region == 'nrcc' or region == 'NR' or region == 'nr':
        western_bound = -117.7
        eastern_bound = -96
        southern_bound = 41.5
        northern_bound = 50
        shrink = 0.325
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'RMCC' or region == 'rmcc' or region == 'RM' or region == 'rm':
        western_bound = -111.3
        eastern_bound = -94.2
        southern_bound = 35.2
        northern_bound = 46.8
        shrink = 0.6
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'SWCC' or region == 'swcc' or region == 'SW' or region == 'sw':
        western_bound = -114.89
        eastern_bound = -101.7
        southern_bound = 30.2
        northern_bound = 38
        shrink = 0.5
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'SACC' or region == 'sacc' or region == 'SE' or region == 'se':
        western_bound = -106.88
        eastern_bound = -74.7
        southern_bound = 23.5
        northern_bound = 39.65
        shrink = 0.4
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'EACC' or region == 'eacc' or region == 'E' or region == 'e':
        western_bound = -97.35
        eastern_bound = -66.18
        southern_bound = 33.5
        northern_bound = 49.65
        shrink = 0.425
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'PNW' or region == 'pnw' or region == 'NWCC' or region == 'nwcc' or region == 'NW' or region == 'nw':
        western_bound = -125
        eastern_bound = -116.25
        southern_bound = 41
        northern_bound = 49.1
        shrink = 0.75
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'CONUS & South Canada & North Mexico':
        western_bound, eastern_bound, southern_bound, northern_bound = -140, -45, 20, 65
        shrink = 0.4
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5

    if region == 'Canada' or region == 'canada':
        western_bound, eastern_bound, southern_bound, northern_bound = -141.5, -51, 41, 85
        shrink = 0.4
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.725, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5
        
    if region == 'NA' or region == 'na' or region == 'North America' or region == 'north america':
        western_bound, eastern_bound, southern_bound, northern_bound = -180, -51, 20, 85
        shrink = 0.4
        x1, y1 = 0.01, -0.03
        x2, y2 = 0.68, -0.025
        x3, y3 = 0.01, 0.01
        signature_fontsize = 6
        stamp_fontsize = 5
        
    return western_bound, eastern_bound, southern_bound, northern_bound, x1, y1, x2, y2, x3, y3, signature_fontsize, stamp_fontsize, shrink
