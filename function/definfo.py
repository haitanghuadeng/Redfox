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


# 有关于Bar柱形图的帮助
def bar_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称', 
          'x_axis -> list': 'x坐标轴数据', 
          'y_axis -> list': 'y坐标轴数据', 
          'is_stack -> bool': '数据堆叠，同个类目轴上系列配置相同的stack值可以堆叠放置', 
          'bar_category_gap -> int/str': '类目轴，当设置为 0 时柱状是紧挨着（直方图类型），默认为 "20%"', 
          'Note': '\n\t全局配置项要在最后一个 add() 上设置，否侧设置会被冲刷掉'}

    value = helpme
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


# 有关Bar3D的帮助
def bar3d_help(helpme):

    i = ['help', 'more', 'parameter']
    ii = {'name -> str': '图裂名称',
          'x_axis -> str': 'x坐标轴数据。需为类目轴，也就是不能为数值。',
          'y_axis -> str': 'y坐标轴数据。需为类目轴，也就是不能为数值。',
          'data -> list': '包含列表的列表：数据项，数据中，每一行是一个【数据项】，每一列属于一个【维度】',
          'grid3d_opactiy -> int': '3D笛卡尔坐标系组的透明度(柱状的透明度)，默认为1，完全不透明。',
          'grid3d_shading -> str':
          "三维柱状图中三维图形的着色效果：" +
          "\n\t①color:只显示颜色，不受光照等其他因素的影响。" +
          "\n\t②lambert:通过经典的lambert着色表现光照带来的明暗。" +
          "\n\t③realistic:真实感渲染，配合 light.ambientCubemap 和 postEffect 使用可以让展示的画面效果和质感有质的提升。" +
          "ECharts GL 中使用了基于物理的渲染（PBR) 来表现真实感材质。"}
    ia = {
        'grid3d_shading -> str': '设置该选项，图表渲染时将会更加真实。',
        'is_grid3d_rotate -> bool': '启动该选项，图表将自动旋转[默认为False]。',
        'grid3d_rotate_speed -> int': '设置该选项，依赖于is_grid3d_rotate=True，可根据输入值调整旋转速度。',
        'Note，此项与axis3d通用': '详细信息查询pyecharts官方文档[通用配置项]。'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO_help")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
        else:
            print(ia)
    else:
        print("传入实参未达到预期值" + "\n可写选项为 bar3d_help( [help] | [more] )")


# 有关于Boxplot的帮助
def boxplot_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称', 'x_axis -> list': 'x坐标轴数据', 'y_axis -> [list]':
          '\n\ty 坐标轴数据，二维数组的每一数组项（下例中的每行）是渲染一个 box，它含有五个量值，依次是:' +
          '\n\t[min, Q1, median (or Q2), Q3, max]'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO_help")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 boxplot_help( [help] | [more] )")


# 有关于涟漪特效的散点图帮助
def effectscatter_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'x_axis -> list': 'x 坐标轴数据',
          'y_axis -> list': 'y 坐标轴数据',
          'symbol_size -> int': '标记图形大小，默认为 10'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO_help")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 effectscatter_help( [help] | [more] )")


# 有关于漏斗图的帮助
def funnel_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'attr -> list': '属性名称',
          'value -> list': '属性所对应的值',
          'funnel_sort -> str/func': '数据排序，可以取“ascending”、“descending”、“none”(表示按data顺序，即不排序)',
          'funnel_gap -> int': '数据图形间距，默认为0。'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO_help")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 funnel_help( [help] | [more] )")


# 有关于仪表盘的帮助
def gauge_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'attr -> list': '属性名称',
          'value -> list': '属性对应的值',
          'scale_range -> list': '仪表盘数据范围，默认为[0，100]',
          'angle_range -> list': '仪表盘角度范围，默认为[225，45]'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO_help")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 gauge_help( [help] | [more] )")


