#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


import streamlit as st
import pandas as pd
import numpy as np


# In[6]:


HairEye = pd.read_csv('HairEyeColor.csv')


# In[ ]:


st.title('Hair Eye Color Database')


# In[ ]:


InputHair = st.sidebar.selectbox('Select Hair Colour', ('Brown', 'Black', 'Blond', 'Red'))


# In[ ]:


HairEyeSelect = HairEye[HairEye['Hair'] == InputHair]


# In[ ]:


st.dataframe(HairEyeSelect)

