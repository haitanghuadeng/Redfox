# -*- coding:utf-8 -*-


class Funnel:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'attr -> list': '属性名称',
              'value -> list': '属性所对应的值',
              'funnel_sort -> str/func': '数据排序，可以取“ascending”、“descending”、“none”(表示按data顺序，即不排序)',
              'funnel_gap -> int': '数据图形间距，默认为0。'}

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
            print("传入实参未达到预期值" + "\n可写选项为 Funnel( [help] | [more] )")

    @staticmethod
    def add():
        
        class_zero = ("add:(" + "name, attr, value, " +
                      "\n\t funnel_sort='ascending', " +
                      "\n\t funnel_gap=0, " +
                      "\n\t **kwargs)")
        print(class_zero)


# if __name__ == '__main__':
#     funnel = Funnel
#     funnel.add()
