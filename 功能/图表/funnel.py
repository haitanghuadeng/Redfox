# -*- coding:utf-8 -*-


# 有关于漏斗图的帮助
# def funnel_help(helpme):
#
#     i = ['help', 'more']
#     ii = {'name -> str': '图例名称',
#           'attr -> list': '属性名称',
#           'value -> list': '属性所对应的值',
#           'funnel_sort -> str/func': '数据排序，可以取“ascending”、“descending”、“none”(表示按data顺序，即不排序)',
#           'funnel_gap -> int': '数据图形间距，默认为0。'}
#
#     value = helpme
#     if value in i:
#         print("From dictionaries read INFO_help")
#         if value == i[0]:
#             for key in ii.keys():
#                 print(key)
#         elif value == i[1]:
#             for key in ii.keys():
#                 print(key + ii[key])
#     else:
#         print("传入实参未达到预期值" + "\n可写选项为 funnel_help( [help] | [more] )")


class Funnel:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'attr -> list': '属性名称',
              'value -> list': '属性所对应的值',
              'funnel_sort -> str/func': '数据排序，可以取“ascending”、“descending”、“none”(表示按data顺序，即不排序)',
              'funnel_gap -> int': '数据图形间距，默认为0。'}

        value = self.helpme
        if value in i:
            print("From dictionaries read INFO_help")
            if value == i[0]:
                for key in ii.keys():
                    print(key)
            elif value == i[1]:
                for key in ii.keys():
                    print(key + ii[key])
        else:
            print("传入实参未达到预期值" + "\n可写选项为 funnel_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
