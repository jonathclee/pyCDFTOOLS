#!/usr/bin/env python3

"""
Collection of routines to analyse and process NEMO data, using the xgcm
formalism to a certain extent (via the xnemogcm interface).

Default loads numpy, xarray, some things from xgcm

Routines aim to mirror the CDFTOOLS/NEMO variable naming conventions up to a 
point. 
"""

# default module loads

import numpy as np
import xarray as xr

