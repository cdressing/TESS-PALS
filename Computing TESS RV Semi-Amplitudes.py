import requests
url = 'https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv'
r = requests.get(url, allow_redirects=True) 
open('All Rows (CSV)', 'wb').write(r.content) #this downloads and saves the file to wherever this notebook is saved
r.status_code #200 means the request was successful, 404 indicates an unsuccessful request

import pandas as pd
pd.set_option('display.max_columns', 100)
data = pd.read_csv("All Rows (CSV)")
exofop = pd.DataFrame(data)

#make sure you have astroquery pip installed before running this code

#Need to import stellar mass values from other source
#import astroquery.mast catalogs
from astroquery.mast import Catalogs
#Make list of TIC IDs to pull from the catalog
TICID_list = (exofop['TIC ID']).tolist()
#pull the data for the TIC ID's that are also in EXOFOP
catalog_data = Catalogs.query_criteria(catalog='Tic',objType='STAR', ID = TICID_list)
#Turn it into panda df
catalog_data_df = catalog_data.to_pandas()
#Only pull the masses and IDs since that's all I need
catalog_data_df2 = catalog_data_df[['ID','mass']]

OP = exofop['Period (days)']
M_sol = catalog_data_df2['mass']
#assume e = 0
#sin(i) = 1
#M2 = 1/317.8
#M1 >> M2
RV = 28.4329 * (1/317.8) * (M_sol)**(-2/3) * (OP / 365.25)**(-1/3)

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize = (8, 8))
plt.hist(RV[np.isfinite(RV)], color = 'green', bins = np.linspace(0, 1, 50))
plt.axvline(x=.3, color = 'red', linestyle = '--', label = 'representative detection limit')
plt.legend(fontsize = 14)
plt.xlabel('RV Semi-Amplitude (m/s)', fontsize = 15)
plt.ylabel('Count', fontsize = 15)
plt.ylim(0, 110)
plt.tick_params(labelsize = 12)
plt.title('TOI RV Semi-Amplitude Distribution', fontsize = 18)
plt.savefig('TOI Semi-Amplitude Distribution.png')