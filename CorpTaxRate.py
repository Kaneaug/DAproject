#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#return countires with 20% or under Corporate tax rate with A rating
#21-25%  Corporate tax rate with B rating
#26-30% Corporate tax rate with A rating
#30% or over Corporate tax rate with Poor rating


# In[3]:


df = pd.read_csv('corptaxrate2021.csv')
df


# In[4]:


def corp_tax(rate):
    if rate <= 20:
        return "A"
    elif rate <= 25:
        return "B"
    elif rate <= 30:
        return "C"
    else:
        return "Poor"
    

        
        
    
    
        


# In[5]:


corp_tax(18)


# In[6]:


df["rate"] = df["rate"].apply(corp_tax)
df


# In[7]:


df[['country','rate']]


# In[8]:


df.groupby("rate")['country'].agg('count').plot.bar()


# In[12]:


df[['country','rate']].loc[df["rate"] == "A"]

