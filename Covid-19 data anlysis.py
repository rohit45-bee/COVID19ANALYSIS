#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[3]:


covid_df = pd.read_csv("C:/Users/barsh/Downloads/covid19/covid_19_india.csv")


# In[4]:


covid_df.head(10)


# In[5]:


covid_df.info()  


# In[6]:


covid_df.describe()


# In[7]:


vaccine_df=pd.read_csv("C:/Users/barsh/Downloads/covid19/covid_vaccine_statewise.csv")


# In[8]:


vaccine_df.head(7)


# In[15]:


covid_df.drop(["Sno","Time","ConfirmedForeignNational","ConfirmedIndianNational"],inplace = True,axis=1)


# In[16]:


covid_df.head(5)


# In[26]:


covid_df['Date']=pd.to_datetime(covid_df['Date'],format = '%Y-%m-%d')


# In[27]:


covid_df.head(5)


# In[32]:


#active cases

covid_df['Active_Cases']=covid_df['Confirmed'] - (covid_df['Cured']+covid_df['Deaths'])
covid_df.tail()


# In[36]:


statewise = pd.pivot_table(covid_df,values = ["Confirmed","Deaths","Cured"],index="State/UnionTerritory",aggfunc = max)   


# In[39]:


statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]


# In[41]:


statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise["Confirmed"]


# In[43]:


statewise= statewise.sort_values(by= "Confirmed" , ascending = False)


# In[44]:


statewise.style.background_gradient(cmap ="cubehelix")


# In[55]:


top_10_active_cases = covid_df.groupby(by = "State/UnionTerritory").max()[['Active_Cases','Date']].sort_values(by = ['Active_Cases'],ascending = False).reset_index()


# In[56]:


fig = plt.figure(figsize=(16,9))


# In[57]:


plt.title("Top 10 Strates With Active Cases In India")


# In[60]:


ax = sns.barplot(data= top_10_active_cases.iloc[:10],y="Active_Cases", x = "State/UnionTerritory" , linewidth = 2 ,edgecolor = 'red')


# In[63]:


top_10_active_cases = covid_df.groupby(by = "State/UnionTerritory").max()[['Active_Cases','Date']].sort_values(by = ['Active_Cases'],ascending = False).reset_index()
fig = plt.figure(figsize=(16,9))
plt.title("Top 10 Strates With Active Cases In India")
ax = sns.barplot(data= top_10_active_cases.iloc[:10],y="Active_Cases", x = "State/UnionTerritory" , linewidth = 2 ,edgecolor = 'red')
plt.xlabel("States")
plt.ylabel("Total Active Cases")   


# In[ ]:





# In[ ]:




