#### 1. InitOpts：初始化配置项
```python

# 用法
from pyecharts import options as opts
init_options = opts.InitOpts(theme= , width='', height='')
bar = Bar(init_opts=init_options)


# 参数
class InitOpts(
    # 图表画布宽度，css 长度单位。
    width: str = "900px",

    # 图表画布高度，css 长度单位。
    height: str = "500px",

    # 图表 ID，图表唯一标识，用于在多图表时区分。
    chart_id: Optional[str] = None,

    # 渲染风格，可选 "canvas", "svg"
    # # 参考 `全局变量` 章节
    renderer: str = RenderType.CANVAS,

    # 网页标题
    page_title: str = "Awesome-pyecharts",

    # 图表主题
    theme: str = "white",

    # 图表背景颜色
    bg_color: Optional[str] = None,

    # 远程 js host，如不设置默认为 https://assets.pyecharts.org/assets/"
    # 参考 `全局变量` 章节
    js_host: str = "",

    # 画图动画初始化配置，参考 `global_options.AnimationOpts`
    animation_opts: Union[AnimationOpts, dict] = AnimationOpts(),
)
```

#### 2. TitleOpts：标题配置项
```python
from pyecharts import options as opts
# --用法一--
obj.set_global_opts(
    title_opts=opts.TitleOpts(title="主标题", subtitle="副标题")
)
# --用法二--
obj.set_global_opts(
    # 直接通过字典设置标题，副标题
    title_opts={"text": "主标题", "subtext": "副标题"}
)

# --参数--
class TitleOpts(
    # 主标题文本，支持使用 \n 换行。
    title: Optional[str] = None,

    # 主标题跳转 URL 链接
    title_link: Optional[str] = None,

    # 主标题跳转链接方式
    # 默认值是: blank
    # 可选参数: 'self', 'blank'
    # 'self' 当前窗口打开; 'blank' 新窗口打开
    title_target: Optional[str] = None,

    # 副标题文本，支持使用 \n 换行。
    subtitle: Optional[str] = None,

    # 副标题跳转 URL 链接
    subtitle_link: Optional[str] = None,

    # 副标题跳转链接方式
    # 默认值是: blank
    # 可选参数: 'self', 'blank'
    # 'self' 当前窗口打开; 'blank' 新窗口打开
    subtitle_target: Optional[str] = None,

    # title 组件离容器左侧的距离。
    # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
    # 也可以是 'left', 'center', 'right'。
    # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
    pos_left: Optional[str] = None,

    # title 组件离容器右侧的距离。
    # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
    pos_right: Optional[str] = None,

    # title 组件离容器上侧的距离。
    # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
    # 也可以是 'top', 'middle', 'bottom'。
    # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。
    pos_top: Optional[str] = None,

    # title 组件离容器下侧的距离。
    # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
    pos_bottom: Optional[str] = None,

    # 主标题字体样式配置项，参考 `series_options.TextStyleOpts`
    title_textstyle_opts: Union[TextStyleOpts, dict, None] = None,

    # 副标题字体样式配置项，参考 `series_options.TextStyleOpts`
    subtitle_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
)
```

