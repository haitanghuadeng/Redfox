#! /usr/bin/python
# -*- coding:utf-8 -*-


def initializer():

    print("\t\t>>>> RedFox <<<<")
    print(" RedFox解释pyecharts库函数时，将会借用字典存储。")
    print("然而RedFox的开发，一直追随着python之禅的宗旨！")
    print("\t\t>>>> RedFox <<<<")
    print("从函数形参到调用传入实参，将以同道者的身份研究View！")
    print("初始d化将向输出界面打印本页所包含的函数名\n")


# 有关于pyecharts的编写思路
def python_pyecharts():
  
    print("编写模式参照Polar_help函数")
    print("字典存储帮助信息，函数调用")


# 有关于RedFox的帮助
def redfox_help(helpme):

    i = ['help', 'more', 'versions', 'partner', 'official_web']
    ii = {'help': '\t特殊声明： RedFox使用时请配合Pyecahrts', 
          'more': '\t关于view领域，RedFox支持Pyecharts', 
          'versions': '\tRedFox版本：1.0.1a (所属版本为母版本) ', 
          'partner': '\tgithub开源库 -> 开源伙伴：@haitanghuadeng', 
          'official_web': '\tgithub开源库 -> https://haitanghuadeng.github.io/Redfox/'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value in ii.keys():
            print(value + ii[value])
    else:
        print("选择获取的帮助 [ help | more | versions | partner | official_web]")


# 有关于主题色系
def use_theme_color(helpme):
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

    value = helpme
    if value in i:
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
        # print("False")
        print("use_theme_color帮助：{} 传入实参：'help'\t声明字符串变量".format(i))



# 开发者冗余空间

initializer()
