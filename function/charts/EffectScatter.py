# -*- coding:utf-8 -*-


class EffectScatter:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'x_axis -> list': 'x 坐标轴数据',
              'y_axis -> list': 'y 坐标轴数据',
              'symbol_size -> int': '标记图形大小，默认为 10'}

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
            print("传入实参未达到预期值" + "\n可写选项为 EffectScatter( [help] | [more] )")

    @staticmethod
    def add():
        
        class_zero = ("add:(" + "name, x_axis, y_axis," +
                      "\n\t symbol_size=10, **kwargs)")
        print(class_zero)


# if __name__ == '__main__':
#     effectscatter = EffectScatter
#     effectscatter.add()
