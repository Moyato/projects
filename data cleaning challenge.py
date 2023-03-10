#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd
import numpy as np
import datetime as dt
import warnings
warnings.filterwarnings('ignore')
f1 = pd.read_csv('fifa21_raw_data.csv')
f2 = pd.read_csv('fifa21 raw data v2.csv')


# In[70]:


f1.head()


# In[71]:


f2.head()


# In[72]:


f2.info()


# In[73]:


pd.set_option('display.max_columns',None)
f2.head()


# In[74]:


f21 = fifa2.copy()


# In[75]:


f21['Height'] = fifa21['Height'].str.replace('cm','')


# In[76]:


f21['Height'].unique()


# In[77]:


f21['Height'] = f21['Height'].str.replace('5\'4"','163')
f21['Height'] = f21['Height'].str.replace('5\'6"','168')
f21['Height'] = f21['Height'].str.replace('5\'7"','170')
f21['Height'] = f21['Height'].str.replace('5\'9"','175')
f21['Height'] = f21['Height'].str.replace('5\'10"','178')
f21['Height'] = f21['Height'].str.replace('5\'11"','180')
f21['Height'] = f21['Height'].str.replace('6\'0"','183')
f21['Height'] = f21['Height'].str.replace('6\'1"','185')
f21['Height'] = f21['Height'].str.replace('6\'2"','188')
f21['Height'] = f21['Height'].str.replace('6\'3"','191')
f21['Height'] = f21['Height'].str.replace('6\'4"','193')
f21['Height'] = f21['Height'].str.replace('6\'5"','196')


# In[78]:


f21['Height'].unique()


# In[79]:


f21['Weight'].unique()


# In[80]:


f21['Weight'] = f21['Weight'].str.replace('kg','')

f21['Weight'] = f21['Weight'].str.replace('146lbs','66')
f21['Weight'] = f21['Weight'].str.replace('148lbs','67')
f21['Weight'] = f21['Weight'].str.replace('130lbs','59')
f21['Weight'] = f21['Weight'].str.replace('179lbs','81')
f21['Weight'] = f21['Weight'].str.replace('172lbs','78')
f21['Weight'] = f21['Weight'].str.replace('196lbs','89')
f21['Weight'] = f21['Weight'].str.replace('176lbs','80')
f21['Weight'] = f21['Weight'].str.replace('185lbs','84')
f21['Weight'] = f21['Weight'].str.replace('170lbs','77')
f21['Weight'] = f21['Weight'].str.replace('203lbs','92')
f21['Weight'] = f21['Weight'].str.replace('168lbs','76')
f21['Weight'] = f21['Weight'].str.replace('161lbs','73')
f21['Weight'] = f21['Weight'].str.replace('190lbs','86')
f21['Weight'] = f21['Weight'].str.replace('174lbs','79')
f21['Weight'] = f21['Weight'].str.replace('165lbs','75')
f21['Weight'] = f21['Weight'].str.replace('159lbs','72')
f21['Weight'] = f21['Weight'].str.replace('192lbs','87')
f21['Weight'] = f21['Weight'].str.replace('181lbs','82')
f21['Weight'] = f21['Weight'].str.replace('139lbs','63')
f21['Weight'] = f21['Weight'].str.replace('154lbs','70')
f21['Weight'] = f21['Weight'].str.replace('157lbs','71')
f21['Weight'] = f21['Weight'].str.replace('163lbs','74')
f21['Weight'] = f21['Weight'].str.replace('183lbs','83')


# In[81]:


f21['Weight'].unique()


# In[82]:


list(f21['Joined'].unique())


# In[83]:


f21['Joined'] = pd.to_datetime(f21['Joined'], format = '%b %d, %Y')


# In[84]:


f21['Joined'] = f21['Joined'].dt.strftime('%Y/%m/%d')


# In[85]:


f21['Joined'].loc[150:200]


# In[86]:


f21['Loan Date End'].unique()


# In[87]:


f21['Loan Date End'].value_counts()


# In[88]:


f21['Loan Date End'].fillna('Jun 30, 2021', inplace = True)


# In[89]:


f21['Loan Date End'].unique()


# In[90]:


f21['Loan Date End'] = pd.to_datetime(f21['Loan Date End'], format = '%b %d, %Y')
f21['Loan Date End'] = f21['Loan Date End'].dt.strftime('%Y/%m/%d')


# In[91]:


f21['Loan Date End'].loc[50:89]


# In[92]:


f21.info()


# In[93]:


f21['Height'] = f21['Height'].astype('int64')
f21.info()


# In[94]:


f21.head()


# In[95]:


f21["Weight"] = f21["Weight"].astype('int64')
f21.info()


# In[96]:


f21['Value'] = f21['Value'].str.replace('€','')
f21.head()


# In[97]:


f21['Wage'] = f21['Wage'].str.replace('€','')
f21['Release Clause'] = f21['Release Clause'].str.replace('€','')
f21.head()


# In[98]:


f21['Value'] = f21['Value'].str.replace('M','')
f21['Wage'] = f21['Wage'].str.replace('K','')
f21['Release Clause'] = f21['Release Clause'].str.replace('M','')
f21.head()


# In[99]:


f21 = f21.rename(columns={'Value' : 'Value_millions(€)'})
f21.head()                          


# In[100]:


f21 = f21.rename(columns={'Wage' : 'Wage_thousands(€)'})
f21 = f21.rename(columns={'Release Clause' : 'Release Clause_millions(€)'})
f21.head()


# In[103]:


f21.head()


# In[106]:


f21["Club"] = f21["Club"].str.removeprefix('\n\n\n\n')
f21.head()


# In[ ]:




