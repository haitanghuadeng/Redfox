# -*- coding:utf-8 -*-


# 有关于极坐标系的帮助
# def polar_help(helpme):
#
#     i = ['help', 'more']
#     ii = {'add()': '方法签名',
#           'name -> str': '图例名称',
#           'data -> list': '数据项[极径,极角[数据值]]',
#           'angle_data -> list': '角度类目数据',
#           'radius_data -> list': '半径类目数据',
#           'type -> str': '图例类型，包含["line", "scatter","effectScatter","barAngle", "barRadius"可选。默认为 "line"]',
#           'symbol_size ->int': '标记图形大小，默认为 [4]',
#           'start_angle ->int': '起始刻度的角度，默认为 [90] 度，即圆心的正上方。0度为圆心的正右方',
#           'rotate_step -> int': '刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转放置标签之间重叠，旋转的角度从 [-90] 度到 [90] 度。 默认为 [0]\n',
#           'boundary_gap -> bool': '坐标轴两边留白策略，默认为 [True]，这个时候刻度只是作为分割线，标签和数据点都会在两个刻度之间的带(band)中间\n',
#           'clockwise -> bool': '刻度增长是否按顺时针，默认 [True]',
#           'is_stack=bool': '数据堆叠，同个类目轴上系列配置相同的stack值可以堆叠放置',
#           'axis_range -> list': '坐标轴刻度范围，默认值为 [None, None]。',
#           'angleaxis_label_interval -> int/str': '\n\t坐标轴刻度标签的显示间隔，在类目轴中有效。可以采用标签不重叠的策略间隔显示标签，即(auto)。' +
#                                                  '\n\t可以设置成0强制显示所有标签。如果设置为1，表示【隔一个标签显示一个标签】，' +
#                                                  '\n\t如果值为2，表示隔两个标签显示一个标签，以此类推。默认为0。',
#           'is_angleaxis_show -> bool': '是否显示极坐标系的角度轴，默认为 [True]',
#           'radiusaxis_z_index -> int': 'radius轴的z指数，默认为 [50]',
#           'angleaxis_z_index -> int': 'angle轴的z指数，默认为 [50]',
#           'is_radiusaxis_show -> bool': '是否显示极坐标系的径向轴，默认为 [True]\n',
#           'render_item -> function': '开发者自己提供图形渲染的逻辑，这个渲染逻辑一般命名为render_item, 参考高级用法篇\n'}
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
#         print("传入实参未达到预期值" + "\n可写选项为 polar_help( [help] | [more] )")


class Polar:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'add()': '方法签名',
              'name -> str': '图例名称',
              'data -> list': '数据项[极径,极角[数据值]]',
              'angle_data -> list': '角度类目数据',
              'radius_data -> list': '半径类目数据',
              'type -> str': '图例类型，包含["line", "scatter","effectScatter","barAngle", "barRadius"可选。默认为 "line"]',
              'symbol_size ->int': '标记图形大小，默认为 [4]',
              'start_angle ->int': '起始刻度的角度，默认为 [90] 度，即圆心的正上方。0度为圆心的正右方',
              'rotate_step -> int': '刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转放置标签之间重叠，旋转的角度从 [-90] 度到 [90] 度。 默认为 [0]\n',
              'boundary_gap -> bool': '坐标轴两边留白策略，默认为 [True]，这个时候刻度只是作为分割线，标签和数据点都会在两个刻度之间的带(band)中间\n',
              'clockwise -> bool': '刻度增长是否按顺时针，默认 [True]',
              'is_stack=bool': '数据堆叠，同个类目轴上系列配置相同的stack值可以堆叠放置',
              'axis_range -> list': '坐标轴刻度范围，默认值为 [None, None]。',
              'angleaxis_label_interval -> int/str': '\n\t坐标轴刻度标签的显示间隔，在类目轴中有效。可以采用标签不重叠的策略间隔显示标签，即(auto)。' +
                                                     '\n\t可以设置成0强制显示所有标签。如果设置为1，表示【隔一个标签显示一个标签】，' +
                                                     '\n\t如果值为2，表示隔两个标签显示一个标签，以此类推。默认为0。',
              'is_angleaxis_show -> bool': '是否显示极坐标系的角度轴，默认为 [True]',
              'radiusaxis_z_index -> int': 'radius轴的z指数，默认为 [50]',
              'angleaxis_z_index -> int': 'angle轴的z指数，默认为 [50]',
              'is_radiusaxis_show -> bool': '是否显示极坐标系的径向轴，默认为 [True]\n',
              'render_item -> function': '开发者自己提供图形渲染的逻辑，这个渲染逻辑一般命名为render_item, 参考高级用法篇\n'}

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
            print("传入实参未达到预期值" + "\n可写选项为 polar_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
