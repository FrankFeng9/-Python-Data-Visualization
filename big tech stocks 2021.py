"""A visualization illustrating the gains in three major technology stocks in 2021.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors


"""read csv files and organize data"""
amzn_file_name = 'a5_AMZN.csv'
googl_file_name = 'a5_GOOGL.csv'
msft_file_name = 'a5_MSFT.csv'

amzn_data = pd.read_csv(amzn_file_name,parse_dates=['Date'])
googl_data = pd.read_csv(googl_file_name,parse_dates=['Date'])
msft_data = pd.read_csv(msft_file_name,parse_dates=['Date'])

amzn_data['ratio'] = np.nan
amzn_data_basis = amzn_data['Open'][0]
amzn_data['ratio'] = amzn_data['Open']/amzn_data_basis*100
amzn_data = amzn_data.loc[:,['Date','ratio']]

googl_data['ratio'] = np.nan
googl_data_basis = googl_data['Open'][0]
googl_data['ratio'] = googl_data['Open']/googl_data_basis*100
googl_data = googl_data.loc[:,['Date','ratio']]

msft_data['ratio'] = np.nan
msft_data_basis = msft_data['Open'][0]
msft_data['ratio'] = msft_data['Open']/msft_data_basis*100
msft_data = msft_data.loc[:,['Date','ratio']]


"""setup the figure and axes"""
fig = plt.figure(figsize=(8,6),dpi=100)
ax1 = fig.add_subplot(projection='3d')
ax2 = fig.gca(projection='3d')
ax1.set_title('Tech Stock Gains for 2021',fontsize=13)
width =1
depth = 0


"""Amazon figure """
_x = np.arange(-20,231,1)
_y = np.zeros(1)
_z = amzn_data['ratio'].values-91
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = _z
bottom = np.zeros_like(top)+90
ax1.bar3d(x, y, bottom, width, depth, top, alpha=0.2, shade=True,color='turquoise')
ax2.plot(_x, _z+90, zs=0, zdir='y',color='black')

"""Microsoft figure"""
_x = np.arange(-20,231,1)
_y = np.zeros(1)+1
_z = msft_data['ratio'].values-90
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = _z
bottom = np.zeros_like(top)+90
ax1.bar3d(x, y, bottom, width, depth, top,alpha=0.2,  shade=True,color='darkviolet')
ax2.plot(_x, _z + 90, zs=1, zdir='y',color='black')

"""Google figure"""
_x = np.arange(-20,231,1)
_y = np.zeros(1)+2
_z = googl_data['ratio'].values-90
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = _z
bottom = np.zeros_like(top)+90
ax1.bar3d(x, y, bottom, width, depth, top,alpha=0.2, shade=True,color='yellow')
ax2.plot(_x, _z + 90, zs=2, zdir='y',color='black')

ax1.view_init(elev=10, azim=-65)
plt.xticks(np.arange(0,250,21), rotation=70,labels=['Jan','Feb','March','Apr','May','Jun','Jul','Aug',
                                    'Sep','Oct','Nov','Dec'])
plt.yticks(np.arange(0,3,1), labels=['Amazon', 'Microsoft', 'Google'])
ax1.set_zticklabels(labels=['90%','100%','110%','120%','130%','140%','150%'])

ax1.set_zlim3d(91,150)

plt.show()
