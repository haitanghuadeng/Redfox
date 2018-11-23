

<br>

<h3 align="center">Redfox使用时注意事项：</h3>
<hr>

<h3 align="center"><font color="red">》》》Redfox库不能与pyecharts库共同使用《《《</font></h3>
>
> <h3><font>原因如下 : </font></h3>
>
> ```python
> from pyecharts import *
> from redfox import *
> 
> 
> bar = Bar
> # 该行为将会使程序无法查找到所对应的对象Bar
> # 因为RedFox库中，所有charts命名和pyecharts相同……
> # 在此，Redfox宗旨是将代码进行注释之后，调用该库，获得帮助
> ```
>
> <h3><font>不过，Redfox开发团队相信，这个问题将会在1.1.1c版本(也就是第二个正式版本时，解决该问题)</font></h3>
>
 
<hr>

<br>

<h3 align="center">关于极坐标系的获取帮助(For polar plots, get help)</h3>

<hr>

```python
#! /usr/bin/python
# -*- coding:utf-8 -*-
# author: haitanghuadeng(github)
# project: Redfox
# project hub: Redfox

            
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
        pass # 截止到2018年11月19日，Redfox最新版本为1.0.1a，目前.add()方法签名帮助暂未实现。


```

> 此处展示Redfox中对极坐标系的帮助，源码编写方式如上。
>
> 特殊声明：Redfox函数式编程在版本1.0.1a之后被面向对象式编程取代

<hr>
<br>

