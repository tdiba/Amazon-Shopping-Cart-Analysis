#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[7]:


df=pd.read_excel(r"C:\Users\USER\Documents\Chat GPT Projects\RAW DATA\Ecommerce Shopping Cart Analysis\Amazon Sale Report.xlsx")


# In[9]:


df.head()


# In[10]:


df.info()


# In[12]:


# Handle missing values as needed (e.g., fillna or dropna)
df = df.dropna(subset=['Amount'])


# ## Sales Overview Analysis

# In[15]:


# Basic statistics
total_orders = df['Order ID'].nunique()
total_orders

total_sales = df['Amount'].sum()
total_sales

average_order_value = total_sales / total_orders
average_order_value




# ## Order Status Analysis

# In[16]:


# Count of each order status
order_status_counts = df['Status'].value_counts()
order_status_counts


# ## Category and Product Analysis

# In[18]:


# Top categories in terms of order count
top_categories = df['Category'].value_counts().head(10)
top_categories


# In[20]:


# Cancellation rate by category
cancelled_orders = df[df['Status'] == 'Cancelled']
cancellation_rate_by_category = cancelled_orders['Category'].value_counts() / df['Category'].value_counts()
cancellation_rate_by_category


# ## Temporal Analysis

# In[22]:


df['Date'] = pd.to_datetime(df['Date'])


# In[23]:


df.info()


# In[25]:


# Monthly trend of orders and cancellations
monthly_orders = df.groupby(df['Date'].dt.to_period("M")).size()
monthly_cancellations = df[df['Status'] == 'Cancelled'].groupby(df['Date'].dt.to_period("M")).size()
monthly_cancellations


# ## Visualizations

# In[26]:


#Import Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns


# In[27]:


# Sales Overview Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x=top_categories.values, y=top_categories.index)
plt.title('Top 10 Categories by Order Count')
plt.xlabel('Order Count')
plt.ylabel('Category')


# In[28]:


# Order Status Visualization
plt.figure(figsize=(8, 8))
plt.pie(order_status_counts, labels=order_status_counts.index, autopct='%1.1f%%')
plt.title('Order Status Distribution')


# In[29]:


# Cancellation Rate Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x=cancellation_rate_by_category.head(10).values, y=cancellation_rate_by_category.head(10).index)
plt.title('Top 10 Categories by Cancellation Rate')
plt.xlabel('Cancellation Rate')
plt.ylabel('Category')


# In[ ]:




