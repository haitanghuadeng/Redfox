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
              'Note': '\n\t全局配置项要在最后一个 add() 上设置，否侧设置会被冲刷掉' +
              '\n\tdatazoom 适合所有平面直角坐标系图形，也就是(Line、Bar、Scatter、EffectScatter、Kline)' +
              '可通过设置xaxis_min/xaxis_max/yaxis_min/yaxis_max 来调整x轴和y轴上的最大最小值。针对数值轴有效！' +
              '可以通过label_color来设置柱状图的颜色，如["#eee", "#000"]，所有的图表类型的图例颜色都可通过label_color来修改。'}

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
            print("传入实参未达到预期值" + "\n可写选项为 Bar( [help] | [more] )")

    @staticmethod
    def add():

        class_zero = ("add:(" + "name, x_axis, y_axis," + 
                      "\n\t is_stack=False," +
                      "\n\t bar_category_gap='20%', **kwargs")
        print(class_zero)

        
# if __name__ == '__main__':
#     bar = Bar
#     bar.add()
