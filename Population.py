#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#return countires with over 1 billon population with A rating in 2021
#with over 500 million population with B rating
#with over 100 million population with C rating
#with under 100 million population with Poor rating


# In[3]:


df=pd.read_csv('Population.csv')
df.head(20)


# In[4]:


def total_pop(people):
    if people>=1000000000:
        return "A"
    elif people>=500000000:
        return "B"
    elif people>=100000000:
        return "C"
    else:
        return "Poor"


# In[6]:


df = df.loc[4:,["Data Source", "Unnamed: 65"]]


# In[7]:


df


# In[9]:


df["Rating"] = df["Unnamed: 65"].apply(total_pop)
df


# In[11]:


df = df.loc[4:,["Data Source", "Rating"]]
df


# In[12]:


df.groupby("Rating")['Data Source'].agg('count').plot.bar()


# In[13]:


df.loc[  df["Rating"] == "A"  ]

