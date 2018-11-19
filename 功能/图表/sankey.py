# -*- coding:utf-8 -*-


# 有关于桑基图的帮助
# def sankey_help(helpme):
#
#     i = ['help', 'more']
#     ii = {'name -> str': '图例名称',
#           'nodes -> list': '桑基图结点，必须包含的数据项有：',
#           '\t·name': '数据项名称',
#           '\t·nodes_value': '数据项数值。(使用时：value)',
#           'links -> list': '桑基图结点关系',
#           '\t·source': '边的源节点名称（必须有！）',
#           '\t·targt': '边的目标节点名称（必须有！）',
#           '\t·links_value': '边的数值，决定边的宽度。(使用时：value)',
#           '\t\t·sankey_node_width -> int': '图中每个矩形节点的宽度。默认为20',
#           '\t\t·sankey_node_gap -> int': '图中每一列两个矩形节点之间的间隔。默认为8'}
#
#     value = helpme
#     if value in i:
#         print("From dictionaries read TNFO")
#         if value == i[0]:
#             for key in ii.keys():
#                 print(key)
#         elif value == i[1]:
#             for key in ii.keys():
#                 print(key + ii[key])
#     else:
#         print("传入实参未达到预期值" + "\n可写选项为 sankey_help( [help] | [more] )")


class Sankey:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'nodes -> list': '桑基图结点，必须包含的数据项有：',
              '\t·name': '数据项名称',
              '\t·nodes_value': '数据项数值。(使用时：value)',
              'links -> list': '桑基图结点关系',
              '\t·source': '边的源节点名称（必须有！）',
              '\t·targt': '边的目标节点名称（必须有！）',
              '\t·links_value': '边的数值，决定边的宽度。(使用时：value)',
              '\t\t·sankey_node_width -> int': '图中每个矩形节点的宽度。默认为20',
              '\t\t·sankey_node_gap -> int': '图中每一列两个矩形节点之间的间隔。默认为8'}

        value = self.helpme
        if value in i:
            print("From dictionaries read TNFO")
            if value == i[0]:
                for key in ii.keys():
                    print(key)
            elif value == i[1]:
                for key in ii.keys():
                    print(key + ii[key])
        else:
            print("传入实参未达到预期值" + "\n可写选项为 sankey_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
