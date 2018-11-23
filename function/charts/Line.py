# -*- coding:utf-8 -*-


class Line:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

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
            print("传入实参未达到预期值" + "\n可写选项为 Line( [help] | [more] )")

    @staticmethod
    def add():
        
        class_zero = ("add:(" + "name, x_axis, y_axis, " + 
                      "\n\t is_symbol_show=True, " +
                      "\n\t is_smooth=False, " +
                      "\n\t is_stack=False, " +
                      "\n\t is_step=False, " +
                      "\n\t is_fill=False, **kwargs)")
        print(class_zero)


# if __name__ == '__main__':
#     line = Line
#     line.add()
