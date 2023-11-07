#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt
import seaborn as sns
pio.templates.default = "plotly_white"


# In[6]:


df = pd.read_csv("customer_acquisition_data.csv")


# In[7]:


print(df.head())


# In[33]:


# Group the data by 'channel' and calculate the total cost for each channel
channel_cost = df.groupby('channel')['cost'].sum().reset_index()

# Sort the channels by total cost
channel_cost = channel_cost.sort_values(by='cost', ascending=False)

# Create a bar plot to visualize the total cost by channel
plt.figure(figsize=(12, 6))
sns.barplot(data=channel_cost, x='channel', y='cost', palette="Reds")
plt.title('Customer Acquisition Cost by Channel')
plt.xlabel('Channel')
plt.ylabel('Total Cost')
plt.xticks(rotation=45)

# Show the plot
plt.show()


# In[19]:


# Group the data by 'channel' and calculate relevant metrics
channel_metrics = df.groupby('channel').agg({
    'conversion_rate': 'mean',  # average conversion rate for each channel
    'revenue': 'sum'            # total revenue for each channel
}).reset_index()

# Sort the channels by conversion rate and revenue
channel_metrics = channel_metrics.sort_values(by=['conversion_rate', 'revenue'], ascending=False)

# Show the top-performing channels
top_channels = channel_metrics.head(5)
print("Top-performing channels by conversion rate:")
print(top_channels)


# In[23]:


# Visualize the data
plt.figure(figsize=(12, 6))
sns.barplot(data=channel_metrics, x='channel', y='conversion_rate', color='palevioletred')
plt.title('Conversion Rate by Channel')
plt.xlabel('Channel')
plt.ylabel('Average Conversion Rate')
plt.xticks(rotation=45)


# In[26]:


# Visualize the data
plt.figure(figsize=(12, 6))
sns.barplot(data=channel_metrics, x='channel', y='revenue', color='teal')
plt.title('Total Revenue by Channel')
plt.xlabel('Channel')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)

# Show the plot
plt.show()


# In[28]:


# Calculate the ROI for each channel
df['roi'] = (df['revenue'] - df['cost']) / df['cost']

# Group the data by 'channel' and calculate the average ROI for each channel
channel_roi = df.groupby('channel')['roi'].mean().reset_index()

# Print the ROI for each channel
print("ROI for each channel:")
print(channel_roi)


# In[34]:


# Group the data by 'channel' and calculate the average ROI for each channel
channel_roi = df.groupby('channel')['roi'].mean().reset_index()

# Sort the channels by average ROI
channel_roi = channel_roi.sort_values(by='roi', ascending=False)

# Create a bar plot to visualize the average ROI by channel
plt.figure(figsize=(12, 6))
sns.barplot(data=channel_roi, x='channel', y='roi', palette="Greens")
plt.title('Average ROI by Channel')
plt.xlabel('Channel')
plt.ylabel('Average ROI')
plt.xticks(rotation=45)

# Show the plot
plt.show()


# In[31]:


# Calculate the CLTV for each customer
# CLTV = (revenue - cost)
df['cltv'] = (df['revenue'] - df['cost']) * (df['conversion_rate']/df['cost'])

# Group the data by 'channel' and calculate the average CLTV for each channel
channel_cltv = df.groupby('channel')['cltv'].mean().reset_index()

# Sort the channels by average CLTV
channel_cltv = channel_cltv.sort_values(by='cltv', ascending=False)

# Create a bar plot to visualize CLTV by channel
plt.figure(figsize=(12, 6))
sns.barplot(data=channel_cltv, x='channel', y='cltv', palette="Blues")
plt.title('CLTV by Channel')
plt.xlabel('Channel')
plt.ylabel('Average CLTV')
plt.xticks(rotation=45)

# Show the plot
plt.show()


# In[36]:


# Filter data for the 'social media' and 'referral' channels
social_media_data = df[df['channel'] == 'social media']
referral_data = df[df['channel'] == 'referral']

# Create a box plot to compare CLTV distributions
plt.figure(figsize=(12, 6))

# Create a box plot for the 'social media' channel
plt.boxplot(social_media_data['cltv'], positions=[1], widths=0.6, showfliers=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.text(1, social_media_data['cltv'].median() + 0.5, 'Social Media', ha='center')

# Create a box plot for the 'referral' channel
plt.boxplot(referral_data['cltv'], positions=[2], widths=0.6, showfliers=False, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.text(2, referral_data['cltv'].median() + 0.5, 'Referral', ha='center')

plt.title('CLTV Distribution Comparison: Social Media vs. Referral')
plt.xlabel('Channel')
plt.ylabel('CLTV')
plt.xticks([1, 2], ['Social Media', 'Referral'])

# Show the plot
plt.show()


# In[ ]:




