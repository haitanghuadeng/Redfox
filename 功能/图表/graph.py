# -*- codind:utf-8 -*-


# 有关于节点关系图的帮助
# def graph_help(helpme):
#
#     i = ['help', 'more']
#     ii = {'name -> str': '图例名称',
#           'nodes -> dict': '关系图结点，包含的数据项有' +
#           '·name：结点名称（必须有！）' +
#           '·x：节点的初始x值' +
#           '·y：节点的初始y值' +
#           '·value：结点数值' +
#           '·category：结点类目' +
#           '·symbol：标记图形' +
#           '·symbolSize：标记图形到',
#           'links -> dict': '结点间的关系数据，包含的数据项有' +
#           '·source：边的源节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）' +
#           '·target：边的目标节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）' +
#           '·value：边的数值，可以在力引导布局中用于映射到边的长度',
#           'categories -> list': '节点分类的类目，结点可以指定分类，也可以不指定。' +
#           '如果节点有分类的话可以通过nodes[i].category指定每个节点的类目，类目的样式会被应用到节点样式上',
#           'is_focusnode -> bool': '是否在鼠标移到节点上的时候吐出显示节点以及节点的边和邻接节点。默认为True',
#           'is_roam -> bool/str': '是否开启鼠标缩放和平移漫游。默认为True' +
#           '如果只想要开启缩放或者平移，可以设置成"scale"和"move"。设置成True为都开启。',
#           'is_rotatel -> bool': '是否旋转标签，默认为False',
#           'greah_layout -> str': '关系图布局，默认为"force"' +
#           '·none：不采用任何布局，使用节点中必须提供的x，y作为节点的位置。' +
#           '·circular：采用环形布局' +
#           '·force：采用力引导布局',
#           'graph_edge_length -> int': '力布局下边的两个节点之间的距离，这个距离也会受repulsion影响。默认为50' +
#           '支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长',
#           'graph_gravity -> int': '节点受到向中心的引力因子。该值越大节点越往中心点靠拢。默认为0.2',
#           'graph_repulsion -> int': '节点之间的斥力因子。默认为50' +
#           '支持设置成表达数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大哦则斥力越大',
#           'graph_edge_symbol -> str/list': '边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。默认不显示标记，常见的可以设置为箭头，如下：' +
#           'edgeSymbol:["circle", "arrow"]',
#           'fraph_edge_symbolsize -> int/list': '边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。'}
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
#         print("传入实参未达到预期值" + "\n可写选项为 graph_help( [help] | [more] )")


class Graph:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'nodes -> dict': '关系图结点，包含的数据项有' +
                               '·name：结点名称（必须有！）' +
                               '·x：节点的初始x值' +
                               '·y：节点的初始y值' +
                               '·value：结点数值' +
                               '·category：结点类目' +
                               '·symbol：标记图形' +
                               '·symbolSize：标记图形到',
              'links -> dict': '结点间的关系数据，包含的数据项有' +
                               '·source：边的源节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）' +
                               '·target：边的目标节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）' +
                               '·value：边的数值，可以在力引导布局中用于映射到边的长度',
              'categories -> list': '节点分类的类目，结点可以指定分类，也可以不指定。' +
                                    '如果节点有分类的话可以通过nodes[i].category指定每个节点的类目，类目的样式会被应用到节点样式上',
              'is_focusnode -> bool': '是否在鼠标移到节点上的时候吐出显示节点以及节点的边和邻接节点。默认为True',
              'is_roam -> bool/str': '是否开启鼠标缩放和平移漫游。默认为True' +
                                     '如果只想要开启缩放或者平移，可以设置成"scale"和"move"。设置成True为都开启。',
              'is_rotatel -> bool': '是否旋转标签，默认为False',
              'greah_layout -> str': '关系图布局，默认为"force"' +
                                     '·none：不采用任何布局，使用节点中必须提供的x，y作为节点的位置。' +
                                     '·circular：采用环形布局' +
                                     '·force：采用力引导布局',
              'graph_edge_length -> int': '力布局下边的两个节点之间的距离，这个距离也会受repulsion影响。默认为50' +
                                          '支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长',
              'graph_gravity -> int': '节点受到向中心的引力因子。该值越大节点越往中心点靠拢。默认为0.2',
              'graph_repulsion -> int': '节点之间的斥力因子。默认为50' +
                                        '支持设置成表达数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大哦则斥力越大',
              'graph_edge_symbol -> str/list': '边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。默认不显示标记，常见的可以设置为箭头，如下：' +
                                               'edgeSymbol:["circle", "arrow"]',
              'fraph_edge_symbolsize -> int/list': '边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。'}

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
            print("传入实参未达到预期值" + "\n可写选项为 graph_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
