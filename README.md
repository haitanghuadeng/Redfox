# -*- coding:utf-8 -*-
# 存储的帮助信息，数据类型将是字典。

i = ['help', 'more', 'help-all']
ii = {key:value, key:[value, value1]}
  

# 面向对象编程方式
class Polar:

    def __init__(self, helpme):
        self.helpme = helpme

    def help(self):

        i = ['help', 'more', 'help-all']
        ii = {key:value, key:[value, value1]}

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
            print("传入实参未达到预期值" + "\n可写选项为 polar_help( [help] | [more] )")

    @staticmethod
    def add():
        
        # pass  截止到2018年11月19日，Redfox最新版本为1.0.1a，目前.add()方法签名帮助暂未实现。
                
        class_zero = ("add:(" + "name, data, " + 
                      "\n\t angle_data=None, " +
                      "\n\t radius_data=None, " +
                      "\n\t type='line', " +
                      "\n\t symbol_size=4, " +
                      "\n\t start_angle=90, " +
                      "\n\t rotate_step=0, " +
                      "\n\t boundary_gap=True, " +
                      "\n\t clockwise=True, **kwargs)")
        print(class_zero)
    

# 类似这种方式
Polar_help('help')
```

<hr>

<br>

<table><tr><td bgcolor=#000000><font color=#FFFFFF>Redfox:deftest</font><br>
    <font>函数式编程</font><hr></td></tr></table>

<p align="center"><font color=#000000>Python Redfox 遵循funtion编程规范。在此，Redfox的较为喜欢字典类型。因此，帮助信息的数据类型为字典。</font></p>

```python
#! /usr/bin/python 
# -*- coding:utf-8 -*-
# 存储的帮助信息，数据类型将是字典。
i = ['help', 'more']
helpdic = {'a':'b'}

    value = helpme
    if value in i:
        print("From dictionaries read INFO")
        if value == i[0]:
            for key in ii.keys():
                print(key)
        elif value == i[1]:
            print(ii)
    else:
        print("传入实参未达到预期值" + "\n可写选项为 Polar_help( 'help' | 'more' )")
```













