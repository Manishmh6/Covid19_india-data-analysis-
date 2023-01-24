#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[16]:


data1=pd.read_csv(r"https://api.covid19india.org/csv/latest/raw_data1.csv")


# In[17]:


data1.head(2)


# In[ ]:





# In[18]:


data1=pd.read_csv(r"https://api.covid19india.org/csv/latest/raw_data1.csv")
data2=pd.read_csv(r"https://api.covid19india.org/csv/latest/raw_data2.csv")
data3=pd.read_csv(r"https://api.covid19india.org/csv/latest/raw_data3.csv")
data4=pd.read_csv(r"https://api.covid19india.org/csv/latest/raw_data4.csv")
data5=pd.read_csv(r"https://api.covid19india.org/csv/latest/raw_data5.csv")
data6=pd.read_csv(r"https://api.covid19india.org/csv/latest/raw_data6.csv")
data7=pd.read_csv(r"https://api.covid19india.org/csv/latest/raw_data7.csv")
data8=pd.read_csv(r"https://api.covid19india.org/csv/latest/raw_data8.csv")


# In[20]:


data1.info()


# In[ ]:





# In[6]:


data3.columns


# # Retain Necesary Columns 

# In[7]:


data1=data1.loc[:,['Num Cases', 'Date Announced', 'Age Bracket', 'Gender', 'Detected City', 'Detected District', 'Detected State', 'Current Status']]
data2=data2.loc[:,['Num Cases', 'Date Announced', 'Age Bracket', 'Gender', 'Detected City', 'Detected District', 'Detected State', 'Current Status']]
data3=data3.loc[:,['Num Cases', 'Date Announced', 'Age Bracket', 'Gender', 'Detected City', 'Detected District', 'Detected State', 'Current Status']]
data4=data4.loc[:,['Num Cases', 'Date Announced', 'Age Bracket', 'Gender', 'Detected City', 'Detected District', 'Detected State', 'Current Status']]
data5=data5.loc[:,['Num Cases', 'Date Announced', 'Age Bracket', 'Gender', 'Detected City', 'Detected District', 'Detected State', 'Current Status']]
data6=data6.loc[:,['Num Cases', 'Date Announced', 'Age Bracket', 'Gender', 'Detected City', 'Detected District', 'Detected State', 'Current Status']]
data7=data7.loc[:,['Num Cases', 'Date Announced', 'Age Bracket', 'Gender', 'Detected City', 'Detected District', 'Detected State', 'Current Status']]
data8=data8.loc[:,['Num Cases', 'Date Announced', 'Age Bracket', 'Gender', 'Detected City', 'Detected District', 'Detected State', 'Current Status']]


# In[8]:


# Merge All data data 1 to data append 


# In[21]:


df  = data1.append([data2, data3, data4, data5, data6, data7, data8])


# In[22]:


df.head(2)


# In[23]:


# Makeing seperate day month year


# In[24]:


DATE = df['Date Announced'].str.split('/',expand=True)
DATE.columns=['Day', 'Month', 'Year']
DATE


# # concatinate both the Data frame's along axis=1

# In[13]:


df = pd.concat([df,DATE],axis=1)
df


# In[14]:


df.to_csv('E:Covid19India_csv',index=False)


# In[ ]:





# # final data set

# In[ ]:





# In[ ]:





# In[ ]:




