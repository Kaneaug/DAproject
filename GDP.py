#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#return countires with 1000 billon or over GDP with A rating
#500 billon or over GDP with B rating
#180 billon or over GDP with c rating
#100 billon or under GDP with Poor rating


# In[3]:


df = pd.read_csv('corptaxrate2021.csv')
df


# In[4]:


def total_gdp(amount):
    if amount >= 1000:
        return "A"
    elif amount >= 500:
        return "B"
    elif amount >= 100:
        return "C"
    else:
        return "Poor"
    


# In[5]:


df['gdp'] = df['gdp'].apply(total_gdp)
df


# In[6]:


df[['country','gdp']]


# In[7]:


df.groupby("gdp")['country'].agg('count').plot.bar()


# In[8]:


df.loc[  df["gdp"] == "A"  ]


# In[11]:


df[['country','gdp']].loc[df["gdp"] == "A"]

