<h1 align="center">Redfox</h1>

------

<h1 align="center">Secondary development based on pyecharts</h1>

<h3 align="center">When it comes to development, I'm a little embarrassed myself.</h3>

<center>Because Redfox is not really developed, but based on pyecharts, for readers and the original Python scholars, as well as those who are going into the visual field, to redevelop.And I hope that Redfox will be able to face the world in the near future, just like anaconda.</center><hr><br>

<h1 align="center">Redfox introduction</h1>

<br>

<center>……There's a lot to say, though, but I want to be very clear about what Redfox does。When beginners use Pyecharts to make the first chart, the threshold of data visualization is doomed.When we want to do the visualization of massive data, we must not be clueless!The author only wants to realize his dream here, which is to make a massive data visualization of himself.</center><hr>

  [Read official document](https://github.com/pyecharts/pyecharts//)<br>
  [Read official description](http://pyecharts.org/#/)

------

### install

```shell
$ pip install

```

------

### clone

```shell
$ git clone https://github.com/pyecharts/pyecharts.git
$ cd pyecharts
$ pip install -r requirements.txt
$ python setup.py安装

```

------

### python import

```python
import pyecharts

```

------

<h3 align="center">pyecharts presentation</h3>

<p align="center">
    <img src="https://user-images.githubusercontent.com/19553554/39612358-499eb2ae-4f91-11e8-8f56-179c4f0bf2df.png" alt="pyecharts logo" width="200" height="200" />
</p>
<p align="center">Pyecharts</p>

<br>

> Legend, this is the creator of pyecharts……
> <br>

<p align="center">Pyecharts is a class library for generating Echarts charts.Echarts is a data visualization JS library of baidu open source.The visualization of graphs generated by Echarts is great, and pyecharts is designed to interface with Python to facilitate direct use of data generation diagrams in Python.</p>

------

<p align="center">
    <a href="https://travis-ci.org/pyecharts/pyecharts">
        <img src="https://travis-ci.org/pyecharts/pyecharts.svg?branch=master" alt="Travis Build Status">
    </a>
    <a href="https://ci.appveyor.com/project/chenjiandongx/pyecharts">
        <img src="https://ci.appveyor.com/api/projects/status/81cbsfjpfryv1cl8?svg=true" alt="Appveyor Build Status">
    </a>
    <a href="https://codecov.io/gh/pyecharts/pyecharts">
        <img src="https://codecov.io/gh/pyecharts/pyecharts/branch/master/graph/badge.svg" alt="Codecov">
    </a>
    <a href="https://badge.fury.io/py/pyecharts">
        <img src="https://badge.fury.io/py/pyecharts.svg" alt="Package version">
    </a>
    <a href="https://pypi.org/project/pyecharts/">
        <img src="https://img.shields.io/pypi/pyversions/pyecharts.svg?colorB=brightgreen" alt="PyPI - Python Version">
    </a>
</p>
<p align="center">
    <a href="https://pypi.org/project/pyecharts">
        <img src="https://img.shields.io/pypi/format/pyecharts.svg" alt="PyPI - Format">
    </a>
     <a href="https://github.com/pyecharts/pyecharts/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
</p>

<br>



<h3 align="center">For example, here we use the example provided by pyecharts</h3>

------

```python
from pyecharts import Bar

bar = Bar("My first chart", "here's the subtitle")
bar.add("costume", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
# (The previous line is used only for printing configuration items to facilitate debugging.)
bar.render()    # 生成本地 HTML 文件
# (Generate local HTML files)
```



> 来自官方的使用方式，非常简便。
