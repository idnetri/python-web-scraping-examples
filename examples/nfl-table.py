#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 06:05:25 2022

@author: tripurnomo
"""

#import libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup


#define url we want to scrape
url = 'https://www.nfl.com/standings/league/2022/REG'


#store whole page request from url
page = requests.get(url)


#storing data into beautifulsoup in xml format
soup = BeautifulSoup(page.text,'lxml')


#get data from table according to property of table
table = soup.find('table',summary = 'Standings - Detailed View')


# getting All Column For Header
th_row = table.findAll('th')

headers = []

# Looping for appending text to array Headers
for i in th_row:
    headers.append(i.text.strip())

    
#set Header array to dataframe header(column)
df = pd.DataFrame(columns=headers)    


#get All body data
table_body = table.findAll('tr')[1:]


#looping for filling dataframe from the first index to the last
for j in table_body:
    first_td = j.findAll('td')[0].find('div', class_ = 'd3-o-club-fullname').text.strip()
    row_data = j.findAll('td')[1:]
    row = [tr.text for tr in row_data]
    row.insert(0, first_td)
    length = len(df)
    df.loc[length] = row


#export to csv
df.to_csv('/Users/tripurnomo/Downloads/nfl2.csv')
