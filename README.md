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

<table><tr><td bgcolor=#000000><font color=#FFFFFF>Redfox_help: 函数式帮助</font><hr></td></tr></table>

<p align="center"><font color=#000000>There's a lot to say, though, but I want to be very clear about what Redfox does。Data visualization takes on a new dimension when scholars use Pyecharts to create their first charts.When we want to do the visualization of massive data, we must not be clueless!The author only wants to realize his dream here, which is to make a massive data visualization of himself.</font></p>

```python
from.import deftest


Polar_help('help')
```

<table><tr><td bgcolor=#000000><font color=#FFFFFF>Polar_help('help')</font><br>
    <font>很多时候，这方法显而易见</font><hr></td></tr></table>

```shell
# 终端方法
apt-get --help

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