# 有关于地理坐标系的帮助
def geo_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称', 'attr -> list': '属性名称', 'value -> list': '属性所对应的值',
          'type -> str': '图例类型，有"scatter", "effectScatter", "heatmap"可选。默认为 "scatter"',
          'maptype -> str': '地图类型。 从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 [地图自定义篇]',
          'coordinate_regin -> str': '城市坐标所属国家。从 v0.5.7 引入，针对国际城市的地理位置的查找。' +
                                     '默认为 中国。具体的国家/地区映射表参照 countries_regions_db.json。更多地理坐标信息可以参考 [数据集篇]',
          'symbol_size -> int': '标记图形大小，默认为12。',
          'border_color -> str': '地图边界颜色，默认为 #111。',
          'geo_normal_color -> str': '正常状态下地图区域的颜色。默认为 #323c48',
          'geo_emphasis_color -> str': '高亮状态下地图区域的颜色。默认为 #2a333d',
          'geo_cities_coords -> dict': '用户自定义地区经纬度，类似如{"阿城": [126.58.45.32],}这样的字典。',
          'is_roam -> bool': '\n\t是否开启鼠标缩放和平移漫游，默认为True。' + 
          '\n\t如果只想要开启缩放或者平移，可以设置成"scale"或者"move"。设置成True为都开启。'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO_help")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 geo_help( [help] | [more] )")


# 有关于地理坐标系线图的帮助
def geolines_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'data -> [list]': '包含列表的列表' +
          '数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。' +
          '每一行包含两个或三个数据，如 ["广州", "北京"] 或 ["广州", "北京"，100]，' +
          '则指定从广州到北京。第三个值用于表示该 line 的数值，该值可省略。',
          'maptype -> str': '地图类型。 从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 [地图自定义篇]',
          'coordinate_regin -> str': '城市坐标所属国家。'
                                     '从 v0.5.7 引入，针对国际城市的地理位置的查找。默认为 [中国]。具体的国家/地区映射表参照 countries_regions_db.json。'
                                     '更多地理坐标信息可以参考 [数据集篇]',
          'symbol -> str': '线两端的标记类型，可以是一个数组分别将指定两端，也可以是单个统一指定。',
          'symbol_size -> int': '线两端的标记大小， 可以是一个数组分别指定两端，也可以是单个统一指定。',
          'border_color -> str': '地图边界颜色，默认为 #111',
          'geo_normal_color -> str': '正常状态下地图区域的颜色。默认为 #323c48',
          'gep_emphasis_color -> str': '高亮状态下地图区域的颜色。默认为 #2a333d',
          'geo_cities_coords -> dict': '用户自定义地区经纬度，类似如 {"阿城": [126.58, 45.32],} 这样的字典。',
          'geo_effect_period -> int/float': '特效动画的时间，单位为s，默认为6s',
          'geo_effect_traillength -> float': '特效尾迹的长度，取从0到1的值，数值越大尾迹越长。默认为0',
          'geo_effect_color -> str': '特效标记的颜色，默认为 #fff',
          'geo_effect_symbol -> str': '特效图形的标记， '
                                      '有[circle], [rect], [roundRect], [triangle], '
                                      '[diamond], [pin], [arrow], [plane]可选。',
          'geo_effect_symbolsize -> int/list': '特效标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示高和宽，例如 [20, 10] 表示标记宽为 20，高为 10。',
          'is_geo_effect_show -> bool': '是否显示特效。',
          'is_roam -> bool': '是否开启鼠标缩放和平移漫游。默认为 True' +
          '如果只想要开启缩放或者平移，可以设置成"scale"或者"move"。设置成 True 为都开启'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO_help")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 geolines_help( [help] | [more] )")


# 有关于节点关系图的帮助
def graph_help(helpme):

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

    value = helpme
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


