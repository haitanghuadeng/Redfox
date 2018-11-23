# -*- coding:utf-8 -*-


class Gauge:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'attr -> list': '属性名称',
              'value -> list': '属性对应的值',
              'scale_range -> list': '仪表盘数据范围，默认为[0，100]',
              'angle_range -> list': '仪表盘角度范围，默认为[225，45]'}

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
            print("传入实参未达到预期值" + "\n可写选项为 Gauge( [help] | [more] )")

    @staticmethod
    def add():
        
        class_zero = ("add:(" + "name, attr, value" +
                      "\n\t scale_range=None, " +
                      "\n\t angle_range=None, **kwargs)")
        print(class_zero)


# if __name__ == '__main__':
#     gauge = Gauge
#     gauge.add()
