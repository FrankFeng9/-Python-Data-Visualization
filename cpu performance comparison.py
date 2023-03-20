""" a Python script capable of reading in an unstructured list of CPU benchmark
performance numbers, plot the CPU performance vs cost and vs GHz in a pair of
subfigures. List the best performing CPUs for a generation.
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib as mpl

CPU_GEN = None

while True:
    """user select specific Intel CPU generation"""
    try:
        CPU_GEN = int(input("Plese select a specific Intel CPU generation form 4th to 11th:"))
    except:
        print("Error,please re-enter")
    if type(CPU_GEN) == int:
        if int(CPU_GEN) >=4 and int(CPU_GEN) <=11:
            break
    print("Error, plase re-enter")


CPU_lst = []
intel_CPU_lst = []
CPU_mark_lst = []
CPU_GHz_lst = []
CPU_gen_lst = []
CPU_price_lst = []
gen_info = ['i3', 'i5', 'i7', 'i9']


try:
    file = open("a2_cpu_amd_intel.txt")
    """reading data form txt file"""
    for line in file:
        if '#' in line or '\n' == line:
            pass
        elif 'GHz' not in line or '$' not in line:
            pass
        else:
            CPU_lst.append(line.strip())
except IOError:
    print("Error: file not found")


intel_CPU_lst = [x for x in CPU_lst if '-' in x]
"""list the Intel CPUs"""
for i in intel_CPU_lst:
    gen = i[i.find('-'):]
    gen = gen[1:gen.find(' ')]
    CPU_gen_lst.append(gen)

CPU_gen_lst = []


for i in intel_CPU_lst:
    """data of CPU generation"""
    gen = i[i.find('-'):]
    gen = gen[1:gen.find(' ')]
    CPU_gen_lst.append(gen)

for i in intel_CPU_lst:
    """reading data of CPU clock speed"""
    GHz = i[i.find('@'):]
    GHz = GHz[2:GHz.find('GHz')]
    CPU_GHz_lst.append(GHz)

for i in intel_CPU_lst:
    """reading data of CPU benchmark"""
    mark = i.split(' ')[-2]
    mark = mark.replace(',', '')
    CPU_mark_lst.append(mark)

for i in intel_CPU_lst:
    """reading data of CPU price"""
    price = i.split(' ')[-1]
    price = price.replace('$', '').replace('*', '').replace(',', '')
    CPU_price_lst.append(price)


try:
    CPU_mark_lst = [round(float(x), 2) for x in CPU_mark_lst]
    CPU_price_lst = [round(float(x), 2) for x in CPU_price_lst]
    CPU_GHz_lst = [round(float(x), 2) for x in CPU_GHz_lst]
except ValueError:
    print("Format Error")


select_gen_index = []

try:
    """getting the required generations"""
    if CPU_GEN > 0:
        if CPU_GEN >= 10:
            for i in range(len(CPU_gen_lst)):
                gen = ''.join(list(filter(str.isdigit, CPU_gen_lst[i])))
                if int(gen) >= 10000 and int(gen[0:2]) == int(CPU_GEN):
                    select_gen_index.append(i)
        else:
            for i in range(len(CPU_gen_lst)):
                gen = ''.join(list(filter(str.isdigit, CPU_gen_lst[i])))
                if int(gen) < 10000 and int(gen[0: 1]) == int(CPU_GEN):
                    select_gen_index.append(i)
    else:
        select_gen_index = list(range(len(CPU_gen_lst)))
except ValueError:
    print("Error")


series_select_index = [[], [], [], []]
frag_select_index = [[], [], [], []]

for i in range(len(intel_CPU_lst)):
    if 'i3' in intel_CPU_lst[i]:
        series_select_index[0].append(i)
    if 'i5' in intel_CPU_lst[i]:
        series_select_index[1].append(i)
    if 'i7' in intel_CPU_lst[i]:
        series_select_index[2].append(i)
    if 'i9' in intel_CPU_lst[i]:
        series_select_index[3].append(i)

for i in range(len(select_gen_index)):
    if 'i3' in intel_CPU_lst[select_gen_index[i]]:
        frag_select_index[0].append(select_gen_index[i])
    if 'i5' in intel_CPU_lst[select_gen_index[i]]:
        frag_select_index[1].append(select_gen_index[i])
    if 'i7' in intel_CPU_lst[select_gen_index[i]]:
        frag_select_index[2].append(select_gen_index[i])
    if 'i9' in intel_CPU_lst[select_gen_index[i]]:
        frag_select_index[3].append(select_gen_index[i])


best_GHZ_index = [-1, -1, -1, -1]
best_price_index = [-1, -1, -1, -1]
for i in range(len(frag_select_index)):
    """find the best CPUs of specific generations"""
    best_GHZ = 0.00
    best_price = 0.00
    CPU_num = len(frag_select_index[i])
    for j in range(CPU_num):
        temp = CPU_mark_lst[j]
        if temp > best_GHZ:
            best_GHZ = temp
            best_GHZ_index[i] = frag_select_index[i][j]
    for j in range(CPU_num):
        temp = CPU_mark_lst[j]
        if temp > best_price:
            best_price = temp
            best_price_index[i] = frag_select_index[i][j]



plt.figure(figsize=(18, 8), dpi=50)
plt.rc('xtick', labelsize=17)
plt.rc('ytick', labelsize=17)
xmajorLocator = MultipleLocator(0.5)
ymajorLocator = MultipleLocator(500)

ax = plt.subplot(1, 2, 1)
"""subplot one: Benchmark vs clock speed"""

ax.set_xlim(1.0, 4.5)
ax.set_ylim(500, 4500)

x = [[], [], [], []]
y = [[], [], [], []]
for i in range(len(series_select_index)):
    for j in series_select_index[i]:
        x[i].append(CPU_GHz_lst[j])
for i in range(len(series_select_index)):
    for j in series_select_index[i]:
        y[i].append(CPU_mark_lst[j])

ax.set_title('Intel Single Core Performance vs. Clock Speed', size=18)
ax.set_xlabel('Clock Speed in GHz', size=18)

plt.text(0.05, 0.96, 'Best ' + str(CPU_GEN) + 'th Gen Intel Processors', fontsize=18,
         horizontalalignment='center',
         verticalalignment='center', ha='left',
         transform=ax.transAxes)

ax.set_ylabel('cpuMark', size=18)

ax.scatter(x[0], y[0], 180, c='tab:blue', marker='^', label=gen_info[0])
ax.scatter(x[1], y[1], 180, c='orange', marker='x', label=gen_info[1])
ax.scatter(x[2], y[2], 180, c='g', marker='*', label=gen_info[2])
ax.scatter(x[3], y[3], 180, c='r', marker='o', label=gen_info[3])

arrowprops = dict(ls="-.", arrowstyle="->", color="black", lw=2.5)

for i in range(0, 4):
    if (best_price_index[i] == -1):
        continue
    ax.annotate(gen_info[i] + "-" + CPU_gen_lst[best_GHZ_index[i]], (
        CPU_GHz_lst[best_GHZ_index[i]], CPU_mark_lst[best_GHZ_index[i]]),
                xytext=(0.143, 0.68 + i * 0.04), textcoords='figure fraction', arrowprops=arrowprops, size=18)

plt.legend(fontsize=15,loc ="lower left" )


ax = plt.subplot(1, 2, 2)
"""subplot two: Benchmark vs cost"""
ax.set_xscale('log')
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.set_xticks([25, 50, 100, 250, 500, 1000, 2500])
ax.set_ylim(500, 4500)

x = [[], [], [], []]
y = [[], [], [], []]

for i in range(len(series_select_index)):
    for j in series_select_index[i]:
        x[i].append(CPU_price_lst[j])
for i in range(len(series_select_index)):
    for j in series_select_index[i]:
        y[i].append(CPU_mark_lst[j])

ax.set_title('Intel Single Core Performance vs. Cost', size=18)
ax.set_xlabel('Price in USD', size=18)
plt.text(0.05, 0.96, 'Best ' + str(CPU_GEN) + 'th Gen Intel Processors', fontsize=18,
         horizontalalignment='center',
         verticalalignment='center', ha='left',
         transform=ax.transAxes)
ax.set_ylabel('cpuMark', size=20)

ax.scatter(x[0], y[0], 180, c='tab:blue', marker='^', label='i3')
ax.scatter(x[1], y[1], 180, c='orange', marker='x', label='i5')
ax.scatter(x[2], y[2], 180, c='g', marker='*', label='i7')
ax.scatter(x[3], y[3], 180, c='r', marker='o', label='i9')

for i in range(0, 4):
    if (best_price_index[i] == -1):
        continue
    ax.annotate(gen_info[i] + "-" + CPU_gen_lst[best_price_index[i]], (
        CPU_price_lst[best_price_index[i]], CPU_mark_lst[best_price_index[i]]),
                xytext=(0.567, 0.68 + i * 0.04), textcoords='figure fraction', arrowprops=arrowprops, size=18)
plt.show()
print()


