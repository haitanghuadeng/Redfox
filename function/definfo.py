#! /usr/bin/python
# -*- coding:utf-8 -*-


def initializer():
    print("\t>>>> RedFox <<<<")
    print("RedFox解释pyecharts库函数时，将会借用字典存储。")
    print("然而RedFox的开发，一直追随着python之禅的宗旨！")
    print("\t>>>> RedFox <<<<")
    print("从函数形参到调用传入实参，将以同道者的身份研究View！\n")


# 有关于pyecharts的编写思路
def python_pyecharts():
  pass


# 有关于主题色系
def use_theme_color(*arge):
    """
    usr_theme_color:
    可支持的主题色系
    vintage | macarons | infographic | 
    shine | roma | westeros | 
    wonderland | chalk | halloween |
    essos | walden | purple-passion | 
    romantic

    """

    i = ['help', 'more-color', 'source']
    for i in arge:
        if help == "help":
            print("主题色列表源于pyecharts")
            print("可写选项：[help] | [more-color] | [source]")
        elif help == "more-color":
            print("\nvintage\t", "macarons\t", "infographic\t", 
                  "\nshine\t", "roma\t", "westeros\t",
                  "\nwonderland\t", "chalk\t", "halloween\t", 
                  "\nessos\t", "walden\t", "purple-passion\t", 
                  "\nromantic\n")
        elif help == "source":
            print("pyecharts default is use_theme")
            print("use_theme == backgroundcolor:browser-backgroundcolor")
        else:
            print("value!")
    else:
        # print("False")
        print("use_theme_color帮助：{} 传入实参：'help'\t声明字符串变量".format(i))


# 有关于Bar柱形图的帮助
def Bar_help(*arge):
    """

    """

    i = ['help', 'more', 'help-all']
    for i in arge:
        print("\nBar帮助：{}".format(i))
        if i == 'help':
            print("\n可写选项：[help] | [more] | [help--all]\n")
        elif i == 'more':
            print("\n--bar.use_theme()：支持主题色系,选参")
            print("--bar.add()：写入数据,\033[1;31;47m必写项\033[0m\n")
        elif i == 'help-all':
            print("\n--bar.use_theme()：支持更换主题色系,选参")
            print("--bar.print_echarts_options():打印详细的配置项，选参")
            print("--bar.add()：写入数据*arge,\033[1;31;47m必写项\033[0m")
            print("--bar.rander(),将所写的python文件存储到指定位置。默认为当前文件路径。\n")
        break
    else:
        # print("False")
        print("Bar帮助：{} 传入实参：'help'\t声明字符串变量".format(i))


# 有关于.add函数的建设
def Bar_add_help(helpme):
    if helpme == 'add_help':
        print("图表中显示更多信息：is_more_utils=True")


