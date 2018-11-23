# -*- coding:utf-8 -*-


class Themerive:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> list': '图例名称, 必须为list类型，list中每个值为数据项中的种类。',
              'data -> [list]': '包含列表的列表' +
                                '\n\t数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。' +
                                '\n\t每个数据项至少需要是哪个为读，如["2015/11/08", 10, "DQ"], 分别为[时间，数值， 种类(图例名)]',
              'Note': '可以看到，每个数据项中的第三个数值就是该项的种类，而种类可以在add()第一个参数指定。'}

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
            print("传入实参未达到预期值" + "\n可写选项为 Themerive( [help] | [more] )")

    @staticmethod
    def add():
        
        class_zero = ("add:(" + "name, data)")
        print(class_zero)


# if __name__ == '__main__':
#     themerive = Themerive
#     themerive.add()
