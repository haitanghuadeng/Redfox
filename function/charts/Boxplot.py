# -*- coding:utf-8 -*-


class Boxplot:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称', 'x_axis -> list': 'x坐标轴数据', 'y_axis -> [list]':
              '\n\ty 坐标轴数据，二维数组的每一数组项（下例中的每行）是渲染一个 box，它含有五个量值，依次是:' +
              '\n\t[min, Q1, median (or Q2), Q3, max]'}

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
            print("传入实参未达到预期值" + "\n可写选项为 Boxplot( [help] | [more] )")

    @staticmethod
    def add():

        class_zero = ("add:(" + "name, x_axis, y_axis, **kwargs)")
        print(class_zero)


# if __name__ == '__main__':
#     boxplot = Boxplot
#     boxplot.add()
