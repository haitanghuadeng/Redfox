# -*- coding:utf-8 -*-


class Heatamp:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

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
            print("传入实参未达到预期值" + "\n可写选项为 Heatamp( [help] | [more] )")

    @staticmethod
    def add():
        
        class_zero = ("add:(" + "*args, " + "**kwargs" +
                      "\n\t 热力图主要通过颜色去表现数值的大小，必须要配合visualMap组件使用。直角坐标系上必须要使用两个类目轴。)")
        print(class_zero)


# if __name__ == '__main__':
#     heatmap = Heatamp
#     heatmap.add()
