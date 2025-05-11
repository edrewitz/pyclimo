import sys
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
  print("ERROR: User is running a version of Python older than Python 3\nTo use PyClimo, the user must be using Python 3 or newer.")

setup(
    name = "pyclimo",
    version = "1.0",
    packages = find_packages(),
    install_requires=[
        "matplotlib>=3.7",
        "metpy>=1.5.1",
        "numpy>=1.24",
        "pandas>=2.2",
        "xarray>=2023.1.0",
        "netcdf4>=1.7.1",
        "cartopy>=0.21.0",
        "xeofs>=3.0.4",
        "rasterio>=1.4.3",
        "pytz>=2024.1"
      
    ],
    author="Eric J. Drewitz",
    description="An Open Source Package For Climate Analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"

)
