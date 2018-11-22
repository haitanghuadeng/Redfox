# -*- coding:utf-8 -*-


class Initializer:

    def __init__(self, helpme):
        self.helpme = helpme

    @staticmethod
    def info():
        print("\t\t>>>> RedFox <<<<")
        print(" RedFox解释pyecharts库函数时，将会借用字典存储。")
        print("然而RedFox的开发，一直追随着python之禅的宗旨！")
        print("\t\t>>>> RedFox <<<<")
        print("从函数形参到调用传入实参，将以同道者的身份研究View！")
        print("初始化将向输出界面打印本页所包含的函数名\n")
        print("如果需要更多帮助，那么: Redfox.redfox() 会帮助您！")


# 有关于pyecharts的编写思路
def python_pyecharts():
  
    print("编写模式参照Polar_help函数")
    print("字典存储帮助信息，函数调用")


# 有关于RedFox的帮助
class Redfox:

    def __init__(self, helpme):
        self.helpme = helpme

    def redfox_help(self):

        i = ['help', 'more', 'versions', 'partner', 'official_web']
        ii = {'help': '\t特殊声明： RedFox使用时请配合Pyecahrts', 
              'more': '\t关于view领域，RedFox支持Pyecharts', 
              'versions': '\tRedFox版本：1.0.1a (所属版本为母版本) ', 
              'partner': '\tgithub开源库 -> 开源伙伴：@haitanghuadeng', 
              'official_web': '\tgithub开源库 -> https://haitanghuadeng.github.io/Redfox/'}

        value = self.helpme
        if value in i:
            print("From dictionaries read INFO")
            if value in ii.keys():
                print(value + ii[value])
        else:
            print("选择获取的帮助 {}".format(i))

    def pyehcharts_oop(self):

        i = ['OOP编写规范']
        ii = {'OOP编写规范': 'pyecharts官方提议中，对编写可视化数据的方式有着最简的建议。' +
              '\n\t五步编写方式：' + 
              '\n\t\t一：实例一个具体类型图表的对象 [ 代码示例：chart = FooChart() ] ' + 
              '\n\t\t二：为图表添加通用的配置，如主题 [ 代码示例：chart.use_theme() ] ' + 
              '\n\t\t三：为图表添加特定的配置 [代码示例：geo.add_coordinate() ] ' + 
              '\n\t\t四：添加数据及配置项 [ 代码示例：chart.add() ]' + 
              '\n\t\t五：生成本地文件(html/svg/jpeg/png/pdf/gif) [ 代码示例：chart.render() ]'}

        value = self.helpme
        if value in i:
            print("From dictionaries read INFO")
            if value in ii.keys():
                print(value + ii[value])
        else:
            print("可选择获取的帮助 {}".format(i))
 
    def redfox(self):

        print("该方法用于RedFox提示指令树")
        i = ['versions声明', '编写格式声明', '可用参数声明']
        ii = {'versions声明': '该方法请调用 Redfox.redfox("更多")',
              '编写格式声明': '该方法来自pyecharts官方，Redfox转换为 Redfox.pyehcharts_oop("OOP编写规范")',
              '可用参数声明': '与官方charts文档相同，可以通过 [from Redfox.function.charts.[需要的图表名称] import [需要的图表名称]]'}
        
        value = self.helpme
        if value in i:
            print("From dictionaries read INFO")
            if value in ii.keys():
                print(value + ii[value])
        else:
            print("可选择获取的帮助 {}".format(i))


# 开发者冗余空间

if __name__ == '__main__':
    IO = Initializer
    IO.info()
