# -*- coding: utf-8 -*-
"""
Get data from https://rtdata.dtcc.com/gtr/ 

inspecting source on https://rtdata.dtcc.com/gtr/ points us to

https://kgc0418-tdw-data-0.s3.amazonaws.com/gtr/static/gtr/html/CUMULATIVE_SLICE_GRID.html for cumulative slice reports i.e. daily reports

and https://kgc0418-tdw-data-0.s3.amazonaws.com/gtr/static/gtr/html/GENERAL_SLICE_GRID.html for intraday slices by the minute

We start with daily RATES reports and inspect further to see that we can find the data (.zip files) in
sourceFile="../../../../slices/CUMULATIVE_RATES_SLICE.HTML"


NOTE!! FUTERE is moved to -> NOTE  future https://pddata.dtcc.com/gtr/         !!!
Same drill
-> https://kgc0418-tdw-data-0.s3.amazonaws.com/gtr/static/gtr/html/CUMULATIVE_SLICE_GRID_CAN.html
-> sourceFile="../../../../ca/eod/CA_CUMULATIVE_RATES.HTML"

"""

import pandas as pd
import urllib
from zipfile import ZipFile
from io import BytesIO


url = "https://kgc0418-tdw-data-0.s3.amazonaws.com/ca/eod/CA_CUMULATIVE_RATES_2020_12_10.zip"


# The file name is formatted as 'CA CUMULATIVE RATES YYYY MM DD.zip'
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)

zipfile = ZipFile(BytesIO(resp.read()))

# Zip file contains one file, so we simply grab the first in the 'list'
file = zipfile.namelist()[0]

# Open zip file and read csv file to Pandas dataframe
df = pd.read_csv(zipfile.open(file))

# From here we can do whatever we want with the data:
# Save to DB
# Filter to get specific trades fx. USD IRS or XCCY swaps
# Particularly interesting is Fwd starting XCCY as its typically fast money 