#### 3. AxisOpts：坐标轴配置项
```python
# --用法--
from pyecharts import options as opts
obj.set_global_opts(
    yaxis_opts=opts.AxisOpts(
        # 修改y轴刻度标签值
        axislabel_opts=opts.LabelOpts(formatter="{value}/月")
    )
)

# --参数--
class AxisOpts(
    # 坐标轴类型。可选：
    # 'value': 数值轴，适用于连续数据。
    # 'category': 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。
    # 'time': 时间轴，适用于连续的时序数据，与数值轴相比时间轴带有时间的格式化，在刻度计算上也有所不同，
    # 例如会根据跨度的范围来决定使用月，星期，日还是小时范围的刻度。
    # 'log' 对数轴。适用于对数数据。
    type_: Optional[str] = None,

    # 坐标轴名称。
    name: Optional[str] = None,

    # 是否显示 x 轴。
    is_show: bool = True,

    # 只在数值轴中（type: 'value'）有效。
    # 是否是脱离 0 值比例。设置成 true 后坐标刻度不会强制包含零刻度。在双数值轴的散点图中比较有用。
    # 在设置 min 和 max 之后该配置项无效。
    is_scale: bool = False,

    # 是否强制设置坐标轴分割间隔。
    is_inverse: bool = False,

    # 坐标轴名称显示位置。可选：
    # 'start', 'middle' 或者 'center','end'
    name_location: str = "end",

    # 坐标轴名称与轴线之间的距离。
    name_gap: Numeric = 15,

    # 坐标轴名字旋转，角度值。
    name_rotate: Optional[Numeric] = None,

    # 强制设置坐标轴分割间隔。
    # 因为 splitNumber 是预估的值，实际根据策略计算出来的刻度可能无法达到想要的效果，
    # 这时候可以使用 interval 配合 min、max 强制设定刻度划分，一般不建议使用。
    # 无法在类目轴中使用。在时间轴（type: 'time'）中需要传时间戳，在对数轴（type: 'log'）中需要传指数值。
    interval: Optional[Numeric] = None,

    # x 轴所在的 grid 的索引，默认位于第一个 grid。
    grid_index: Numeric = 0,

    # x 轴的位置。可选：
    # 'top', 'bottom'
    # 默认 grid 中的第一个 x 轴在 grid 的下方（'bottom'），第二个 x 轴视第一个 x 轴的位置放在另一侧。
    position: Optional[str] = None,

    # Y 轴相对于默认位置的偏移，在相同的 position 上有多个 Y 轴的时候有用。
    offset: Numeric = 0,

    # 坐标轴的分割段数，需要注意的是这个分割段数只是个预估值，最后实际显示的段数会在这个基础上根据分割后坐标轴刻度显示的易读程度作调整。 
    # 默认值是 5
    split_number: Numeric = 5,

    # 坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样。
    # 类目轴中 boundaryGap 可以配置为 true 和 false。默认为 true，这时候刻度只是作为分隔线，
    # 标签和数据点都会在两个刻度之间的带(band)中间。
    # 非类目轴，包括时间，数值，对数轴，boundaryGap是一个两个值的数组，分别表示数据最小值和最大值的延伸范围
    # 可以直接设置数值或者相对的百分比，在设置 min 和 max 后无效。 示例：boundaryGap: ['20%', '20%']
    boundary_gap: Union[str, bool, None] = None,

    # 坐标轴刻度最小值。
    # 可以设置成特殊值 'dataMin'，此时取数据在该轴上的最小值作为最小刻度。
    # 不设置时会自动计算最小值保证坐标轴刻度的均匀分布。
    # 在类目轴中，也可以设置为类目的序数（如类目轴 data: ['类A', '类B', '类C'] 中，序数 2 表示 '类C'。
    # 也可以设置为负数，如 -3）。
    min_: Union[Numeric, str, None] = None,

    # 坐标轴刻度最大值。
    # 可以设置成特殊值 'dataMax'，此时取数据在该轴上的最大值作为最大刻度。
    # 不设置时会自动计算最大值保证坐标轴刻度的均匀分布。
    # 在类目轴中，也可以设置为类目的序数（如类目轴 data: ['类A', '类B', '类C'] 中，序数 2 表示 '类C'。
    # 也可以设置为负数，如 -3）。
    max_: Union[Numeric, str, None] = None,

    # 自动计算的坐标轴最小间隔大小。
    # 例如可以设置成1保证坐标轴分割刻度显示成整数。
    # 默认值是 0
    min_interval: Numeric = 0,

    # 自动计算的坐标轴最大间隔大小。
    # 例如，在时间轴（（type: 'time'））可以设置成 3600 * 24 * 1000 保证坐标轴分割刻度最大为一天。
    max_interval: Optional[Numeric] = None,

    # 坐标轴刻度线配置项，参考 `global_options.AxisLineOpts`
    axisline_opts: Union[AxisLineOpts, dict, None] = None,

    # 坐标轴刻度配置项，参考 `global_options.AxisTickOpts`
    axistick_opts: Union[AxisTickOpts, dict, None] = None,

    # 坐标轴标签配置项，参考 `series_options.LabelOpts`
    axislabel_opts: Union[LabelOpts, dict, None] = None,

    # 坐标轴指示器配置项，参考 `global_options.AxisPointerOpts`
    axispointer_opts: Union[AxisPointerOpts, dict, None] = None,

    # 坐标轴名称的文字样式，参考 `series_options.TextStyleOpts`
    name_textstyle_opts: Union[TextStyleOpts, dict, None] = None,

    # 分割区域配置项，参考 `series_options.SplitAreaOpts`
    splitarea_opts: Union[SplitAreaOpts, dict, None] = None,

    # 分割线配置项，参考 `series_options.SplitLineOpts`
    splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(),
)
```
#### 4. BrushOpts：区域选择组件配置项
```python
# --用法--
from pyecharts import options as opts
obj.set_global_opts(
    brush_opts=opts.BrushOpts()
)

# --参数--
class BrushOpts(
    # 使用在 toolbox 中的按钮。默认值为 ["rect", "polygon", "keep", "clear"]
    # brush 相关的 toolbox 按钮有：
    # "rect"：开启矩形选框选择功能。
    # "polygon"：开启任意形状选框选择功能。
    # "lineX"：开启横向选择功能。
    # "lineY"'：开启纵向选择功能。
    # "keep"：切换『单选』和『多选』模式。后者可支持同时画多个选框。前者支持单击清除所有选框。
    # "clear"：清空所有选框。
    tool_box: Optional[Sequence] = None,

    # 不同系列间，选中的项可以联动。
    # brush_link 配置项是一个列表，内容是 seriesIndex，指定了哪些 series 可以被联动。
    # 例如可以是：
    # [3, 4, 5] 表示 seriesIndex 为 3, 4, 5 的 series 可以被联动。
    # "all" 表示所有 series 都进行 brushLink。
    # None 表示不启用 brush_link 功能。
    brush_link: Union[Sequence, str] = None,

    # 指定哪些 series 可以被刷选，可取值为：
    # "all": 所有 series
    # series index 列表, 如 [0, 4, 2]，表示指定这些 index 所对应的坐标系。
    # 某个 series index, 如 0，表示这个 index 所对应的坐标系。
    series_index: Union[Sequence, Numeric, str] = None,

    # 指定哪些 geo 可以被刷选。可以设置 brush 是全局的还是属于坐标系的。
    # 全局 brush
    # 在 echarts 实例中任意地方刷选。这是默认情况。如果没有指定为坐标系 brush，就是全局 brush。
    # 坐标系 brush
    # 在指定的坐标系中刷选。选框可以跟随坐标系的缩放和平移（ roam 和 dataZoom ）而移动。
    # 坐标系 brush 实际更为常用，尤其是在 geo 中。
    # 通过指定 brush.geoIndex 或 brush.xAxisIndex 或 brush.yAxisIndex 来规定可以在哪些坐标系中进行刷选。
    # 指定哪些 series 可以被刷选，可取值为：
    # "all": 表示所有 series
    # series index 列表, 如 [0, 4, 2]，表示指定这些 index 所对应的坐标系。
    # 某个 series index, 如 0，表示这个 index 所对应的坐标系。
    geo_index: Union[Sequence, Numeric, str] = None,

    # 指定哪些 xAxisIndex 可以被刷选。可以设置 brush 是全局的还是属于坐标系的。
    # 全局 brush
    # 在 echarts 实例中任意地方刷选。这是默认情况。如果没有指定为坐标系 brush，就是全局 brush。
    # 坐标系 brush
    # 在指定的坐标系中刷选。选框可以跟随坐标系的缩放和平移（ roam 和 dataZoom ）而移动。
    # 坐标系 brush 实际更为常用，尤其是在 geo 中。
    # 通过指定 brush.geoIndex 或 brush.xAxisIndex 或 brush.yAxisIndex 来规定可以在哪些坐标系中进行刷选。
    # 指定哪些 series 可以被刷选，可取值为：
    # "all": 表示所有 series
    # series index 列表, 如 [0, 4, 2]，表示指定这些 index 所对应的坐标系。
    # 某个 series index, 如 0，表示这个 index 所对应的坐标系。
    x_axis_index: Union[Sequence, Numeric, str] = None,

    # 指定哪些 yAxisIndex 可以被刷选。可以设置 brush 是全局的还是属于坐标系的。
    # 全局 brush
    # 在 echarts 实例中任意地方刷选。这是默认情况。如果没有指定为坐标系 brush，就是全局 brush。
    # 坐标系 brush
    # 在指定的坐标系中刷选。选框可以跟随坐标系的缩放和平移（ roam 和 dataZoom ）而移动。
    # 坐标系 brush 实际更为常用，尤其是在 geo 中。
    # 通过指定 brush.geoIndex 或 brush.xAxisIndex 或 brush.yAxisIndex 来规定可以在哪些坐标系中进行刷选。
    # 指定哪些 series 可以被刷选，可取值为：
    # "all": 表示所有 series
    # series index 列表, 如 [0, 4, 2]，表示指定这些 index 所对应的坐标系。
    # 某个 series index, 如 0，表示这个 index 所对应的坐标系。
    y_axis_index: Union[Sequence, Numeric, str] = None,

    # 默认的刷子类型。默认值为 rect。
    # 可选参数如下：
    # "rect"：矩形选框。
    # "polygon"：任意形状选框。
    # "lineX"：横向选择。
    # "lineY"：纵向选择。
    brush_type: str = "rect",

    # 默认的刷子的模式。可取值为：
    # 默认为 single
    # "single"：单选。
    # "multiple"：多选。
    brush_mode: str = "single",

    # 已经选好的选框是否可以被调整形状或平移。默认值为 True
    transformable: bool = True,

    # 选框的默认样式，值为
    # {
    #      "borderWidth": 1,
    #      "color": "rgba(120,140,180,0.3)",
    #      "borderColor": "rgba(120,140,180,0.8)"
    # },
    brush_style: Optional[dict] = None,

    # 默认情况，刷选或者移动选区的时候，会不断得发 brushSelected 事件，从而告诉外界选中的内容。
    # 但是频繁的事件可能导致性能问题，或者动画效果很差。
    # 所以 brush 组件提供了 brush.throttleType，brush.throttleDelay 来解决这个问题。
    # throttleType 取值可以是：
    # "debounce"：表示只有停止动作了（即一段时间没有操作了），才会触发事件。时间阈值由 brush.throttleDelay 指定。
    # "fixRate"：表示按照一定的频率触发事件，时间间隔由 brush.throttleDelay 指定。
    throttle_type: str = "fixRate",

    # 默认为 0 表示不开启 throttle。
    throttle_delay: Numeric = 0,

    # 在 brush_mode 为 "single" 的情况下，是否支持单击清除所有选框。
    remove_on_click: bool = True,

    # 定义在选中范围外的视觉元素。最终参数以字典的形式进行配置
    # 可选的视觉元素有：
    # symbol: 图元的图形类别。
    # symbolSize: 图元的大小。
    # color: 图元的颜色。
    # colorAlpha: 图元的颜色的透明度。
    # opacity: 图元以及其附属物（如文字标签）的透明度。
    # colorLightness: 颜色的明暗度，参见 https://en.wikipedia.org/wiki/HSL_and_HSV。
    # colorSaturation: 颜色的饱和度，参见 https://en.wikipedia.org/wiki/HSL_and_HSV。
    # colorHue: 颜色的色调，参见 https://en.wikipedia.org/wiki/HSL_and_HSV。
    out_of_brush: dict = None,
)
```
#### 5. LegendOpts：图例配置项
```python

# --用法--
from pyecharts import options as opts
obj.set_global_opts(
    legend_opts=opts.LegendOpts(
        type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
    )
)

# --参数--
class LegendOpts(
    # 图例的类型。可选值：
    # 'plain'：普通图例。缺省就是普通图例。
    # 'scroll'：可滚动翻页的图例。当图例数量较多时可以使用。
    type_: Optional[str] = None,

    # 图例选择的模式，控制是否可以通过点击图例改变系列的显示状态。默认开启图例选择，可以设成 false 关闭
    # 除此之外也可以设成 'single' 或者 'multiple' 使用单选或者多选模式。
    selected_mode: Union[str, bool, None] = None,

    # 是否显示图例组件
    is_show: bool = True,

    # 图例组件离容器左侧的距离。
    # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
    # 也可以是 'left', 'center', 'right'。
    # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
    pos_left: Union[str, Numeric, None] = None,

    # 图例组件离容器右侧的距离。
    # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
    pos_right: Union[str, Numeric, None] = None,

    # 图例组件离容器上侧的距离。
    # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
    # 也可以是 'top', 'middle', 'bottom'。
    # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。
    pos_top: Union[str, Numeric, None] = None,

    # 图例组件离容器下侧的距离。
    # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
    pos_bottom: Union[str, Numeric, None] = None,

    # 图例列表的布局朝向。可选：'horizontal', 'vertical'
    orient: Optional[str] = None,

    # 图例组件字体样式，参考 `series_options.TextStyleOpts`
    textstyle_opts: Union[TextStyleOpts, dict, None] = None,
)

```