# 有关于极坐标系的帮助
def polar_help(helpme):
    """
    # 关于极坐标系的函数内建
    # 平衡Redfox-Python代码执行效率之后，删除冗余代码
    # 基于Polar_help函数的执行代码
    
    'add()':'方法签名'
    'name=str':'图例名称'
    'data=list':'数据项[极径,极角[数据值]]'
    'angle_data=list':'角度类目数据'
    'radius_data=list':'半径类目数据'
    'type=str':'图例类型，包含["line", "scatter", "effectScatter", "barAngle", "barRadius"可选。默认为 'line']'
    'symbol_size=int':'标记图形大小，默认为 [4]'
    'start_angle=int':'起始刻度的角度，默认为 [90] 度，即圆心的正上方。0度为圆心的正右方', 
    'rotate_step=int':'刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转放置标签之间重叠，旋转的角度从 [-90] 度到 [90] 度。 默认为 [0]',
    'boundary_gap=bool':'坐标轴两边留白策略，默认为 [True]，这个时候刻度只是作为分割线，标签和数据点都会在两个刻度之间的带(band)中间', 
    'clockwise=bool':'刻度增长是否按顺时针，默认 [True]', 'is_stack=bool':'数据堆叠，同个类目轴上系列配置相同的stack值可以堆叠放置',
    'axis_range=list':'坐标轴刻度范围，默认值为 [None, None]。', 
    'angleaxis_label_interval=int/str':r'坐标轴刻度标签的显示间隔，在类目轴中有效。 可以采用标签不重叠的策略间隔显示标签，即"auto"。可以设置成0强制显示所有标签。如果设置为1，表示【隔一个标签显示一个标签】，如果值为2，表示隔两个标签显示一个标签，以此类推。默认为0。', 
    'is_angleaxis_show=bool':'是否显示极坐标系的角度轴，默认为 [True]', 
    'radiusaxis_z_index':'数据类型为int radius轴的z指数，默认为 [50]', 
    'angleaxis_z_index':'数据类型为int angle轴的z指数，默认为 [50]', 
    'is_radiusaxis_show=bool':'是否显示极坐标系的径向轴，默认为 [True]', 
    'render_item=function':'开发者资金提供图形渲染的逻辑，这个渲染逻辑一般命名为render_item, 参考高级用法篇'

    for arge in i:
    if arge == i[0]:
        # 此处代码编写：遍历字典的KEY
        print("dict的KEY")
    elif arge == i[1]:
        print("dict的KEY：VALUE (除了开发者模式)，")
    else:
        print("dict开发者模式的帮助(单键值对)")

    """


i = ['help', 'more']
ii = {'add()': '方法签名\n', 'name=str': '图例名称\n', 'data=list': '数据项[极径,极角[数据值]]\n',
      'angle_data=list': '角度类目数据\n', 'radius_data=list': '半径类目数据\n',
      'type=str': '图例类型，包含["line", "scatter","effectScatter","barAngle", "barRadius"可选。默认为 "line"]\n',
      'symbol_size=int': '标记图形大小，默认为 [4]\n', 'start_angle=int': '起始刻度的角度，默认为 [90] 度，即圆心的正上方。0度为圆心的正右方\n',
      'rotate_step=int': '刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转放置标签之间重叠，旋转的角度从 [-90] 度到 [90] 度。 默认为 [0]\n',
      'boundary_gap=bool': '坐标轴两边留白策略，默认为 [True]，这个时候刻度只是作为分割线，标签和数据点都会在两个刻度之间的带(band)中间\n',
      'clockwise=bool': '刻度增长是否按顺时针，默认 [True]\n', 'is_stack=bool': '数据堆叠，同个类目轴上系列配置相同的stack值可以堆叠放置\n',
      'axis_range=list': '坐标轴刻度范围，默认值为 [None, None]。\n',
      'angleaxis_label_interval=int/str': r'坐标轴刻度标签的显示间隔，在类目轴中有效。可以采用标签不重叠的策略间隔显示标签，即(auto)。'
                                          r'可以设置成0强制显示所有标签。如果设置为1，表示【隔一个标签显示一个标签】，如果值为2，表示隔两个标签显示一个标签，以此类推。默认为0。\n',
      'is_angleaxis_show=bool': '是否显示极坐标系的角度轴，默认为 [True]\n',
      'radiusaxis_z_index': '数据类型为int radius轴的z指数，默认为 [50]\n',
      'angleaxis_z_index': '数据类型为int angle轴的z指数，默认为 [50]\n',
      'is_radiusaxis_show=bool': '是否显示极坐标系的径向轴，默认为 [True]\n',
      'render_item=function': '开发者自己提供图形渲染的逻辑，这个渲染逻辑一般命名为render_item, 参考高级用法篇\n'}


    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            print(ii)
    else:
        print("传入实参未达到预期值" + "\n可写选项为 Polar_help( [help] | [more] )")


# 开发者冗余空间

if __init__ == '__main__':
    initializer()
    print("初始化将向输出界面打印本页所包含的函数名")
