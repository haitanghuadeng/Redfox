# -*- coding:utf-8 -*-


class Bar3D:

    def __init__(self, helpme):
        self.helpme = helpme

    def bar3d_help(self):

        i = ['help', 'more', 'parameter']
        ii = {'name -> str': '图裂名称',
              'x_axis -> str': 'x坐标轴数据。需为类目轴，也就是不能为数值。',
              'y_axis -> str': 'y坐标轴数据。需为类目轴，也就是不能为数值。',
              'data -> list': '包含列表的列表：数据项，数据中，每一行是一个【数据项】，每一列属于一个【维度】',
              'grid3d_opactiy -> int': '3D笛卡尔坐标系组的透明度(柱状的透明度)，默认为1，完全不透明。',
              'grid3d_shading -> str':
              "三维柱状图中三维图形的着色效果：" +
              "\n\t①color:只显示颜色，不受光照等其他因素的影响。" +
              "\n\t②lambert:通过经典的lambert着色表现光照带来的明暗。" +
              "\n\t③realistic:真实感渲染，配合 light.ambientCubemap 和 postEffect 使用可以让展示的画面效果和质感有质的提升。" +
              "ECharts GL 中使用了基于物理的渲染（PBR) 来表现真实感材质。"}
        ia = {
            'grid3d_shading -> str': '设置该选项，图表渲染时将会更加真实。',
            'is_grid3d_rotate -> bool': '启动该选项，图表将自动旋转[默认为False]。',
            'grid3d_rotate_speed -> int': '设置该选项，依赖于is_grid3d_rotate=True，可根据输入值调整旋转速度。',
            'Note，此项与axis3d通用': '详细信息查询pyecharts官方文档[通用配置项]。'}

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
                print(ia)
        else:
            print("传入实参未达到预期值" + "\n可写选项为 Bar3D( [help] | [more] )")

    @staticmethod
    def add():

        class_zero = ("add:(" + "name, x_axis, y_axis, data" + 
                      "\n\t grid3d_opactiy=1, " + 
                      "\n\t grid3d_shading='color', **kwargs)")
        print(class_zero)


# if __name__ == '__main__':
#     bar3d = Bar3D
#     bar3d.add()
