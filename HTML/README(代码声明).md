

<br>

<h3 align="center">Redfox实例应用</h3><hr>

```python
# 但是，如果我们在进行数据可视化编程的时候，万一忘了想要添加的参数呢？
bar = Bar("我的第一个图表", "这里是副标题")
bar.????		('????')
bar.add("服饰", ['衬衫', '羊毛衫', "雪纺衫", "裤子", "高跟鞋", "袜子"],
        [5, 20, 36, 10, 75, 90], is_more_utils=True)
bar.????("我想在生成HTML文件的同时，能够得到数据的反馈")
bar.render()
```

> 每当作者心血来潮时，想要表现什么时，“忘参数了”这句话会很扎心。

```python
form Redfox.function.charts.[需要获取的帮助] import [需要获取的帮助]

Bar('help') | Bar_help('more')

# Redfox将pyecharm库中的所有的可视化模板进行初次统计
# Redfox诞生之初，意愿为万物皆可帮助
```

<hr>
<br>

<br>

<h3 align="center"><font color="red">图形绘制过程~pyecharts</font></h3>

<hr>



| 步骤 |                   描述                    |       代码示例       |                             备注                             |
| :--: | :---------------------------------------: | :------------------: | :----------------------------------------------------------: |
|  1   |        实例一个具体类型图表的对象         |  chart = FooChart()  |                                                              |
|  2   |       为图表添加通用的配置，如主题        |  chart.use_theme()   |                                                              |
|  3   |           为图表添加特定的配置            | geo.add_coordinate() |                                                              |
|  4   |             添加数据及配置项              |     chart.add()      | 参考 [数据解析与导入篇](http://pyecharts.org/#/zh-cn/data_import) |
|  5   | 生成本地文件（html/svg/jpeg/png/pdf/gif） |    chart.render()    |                                                              |

<hr>
<br>

