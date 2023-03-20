"""Ice Cream Cone Sales
"""

import matplotlib.pyplot as plt
import numpy as np
import calendar
from matplotlib.pyplot import MultipleLocator
import matplotlib.patheffects as path_effects
import matplotlib.ticker as mticker
np.random.seed(seed=1)


sales_raw=[0,1,2,4,5.5,6.7,7.5,8,7.5,7,5,2,1,0.5,0]
def tot_sales(day):
    """Return total sales in dollars for day of the year (0-364)"""
    f2 = 0
    if (day >= 0 and day < 365):
        f1 = (day % 28) / 28
    f2 = (1-f1) * sales_raw[day // 28] + f1 * sales_raw[day // 28 + 1]
    tot = 7 + f2*5 + abs(np.random.normal(2*f2,f2+10))
    return tot * 10


day = list(range(0, 365))
sales = list(map(tot_sales, day))
max = max(sales)
max_index = sales.index(max)
min = min(sales)
min_index = sales.index(min)

plt.figure(figsize=(8, 6))
plt.ylabel("Monthly Sales(Dollars)", fontsize=10)

ax = plt.gca()
ax.set_title("Ice Cream Cone Sales vs. Month", fontsize=22,path_effects=[path_effects.withSimplePatchShadow()])
mdays = calendar.mdays[1:]


month_values = []
days_count = 0
for days in mdays:
    """organize days data"""
    month_value = np.mean(sales[days_count:days_count+days])
    days_count = days_count+days
    month_values.append(month_value)

mean_all = np.mean(month_values)

"""plot scatter and bar graph"""
plt.scatter(np.array(day) / 365*12-0.5, sales, marker='v', s=20, c='r', vmax=0, vmin=100,zorder=2,label="Daily Sales")
plt.bar(np.arange(12), month_values,color='darkkhaki',width=0.9,label='Monthly AVG',zorder=1)

plt.axhline(mean_all,linestyle="-.",color="black",label="Avg = $432.83")
arrowprops = dict(arrowstyle="->", color="black", lw=1.0)


""" max and min sales"""
plt.scatter([max_index/365*12-0.5], [max], marker='o', s=70, c='r', edgecolors='black',zorder=3, label="Max/Min Sales")
plt.scatter([min_index/365*12-0.5], [min], marker='o', s=70, c='r', edgecolors='black',zorder=4)

plt.annotate('Yearly Max = $' + str(round(max, 2)), xy=(max_index/365*12-0.5, max), xytext=(-0.5, 1100), arrowprops=arrowprops,fontweight="bold")
plt.annotate('Yearly Min = $' + str(round(min, 2)), xy=(min_index/365*12-0.5, min), xytext=(-0.5, 1050), arrowprops=arrowprops,fontweight="bold")


y_major_locator = MultipleLocator(200)
ax.yaxis.set_major_locator(y_major_locator)
ax.set_ylim(0, 1199)
x_major_locator = MultipleLocator(1)
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlim(-0.7, 11.7)
ax.grid(axis="y",linestyle="--")

plt.xticks(np.arange(0,12,1), labels=['Jan','Feb','March','Apr','May','Jun','Jul','Aug',
                                    'Sep','Oct','Nov','Dec'])
for item in ax.get_yticklabels():
    item.set_fontweight("bold")

legend_properties = {'weight':'bold'}
plt.legend(prop=legend_properties)

plt.show()


