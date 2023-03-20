"""A Python script capable of reading a CSV file and plotting the frequency of technologies used by students in their coop placements in a pie chart.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as cls
from matplotlib import patheffects
import random

def read_data(path):
    """Read csv file and arrange data in key/value pairs
    Arguments:
    path -- file path
    Return Value:
    a dictionary of organized data
    """
    technology_dict = {}

    try:
        file = pd.read_csv(path)
        for line in file['FALL 2021 Co-op Technologies']:
            if line.upper() not in [i.upper() for i in technology_dict.keys()]:
                technology_dict.update({line:1})
            else:
                for i in technology_dict.keys():
                    if line.upper() == i.upper():
                        technology_dict[i] += 1
    except pd.Error as e:
        print("Error reading CSV file at line %s: %s" % (file.line_num, e))
        sys.exit(-1)

    data_dict = {' ':0}
    """sort dict in order"""
    for key, value in technology_dict.items():
        if value == 1:
            data_dict[' '] += 1
        else:
            data_dict.update({key:value})
    data_dict = dict(sorted(data_dict.items(), key=lambda item:item[1]))
    return data_dict

def percentage_value(val):
    """format percentage values for autopct
    Arguments:
    val -- numeric value
    Return Value:
    formatted percentage values
    """
    val  = np.round(val/100*100., 0)
    if 2 < val < 20:
        return "%.0f%%"%(val)
    elif val > 20:
        """for 'Other' category """
        return "\n\nOther\n\n%.0f%%\n\nMany Specialized Technologies\nWere Reported Only Once"%(val)



technology_dict = read_data('a3_2021f_coop_tech.csv')

labels = [i for i in technology_dict.keys()]
sizes = [i for i in technology_dict.values()]
explode = [0.1 if i == max(sizes) else 0 for i in sizes ]

"""generate random colors"""
colors = random.choices(list(cls.CSS4_COLORS.values()),k = len(sizes))

plt.figure(figsize=(8, 6), dpi=100)

plt.pie(x=sizes, explode=explode, labels=labels, colors=colors, autopct=percentage_value, pctdistance=0.9, shadow=False, startangle=143, radius=0.8, textprops=None, center=(0,0), rotatelabels=True)

title_text_obj = plt.title('Technologies Used by COOPs in Fall 2021', fontsize= 13, fontweight = "bold")
title_text_obj.set_path_effects([patheffects.withSimplePatchShadow()])

plt.show()





