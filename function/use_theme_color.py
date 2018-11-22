# -*- coding:utf-8 -*-


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
