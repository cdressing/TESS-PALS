#!/usr/bin/env python
# coding: utf-8

# !pip --version
# !pip install --upgrade pip

# !pip install PyQt5

# !pip install PyQtWebEngine

# In[1]:


import sys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from bs4.diagnose import diagnose
from bs4 import SoupStrainer
from urllib import request
import numpy as np
import scipy as sp
import requests
import time
import smtplib
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[2]:


request = request.urlopen('https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv')
TOI_csv = request.read()


# In[3]:


X = pd.read_csv('https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv')
X.iloc[:,2]
X


# In[4]:


X.columns


# In[20]:


columns_i_want = ['TIC ID', 'TOI',
       'TESS Mag', 'RA',
       'Dec', 'PM RA (mas/yr)', 'PM Dec (mas/yr)','Epoch (BJD)',
       'Period (days)', 'Duration (hours)', 'Depth (mmag)',
       'Depth (ppm)', 'Planet Radius (R_Earth)', 'Planet Insolation (Earth Flux)',
       'Planet Equil Temp (K)', 'Planet SNR', 'Stellar Distance (pc)', 'Stellar Eff Temp (K)',
        'Stellar log(g) (cm/s^2)', 'Stellar Radius (R_Sun)', 'Stellar Metallicity']
X_columned = X.loc[:,columns_i_want]
X_columned


# In[ ]:





# In[6]:


X.loc[1,:]


# In[ ]:





# In[7]:


wait = pd.DataFrame(X.loc[1,:])
wait["New"] = pd.Series(X.loc[2,:])
wait


# In[8]:


wait = pd.DataFrame(X.loc[1,:])
wait["New"] = pd.Series(X.loc[2,:])
#pd.pivot_table(wait, values=['1', "New"] columns = wait.index(0))


# In[9]:


test = pd.read_csv('https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv')
test_refined = test.loc[:,columns_i_want]

test2 = test[test['TESS Mag']>15]
test2_refined = test2.loc[:,columns_i_want]


# In[10]:


test_ids = test.set_index('TOI')
test2_ids = test2.set_index('TOI')
s1 = set(test_ids.index.tolist())
s2 = set(test2_ids.index.tolist())
removed = test_refined[test_refined['TOI'].isin(s1-s2)]
added = test2_refined[test2_refined['TOI'].isin(s2-s1)]
same = test_refined[test_refined['TOI'].isin(s2)]
len(s1)-len(removed)-len(same)


# In[11]:


duplicates = test_refined[test_refined.duplicated()]
duplicates


# In[12]:


#extract CSV Table
df = pd.read_csv('https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv').set_index('TIC ID')
    
#Slim table down
columns_i_want = ['TIC ID', 'TOI',
       'TESS Mag', 'TESS Mag err','RA',
       'Dec', 'PM RA (mas/yr)', 'PM RA err (mas/yr)', 'PM Dec (mas/yr)',
       'PM Dec err (mas/yr)', 'Epoch (BJD)', 'Epoch (BJD) err',
       'Period (days)', 'Period (days) err', 'Duration (hours)',
       'Duration (hours) err', 'Depth (mmag)', 'Depth (mmag) err',
       'Depth (ppm)', 'Depth (ppm) err', 'Planet Radius (R_Earth)',
       'Planet Radius (R_Earth) err', 'Planet Insolation (Earth Flux)',
       'Planet Equil Temp (K)', 'Planet SNR', 'Stellar Distance (pc)',
       'Stellar Distance (pc) err', 'Stellar Eff Temp (K)',
       'Stellar Eff Temp (K) err', 'Stellar log(g) (cm/s^2)',
       'Stellar log(g) (cm/s^2) err', 'Stellar Radius (R_Sun)',
       'Stellar Radius (R_Sun) err', 'Stellar Metallicity',
       ' Stellar Metallicity err', 'Sectors']
df_columned = df.loc[:,columns_i_want]
df_columned_indexed = df.set_index('TOI')
df_toi_set = set(df_columned_indexed.index.tolist())

while True:
    #Extract new table
    df2 = pd.read_csv('https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv')
    df2_columned = df2.loc[:,columns_i_want]
    df2_columned_indexed = df2_columned.set_index('TOI')
    df2_toi_set = set(df2_columned_indexed.index.tolist())
    
    removed = df_columned[df_columned['TOI'].isin(df_toi_set-df2_toi_set)]
    added = df2_columned[df2_columned['TOI'].isin(df2_toi_set-df_toi_set)]
    #establish difference between tables
    
    
    #Check if they have anything added or removed
    if len(removed) == 0 and len(added) ==0:
        time.sleep(60)
        continue
    else:
        
         # create an email message with just a subject line,
        msg = ('Check ExoFOP, data changed')
        # set the 'from' address
        fromaddress = 'holdenpals@berkeley.edu'
        # set the 'to' address
        toaddress  = ['hgill@berkeley.edu']
        
        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("holdenpals@gmail.com", "Holdenpals1!@#")
        
        #Tell me what changed
        print('Data added' + added)
        print('Data Removed' + removed)
        
        # send the email
        server.sendmail(fromaddress, toaddress, msg)
        # disconnect from the server
        server.quit()
        
        #Reestablish 'original' table
        df = pd.read_csv('https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv')
        df_columned = df.loc[:,columns_i_want]
        df_columned_indexed = df.set_index('TOI')
        df_toi_set = set(df_columned_indexed.index.tolist())
        break
        


# In[ ]:


# create an email message with just a subject line,
msg = ('Check ExoFOP, data changed')
# set the 'from' address
fromaddress = 'holdenpals@berkeley.edu'
# set the 'to' address
toaddress  = ['hgill@berkeley.edu']
        
# setup the email server,
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
# add my account login name and password,
server.login("holdenpals@gmail.com", "Holdenpals1!@#")
        
#Tell me what changed
print('Data added')
print('Data Removed')
        
# send the email
server.sendmail(fromaddress, toaddress, msg)
# disconnect from the server
server.quit()


# In[23]:


X_refined = X_columned[X_columned["Stellar Metallicity"].notnull()]
X_refined2 = X_refined[X_refined['Stellar Radius (R_Sun)'].notnull()]
X_refined3 = X_refined2[X_refined2['Planet Insolation (Earth Flux)'].notnull()]
X_refined4 = X_refined3[X_refined3['Planet Radius (R_Earth)'].notnull()]
X_refined5 = X_refined4[X_refined4['Planet Insolation (Earth Flux)']<1.5]



metallicity_index = X_refined4.set_index('Stellar Metallicity')
metallicity_list = metallicity_index.index.tolist()
stellar_rad_index = X_refined3.set_index('Stellar Radius (R_Sun)')
stellar_rad_list = stellar_rad_index.index.tolist()
plt.scatter(metallicity_list,stellar_rad_list)


# In[28]:


X_refined2 = X_columned[X_columned['Stellar Radius (R_Sun)'].notnull()]
X_refined3 = X_refined2[X_refined2['Planet Insolation (Earth Flux)'].notnull()]
X_refined4 = X_refined3[X_refined3['Planet Radius (R_Earth)'].notnull()]
X_refined5 = X_refined4[X_refined4['Planet Insolation (Earth Flux)']<1.5]
X_refined6 = X_refined5[X_refined5['Planet Insolation (Earth Flux)']>.5]

X_refined6


# In[ ]:




