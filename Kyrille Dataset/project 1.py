#!/usr/bin/env python
# coding: utf-8

# In[109]:


#All visualizations, data, and code produced by Our World in Data are completely open access under the Creative Commons BY license. You have the permission to use, distribute, and reproduce these in any medium, provided the source and authors are credited.
#The data produced by third parties and made available by Our World in Data is subject to the license terms from the original third-party authors. We will always indicate the original source of the data in our documentation, so you should always check the license of any such third-party data before use and redistribution.
#All of our charts can be embedded in any site.


# In[ ]:


METADATA

location: name of the country (or region within a country).
    
iso_code: ISO 3166-1 alpha-3 – three-letter country codes.
    
date: date of the observation.
    
total_vaccinations: total number of doses administered. For vaccines that require multiple doses, each individual 
    dose is counted. If a person receives one dose of the vaccine, this metric goes up by 1. 
    If they receive a second dose, it goes up by 1 again. If they receive a third/booster dose, 
    it goes up by 1 again.

total_vaccinations_per_hundred: total_vaccinations per 100 people in the total population of the country.

daily_vaccinations_raw: daily change in the total number of doses administered. 
    It is only calculated for consecutive days. This is a raw measure provided for data checks and transparency,
    but we strongly recommend that any analysis on daily vaccination rates be conducted using daily_vaccinations
    instead.

daily_vaccinations: new doses administered per day (7-day smoothed). For countries that don't report data 
    on a daily basis,we assume that doses changed equally on a daily basis over any periods in which no data 
    was reported.This produces a complete series of daily figures, which is then averaged over a rolling 
    7-day window.An example of how we perform this calculation can be found here.

daily_vaccinations_per_million: daily_vaccinations per 1,000,000 people in the total population of the country.

people_vaccinated: total number of people who received at least one vaccine dose. 
    If a person receives the first dose of a 2-dose vaccine, this metric goes up by 1. 
    If they receive the second dose, the metric stays the same.

people_vaccinated_per_hundred: people_vaccinated per 100 people in the total population of the country.

people_fully_vaccinated: total number of people who received all doses prescribed by the vaccination protocol. 
    If a person receives the first dose of a 2-dose vaccine, this metric stays the same. 
    If they receive the second dose, the metric goes up by 1.

people_fully_vaccinated_per_hundred: people_fully_vaccinated per 100 people in the total population of the country.

total_boosters: Total number of COVID-19 vaccination booster doses administered 
    (doses administered beyond the number prescribed by the vaccination protocol)

total_boosters_per_hundred: Total number of COVID-19 vaccination booster doses administered per 100 people 
    in the total population.


# In[368]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[369]:


df = pd.read_csv("vaccinations.csv")


# In[370]:


df


# In[371]:


df.head()


# In[372]:


df.tail()


# In[373]:


type(df)


# In[374]:


df.dtypes


# In[375]:


df.columns 


# In[376]:


pd.isna(pd.NA)


# In[384]:


df = df.dropna(how = 'all')
df


# In[386]:



df = df.dropna(subset=['people_vaccinated', 'people_fully_vaccinated','people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred'])


# In[387]:


df.describe()


# In[388]:


df = df.fillna("0")
df


# In[389]:


df.describe()


# In[383]:





# In[338]:


aus = df[(df.location == "Australia")].index.tolist()
aus


# In[339]:


df_aus


# In[340]:


df_aus = df.iloc[2572:2780]
df_aus.reset_index(drop = True,inplace = True)
df_aus


# In[341]:


df_aus.describe()


# In[342]:


df_aus.plot()
plt.show()


# In[343]:


df_aus.plot(kind='scatter', x='date',y = 'people_vaccinated',c='people_vaccinated_per_hundred',colormap='viridis')
plt.show()

df_aus.plot(kind='scatter', x='date',y = 'people_fully_vaccinated',c='people_fully_vaccinated_per_hundred',colormap='viridis')
plt.show()


# In[ ]:





# In[344]:


india = df[(df.location == "India")].index.tolist()

india


# In[345]:


df_in = df.iloc[19304:19543]
df_in.reset_index(drop = True,inplace = True)
df_in


# In[346]:


df_in.describe()


# In[347]:


df_in.plot()
plt.show()

df_in.plot(kind='scatter', x='date',y = 'people_vaccinated',c='people_vaccinated_per_hundred',colormap='viridis')
plt.show()
df_in.plot(kind='scatter', x='date',y = 'people_fully_vaccinated',c='people_fully_vaccinated_per_hundred',colormap='viridis')
plt.show()


# In[348]:


us = df[(df.location == "United States")].index.tolist()
us


# In[349]:


df_us = df.iloc[44507:44772]
df_us.reset_index(drop = True,inplace = True)
df_us


# In[350]:


df_us.describe()


# In[351]:


df_us.plot()
plt.show()

df_us.plot(kind='scatter', x='date',y = 'people_vaccinated',c='people_vaccinated_per_hundred',colormap='viridis')
plt.show()
df_us.plot(kind='scatter', x='date',y = 'people_fully_vaccinated',c='people_fully_vaccinated_per_hundred',colormap='viridis')
plt.show()


# In[ ]:





# In[352]:


uk = df[(df.location == "United Kingdom")].index.tolist()
uk


# In[353]:


df_uk = df.iloc[44235:44506]
df_uk.reset_index(drop = True,inplace = True)
df_uk


# In[354]:


df_uk.describe()


# In[355]:


df_uk.plot()
plt.show()

df_uk.plot(kind='scatter', x='date',y = 'people_vaccinated',c='people_vaccinated_per_hundred',colormap='viridis')
plt.show()
df_uk.plot(kind='scatter', x='date',y = 'people_fully_vaccinated',c='people_fully_vaccinated_per_hundred',colormap='viridis')
plt.show()


# In[356]:


frames = [df_aus, df_in, df_uk,df_us]
result = pd.concat(frames)
result.reset_index(drop = True,inplace = True) 
result


# In[357]:


result.describe()


# In[358]:


import matplotlib.pyplot as plt
import numpy as np

x = df_aus['date']
y = df_aus['people_vaccinated']
area = df_aus['people_vaccinated_per_hundred']
plt.scatter(x, y, s = area, color = 'blue',alpha = 0.5)

x = df_in['date']
y = df_in['people_vaccinated']
area = df_in['people_vaccinated_per_hundred']
plt.scatter(x, y,s = area, color = 'green',alpha = 0.5)

x = df_uk['date']
y = df_uk['people_vaccinated']
area = df_uk['people_vaccinated_per_hundred']
plt.scatter(x, y, s = area, color = 'red',alpha = 0.5)

x = df_us['date']
y = df_us['people_vaccinated']
area = df_us['people_vaccinated_per_hundred']
plt.scatter(x, y,s = area, color = 'yellow',alpha = 0.5)


plt.show()


# In[359]:


x = df_aus['date']
y = df_aus['people_fully_vaccinated']
area = df_aus['people_fully_vaccinated_per_hundred']
plt.scatter(x, y, s = area, color = 'blue',alpha = 0.5)

x = df_in['date']
y = df_in['people_fully_vaccinated']
area = df_in['people_fully_vaccinated_per_hundred']
plt.scatter(x, y,s = area, color = 'green',alpha = 0.5)

x = df_uk['date']
y = df_uk['people_fully_vaccinated']
area = df_uk['people_fully_vaccinated_per_hundred']
plt.scatter(x, y, s = area, color = 'red',alpha = 0.5)

x = df_us['date']
y = df_us['people_fully_vaccinated']
area = df_us['people_fully_vaccinated_per_hundred']
plt.scatter(x, y,s = area, color = 'yellow',alpha = 0.5)


plt.show()


# In[360]:


result.plot(kind='scatter', x= 'date',y = 'people_vaccinated',c='people_vaccinated_per_hundred',colormap='viridis')
plt.show()

result.plot(kind='scatter', x='date',y = 'people_fully_vaccinated',c='people_fully_vaccinated_per_hundred',colormap='viridis')
plt.show()


# In[ ]:


df_1 = df.dropna(how = 'all')
df_2 = df_1.dropna(subset=['people_vaccinated', 'people_fully_vaccinated','people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred'])
df_3 = df_2.fillna('0')
df_3.to_csv(path_or_buf = 'vacci3.csv',index = False )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




