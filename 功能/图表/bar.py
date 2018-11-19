# -*- coding:utf-8 -*-


# 有关于Bar柱形图的方法帮助
class Bar:

    def __init__(self, helpme):
        self.helpme = helpme

    def bar_help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'x_axis -> list': 'x坐标轴数据',
              'y_axis -> list': 'y坐标轴数据',
              'is_stack -> bool': '数据堆叠，同个类目轴上系列配置相同的stack值可以堆叠放置',
              'bar_category_gap -> int/str': '类目轴，当设置为 0 时柱状是紧挨着（直方图类型），默认为 "20%"',
              'Note': '\n\t全局配置项要在最后一个 add() 上设置，否侧设置会被冲刷掉'}

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
            print("传入实参未达到预期值" + "\n可写选项为 bar_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
