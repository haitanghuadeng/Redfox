# -*- coding:utf-8 -*-


# 有关于雷达图的帮助
# def radar_help(helpme):
#
#     i = ['help', 'more']
#     ii = {
#         'name -> str': '图例名称',
#         'value -> [list]': '包含列表的列表' + '数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
#         'item_color -> str': '指定单图例颜色',
#         'schema -> list': r'默认雷达图的指示器，用来指定雷达图中的多个维度，会对数据处理成{name: xx, value: xx}的字典',
#         'c_schema -> dict': '用户自定义雷达图的指示器，用来指定雷达图中的多个维度',
#         '\t·name': '指示器名称',
#         '\t·min': '指示器最小值',
#         '\t·max': '指示器最大值',
#         'shape -> str': '雷达图绘制类型，有"polygon"（多边形）和"circle"可选',
#         'rader_text_color -> str': '雷达图数据项字体颜色，默认为"#000"',
#         'radar_text_size -> int': '雷达图数据项字体大小，默认为12',
#         'is_area_show -> bool': '是否填充区域',
#         'area_opacity  -> float': '填充区域颜色',
#         'is_splitline_show -> bool': '是否显示分割线，默认为True',
#         'is_axisline_show -> bool': '是否显示坐标轴线，默认为True',
#         'Note': '\n\t可配置lineStyle参数' + '\n\tsymblo=None 可隐藏标记图形(小圆圈)'}
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
#         print("传入实参未达到预期值" + "\n可写选项为 radar_help( [help] | [more] )")


class Radar:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {
            'name -> str': '图例名称',
            'value -> [list]': '包含列表的列表' + '数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
            'item_color -> str': '指定单图例颜色',
            'schema -> list': r'默认雷达图的指示器，用来指定雷达图中的多个维度，会对数据处理成{name: xx, value: xx}的字典',
            'c_schema -> dict': '用户自定义雷达图的指示器，用来指定雷达图中的多个维度',
            '\t·name': '指示器名称',
            '\t·min': '指示器最小值',
            '\t·max': '指示器最大值',
            'shape -> str': '雷达图绘制类型，有"polygon"（多边形）和"circle"可选',
            'rader_text_color -> str': '雷达图数据项字体颜色，默认为"#000"',
            'radar_text_size -> int': '雷达图数据项字体大小，默认为12',
            'is_area_show -> bool': '是否填充区域',
            'area_opacity  -> float': '填充区域颜色',
            'is_splitline_show -> bool': '是否显示分割线，默认为True',
            'is_axisline_show -> bool': '是否显示坐标轴线，默认为True',
            'Note': '\n\t可配置lineStyle参数' + '\n\tsymblo=None 可隐藏标记图形(小圆圈)'}

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
            print("传入实参未达到预期值" + "\n可写选项为 radar_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
