# -*- coding:utf-8 -*-


# 有关于词云库的帮助
# def wordcloud_help(helpme):
#
#     i = ['help', 'more']
#     ii = {
#         'name -> str': '图例名称',
#         'attr -> list': '属性名称',
#         'value -> list': '属性所对应的值',
#         'shape -> list': '词云图轮廓，有"circle", "cardioid", "diamond", '
#         '"triangle-forward", "triangle", "pentagon", "star"可选',
#         'word_gap -> int': '单词间隔，默认为20',
#         'word_size_range -> list': '单词字体大小范围，默认为[12, 60]',
#         'rotate_step -> int': '旋转单词角度，默认为45',
#         'Note': '当且仅当shape为默认的"circle"时 rotate_step 参数才生效'}
#
#     value = helpme
#     if value in i:
#         print("From dictionaries read INFO")
#         if value == i[0]:
#             for key in ii.keys():
#                 print(key)
#         elif value == i[1]:
#             for key in ii.keys():
#                 print(key + ii[key])
#     else:
#         print("传入实参未达到预期值" + "\n可写选项为 wordcloud_help( [help] | [more] )")


class WordCloud:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more']
        ii = {
            'name -> str': '图例名称',
            'attr -> list': '属性名称',
            'value -> list': '属性所对应的值',
            'shape -> list': '词云图轮廓，有"circle", "cardioid", "diamond", '
                             '"triangle-forward", "triangle", "pentagon", "star"可选',
            'word_gap -> int': '单词间隔，默认为20',
            'word_size_range -> list': '单词字体大小范围，默认为[12, 60]',
            'rotate_step -> int': '旋转单词角度，默认为45',
            'Note': '当且仅当shape为默认的"circle"时 rotate_step 参数才生效'}

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
            print("传入实参未达到预期值" + "\n可写选项为 wordcloud_help( [help] | [more] )")

    @staticmethod
    def add():
        pass
