# -*- coding:utf-8 -*-


# 有关于地理坐标系线图的帮助
# def geolines_help(helpme):
#
#     i = ['help', 'more']
#     ii = {'name -> str': '图例名称',
#           'data -> [list]': '包含列表的列表' +
#           '数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。' +
#           '每一行包含两个或三个数据，如 ["广州", "北京"] 或 ["广州", "北京"，100]，' +
#           '则指定从广州到北京。第三个值用于表示该 line 的数值，该值可省略。',
#           'maptype -> str': '地图类型。 从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 [地图自定义篇]',
#           'coordinate_regin -> str': '城市坐标所属国家。'
#                                      '从 v0.5.7 引入，针对国际城市的地理位置的查找。默认为 [中国]。具体的国家/地区映射表参照 countries_regions_db.json。'
#                                      '更多地理坐标信息可以参考 [数据集篇]',
#           'symbol -> str': '线两端的标记类型，可以是一个数组分别将指定两端，也可以是单个统一指定。',
#           'symbol_size -> int': '线两端的标记大小， 可以是一个数组分别指定两端，也可以是单个统一指定。',
#           'border_color -> str': '地图边界颜色，默认为 #111',
#           'geo_normal_color -> str': '正常状态下地图区域的颜色。默认为 #323c48',
#           'gep_emphasis_color -> str': '高亮状态下地图区域的颜色。默认为 #2a333d',
#           'geo_cities_coords -> dict': '用户自定义地区经纬度，类似如 {"阿城": [126.58, 45.32],} 这样的字典。',
#           'geo_effect_period -> int/float': '特效动画的时间，单位为s，默认为6s',
#           'geo_effect_traillength -> float': '特效尾迹的长度，取从0到1的值，数值越大尾迹越长。默认为0',
#           'geo_effect_color -> str': '特效标记的颜色，默认为 #fff',
#           'geo_effect_symbol -> str': '特效图形的标记， '
#                                       '有[circle], [rect], [roundRect], [triangle], '
#                                       '[diamond], [pin], [arrow], [plane]可选。',
#           'geo_effect_symbolsize -> int/list': '特效标记的大小，
# 可以设置成诸如 10 这样单一的数字，也可以用数组分开表示高和宽，例如 [20, 10] 表示标记宽为 20，高为 10。',
#           'is_geo_effect_show -> bool': '是否显示特效。',
#           'is_roam -> bool': '是否开启鼠标缩放和平移漫游。默认为 True' +
#           '如果只想要开启缩放或者平移，可以设置成"scale"或者"move"。设置成 True 为都开启'}
#
#     value = helpme
#     if value in i:
#         print("From dictionaries read INFO_help")
#         if value == i[0]:
#             for key in ii.keys():
#                 print(key)
#         elif value == i[1]:
#             for key in ii.keys():
#                 print(key + ii[key])
#     else:
#         print("传入实参未达到预期值" + "\n可写选项为 geolines_help( [help] | [more] )")


class Geolines:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

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
              'geo_effect_symbolsize -> int/list': '特效标记的大小，可以设置成诸如 10 这样单一的数字，'
                                                   '也可以用数组分开表示高和宽，例如 [20, 10] 表示标记宽为 20，高为 10。',
              'is_geo_effect_show -> bool': '是否显示特效。',
              'is_roam -> bool': '是否开启鼠标缩放和平移漫游。默认为 True' +
                                 '如果只想要开启缩放或者平移，可以设置成"scale"或者"move"。设置成 True 为都开启'}

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
            print("传入实参未达到预期值" + "\n可写选项为 geolines_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
