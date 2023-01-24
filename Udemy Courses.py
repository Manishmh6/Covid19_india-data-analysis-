#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as pd


# In[2]:


data=pd.read_csv(r"C:\Users\manis\Desktop\12 Project\Project Excel file\7. Udemy Courses.csv")


# In[3]:


#data


# In[6]:


data.head(2)


# In[7]:


data.shape


# In[9]:


data.subject.value_counts()


# In[11]:


data[data.is_paid==False]


# In[12]:


data[data.is_paid==True]


# In[ ]:





# In[14]:


data.sort_values('num_subscribers',ascending=False)


# In[ ]:





# In[15]:


data.sort_values('num_subscribers')


# In[ ]:





# In[16]:


data.head(2)


# In[28]:


data[data.subject=='Graphic Design']


# In[ ]:





# In[29]:


data[(data.subject=='Graphic Design')&(data.price<'100')]


# In[31]:


data[(data.subject=='Graphic Design')&(data.price=='100')]


# In[ ]:





# In[30]:


data.head(1)


# In[33]:


data[data.course_title.str.contains('Python')]


# In[ ]:





# In[34]:


len(data[data.course_title.str.contains('Python')])


# In[35]:


data.head(1)


# In[36]:


data.dtypes


# In[40]:


data['published_timestamp']=pd.to_datetime(data.published_timestamp)


# In[41]:


data.dtypes


# In[42]:


data.head(1)


# In[57]:


data['Year']=data['published_timestamp'].dt.year


# In[58]:


data


# In[59]:


data.head(1)


# In[60]:


data[data.Year==2015]


# In[61]:


data.head(1)


# In[62]:


data.level.unique()


# In[64]:


data.groupby('level')['num_subscribers'].min()


# In[65]:


data.groupby('level')['num_subscribers'].max()


# In[ ]:




