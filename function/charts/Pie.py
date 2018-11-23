# -*- coding:utf-8 -*-


class Pie:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

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
            print("传入实参未达到预期值" + "\n可写选项为 Pie( [help] | [more] )")

    @staticmethod
    def add():
        
        class_zero = ("add:(" + "name, attr, value" + 
                      "\n\t radius=None, " +
                      "\n\t center=None, " +
                      "\n\t rosetype=None, **kwargs)")
        print(class_zero)


# if __name__ == '__main__':
#     pie = Pie
#     pie.add()
