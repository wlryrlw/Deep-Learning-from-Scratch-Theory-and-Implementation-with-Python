import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im

x = np.arange(0, 6, 0.1) # 单位0.1，生成0-6的数据
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin") # 作图y1，标签
plt.plot(x, y2, linestyle = "--", label="cos") # 作图y2，虚线，标签

plt.xlabel("x") # x轴标签
plt.ylabel("y") # y轴标签
plt.title("sin & cos") # 标题

plt.legend() # 添加图例
plt.show() # 显示

img = im.imread(".\dataset\lena.png") # 导入图像
plt.imshow(img)
plt.show()
