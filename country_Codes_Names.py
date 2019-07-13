#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[2]:


url = ('http://www.fao.org/countryprofiles/iso3list/en/')
html = urlopen(url)


# In[3]:


soup = BeautifulSoup(html, 'lxml')
type(soup)


# In[4]:


# Getting the title of the page
title = soup.title
print(title)


# In[5]:


content = soup.find(id="c460959")


# In[6]:


# content


# In[7]:


headers = content.find_all('th')
headers


# In[8]:


shortName = content.find_all('a')


# In[9]:


shortName[:10]


# In[10]:


type(shortName[0])


# In[11]:


countries = []
for line in shortName:
    country = line.get_text()
    countries.append(country)
print(countries[:10])


# In[12]:


officialName = content.find_all(class_="official")


# In[13]:


officialName[:10]


# In[14]:


type(officialName[-1])


# In[15]:


OfficialNames = []
for line in officialName:
    nation = line.get_text()
    OfficialNames.append(nation)


# In[16]:


print(OfficialNames[:10])


# In[17]:


iso3 = content.find_all(class_="iso3")


# In[18]:


iso3[0]


# In[19]:


ISO3 = []
for line in iso3:
    i = line.get_text()
    ISO3.append(i)


# In[20]:


ISO3[:10]


# In[21]:


iso = content.find_all(class_='iso2')


# In[22]:


ISO2 = []
for line in iso3:
    i = line.get_text()
    ISO2.append(i)


# In[23]:


ISO2[:10]


# In[24]:


uni = content.find_all(class_="uni")


# In[25]:


uni[:10]


# In[26]:


UNI = []
for line in uni:
    i = line.get_text()
    UNI.append(i)    


# In[27]:


UNI[:10]


# In[28]:


undp = content.find_all(class_="undp")


# In[29]:


undp[:10]


# In[30]:


UNDP = []
for line in undp:
    i = line.get_text()
    UNDP.append(i)


# In[31]:


UNDP[:10]


# In[32]:


faostat = content.find_all(class_="faostat")


# In[33]:


FAOSTAT = []
for line in faostat:
    i = line.get_text()
    FAOSTAT.append(i)


# In[34]:


FAOSTAT[:10]


# In[35]:


gaul = content.find_all(class_="gaul")


# In[36]:


GAUL = []
for line in gaul:
    i = line.get_text()
    GAUL.append(i)


# In[37]:


GAUL[:10]


# In[38]:


#  [OfficialNames, ISO3, ISO2, UNI, UNDP,FAOSTAT, GAUL]


# In[39]:


lists_ = [[countries, OfficialNames, ISO3, ISO2, UNI, UNDP,FAOSTAT, GAUL]]


# In[40]:


# u = pd.concat(lists_)


# In[41]:


framesList = []
for value in lists_:
    df = pd.DataFrame(value)
    framesList.append(df)


# In[42]:


# framesList


# In[43]:


df = pd.concat(framesList)


# In[44]:


df.head()


# In[45]:


len(df)


# In[46]:


df = df.transpose()


# In[47]:


df.head()


# In[48]:


df.columns = ['Short Name', 'Official name', 'ISO3', 'ISO2', 'UNI','UNDP', 'FAOSTAT', 'GAUL']


# In[49]:


df.head()


# In[50]:


df


# In[ ]:




