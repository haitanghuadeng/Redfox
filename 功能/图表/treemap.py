# -*- coding:utf-8 -*-


# 有关于矩形树图的帮助
# def treemap_help(helpme):
#
#     i = ['help', 'more']
#     ii = {'name -> str': '图例名称',
#           'data -> list': '矩形树图的数据项是 一个树， 每个节点包括value(可选)，name，children(也是树，可选)',
#           'treemap_left_depth -> int': '\n\tleafDepth表示『展示几层』，层次更深的节点则被隐藏起来。设置了leafDepth后' +
#           '\n\t下钻（drill down）功能开启。drill down）功能即点击后才能展示子层级。例如，leafDepth设置为1，表示展示一层节点。',
#           'treemap_drilldown_icon -> str': '当节点可以下钻时的提示符。只能是字符，默认为△',
#           'treemap_visible_min -> int': '如果某个节点的矩形的面积，小于这个数值(单位：px平方)，这个节点就不显示。'}
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
#         print("传入实参未达到预期值" + "\n可写选项为 treemap_help(  [help] | [more] )")


class TreeMap:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'data -> list': '矩形树图的数据项是 一个树， 每个节点包括value(可选)，name，children(也是树，可选)',
              'treemap_left_depth -> int': '\n\tleafDepth表示『展示几层』，层次更深的节点则被隐藏起来。设置了leafDepth后' +
                                           '\n\t下钻（drill down）功能开启。drill down）功能即点击后才能展示子层级。例如，leafDepth设置为1，表示展示一层节点。',
              'treemap_drilldown_icon -> str': '当节点可以下钻时的提示符。只能是字符，默认为△',
              'treemap_visible_min -> int': '如果某个节点的矩形的面积，小于这个数值(单位：px平方)，这个节点就不显示。'}

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
            print("传入实参未达到预期值" + "\n可写选项为 treemap_help(  [help] | [more] )")

    @staticmethod
    def add():
        pass
