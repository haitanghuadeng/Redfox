# -*- coding:utf-8 -*-


# 有关于k线图的帮助
# def candlestick_help(helpme):
#
#     i = ['help', 'more']
#     ii = {'name -> str': '图例名称',
#           'x_axis -> list': 'x坐标轴数据',
#           'y_axis -> [list]': 'y坐标轴数据。数据中，每一行是一个每一行是一个『数据项』，每一列属于一个『维度』。' +
#           '数据项具体为[open, close, lowest, highest] (即：[开盘值，收盘值，最低值，最高值])'}
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
#         print("传入实参未达到预期值" + "\n可写选项为 candlestick_help( [help] | [more] )")


class Candlestick:

    def __init__(self, helpme):
        self.helpme = helpme

    def candlestick_help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'x_axis -> list': 'x坐标轴数据',
              'y_axis -> [list]': 'y坐标轴数据。数据中，每一行是一个每一行是一个『数据项』，每一列属于一个『维度』。' +
                                  '数据项具体为[open, close, lowest, highest] (即：[开盘值，收盘值，最低值，最高值])'}

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
            print("传入实参未达到预期值" + "\n可写选项为 candlestick_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
