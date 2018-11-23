# -*- coding:utf-8 -*-


class Liquid:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'data -> list': '数据项',
              'shape -> str': '水球外形，有"circle", "rect", "roundRect", "triangle", "diamond",' +
                              ' "pin", "arrow"可选。默认为"circle"。' +
                              '也可以自定义的SVG路径',
              'liquid_color -> list': '波浪颜色，默认的颜色列表为["#294D99", "#156ACF", "#1598ED", "#45BDFF"]。',
              'is_liquid_animation -> bool': '是否显示波浪动画， 默认为True',
              'is_liquid_outline_show -> bool': '是否显示边框，默认为True'}

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
            print("传入实参未达到预期值" + "\n可写选项为 Liquid( [help] | [more] )")

    @staticmethod
    def add():
        
        class_zero = ("add:(" + "name, data, " + 
                      "\n\t shape='circle', " +
                      "\n\t liquid_color='None', " +
                      "\n\t is_liquid_animation=True, " +
                      "\n\t is_liquid_outline_show=True, **kwargs)")
        print(class_zero)


# if __name__ == "__main__":
#     liquid = Liquid
#     liquid.add()
