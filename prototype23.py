import urllib.request
import csv
import os 
import sys
import pandas as pd
import numpy as np
import time 
import requests 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

#this makes sure that I'm in the right directory
os.chdir('/Users/stephaniegomez/Documents/EXOFOPCSV/')

#this downloads the csv file from EXOFOP 
print('Downloading EXOFOP Table CSV as "comparison.csv"...')
url = 'https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv'
urllib.request.urlretrieve(url, '/Users/stephaniegomez/Documents/EXOFOPCSV/comparison.csv')

#this reads the csv files using pandas 
#turns them into dataframe instances 
mainlist = mainlist.csv
comparison = comparison.csv
frame = pd.read_csv(mainlist)
frame = pd.read_csv(comparison) 

#this compares the two files and then checks to send email

if (np.all(frame == frame)):
    print("No Updates")
    os.remove("comparison.csv")
    continue
        
    
    else:
        #this updates masterlist 
        os.remove("masterlist.csv")
        os.rename(r'/Users/stephaniegomez/Documents/EXOFOPCSV/comparison.csv',r'/Users/stephaniegomez/Documents/EXOFOPCSV/masterlist.csv')
        
        
        #this gets the data that is different 
        #concat dataframes and drops duplicates
        result = pd.concat([mainlist, comparison]).drop_duplicates()
        
        #resets the index
        result = df.reset_index(drop=True)
        
        #groups
        result_gpby = df.groupby(list(df.columns)) 
        idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
        
        #puts the results into a csv file
        result.to_csv(r'/Users/stephaniegomez/Documents/EXOFOPCSV/result.csv',index = False, header=True)
        
        #this sets up the email and sends it
        email = ${{ secrets.EMAIL_USER }}
        password = ${{ secrets.EMAIL_PASSWORD }}
        send_to_email = 'steph_7806@berkeley.edu'
        subject = 'TESS Updated'
        message = 'This email has attached the new updates within TESS. Have fun!'
        file_location = '/Users/stephaniegomez/Documents/EXOFOPCSV/result.csv'

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))
        
        # Setup the attachment
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        # Attach the attachment to the MIMEMultipart object
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()

        
        break
        
        




