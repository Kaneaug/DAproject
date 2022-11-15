#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df_tax = pd.read_csv("taxrating.csv", index_col='Unnamed: 0')
df_gdp = pd.read_csv("gdprating.csv", index_col='Unnamed: 0')
df_unem = pd.read_csv("unemrating.csv", index_col='Unnamed: 0')
df_pop = pd.read_csv("poprating.csv", index_col='Unnamed: 0')


# In[3]:


df_tax.columns



# In[4]:


df_tax.set_index('country',inplace = True)
df_gdp.set_index('country',inplace = True)
df_unem.set_index('Country',inplace = True)
df_pop.set_index('Country',inplace = True)


# In[6]:


df_join = df_tax.join(df_gdp, how='outer').join(df_unem, how='outer').join(df_pop, how='outer')


# In[13]:


df_join = df_join.sort_values(by = ["rate", "gdp", "Unemployment Rating", "Pop Rating"])


# In[15]:


df_join.head(80)

