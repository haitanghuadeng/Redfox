<h1 align="center"><font color="red">RedFox</font></h1>

<hr>

> ### Redfox基于pyecharts进行的二次开发

<p align="center"><font color=#000000>Because Redfox is not really developed, but based on pyecharts, for readers and the original Python scholars, as well as those who are going into the visual field, to redevelop.And I hope that Redfox will be able to face the world in the near future, just like anaconda.</font></p>

<table><tr><td bgcolor=#000000><font color=#FFFFFF>Data View 领域</font><hr></td></tr></table>

```python
from pyecharts import Polar


import random
date_1 = [(10, random.randint(1, 100) for i in range(300))]
polar = Polar("极坐标系-散点图示例", width=1200, height=600)
polar.add("", data_1 type='effectScatter', effect_scale=10, effect_period=5)
polar.render()

```

> README.md将以Polar为例子，展示View的特色。

<hr>
<br>
<table><tr><td bgcolor=#000000><font color=#FFFFFF>Redfox_help: 面向对象方式调用帮助</font><hr></td></tr></table><br>

<p align="center"><font color=#000000>There's a lot to say, though, but I want to be very clear about what Redfox does。Data visualization takes on a new dimension when scholars use Pyecharts to create their first charts.When we want to do the visualization of massive data, we must not be clueless!The author only wants to realize his dream here, which is to make a massive data visualization of himself.</font></p>

```python
from.import definfo


# 此方法已被丢弃，将以新的方式调用帮助
Polar_help('help')
```

```python
from Redfox.funtion.charts.Polar import Polar


 · polar = Polar('help')
 · polar.help()
```



<table><tr><td bgcolor=#000000><font color=#FFFFFF>Polar('help')</font><br><br><font color=#FFFFFF>在1.0.1b版本之前，统一使用的是Polar_help('help')</font><br>
    <font>很多时候，这方法显而易见</font><hr></td></tr></table><br>

<p align="center"><font color=#000000>如下是关于编写程序时所遇到问题时，该如何调用Redfox的帮助</font></p>

```shell
# 终端方式
Ubunut: apt-get --help
CentOS: yum --help
```

<br>

```shell
# 调用时获得帮助

Polar_help('help')  ---此方法在Redfox1.0.1b版本之前有效
Polar('help')  ---此方法适用于Redfox1.0.1b版本之后
```

<hr>
<br>

<table><tr><td bgcolor=#000000><font color=#FFFFFF>Redfox:OOP (object-oriented-programming)</font><br>
    <font>面向对象编程</font><hr></td></tr></table><br>

<p align="center"><font color=#000000>Python Redfox较为喜欢字典类型。因此，帮助信息的数据类型为字典。</font></p>

```python
# -*- coding:utf-8 -*-
# 存储的帮助信息，数据类型将是字典。
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
    
```

<hr><br>

<table><tr><td bgcolor=#000000><font color=#FFFFFF>Redfox:OOP .add()方法签名</font><br>
    <font>1.0.*版本之后，Redfox团队将代码重构为OOP</font><hr></td></tr></table>

<br>

<p align="center"><font color=#000000>尽管，"class_zero"这样的命名不符合命名约定，目前仅仅用作开发阶段。</font></p>

```python
# 关于命名方式
from Redfox.funtion.charts.Polar import Polar

class ...

	...

    @staticmethod
	def add():
        
        class_zero = ("...")
        print(class_zero)
        
```

<br>

```python
polar.add()
```

<p align="center"><font color=#000000>仅此一条便可调用，这便是Redfox在后续开发中，无论录入任何代码，将会以简而有效的方式呈现。</font></p>

<hr><br>

<table><tr><td bgcolor=#000000><font color=#FFFFFF>Redfox:Path文件</font><br>
    <font>1.0.1c版本之后，Redfox每次版本更新时，将会对版本生成一个"树目录图"</font><hr></td></tr></table>

<br>

<p align="center"><font color=#000000>这么做，只是希望使用者在查看当前版本所有信息时，可以最快速的得到反馈。</font></p>

<hr><br>

