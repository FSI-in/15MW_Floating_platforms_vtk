# 15MW_Floating_platforms_vtk
此代码是生成openfast IEA-15MW 浮式平台可视化代码

使用说明：python3 main.py

设置说明：
openfast中时间步长设置成0.01， 0.001, 0.0001 ... (建议这样)
输出的时间步长与计算时间步长要相同
必须输出outb文件
可视化帧数为10
在ElastoDyn中的输出参数中加上以下参数

"PtfmTDxi" ————平台纵荡（前后）

"PtfmTDyi" ————平台横荡（左右）

"PtfmTDzi" ————平台垂荡（上下）

"PtfmRDxi" ————平台横摇（左右）

"PtfmRDyi" ————平台纵摇（前后）

"PtfmRDzi" ————平台艏摇（偏航摇）

然后吧outb文件重命名为1.outb

然后执行：python3 main.py
