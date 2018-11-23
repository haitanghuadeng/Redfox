# -*- coding:utf-8 -*-


class Geo:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称', 'attr -> list': '属性名称', 'value -> list': '属性所对应的值',
              'type -> str': '图例类型，有"scatter", "effectScatter", "heatmap"可选。默认为 "scatter"',
              'maptype -> str': '地图类型。 '
                                '从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 [地图自定义篇]',
              'coordinate_region -> str': '城市坐标所属国家。从 v0.5.7 引入，针对国际城市的地理位置的查找。' +
                                          '默认为 中国。具体的国家/地区映射表参照 countries_regions_db.json。'
                                          '更多地理坐标信息可以参考 [数据集篇]',
              'symbol_size -> int': '标记图形大小，默认为12。',
              'border_color -> str': '地图边界颜色，默认为 #111。',
              'geo_normal_color -> str': '正常状态下地图区域的颜色。默认为 #323c48',
              'geo_emphasis_color -> str': '高亮状态下地图区域的颜色。默认为 #2a333d',
              'geo_cities_coords -> dict': '用户自定义地区经纬度，类似如{"阿城": [126.58.45.32],}这样的字典。',
              'is_roam -> bool': '\n\t是否开启鼠标缩放和平移漫游，默认为True。' +
                                 '\n\t如果只想要开启缩放或者平移，可以设置成"scale"或者"move"。设置成True为都开启。'}

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
            print("传入实参未达到预期值" + "\n可写选项为 Geo( [help] | [more] )")

    @staticmethod
    def add():
        
        class_zero = ("add:(" + "name, attr, value, " +
                      "\n\t type='scatter', " +
                      "\n\t maptype='china', " +
                      "\n\t symbol_size=12, " +
                      "\n\t border_color='#111', " +
                      "\n\t geo_normal_color='#323c48', " +
                      "\n\t geo_emphasis_color='#2a333d', " +
                      "\n\t geo_cities_coords=None, " +
                      "\n\t is_roam=True, **kwargs)")
        print(class_zero)


# if __name__ == '__main__':
#     geo = Geo
#     geo.add()
