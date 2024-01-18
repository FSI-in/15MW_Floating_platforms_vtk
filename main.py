
import numpy as np
from input_outb import *
from vtp_change import *

# 主文件


# 创建fast输出文件对象
data = open_fast_data()
# 提取变量到字典
data.open_data()

vtp_run = vtp_change()

# 二者对比图
x = data.fast['PtfmTDxi_[m]_1']
y = data.fast['PtfmTDyi_[m]_1']
z = data.fast['PtfmTDzi_[m]_1']
rx = data.fast['PtfmRDxi_[deg]_1']
ry = data.fast['PtfmRDyi_[deg]_1']
rz = data.fast['PtfmRDzi_[deg]_1']

print(x.shape)

z_number = int(input("请输入可视化帧数(注意，这要与openfast中设置一样)："))
dt = float(input("请输入openfast计算时间步长："))
td = 1 / dt

result = td / z_number

i = 0
if result % 1 == 0:
    jump = int(result)

    while True:
        if i * jump > int(x.shape[0]):
            break
        vtp_run.change(x[i*jump], y[i*jump], z[i*jump], rx[i*jump], ry[i*jump], rz[i*jump], i)
        i += 1

else:
    print("不是整数")




