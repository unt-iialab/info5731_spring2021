#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/5/2020 10:12 PM
# @Author  : Haihua
# @Contact : haihua.chen@unt.edu
# @File    : wikiCrawler.py
# Software : PyCharm

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(wiki)
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)
# print(soup.prettify())
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
# find the content of the whole table
# print(right_table)
#Extract and save the information: Here, we need to iterate through each row (tr)
#and then assign each element of tr (td) to a variable and append it to a list.
#Let’s first look at the HTML structure of the table
#(I am not going to extract information for table heading)
# Generate list to save all data
all_data = []
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
      item = []
      item.append(cells[0].find(text=True).strip("\n"))
      item.append(states[0].find(text=True).strip("\n"))
      item.append(cells[1].find(text=True).strip("\n"))
      item.append(cells[2].find(text=True).strip("\n"))
      item.append(cells[3].find(text=True).strip("\n"))
      item.append(cells[4].find(text=True).strip("\n"))
      item.append(cells[5].find(text=True).strip("\n"))
      all_data.append(item)
# print(all_data)

# Convert list to dictionary for better undersantding
# define a new list to save data
all_new_clear_data = []
# define the table heading
heading = ['Number','State/UT','Admin_Capital','Legislative_Capital', 'Judiciary_Capital', 'Year_Capital','Former_Capital']
# combine two lists to a dictionary
for record in all_data:
  record_dict = dict(zip(heading,record))
  all_new_clear_data.append(record_dict)
# print(all_new_clear_data)

#Or Use DataFrame to save the data in a table
#Generate lists
A,B, C, D, E, F, G=[], [], [], [], [], [], []
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
# print(A,B, C, D, E, F, G)
pd.set_option('display.max_columns', 500)
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
print(df.head(n=10))