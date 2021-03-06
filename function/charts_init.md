<h1 align="center"><font color="red">图形初始化</font></h1>

> 图表类初始化所接受的参数（所有类型的图表都一样）。
>
> 对照Pyecharts官网标准解释

- title -> str
  默认 -> ""
  主标题文本，支持 \n 换行。
- subtitle -> str
  默认 -> ""
  副标题文本，支持 \n 换行。
- width -> int
  默认 -> 800（px）
  画布宽度。
- height -> int
  默认 -> 400（px）
  画布高度。
- title_pos -> str/int
  默认 -> 'left'
  标题距离左侧距离，有'auto', 'left', 'right', 'center'可选，也可为百分比或整数
- title_top -> str/int
  默认 -> 'top'
  标题距离顶部距离，有'top', 'middle', 'bottom'可选，也可为百分比或整数
- title_color -> str 默认 -> '#000'
  主标题文本颜色。
- subtitle_color -> str
  默认 -> '#aaa'
  副标题文本颜色。
- title_text_size -> int
  默认 -> 18
  主标题文本字体大小。
- subtitle_text_size -> int
  默认 -> 12
  副标题文本字体大小。
- background_color -> str
  默认 -> '#fff'
  画布背景颜色。
- page_title -> str
  默认 -> 'Echarts'
  指定生成的 html 文件中 `<title>` 标签的值。
- renderer -> str
  默认 -> 'canvas'
  指定使用渲染方式，有 'svg' 和 'canvas' 可选。3D 图仅能使用 'canvas'。
- extra_html_text_label -> list
  额外的 HTML 文本标签，`(<p> 标签)`。类型为 list，list[0] 为文本内容，list[1] 为字体风格样式（选填）。如 ["this is a p label", "color:red"]。**仅限于在单个图形或者 page 类时使用。**
- is_animation -> bool
  默认 -> True
  是否开启动画。V0.5.9+

<hr>