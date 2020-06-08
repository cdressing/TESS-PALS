import requests
url = 'https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv'
r = requests.get(url, allow_redirects=True) 
open('All Rows (CSV)', 'wb').write(r.content) #this downloads and saves the file to wherever this notebook is saved
r.status_code #200 means the request was successful, 404 indicates an unsuccessful request

import pandas as pd
pd.set_option('display.max_columns', 100)
data = pd.read_csv("All Rows (CSV)")
exofop = pd.DataFrame(data)

P_Insol = exofop['Planet Insolation (Earth Flux)']
exofop.loc[(P_Insol >= 0.5) & (P_Insol <= 1.5)]

E_Rad = exofop['Planet Radius (R_Earth)']
exofop.loc[(E_Rad >= 0.5) & (E_Rad <= 2.5)]

exofop.loc[(P_Insol >= 0.5) & (P_Insol <= 1.5) & (E_Rad >= 0.5) & (E_Rad <= 2.5)]