#### 6. VisualMapOpts：视觉映射配置项
```python
# 用法
from pyecharts import options as opts
obj.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(max_=200)
)

# 参数
class VisualMapOpts(
    # 是否显示视觉映射配置
    is_show: bool = True,

    # 映射过渡类型，可选，"color", "size"
    type_: str = "color",

    # 指定 visualMapPiecewise 组件的最小值。
    min_: Union[int, float] = 0,

    # 指定 visualMapPiecewise 组件的最大值。
    max_: Union[int, float] = 100,

    # 两端的文本，如['High', 'Low']。
    range_text: Union[list, tuple] = None,

    # visualMap 组件过渡颜色
    range_color: Union[Sequence[str]] = None,

    # visualMap 组件过渡 symbol 大小
    range_size: Union[Sequence[int]] = None,

    # 如何放置 visualMap 组件，水平（'horizontal'）或者竖直（'vertical'）。
    orient: str = "vertical",

    # visualMap 组件离容器左侧的距离。
    # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
    # 也可以是 'left', 'center', 'right'。
    # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
    pos_left: Optional[str] = None,

    # visualMap 组件离容器右侧的距离。
    # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
    pos_right: Optional[str] = None,

    # visualMap 组件离容器上侧的距离。
    # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
    # 也可以是 'top', 'middle', 'bottom'。
    # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。
    pos_top: Optional[str] = None,

    # visualMap 组件离容器下侧的距离。
    # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
    pos_bottom: Optional[str] = None,

    # 对于连续型数据，自动平均切分成几段。默认为5段。连续数据的范围需要 max 和 min 来指定
    split_number: int = 5,

    # 指定取哪个系列的数据，默认取所有系列。
    series_index: Union[Numeric, Sequence, None] = None,

    # 组件映射维度
    dimension: Optional[Numeric] = None,

    # 是否显示拖拽用的手柄（手柄能拖拽调整选中范围）。
    is_calculable: bool = True,

    # 是否为分段型
    is_piecewise: bool = False,

    # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。例如：
    # pieces: [
    #   {"min": 1500}, // 不指定 max，表示 max 为无限大（Infinity）。
    #   {"min": 900, "max": 1500},
    #   {"min": 310, "max": 1000},
    #   {"min": 200, "max": 300},
    #   {"min": 10, "max": 200, "label": '10 到 200（自定义label）'},
    #   {"value": 123, "label": '123（自定义特殊颜色）', "color": 'grey'}, //表示 value 等于 123 的情况
    #   {"max": 5}     // 不指定 min，表示 min 为无限大（-Infinity）。
    # ]
    pieces: Optional[Sequence] = None,

    # 定义 在选中范围外 的视觉元素。（用户可以和 visualMap 组件交互，用鼠标或触摸选择范围）
    #  可选的视觉元素有：
    #  symbol: 图元的图形类别。
    #  symbolSize: 图元的大小。
    #  color: 图元的颜色。
    #  colorAlpha: 图元的颜色的透明度。
    #  opacity: 图元以及其附属物（如文字标签）的透明度。
    #  colorLightness: 颜色的明暗度，参见 HSL。
    #  colorSaturation: 颜色的饱和度，参见 HSL。
    #  colorHue: 颜色的色调，参见 HSL。
    out_of_range: Optional[Sequence] = None,

    # 文字样式配置项，参考 `series_options.TextStyleOpts`
    textstyle_opts: Union[TextStyleOpts, dict, None] = None,
)
```

#### 1、def dump_options()
>获取全局 options，JSON 格式（JsCode 生成的函数不带引号）


#### 2、def dump_options_with_quotes()
>获取全局 options，JSON 格式（JsCode 生成的函数带引号，在前后端分离传输数据时使用）

#### 3、def render() -> str
>渲染图表到 HTML 文件
```python
def render(
    # 生成图片路径
    path: str = "render.html",

    # 模板路径
    template_name: str = "simple_chart.html",

    # jinja2.Environment 类实例，可以配置各类环境参数
    env: Optional[Environment] = None,
)
```

#### 4、def render_notebook()
>将图形渲染到 notebook

