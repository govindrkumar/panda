#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


df = pd.read_csv('NCRB_CII-2019_Table_17A.1.csv')


# In[12]:


print('Top 5 Crime Type in 2019')
df.head(5)


# In[11]:


df.describe()


# In[13]:


print('Lowest Crime Type in 2019')
df.tail(5)


# In[14]:


df.info()


# In[15]:


df.duplicated().sum() 

Okay! No duplicate Data
Now, Let's print Graph!
# In[38]:


plt.figure(figsize=(18, 8))  # Pehle figure size set karo
ax = df.plot(x='Crime Head', y='Charge-Sheeting Rate (Col.18/ Col.19) *100', kind='bar', color='g')
ax.set_xticks(ax.get_xticks()[::4])  # Har doosra label hatao

plt.title('Crime Percent in 2019', fontsize=14)
plt.xticks(rotation=90, ha='right', fontsize=8)  # Rotate + Align Right + Font Chhota
plt.subplots_adjust(bottom=0.4)  # Neeche Space Zyada Karo
plt.show()


# In[39]:


df.groupby('Crime Head')['Cases Reported during the year'].sum().plot(kind='pie')


# In[ ]:




