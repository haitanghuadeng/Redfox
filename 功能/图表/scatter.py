# -*- coding:utf-8 -*-


# 有关于散点图的帮助
# def scatter_help(helpme):
#
#     i = ['help', 'more']
#     ii = {
#         'name -> str': '图例名称',
#         'x_axis -> list': 'x坐标轴数据',
#         'y_axis -> list': 'y坐标轴数据',
#         'extra_data -> list[int]': '第三维度数据，x轴为第一个维度，y轴为第二个维度。（可在visualmap中将视图元素映射到第三维度）',
#         'extra_name -> list[str]': '额外的数据项的名称，可以为每个数据点指定一个名称',
#         'symbol_size -> int': '标记图形大小，默认为10',
#         '\tNote': '请配合 通用配置项 中的Visualmap使用',
#         'draw()': 'Scatter还内置了画画方式',
#         '\tpath -> str': '转换图片的地址',
#         '\tcolor -> str': '所要排除的颜色',
#         'Note': '\n\t关于gird3D部分的设置，请参照通用配置项中的介绍 通用配置项' + '\n\t可配合axis3D通用配置项一起使用'}
#
#     value = helpme
#     if value in i:
#         print("From dictionaries read INFO")
#         if value == i[0]:
#             for key in ii.keys():
#                 print(key)
#         elif value == i[1]:
#             for key in ii.keys():
#                 print(key + ii[key])
#     else:
#         print("传入实参未达到预期值" + "\n可写选项为 scatter_help( [help] | [more] )")


class Scatter:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {
            'name -> str': '图例名称',
            'x_axis -> list': 'x坐标轴数据',
            'y_axis -> list': 'y坐标轴数据',
            'extra_data -> list[int]': '第三维度数据，x轴为第一个维度，y轴为第二个维度。（可在visualmap中将视图元素映射到第三维度）',
            'extra_name -> list[str]': '额外的数据项的名称，可以为每个数据点指定一个名称',
            'symbol_size -> int': '标记图形大小，默认为10',
            '\tNote': '请配合 通用配置项 中的Visualmap使用',
            'draw()': 'Scatter还内置了画画方式',
            '\tpath -> str': '转换图片的地址',
            '\tcolor -> str': '所要排除的颜色',
            'Note': '\n\t关于gird3D部分的设置，请参照通用配置项中的介绍 通用配置项' + '\n\t可配合axis3D通用配置项一起使用'}

        value = self.helpme
        if value in i:
            print("From dictionaries read INFO")
            if value == i[0]:
                for key in ii.keys():
                    print(key)
            elif value == i[1]:
                for key in ii.keys():
                    print(key + ii[key])
        else:
            print("传入实参未达到预期值" + "\n可写选项为 scatter_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
