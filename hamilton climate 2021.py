"""A Python script capable of reading a CSV file and plotting Hamilton temperature statistics for 2021.
"""

import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from matplotlib.pyplot import MultipleLocator


file_name = "a4_hamilton_climate_2021.csv"
if os.path.exists(file_name):
    """read csv file"""
    pd_data = pd.read_csv(file_name)
else:
    pd_data = None
    print("Error: file not found")
    exit(0)

months_to_label = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'July':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
month_index_classify = {month:[] for month in months_to_label.keys()}
for index,row in pd_data.iterrows():
    """arrange data for ploting"""
    month_name = list(months_to_label.keys())[list(months_to_label.values()).index(row['Month'])]
    if not np.isnan(row['Mean Temp (°C)']):
        month_index_classify[month_name].append(row['Mean Temp (°C)'])


plt.figure(figsize=(8,6),dpi=100)
plt.suptitle("Hamilton Temperature Statistics By Month and Day for 2021")
plt.ylim([-15, 28])

"""subplots position"""
ax1 = plt.subplot2grid((7, 7), (0, 0), rowspan=2,colspan=7)
ax2 = plt.subplot2grid((7, 7), (3, 0), rowspan=4, colspan=7,sharey=ax1)

"""subplot 1 daily avergae"""
y = pd_data[pd_data['Mean Temp (°C)'].notnull()]['Mean Temp (°C)']
x = np.arange(0, len(y))
ax1.plot(x, y, color='grey')

ax1.set_title("Daily Average")
ax1.set_ylabel("Degress Celcius")

ax1.yaxis.set_major_locator(MultipleLocator(5))
ax1.yaxis.grid(linestyle='dashed',color='silver')
ax1.set_xlim(0,356)
ax1.xaxis.set_visible(False)

"""subplot 2 monthly data"""
x1 = list(month_index_classify.values())
y1 = [np.mean(x_item) for x_item in x1]
obs_num = list(month_index_classify.keys())
obs_num_index = [1,2,3,4,5,6,7,8,9,10,11,12]

"""boxplot"""
ax2.boxplot(x1,labels=obs_num,widths=.3,boxprops=dict(color='darkgrey', lw=1.5),
whiskerprops = dict(color='darkgrey', lw=1.5),
medianprops = dict(color='black',lw=1.6,ls=':'),
flierprops= dict(color='black', lw=15),
capprops=dict(color='darkgrey',lw=1.5))
ax2.grid(True, alpha=0.5,linestyle='--',color='silver')
"""barplot"""
ax2.bar(obs_num_index, y1, align='center', width=.7, color='white', edgecolor='darkgrey',hatch='/', lw=1.5)
ax2.set_title("Monthly Mean,Median,Min and Max(of Daily Average)")
ax2.set_ylabel("Degress Celcius")
ax2.yaxis.set_major_locator(MultipleLocator(5))

plt.show()

