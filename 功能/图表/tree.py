# -*- coding:utf-8 -*-


# 有关于树图的帮助
# def tree_help(helpme):
#
#     i = ['help', 'more']
#     ii = {'name -> str': '系列名称，用于toopltip的显示，legend的图例筛选。',
#           'data -> list': '树图的数据项是 一个树， 每个节点包括value(可选)，name，children(也是树，可选)',
#           'tree_layout -> str': '\n\t树图的布局，有 正交 的 径向 两种。 这里的 正交布局 就是我们通常所说的水平 和 垂直方向，对应的参数' +
#           '\n\t取值为"orthogonal"。而 径向布局 是指以根节点为原点，每一层节点为环，一层层向外发散绘制而成的布局，对应的参数取值为"radial"。' +
#           '\n\t 默认为"orthogonal"。',
#           'tree_symbol -> str': '\n\t标记的图形，ECharts提供的标记类型包括"emptyCircle", "circle", "rect", "roundRect", "triangle"' +
#           '\n\t"diamond", "pin", "arrow", "None"。 默认为"emptyCircle"。',
#           'tree_symbol_size -> int/list': '\n\t标记的大小，可以设置成诸如10这样的单一数字，也可以用数组分开表示宽和高' +
#           '\n\t例如[20, 10]表示标记宽为20，高为10。默认为7',
#           'tree_orient -> str': '\n\t树图中 正交布局 方向，也就是说只有在layout="orthogonal"的时候，该配置项才生效。' +
#           '\n\t对应有 水平 方向的 从左到右，从右到左；以及垂直方向的从上到下，从下到上。取值为"LR", "RL", "TB", "BT"。' +
#           '\n\t注意，之前的配置项值"horizontal"等同于"LR"，"vertical"等同于"TB"。默认为"LR"',
#           'tree_top -> str': 'tree组件离容器顶部的距离。可以是想20这样的具体像素值，可以像"20%"这样相对于容器高宽的百分比。默认为"12%"',
#           'tree_left -> str': 'tree组件离容器左侧的距离。可以是想20这样的具体像素值，可以像"20%"这样相对于容器高宽的百分比。默认为"12%"',
#           'tree_bottom -> str': 'tree组件离容器底部的距离。可以是想20这样的具体像素值，可以像"20%"这样相对于容器高宽的百分比。默认为"12%"',
#           'tree_right -> str': 'tree组件离容器右侧的距离。可以是想20这样的具体像素值，可以像"20%"这样相对于容器高宽的百分比。默认为"12%"',
#           'tree_collapse_interval -> int': '折叠节点间隔，当节点过多时可以解决节点显示过杂间隔。默认为0',
#           'tree_label_position -> str/list': '标签的位置。默认为"left"',
#           'tree_label_vertical_align -> str': '父节点文字垂直对齐方式，默认自动。可选:"top", "middle", "bottom"',
#           'tree_label_align -> str': '父节点文字水平对齐方式，默认自动。可选:"left", "center", "right"',
#           'tree_label_text_size -> int': '父节点文字的字体大小',
#           'tree_label_rotate -> int': '父节点标签旋转。从-90度到90度。正值是逆时针。默认为0',
#           'tree_leaves_position -> str': '距离图形元素的距离。当position为字符描述值(如"top", "insideRight")时候有效。参加tree_label_position',
#           'tree_leaves_vertical_align -> str': '叶节点文字垂直对齐方式，默认自动。可选： "top", "maiddle", "bottom"。',
#           'tree_leaves_align -> str': '叶节点文字水平对齐方式，默认自动。可选："left", "center", "right"。',
#           'tree_leaves_text_size -> int': '叶节点文字的字体大小',
#           'tree_leaves_rotatr -> int': '叶节点标签旋转。从-90到90度。正值是逆时针。默认为0'}
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
#         print("传入实参未达到预期值" + "\n可写选项为 tree_help( [help] | [more] )")


class Tree:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '系列名称，用于toopltip的显示，legend的图例筛选。',
              'data -> list': '树图的数据项是 一个树， 每个节点包括value(可选)，name，children(也是树，可选)',
              'tree_layout -> str': '\n\t树图的布局，有 正交 的 径向 两种。 这里的 正交布局 就是我们通常所说的水平 和 垂直方向，对应的参数' +
                                    '\n\t取值为"orthogonal"。而 径向布局 是指以根节点为原点，每一层节点为环，一层层向外发散绘制而成的布局，对应的参数取值为"radial"。' +
                                    '\n\t 默认为"orthogonal"。',
              'tree_symbol -> str': '\n\t标记的图形，ECharts提供的标记类型包括"emptyCircle", "circle", "rect", ' +
                                    '"roundRect", "triangle","diamond", ' +
                                    '"pin", "arrow", "None"。 默认为"emptyCircle"。',
              'tree_symbol_size -> int/list': '\n\t标记的大小，可以设置成诸如10这样的单一数字，也可以用数组分开表示宽和高' +
                                              '\n\t例如[20, 10]表示标记宽为20，高为10。默认为7',
              'tree_orient -> str': '\n\t树图中 正交布局 方向，也就是说只有在layout="orthogonal"的时候，该配置项才生效。' +
                                    '\n\t对应有 水平 方向的 从左到右，从右到左；以及垂直方向的从上到下，从下到上。取值为"LR", "RL", "TB", "BT"。' +
                                    '\n\t注意，之前的配置项值"horizontal"等同于"LR"，"vertical"等同于"TB"。默认为"LR"',
              'tree_top -> str': 'tree组件离容器顶部的距离。可以是想20这样的具体像素值，可以像"20%"这样相对于容器高宽的百分比。默认为"12%"',
              'tree_left -> str': 'tree组件离容器左侧的距离。可以是想20这样的具体像素值，可以像"20%"这样相对于容器高宽的百分比。默认为"12%"',
              'tree_bottom -> str': 'tree组件离容器底部的距离。可以是想20这样的具体像素值，可以像"20%"这样相对于容器高宽的百分比。默认为"12%"',
              'tree_right -> str': 'tree组件离容器右侧的距离。可以是想20这样的具体像素值，可以像"20%"这样相对于容器高宽的百分比。默认为"12%"',
              'tree_collapse_interval -> int': '折叠节点间隔，当节点过多时可以解决节点显示过杂间隔。默认为0',
              'tree_label_position -> str/list': '标签的位置。默认为"left"',
              'tree_label_vertical_align -> str': '父节点文字垂直对齐方式，默认自动。可选:"top", "middle", "bottom"',
              'tree_label_align -> str': '父节点文字水平对齐方式，默认自动。可选:"left", "center", "right"',
              'tree_label_text_size -> int': '父节点文字的字体大小',
              'tree_label_rotate -> int': '父节点标签旋转。从-90度到90度。正值是逆时针。默认为0',
              'tree_leaves_position -> str': '距离图形元素的距离。' +
                                             '当position为字符描述值(如"top","insideRight")时候有效。参加tree_label_position',
              'tree_leaves_vertical_align -> str': '叶节点文字垂直对齐方式，默认自动。可选： "top", "maiddle", "bottom"。',
              'tree_leaves_align -> str': '叶节点文字水平对齐方式，默认自动。可选："left", "center", "right"。',
              'tree_leaves_text_size -> int': '叶节点文字的字体大小',
              'tree_leaves_rotatr -> int': '叶节点标签旋转。从-90到90度。正值是逆时针。默认为0'}

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
            print("传入实参未达到预期值" + "\n可写选项为 tree_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
