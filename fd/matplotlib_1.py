import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
data_1 = pd.read_csv("titanic_dataset.csv")
print(data_1[0:5])
plt.plot(data_1["ticket"],data_1["fare"])
plt.xticks(rotation=90)
plt.show()

figure = plt.figure()
ax_1 = figure.add_subplot(2,3,1)
ax_2 = figure.add_subplot(2,3,2)
ax_3 = figure.add_subplot(2,3,4)
fig_1 = ax_1.plot(np.random.randint(1,5,5),np.arange(5))
fig_2 = ax_2.plot(np.sin(np.random.random(5)),np.arange(5))
plt.show()

data = pd.DataFrame({"age":np.random.random(100),
                     "weight":np.random.random(100)})

bar_heights = data[0:5]["weight"]
bar_positions = np.arange(5)+0.75
print(bar_heights)
print(bar_positions)
#ax = plt.subplots()
plt.bar(bar_positions,bar_heights,0.3)
#ax.bar(bar_positions,bar_heights,0.3)
plt.show()

plt.scatter(data['age'],data['weight'],c='red')
plt.xlabel("age")
plt.ylabel("weight")
plt.show()

x = np.linspace(-2*np.pi,2*np.pi,1000)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,color='r',linestyle='--',linewidth=2,alpha=0.8,label="sin")
plt.plot(x,y2,color='g',linewidth=2,alpha=0.8,label="cos")
plt.xlabel("X")
plt.ylabel("y")
plt.title("tu")
plt.legend()
plt.show()


x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
size = np.random.normal(50, 60, 10)
print(size)
plt.scatter(x, y, s=size, c=colors)
plt.show()

label = ['Cat', 'Dog', 'Cattle', 'Sheep', 'Horse']  # 各类别标签
color = ['r', 'g', 'r', 'g', 'y']  # 各类别颜色
size = [1, 2, 3, 4, 5]  # 各类别占比
explode = (0, 0, 0, 0, 0.2)  # 各类别的偏移半径
# 绘制饼状图
plt.pie(size, colors=color, explode=explode,
        labels=label, shadow=True, autopct='%1.1f%%')
# 饼状图呈正圆
plt.axis('equal')
plt.show()

x = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
y_bar = [3, 4, 6, 8, 9, 10, 9, 11, 7, 8]
y_line = [2, 3, 5, 7, 8, 9, 8, 10, 6, 7]

plt.bar(x, y_bar)
plt.plot(x, y_line, '-o', color='y')
plt.show()
'''
# fig = plt.figure()
# axes = fig.add_axes([0.5,0.5,0.8,0.8])
# axes.plot(x,y,'r')
# plt.show()

# fig = plt.figure()  # 新建画板
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # 大画布
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
# axes1.plot(x,y,'r')
# axes2.plot(x,y,'b')
# plt.show()
# fig,axes = plt.subplots(nrows=2,ncols=3,figsize=(16,9),dpi=50)
# for i in range(2):
#     for ax in axes[i]:
#         ax.plot(x,y,'-o',color='r')
# plt.show()
# fig = plt.figure()
# axes.set_xlabel("x_label")
# axes.set_ylabel("y_label")
# axes.plot(x,x**2,color='r',alpha=0.5,linewidth=2)
# axes.plot(x,x**3,color='b',linewidth=2,ls=':',marker='+',markersize=2,markerfacecolor="yellow")
# axes.legend(["y = x**2", "y = x**3"], loc=0)
# plt.show()
# ax_1 = fig.add_subplot(2,2,1)
# ax_2 = fig.add_subplot(2,2,2)
# ax_1.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
# ax_2.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
#
# plt.show()
# x = np.linspace(0,10,20)
# y = x*x+2
# fig, axes = plt.subplots(1, 2, figsize=(10, 5))
# axes[0].plot(x,x**2,lw=2,ls=":",color="b",marker="+",markersize=2)
# axes[0].grid(True)
# plt.show()
# n = np.array([0,1,2,3,4,5])
# fig,axes = plt.subplots(2,2,figsize=(10,5))
# axes[0,0].plot(n,n,color='r',lw=2,ls=":",marker="+",markerfacecolor="b")
# axes[0,1].scatter(np.random.randint(1,10,100),np.random.randint(1,10,100),color='b')
# axes[1,0].step(n,n**2,lw=2)
# axes[1,1].bar(n,n**2,align="center")
# plt.show()
# fig, axes = plt.subplots()
#
# x_bar = [10, 20, 30, 40, 50]  # 柱形图横坐标
# y_bar = [0.5, 0.6, 0.3, 0.4, 0.8]  # 柱形图纵坐标
# bars = axes.bar(x_bar, y_bar, color='blue', width=2)  # 绘制柱形图
# print(list(enumerate(bars)))
# for i, rect in enumerate(bars):
#     x_text = rect.get_x()  # 获取柱形图横坐标
#     y_text = rect.get_height()+0.01  # 获取柱子的高度并增加 0.01
#     print(x_text,y_text)
#     plt.text(x_text, y_text, '%.2f' % y_bar[i])  # 标注文字
#     plt.annotate('Min', xy=(32, 0.3), xytext=(36, 0.3),
#                  arrowprops=dict(facecolor='black', width=1, headwidth=7))
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
ax = plt.gca()
ax.set_ylim([-2*np.pi,2*np.pi])
ax.set_xlim([-2*np.pi,2*np.pi])
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

a = np.arange(-np.pi,np.pi,np.pi/1000)
x = np.cos(2*a)*np.cos(a)
y = np.cos(2*a)*np.sin(a)
ax.plot(x,y)
ax.fill_between(x,y)
plt.show()
