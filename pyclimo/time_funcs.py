import pytz 

try:
    from datetime import datetime, timedelta, UTC
except Exception as e:
    from datetime import datetime, timedelta
from dateutil import tz

def get_timezone_abbreviation():

    """
    This function returns the current timezone abbreviation from the computer's date/time settings.
    Example: Pacific Standard Time = PST
    """
    now = datetime.now()
    timezone = now.astimezone().tzinfo
    capital_letters = ""
    for char in str(timezone):
        if char.isupper():
            capital_letters += char
            
    return capital_letters

def get_timezone():

    """
    This function returns the correct timezone abbreviation of the timezone at which the user is in. 

    Required Arguments: None

    Returns: The timezone abbreviation as a string 
    """

    now = datetime.now()
    timezone = now.astimezone().tzinfo

    return timezone
    


def plot_creation_time():

    """
    This function uses the datetime module to find the time at which the script ran. 

    This can be used in many ways:
    1) Timestamp for graphic in both local time and UTC
    2) When downloading data with functions in the data_access module, this function is called to find 
       the time which is passed into the data downloading functions in order for the latest data to be
       downloaded. 

    There are no variables to pass into this function. 

    Returns: 1) Current Local Time
             2) Current UTC Time
            
    """

    now = datetime.now()
    UTC = now.astimezone(pytz.utc)
    
    sec = now.second
    mn = now.minute
    hr = now.hour
    dy = now.day
    mon = now.month
    yr = now.year
    
    sec1 = UTC.second
    mn1 = UTC.minute
    hr1 = UTC.hour
    dy1 = UTC.day
    mon1 = UTC.month
    yr1 = UTC.year
    
    Local_Time_Now = datetime(yr, mon, dy, hr, mn, sec)
    UTC_Now = datetime(yr1, mon1, dy1, hr1, mn1, sec1)
    
    return Local_Time_Now, UTC_Now
