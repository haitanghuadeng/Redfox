# -*- coding:utf-8 -*-


class Parallel:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {'name -> str': '图例名称',
              'data -> [list]': '包含列表的列表' +
                                '数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。',
              'schema': '默认平行坐标系的坐标轴信息， 如["dim_name1", "dim_name2", "dim_name3"]。',
              'c_schema': '用户自定义平行坐标系的坐标轴信息。',
              '\t·dim -> int': '维度索引',
              '\t·nae -> str': '维度名称',
              '\t·type -> str': '维度类型，有"value", "category"可选' +
                                '\n\t\t value: 数据轴，适用于连续数据。' +
                                '\n\t\t category： 类目卷，适用于离散的类目数据。',
              '\t·min -> int': '坐标轴刻度最小值',
              '\t·max -> int': '坐标轴刻度最大值',
              '\t·inverse -> bool': '是否是反向坐标轴。默认为False',
              '\t·nameLocation -> str': '坐标轴名称显示位置。有"start", "middle", "end"可选',
              'Note': '可配置lineStyle参数'}

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
            print("传入实参未达到预期值" + "\n可写选项为 Parallel( [help] | [more] )")

    @staticmethod
    def add():
        
        class_zero = ("add:(" + "name, data, **kwargs)" + 
                      "\n\t set_schema:(" +
                      "\n\t schema=None, c_schema=None)" +
                      "\n\t config:(schema=None, c_schema=None)" +
                      "\n\t 从v0.5.9开始，原有config方法被废弃，推荐使用set_schema方法。")
        print(class_zero)


# if __name__ == '__main__':
#     parallel = Parallel
#     parallel.add()
