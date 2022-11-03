#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#return countires with under 5% unemployemnt with A rating in 2021
#under 9% unemployemnt with B rating
#under 12% unemployemnt with C rating
#under 15% unemployemnt with Poor rating


# In[3]:


df=pd.read_csv('Unemploymentrate.csv')
df.head()


# In[4]:


def total_em(unemp):
    if unemp <= 5:
        return 'A'
    elif unemp <= 9:
        return 'B'
    elif unemp <= 12:
        return 'C'
    else:
        return 'Poor'


# In[5]:


df[['Data Source','Unnamed: 65']]


# In[6]:


df['Unnamed: 65'] = df['Unnamed: 65'].apply(total_em)
df


# In[9]:


df.groupby('Unnamed: 65')['Data Source'].agg('count').plot.bar()


# In[10]:


df[['Data Source','Unnamed: 65']].loc[df['Unnamed: 65']=='A']

