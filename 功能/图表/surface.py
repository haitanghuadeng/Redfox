# -*- coding:utf-8 -*-


# 有关于3D曲面图的帮助
# def surface_help(helpme):
#
#     i = ['help', 'more']
#     ii = {
#         'name -> str': '图例名称',
#         'data -> [list]/ndarray': '\n\t包含列表的列表' + '\n\t数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
#         'grid3d_opactiy -> str': '3D笛卡尔坐标系组的透明度，默认为1，完全不透明',
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
#         print("传入实参未达到预期值" + "\n可写选项为 surface_help( [help] | [more] )")


class Surface:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {
            'name -> str': '图例名称',
            'data -> [list]/ndarray': '\n\t包含列表的列表' + '\n\t数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
            'grid3d_opactiy -> str': '3D笛卡尔坐标系组的透明度，默认为1，完全不透明',
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
            print("传入实参未达到预期值" + "\n可写选项为 surface_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
