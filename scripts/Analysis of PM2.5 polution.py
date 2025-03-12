#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#Importing CSV file of indian subcontinent pm 2.5
df = pd.read_csv('indiasubcont_satpm_allyears.csv')
df


# In[3]:


df.describe()


# In[4]:


(df == 0).sum()
#to many zeroes. 


# In[5]:


#Dropping all zeroes. code picked up from stack overflow
df.loc[~(df==0).all(axis=1)]
df = df.loc[~(df == 0).any(axis=1)]


# In[6]:


df


# In[7]:


df.reset_index(drop=True, inplace=True)


# ##### df

# In[8]:


plt.scatter(df['ix'], df['iy'], alpha=0.5, s=1)
plt.xlabel("Grid X (ix)")
plt.ylabel("Grid Y (iy)")
plt.title("Grid-based Data Distribution")
plt.show()


# In[9]:


plt.scatter(df['midlong'], df['midlat'], alpha=0.5, s=1)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Geospatial Distribution of Data Points")
plt.show()


# In[10]:


df.keys()


# In[11]:


new_columns = {col: col.strip() for col in df.columns}  # Remove accidental spaces
df.rename(columns=new_columns, inplace=True)  # Rename in-place


# In[12]:


rename_dict = {col: f'{col[1:]}' for col in df.columns if col.startswith('Y')}
df.rename(columns=rename_dict, inplace=True)


# In[13]:


df


# In[14]:


df.keys()


# In[18]:


df.columns[4] #to index columns


# In[25]:


t = 1998
for x in range(1,26):
    print(t)
    t += 1


# In[21]:


n = 1998  # Start from first year
for i in range(1, 26):
    print(df[str(n)].mean())  # Convert int to string
    n += 1  # Move to next year

ak = pd.DataFrame({
    1998:22.41032442006134,
    1999:23.545931429723385,
    2000:26.076068080694633,
    2001:29.344682995665764,
    2002:29.624755568995056,
    2003:30.044164614742176,
    2004:30.95601393868706,
    2005:31.803379555632358,
    2006:32.73339813094878,
    2007:33.174124152231194,
    2008:33.15985139746857,
    2009:33.68395899030916,
    2010:33.05679151007243,
    2011:33.0370915950293,
    2012:33.511732688237075,
    2013:33.55538324189669,
    2014:33.73866401716417,
    2015:33.21742767866143,
    2016:35.664346912033636,
    2017:32.48387259348856,
    2018:33.73866401716417,
    2019:32.60908174579176,
    2020:34.167062652094394,
    2021:32.08627586504816,
    2022:33.73866401716417,

})

Ye kaam nahi karega, kyunki Pandas DataFrame column-wise dictionary expect karta hai, row-wise nahi.
# In[28]:


# Data in dictionary form
data = {
    "Year": list(range(1998, 2023)),
    "Mean_PM2.5": [22.41, 23.54, 26.07, 29.34, 29.62, 30.04, 30.95, 28.97, 30.69, 31.80, 
                   32.73, 33.17, 33.15, 33.68, 33.05, 33.03, 33.51, 33.55, 33.73, 33.21, 
                   35.66, 32.48, 32.60, 34.16, 32.08]
}

# Creating DataFrame
ak = pd.DataFrame(data)

print(ak)


# In[34]:


plt.plot(ak['Year'], ak['Mean_PM2.5'], alpha=0.5, marker='o', linestyle='-',label='Graph By Issac Newton')
plt.xlabel("Year")
plt.ylabel("Mean_PM2.5")
plt.title("Year-wise PM2.5 graph")
plt.legend()
# Save the image using matplotlib.pyplot.imsave()
plt.savefig('sample_image.png',dpi=400)
plt.show()


# In[36]:


ak['Mean_PM2.5'].rolling(window=5).mean()


# In[38]:


plt.plot(ak['Year'], ak['Mean_PM2.5'].rolling(window=5).mean(), label="5-Year Rolling Mean", color='red')
plt.legend()
plt.show()


# In[40]:


import plotly.graph_objects as go
import pandas as pd

# DataFrame example
df = pd.DataFrame({
    "Year": list(range(1998, 2023)),
    "Mean_PM2.5": [22.41, 23.54, 26.07, 29.34, 29.62, 30.04, 30.95, 28.97, 30.69, 31.80, 
                   32.73, 33.17, 33.15, 33.68, 33.05, 33.03, 33.51, 33.55, 33.73, 33.21, 
                   35.66, 32.48, 32.60, 34.16, 32.08]
})

# Plotly Graph with Matplotlib-style markers
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["Year"], 
    y=df["Mean_PM2.5"], 
    mode="lines+markers",
    marker=dict(size=6, color="blue"), 
    line=dict(width=2),
    name="PM2.5 Levels"
))

# Layout customization
fig.update_layout(
    title="Year-wise PM2.5 Trend",
    xaxis_title="Year",
    yaxis_title="Mean PM2.5",
    template="plotly_white",  # This gives a clean Matplotlib-style look
    hovermode="x"
)

fig.show()



# In[ ]:




