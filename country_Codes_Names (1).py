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


content.find_all(class_="shortname")[:5]


# In[9]:


shortName = content.find_all('a')


# In[10]:


shortName[:10]


# In[11]:


type(shortName[0])


# In[12]:


def tagFunction(tagLines): 
    textList = []
    for line in tagLines:
        text = line.get_text()
        textList.append(text)
    return textList


# In[13]:


shortName = tagFunction(shortName)
print(shortName[:10])


# In[14]:


officialName = content.find_all(class_="official")


# In[15]:


officialName[:10]


# In[16]:


officialName = tagFunction(officialName)
print(officialName[:10])


# In[17]:


iso3 = content.find_all(class_="iso3")


# In[18]:


iso3 = tagFunction(iso3)
print(iso3[:10])


# In[19]:


iso2 = content.find_all(class_='iso2')


# In[20]:


iso2 = tagFunction(iso2)
print(iso2[:10])


# In[21]:


uni = content.find_all(class_="uni")


# In[22]:


uni = tagFunction(uni)
print(uni[:10])


# In[23]:


undp = content.find_all(class_="undp")


# In[24]:


undp = tagFunction(undp[:10])
print(undp[:10])


# In[25]:


faostat = content.find_all(class_="faostat")


# In[26]:


faostat = tagFunction(faostat[:10])
print(faostat[:10])


# In[27]:


gaul = content.find_all(class_="gaul")


# In[28]:


gaul = tagFunction(gaul[:10])
print(gaul[:10])


# In[29]:


listsContainer = [[shortName, officialName, iso3, iso2, uni, undp, faostat, gaul]]


# In[30]:


listsDfs = []
for List in listsContainer:
    df = pd.DataFrame(List)
    listsDfs.append(df)


# In[31]:


df = pd.concat(listsDfs)


# In[32]:


df


# In[33]:


df = df.transpose()


# In[34]:


df.head()


# In[35]:


# Naming the columns
df.columns = ['Short name', 'Official Name', 'ISO3', 'ISO3', 'UNI', 'UNDP','FAOSTAT', 'GAUL']


# In[36]:


df.head()


# In[ ]:




