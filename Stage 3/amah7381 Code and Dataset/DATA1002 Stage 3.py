#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
from math import sqrt
from sklearn import linear_model
from sklearn import metrics 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np 


# In[9]:


df = pd.read_csv("https://raw.githubusercontent.com/Nafi-R/DATA1002-COVID-Data/master/Stage%203/amah7381%20Code%20and%20Dataset/integrate_dataset.csv")


# In[10]:


DFAustralia = df[df["Country"] == "Australia"]

#Predictive model for Australia 
X = DFAustralia[['Government Response Index']]
y = DFAustralia[['New Deaths']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
regr = linear_model.LinearRegression().fit(X_train, y_train)

#Prediction for Australia
sample = [100]
sample_pred = regr.predict([sample])
print('----- Australia -----')
print('Predicted number of New Deaths:', int(sample_pred))
print('-----------------------')
print('Coefficients:')
print(regr.coef_)

#Testing the model for Australia 
y_pred = regr.predict(X_test)
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
print('R-squared score:', metrics.r2_score(y_test, y_pred))


# In[11]:


DFIndia = df[df["Country"] == "India"]

#Predictive model for India 
X = DFIndia[['Government Response Index']]
y = DFIndia[['New Deaths']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
regr = linear_model.LinearRegression().fit(X_train, y_train)

#Prediction for India
sample = [100]
sample_pred = regr.predict([sample])
print('----- India -----')
print('Predicted number of New Deaths:', int(sample_pred))
print('-----------------------')
print('Coefficients:')
print(regr.coef_)

#Testing the model for India
y_pred = regr.predict(X_test)
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
print('R-squared score:', metrics.r2_score(y_test, y_pred))


# In[12]:


DFUS = df[df["Country"] == "US"]

#Predictive model for US
X = DFUS[['Government Response Index']]
y = DFUS[['New Deaths']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
regr = linear_model.LinearRegression().fit(X_train, y_train)

#Prediction for US
sample = [100]
sample_pred = regr.predict([sample])
print('----- US -----')
print('Predicted number of New Deaths:', int(sample_pred))
print('-----------------------')
print('Coefficients:')
print(regr.coef_)

#Testing the model for US
y_pred = regr.predict(X_test)
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
print('R-squared score:', metrics.r2_score(y_test, y_pred))


# In[13]:


DFUnitedKingdom = df[df["Country"] == "United Kingdom"]

#Predictive model for UK 
X = DFUnitedKingdom[['Government Response Index']]
y = DFUnitedKingdom[['New Deaths']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
regr = linear_model.LinearRegression().fit(X_train, y_train)

#Prediction for UK
sample = [100]
sample_pred = regr.predict([sample])
print('----- United Kingdom -----')
print('Predicted number of New Deaths:', int(sample_pred))
print('-----------------------')
print('Coefficients:')
print(regr.coef_)

#Testing the model for UK
y_pred = regr.predict(X_test)
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
print('R-squared score:', metrics.r2_score(y_test, y_pred))


# In[ ]:





# In[ ]:




