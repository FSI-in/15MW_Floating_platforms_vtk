
#此代码应该在out文件夹下来处理已经存转存到该文件夹下的outb文件

#首先遍历当前文件夹下的所有.outb文件。

#然后把每个文件的特定值提取出来

#然后做处理

import numpy as np
from pyFAST.input_output import FASTOutputFile
import os
import glob



# 读取outb文件并且输入到字典中
class open_fast_data:
	def __init__(self):
		pass


	def open_data(self):

		print("正在读取数据，请等待...")

		# 获取当前文件夹路径
		folder_path = os.getcwd()

		# 获取所有.outb文件的文件名
		outb_files = glob.glob(os.path.join(folder_path, '*.outb'))

		fast = {}
		# 遍历所有.outb文件并打开它们
		for outb_file in outb_files:
			# 提取文件名（不包含扩展名）
			file_name = os.path.splitext(os.path.basename(outb_file))[0]

			# 使用FASTOutputFile打开文件并将其内容存储在变量中
			# 将小数点替换为下划线
			df = FASTOutputFile(outb_file).toDataFrame()
			# 输出所有参数的名称
			for column_name in df.columns:
				fast[column_name + '_' + file_name] = np.array(df[column_name])
				#print(fast['Time_[s]_1'])

			self.fast = fast

		print("读取数据完成")



