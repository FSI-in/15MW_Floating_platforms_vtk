import vtkmodules.all as vtk
import os

class vtp_change():

	def __init__(self):
		pass

	def change(self, x, y, z, rx, ry, rz, i):

		# 指定输出文件夹的路径
		output_folder = "vtk"

		# 读取vtp文件
		input_file = "1.vtp"
		# 输出vtp文件名字
		# 输出vtp文件名字
		output_file = os.path.join(output_folder, f'IEA-15-240-RWT-UMaineSemi.Platform.{str(i).zfill(5)}.vtp')

		# 确保输出文件夹存在，如果不存在则创建它
		if not os.path.exists(output_folder):
			os.makedirs(output_folder)
		
		# 读取VTP文件
		reader = vtk.vtkXMLPolyDataReader()
		reader.SetFileName(input_file)
		reader.Update()

		# 获取几何数据
		polydata = reader.GetOutput()

		# 创建平移和旋转变换
		transform = vtk.vtkTransform()
		# 先进行旋转变换
		transform.RotateWXYZ(rx, 1, 0, 0)  # 绕Y轴旋转90度
		transform.RotateWXYZ(ry, 0, 1, 0)  # 绕Y轴旋转90度
		transform.RotateWXYZ(rz, 0, 0, 1)  # 绕Y轴旋转90度
		# 平移变换
		transform.Translate(x, y, z)  # 平移操作，例如在Z轴上平移1个单位


		# 应用变换到几何数据
		transform_filter = vtk.vtkTransformFilter()
		transform_filter.SetInputData(polydata)
		transform_filter.SetTransform(transform)
		transform_filter.Update()

		# 保存变换后的几何数据为新的VTP文件
		writer = vtk.vtkXMLPolyDataWriter()
		writer.SetFileName(output_file)
		writer.SetInputData(transform_filter.GetOutput())
		writer.Write()

		print("文件保存成功")
