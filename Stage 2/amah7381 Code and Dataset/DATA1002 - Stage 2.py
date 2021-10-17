#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[75]:


df = pd.read_csv('https://raw.githubusercontent.com/Nafi-R/DATA1002-COVID-Data/master/Stage%201/Integrated%20Dataset/integrate_dataset.csv')


# In[76]:


import seaborn as sns


# In[77]:


df['mean'] = df[['Stringency Index' , 'Government Response Index' , 'Containment Index' , 'Economic Support Index']].mean(axis=1)


# In[78]:


print(df)


# In[79]:


df['mean'] = df[['Stringency Index' , 'Government Response Index' , 'Containment Index' , 'Economic Support Index']].mean(axis=1)
sns.boxplot(x = df['Country'] , y = df['mean'])
plt.ylabel("Mean of Policy Indexes/Dates")
plt.title("Implementation of Policies by Country")


# In[80]:


DF = df[df["Country"] == "Australia"]


# In[81]:


print(DF)


# In[82]:


DF = df[df["Country"] == "Australia"]
plt.scatter(x = DF['Containment Index'] , y = DF['New Cases'] , s = 10)
plt.xlabel("Containment Index")
plt.ylabel("New Cases")
plt.title("Correlation between Containment Index and New Cases - Australia")


# In[83]:


from tabulate import tabulate


# In[84]:


df['strictness'] = pd.cut(df['Stringency Index'], bins=3 , labels=('low' , 'moderate' , 'high'))
cases_affected_by_strictness = df.groupby(['strictness'])[['New Cases' , 'Country']].max()
print(tabulate(cases_affected_by_strictness , headers = 'keys'))


# In[85]:


df


# In[86]:


df['Govt_Response'] = pd.cut(df['Government Response Index'], bins=3 , labels=('low' , 'moderate' , 'high'))
country_economies = df.groupby(['Country'])[['Govt_Response' , 'New Deaths']].max()


# In[87]:


print(tabulate(country_economies, headers = 'keys'))


# In[88]:


pip install tabulate

