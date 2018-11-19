# -*- coding:utf-8 -*-


# 有关于地图的帮助
# def map_help(helpme):
#
#     i = ['help', 'more']
#     ii = {'name -> str': '图例名称',
#           'attr -> list': '属性名称',
#           'value -> list': '属性所对应的值',
#           'maptype -> str': '\n\t地图类型。从pyecharts V0.3.2+起，地图已经变为扩展包，' +
#           '\n\t支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 [地图自定义篇]',
#           'is_roam -> bool/str': '\n\t是否开启鼠标缩放和平移漫游，默认为True。' +
#           '\n\t如果只想要开启缩放或者平移，可以设置成"scale"或者"more"。设置成True为都开启。',
#           'is_map_symbol_show -> bool': '是否显示地图标记红点，默认为True',
#           'name_map -> dict':
#           '\n\t[用自定义的地图名称], 有些地图提供行政区号，name_map 可以帮助把它们转换成用户满意的地名。' +
#           '\n\t比如英国选区地图，伦敦选区的行政号是E14000639，把它转换成可读地名就需要这么一个字典' +
#           '\n\t以此类推，把英国选区所有的地名都转换一下，就需要个 [更大一些的字典]',
#           'Note': '\n\t请配合 通用配置项 中的 Visualmap 使用' +
#           '\n\t设置 pieces 自定义 visualMap 组件标签'}
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
#         print("传入实参未达到预期值" + "\n可写选项为 map_help( [help] | [more] )")


class Map:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'attr -> list': '属性名称',
              'value -> list': '属性所对应的值',
              'maptype -> str': '\n\t地图类型。从pyecharts V0.3.2+起，地图已经变为扩展包，' +
                                '\n\t支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 [地图自定义篇]',
              'is_roam -> bool/str': '\n\t是否开启鼠标缩放和平移漫游，默认为True。' +
                                     '\n\t如果只想要开启缩放或者平移，可以设置成"scale"或者"more"。设置成True为都开启。',
              'is_map_symbol_show -> bool': '是否显示地图标记红点，默认为True',
              'name_map -> dict':
                  '\n\t[用自定义的地图名称], 有些地图提供行政区号，name_map 可以帮助把它们转换成用户满意的地名。' +
                  '\n\t比如英国选区地图，伦敦选区的行政号是E14000639，把它转换成可读地名就需要这么一个字典' +
                  '\n\t以此类推，把英国选区所有的地名都转换一下，就需要个 [更大一些的字典]',
              'Note': '\n\t请配合 通用配置项 中的 Visualmap 使用' +
                      '\n\t设置 pieces 自定义 visualMap 组件标签'}

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
            print("传入实参未达到预期值" + "\n可写选项为 map_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