# 有关于热力图的帮助
def heatmap_help(helpme):

    i = ['help', 'more']
    ii = {
        '如果指定': ' is_calendar_heatmap (使用日历热力图)为True，则参数为',
        'name -> str': '图例名称',
        'data -> [list]': '包含列表的列表' + '数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
        'calendar_date_range -> str/list': '日历热力图的日期，"2016"表示2016年，["2016-5-5"，"2017-5-5"]表示2016年5月5日至2017年5月5日',
        'calendar_call_size -> list': '日历每格框的大小，可设置单值 或数组 第一个元素是宽 第二个元素是高，支持设置自适应"auto"。默认为["auto"，20]',
        '默认为不指定': '参数为： ' + 'name -> str 图例名称',
        'x_axis -> str': 'x坐标轴数据。需为类目轴，也就是不能为数值。',
        'y_axis -> str': 'y坐标轴数据。需为类目轴，也就是不能为数值。',
        'date -> [list]': '数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
        '默认情况': '不指定 is_calendar_heatmap',
        'Note': '热力图必须配合通用配置项中的VisualMap使用才有效果。'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 heatmap_help( [help] | [more] )")


# 有关k于线图的帮助
def kline_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'x_axis -> list': 'x坐标轴数据',
          'y_axis -> [list]': 'y坐标轴数据。数据中，每一行是一个每一行是一个『数据项』，每一列属于一个『维度』。' +
          '数据项具体为[open, close, lowest, highest] (即：[开盘值，收盘值，最低值，最高值])'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 kline_help( [help] | [more] )")


# 有关于k线图的帮助
def candlestick_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'x_axis -> list': 'x坐标轴数据',
          'y_axis -> [list]': 'y坐标轴数据。数据中，每一行是一个每一行是一个『数据项』，每一列属于一个『维度』。' +
          '数据项具体为[open, close, lowest, highest] (即：[开盘值，收盘值，最低值，最高值])'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 candlestick_help( [help] | [more] )")


# 有关于折线/面积图的帮助
def line_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'x_axis -> list': 'x坐标轴数据',
          'y_axis -> list': 'y坐标轴数据',
          'is_symbol_show -> bool': '是否显示标记图形，默认为True',
          'is_smooth -> bool': '是否平滑曲线显示，默认为False',
          'is_stack -> bool': '数据堆叠，同个类目轴上系列配置相同的stack值可以堆叠放置。默认为False',
          'is_step -> bool/str': '是否是阶梯线图。可以设置为True显示成阶梯线图。默认为False' +
          '也支持设置成"start", "middle", "end"分别配置当前点，当前点与下个点的中间下个点拐弯',
          'is_fill -> bool': '是否为填充曲线所绘制面积，默认为False',
          'area_opacity -> float': '填充区域透明度',
          'area_color -> str': '填充区域颜色',
          'Note': '\n\t可配置lineStyle参数\n\t可以通过label_color来设置线条颜色，' +
          '\n\t如["#eee", "#000"],所有的表图类型的图例颜色都可通过label-color来修改。'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 line_help( [help] | [more] )")


# 有关于3D折线图的帮助
def line3d_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'data -> [list]': '包含列表的列表' +
          '数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
          'grid3d_opactiy -> int': '3D笛卡尔坐标系组的透明度(线的透明度)，默认为1，完全不透明。',
          'Note': '\n\t关于gird3D部分的设置，请参照通用配置项中的介绍 [通用配置项]' +
          '\n\t可配合axis3D通用配置项一起使用'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 line3d_help( [help] | [more] )")


# 有关于水球图的帮助
def liquid_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'data -> list': '数据项',
          'shape -> str': '水球外形，有"circle", "rect", "roundRect", "triangle", "diamond", "pin", "arrow"可选。默认为"circle"。' +
          '也可以自定义的SVG路径',
          'liquid_color -> list': '波浪颜色，默认的颜色列表为["#294D99", "#156ACF", "#1598ED", "#45BDFF"]。',
          'is_liquid_animation -> bool': '是否显示波浪动画， 默认为True',
          'is_liquid_outline_show -> bool': '是否显示边框，默认为True'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 liquid_help( [help] | [more] )")


# 有关于地图的帮助
def map_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'attr -> list': '属性名称',
          'value -> list': '属性所对应的值',
          'maptype -> str': '\n\t地图类型。从pyecharts V0.3.2+起，地图已经变为扩展包，' +
          '\n\t支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 [地图自定义篇]',
          'is_roam -> bool/str': '\n\t是否开启鼠标缩放和平移漫游，默认为True。' +
          '\n\t如果只想要开启缩放或者平移，可以设置成"scale"或者"more"。设置成True为都开启。',
          'is_map_symbol_show -> bool': '是否显示地图标记红点，默认为True',
          'name_map -> dict': 
          '\n\t[用自定义的地图名称], 有些地图提供行政区号，name_map 可以帮助把它们转换成用户满意的地名。' +
          '\n\t比如英国选区地图，伦敦选区的行政号是E14000639，把它转换成可读地名就需要这么一个字典' +
          '\n\t以此类推，把英国选区所有的地名都转换一下，就需要个 [更大一些的字典]',
          'Note': '\n\t请配合 通用配置项 中的 Visualmap 使用' +
          '\n\t设置 pieces 自定义 visualMap 组件标签'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 map_help( [help] | [more] )")


# 有关于平行坐标系的帮助
def parallel_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'data -> [list]': '包含列表的列表' +
          '数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
          'schema': '默认平行坐标系的坐标轴信息， 如["dim_name1", "dim_name2", "dim_name3"]。',
          'c_schema': '用户自定义平行坐标系的坐标轴信息。',
          '\t·dim -> int': '维度索引',
          '\t·nae -> str': '维度名称',
          '\t·type -> str': '维度类型，有"value", "category"可选' +
          '\n\t\t value: 数据轴，适用于连续数据。' +
          '\n\t\t category： 类目卷，适用于离散的类目数据。',
          '\t·min -> int': '坐标轴刻度最小值',
          '\t·max -> int': '坐标轴刻度最大值',
          '\t·inverse -> bool': '是否是反向坐标轴。默认为False',
          '\t·nameLocation -> str': '坐标轴名称显示位置。有"start", "middle", "end"可选',
          'Note': '可配置lineStyle参数'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 parallel_help( [help] | [more] )")


# 有关于饼图的帮助
def pie_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'attr -> list': '属性名称',
          'value -> list': '属性所对应的值',
          'radius -> list': '\n\t饼图的半径，数组的第一项是内半径，第二项是外半径，默认为[0, 75]' +
          '\n\t默认设置成百分比，相比于容器高宽中较小的一项的一半',
          'center -> list': '\n\t饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标，默认为[50, 50]' +
          '\n\t默认设置成百分比，设置成百分比时第一项是相对容器宽度，第二项是相对于容器高度',
          'rosetype -> str': '是否展示成南丁格尔图，通过半径区分数据大小，有"radius"和"area"两种模式。默认为"radius"',
          '\t·radius': '扇区圆心角展现数据的百分比，半径展现数据的大小',
          '\t·area': '所有扇区圆心角相同，仅通过半径展现数据大小'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 pia_help( [help] | [more] )")


# 有关于极坐标系的帮助
def polar_help(helpme):

    i = ['help', 'more']
    ii = {'add()': '方法签名',
          'name -> str': '图例名称',
          'data -> list': '数据项[极径,极角[数据值]]',
          'angle_data -> list': '角度类目数据',
          'radius_data -> list': '半径类目数据',
          'type -> str': '图例类型，包含["line", "scatter","effectScatter","barAngle", "barRadius"可选。默认为 "line"]',
          'symbol_size ->int': '标记图形大小，默认为 [4]', 
          'start_angle ->int': '起始刻度的角度，默认为 [90] 度，即圆心的正上方。0度为圆心的正右方',
          'rotate_step -> int': '刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转放置标签之间重叠，旋转的角度从 [-90] 度到 [90] 度。 默认为 [0]\n',
          'boundary_gap -> bool': '坐标轴两边留白策略，默认为 [True]，这个时候刻度只是作为分割线，标签和数据点都会在两个刻度之间的带(band)中间\n',
          'clockwise -> bool': '刻度增长是否按顺时针，默认 [True]',
          'is_stack=bool': '数据堆叠，同个类目轴上系列配置相同的stack值可以堆叠放置',
          'axis_range -> list': '坐标轴刻度范围，默认值为 [None, None]。',
          'angleaxis_label_interval -> int/str': '\n\t坐标轴刻度标签的显示间隔，在类目轴中有效。可以采用标签不重叠的策略间隔显示标签，即(auto)。' +
                                                 '\n\t可以设置成0强制显示所有标签。如果设置为1，表示【隔一个标签显示一个标签】，' +
                                                 '\n\t如果值为2，表示隔两个标签显示一个标签，以此类推。默认为0。',
          'is_angleaxis_show -> bool': '是否显示极坐标系的角度轴，默认为 [True]',
          'radiusaxis_z_index -> int': 'radius轴的z指数，默认为 [50]',
          'angleaxis_z_index -> int': 'angle轴的z指数，默认为 [50]',
          'is_radiusaxis_show -> bool': '是否显示极坐标系的径向轴，默认为 [True]\n',
          'render_item -> function': '开发者自己提供图形渲染的逻辑，这个渲染逻辑一般命名为render_item, 参考高级用法篇\n'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 polar_help( [help] | [more] )")


# 有关于雷达图的帮助
def radar_help(helpme):

    i = ['help', 'more']
    ii = {
        'name -> str': '图例名称',
        'value -> [list]': '包含列表的列表' + '数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
        'item_color -> str': '指定单图例颜色',
        'schema -> list': r'默认雷达图的指示器，用来指定雷达图中的多个维度，会对数据处理成{name: xx, value: xx}的字典',
        'c_schema -> dict': '用户自定义雷达图的指示器，用来指定雷达图中的多个维度',
        '\t·name': '指示器名称',
        '\t·min': '指示器最小值',
        '\t·max': '指示器最大值',
        'shape -> str': '雷达图绘制类型，有"polygon"（多边形）和"circle"可选',
        'rader_text_color -> str': '雷达图数据项字体颜色，默认为"#000"',
        'radar_text_size -> int': '雷达图数据项字体大小，默认为12',
        'is_area_show -> bool': '是否填充区域',
        'area_opacity  -> float': '填充区域颜色',
        'is_splitline_show -> bool': '是否显示分割线，默认为True',
        'is_axisline_show -> bool': '是否显示坐标轴线，默认为True',
        'Note': '\n\t可配置lineStyle参数' + '\n\tsymblo=None 可隐藏标记图形(小圆圈)'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 radar_help( [help] | [more] )")


# 有关于桑基图的帮助
def sankey_help(helpme):

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

    value = helpme
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


# 有关于散点图的帮助
def scatter_help(helpme):

    i = ['help', 'more']
    ii = {
        'name -> str': '图例名称',
        'x_axis -> list': 'x坐标轴数据',
        'y_axis -> list': 'y坐标轴数据',
        'extra_data -> list[int]': '第三维度数据，x轴为第一个维度，y轴为第二个维度。（可在visualmap中将视图元素映射到第三维度）',
        'extra_name -> list[str]': '额外的数据项的名称，可以为每个数据点指定一个名称',
        'symbol_size -> int': '标记图形大小，默认为10',
        '\tNote': '请配合 通用配置项 中的Visualmap使用',
        'draw()': 'Scatter还内置了画画方式',
        '\tpath -> str': '转换图片的地址',
        '\tcolor -> str': '所要排除的颜色',
        'Note': '\n\t关于gird3D部分的设置，请参照通用配置项中的介绍 通用配置项' + '\n\t可配合axis3D通用配置项一起使用'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 scatter_help( [help] | [more] )")


# 有关于3D曲面图的帮助
def surface_help(helpme):

    i = ['help', 'more']
    ii = {
        'name -> str': '图例名称',
        'data -> [list]/ndarray': '\n\t包含列表的列表' + '\n\t数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
        'grid3d_opactiy -> str': '3D笛卡尔坐标系组的透明度，默认为1，完全不透明',
        'Note': '\n\t关于gird3D部分的设置，请参照通用配置项中的介绍 通用配置项' + '\n\t可配合axis3D通用配置项一起使用'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 surface_help( [help] | [more] )")


# 有关于主题河流图的帮助
def themerive_help(helpme):

    i = ['help', 'more']
    ii = {'name -> list': '图例名称, 必须为list类型，list中每个值为数据项中的种类。',
          'data -> [list]': '包含列表的列表' +
          '\n\t数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。' +
          '\n\t每个数据项至少需要是哪个为读，如["2015/11/08", 10, "DQ"], 分别为[时间，数值， 种类(图例名)]',
          'Note': '可以看到，每个数据项中的第三个数值就是该项的种类，而种类可以在add()第一个参数指定。'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 themerive_help( [help] | [more] )")


# 有关于树图的帮助
def tree_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '系列名称，用于toopltip的显示，legend的图例筛选。',
          'data -> list': '树图的数据项是 一个树， 每个节点包括value(可选)，name，children(也是树，可选)',
          'tree_layout -> str': '\n\t树图的布局，有 正交 的 径向 两种。 这里的 正交布局 就是我们通常所说的水平 和 垂直方向，对应的参数' +
          '\n\t取值为"orthogonal"。而 径向布局 是指以根节点为原点，每一层节点为环，一层层向外发散绘制而成的布局，对应的参数取值为"radial"。' +
          '\n\t 默认为"orthogonal"。',
          'tree_symbol -> str': '\n\t标记的图形，ECharts提供的标记类型包括"emptyCircle", "circle", "rect", "roundRect", "triangle"' +
          '\n\t"diamond", "pin", "arrow", "None"。 默认为"emptyCircle"。',
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
          'tree_leaves_position -> str': '距离图形元素的距离。当position为字符描述值(如"top", "insideRight")时候有效。参加tree_label_position',
          'tree_leaves_vertical_align -> str': '叶节点文字垂直对齐方式，默认自动。可选： "top", "maiddle", "bottom"。',
          'tree_leaves_align -> str': '叶节点文字水平对齐方式，默认自动。可选："left", "center", "right"。',
          'tree_leaves_text_size -> int': '叶节点文字的字体大小',
          'tree_leaves_rotatr -> int': '叶节点标签旋转。从-90到90度。正值是逆时针。默认为0'}

    value = helpme
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


# 有关于矩形树图的帮助
def treemap_help(helpme):

    i = ['help', 'more']
    ii = {'name -> str': '图例名称',
          'data -> list': '矩形树图的数据项是 一个树， 每个节点包括value(可选)，name，children(也是树，可选)',
          'treemap_left_depth -> int': '\n\tleafDepth表示『展示几层』，层次更深的节点则被隐藏起来。设置了leafDepth后' +
          '\n\t下钻（drill down）功能开启。drill down）功能即点击后才能展示子层级。例如，leafDepth设置为1，表示展示一层节点。',
          'treemap_drilldown_icon -> str': '当节点可以下钻时的提示符。只能是字符，默认为△',
          'treemap_visible_min -> int': '如果某个节点的矩形的面积，小于这个数值(单位：px平方)，这个节点就不显示。'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 treemap_help(  [help] | [more] )")


# 有关于词云库的帮助
def wordcloud_help(helpme):

    i = ['help', 'more']
    ii = {
        'name -> str': '图例名称',
        'attr -> list': '属性名称',
        'value -> list': '属性所对应的值',
        'shape -> list': '词云图轮廓，有"circle", "cardioid", "diamond", '
        '"triangle-forward", "triangle", "pentagon", "star"可选',
        'word_gap -> int': '单词间隔，默认为20',
        'word_size_range -> list': '单词字体大小范围，默认为[12, 60]',
        'rotate_step -> int': '旋转单词角度，默认为45',
        'Note': '当且仅当shape为默认的"circle"时 rotate_step 参数才生效'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            for key in ii.keys():
                print(key + ii[key])
    else:
        print("传入实参未达到预期值" + "\n可写选项为 wordcloud_help( [help] | [more] )")


# 开发者冗余空间

initializer()
