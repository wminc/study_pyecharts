# -*- coding:utf8 -*-
"""
Created on 2019/10/10 15:06

@author: minc
"""

from pyecharts import options as opts
from pyecharts.charts import Bar,Page
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Collector,Faker
from pyecharts.globals import ThemeType

obj_C = Collector()

@obj_C.funcs
def bar_base():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis('商家A',Faker.values())
    obj_bar.add_yaxis('商家B',Faker.values())
    obj_bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    return obj_bar


#渐变圆柱
@obj_C.funcs
def bar_border_radius():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("商家A", Faker.values(),category_gap="60%")
    obj_bar.set_series_opts(
        itemstyle_opts={
            "normal":{
                "color":JsCode(
                    """
                    new echarts.graphic.LinearGradient(0, 0, 0, 1, 
                    [{offset: 0,color: 'rgba(0, 244, 255, 1)'}, 
                    {offset: 1,color: 'rgba(0, 77, 167, 1)'}], 
                    false)
                    """
                ),
                "barBorderRadius":[30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)"
            }
        }
    )
    obj_bar.set_global_opts(title_opts = opts.TitleOpts(title = "Bar-渐变圆柱", subtitle = "副标题"))
    return obj_bar


# 柱从底部弹出的动态效果
@obj_C.funcs
def bar_base_with_animation():
    obj_bar = Bar(
        init_opts=opts.InitOpts(
            animation_opts=opts.AnimationOpts(
                animation_delay=1000,
                animation_easing="elasticOut"
            )
        )
    )
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("A", Faker.values())
    obj_bar.add_yaxis("B", Faker.values())
    obj_bar.set_global_opts(title_opts = opts.TitleOpts(title = "Bar-动画配置基本示例", subtitle = "副标题"))
    return obj_bar


# 自定义背景图
@obj_C.funcs
def bar_base_with_custom_background_image():
    obj_bar = Bar(
        init_opts=opts.InitOpts(
            bg_color={
                "type":"pattern",
                "image":JsCode("img"),
                "repeat":"no-repeat"
            }
        )
    )
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("A", Faker.values())
    obj_bar.add_yaxis("B", Faker.values())
    obj_bar.set_global_opts(
        title_opts = opts.TitleOpts(
            title = "Bar-背景图基本示例",
            subtitle = "副标题",
            # 设置标题为白色
            title_textstyle_opts=opts.TextStyleOpts(color="white")
        )
    )
    obj_bar.add_js_funcs(
        "var img = new Image(); img.src = 'https://s2.ax1x.com/2019/07/08/ZsS0fK.jpg';"
    )
    return obj_bar


# 通过字典设置主题，标题，副标题
@obj_C.funcs
def bar_base_dict_config():
    obj_bar = Bar({"theme":ThemeType.MACARONS})
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("A", Faker.values())
    obj_bar.add_yaxis("B", Faker.values())
    obj_bar.set_global_opts(
        # 直接通过字典设置标题付宝体
        title_opts={"text": "Bar-通过 dict 进行配置", "subtext": "我也是通过 dict 进行配置的"}
    )
    return obj_bar


# 设置默认只显示单系列柱
@obj_C.funcs
def bar_is_selected():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("A", Faker.values())
    obj_bar.add_yaxis("B", Faker.values(),is_selected=False)
    obj_bar.set_global_opts(
        # 直接通过字典设置标题，副标题
        title_opts={"text": "Bar-默认取消显示某 Series", "subtext": "副标题"}
    )
    return obj_bar


# 显示 ToolBox
@obj_C.funcs
def bar_toolbox():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("A", Faker.values())
    obj_bar.add_yaxis("B", Faker.values())
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-显示 ToolBox", subtitle="副标题"),
        toolbox_opts=opts.ToolboxOpts(),
        # 设置该参数时，就不会显示图例
        legend_opts=opts.LegendOpts(is_show=False)
    )
    return obj_bar


# 设置单系列柱间距离
@obj_C.funcs
def bar_same_series_gap():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    # category_gap该参数设置单系列柱之间的距离
    obj_bar.add_yaxis("A", Faker.values(),category_gap="60%")
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-单系列柱间距离", subtitle="副标题"),
    )
    return obj_bar


# 设置不同系列柱间距离
@obj_C.funcs
def bar_different_series_gap():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    # gap该参数设置
    obj_bar.add_yaxis("A", Faker.values(),gap="20%")
    obj_bar.add_yaxis("B", Faker.values(),gap="20%")
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-不同系列柱间距离", subtitle="副标题"),
    )
    return obj_bar


# 修改y轴刻度标签值
@obj_C.funcs
def bar_yaxis_formatter():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("A", Faker.values())
    obj_bar.add_yaxis("B", Faker.values())
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-Y 轴 formatter", subtitle="副标题"),
        yaxis_opts=opts.AxisOpts(
            # 修改y轴刻度标签值
            axislabel_opts=opts.LabelOpts(formatter="{value}/月")
        )
    )
    return obj_bar


# 设置x，y轴名称
@obj_C.funcs
def bar_yaxis_formatter():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("A", Faker.values())
    obj_bar.add_yaxis("B", Faker.values())
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-XY 轴名称", subtitle="副标题"),
        yaxis_opts=opts.AxisOpts(name='我是y轴'),
        xaxis_opts = opts.AxisOpts(name='我是x轴')
    )
    return obj_bar


# 翻转 XY 轴
@obj_C.funcs
def bar_reversal_axis():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("A", Faker.values())
    obj_bar.add_yaxis("B", Faker.values())
    # 设置翻转 XY 轴
    obj_bar.reversal_axis()
    # 设置标签靠右显示
    obj_bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-翻转 XY 轴", subtitle="副标题"),)
    return obj_bar


# 把两个系列柱叠起来
@obj_C.funcs
def bar_stack0():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    # stack该参数设置
    obj_bar.add_yaxis("A", Faker.values(),stack="stack1")
    obj_bar.add_yaxis("B", Faker.values(),stack="stack1")
    # 设置标签不显示
    obj_bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-堆叠数据（全部）", subtitle="副标题"),)
    return obj_bar


# 3个系列柱，把两个系列柱叠起来，另一个不堆叠
@obj_C.funcs
def bar_stack1():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    # stack该参数设置
    obj_bar.add_yaxis("A", Faker.values(),stack="stack1")
    obj_bar.add_yaxis("B", Faker.values(),stack="stack1")
    obj_bar.add_yaxis("C", Faker.values())
    # 设置标签不显示
    obj_bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-堆叠数据（部分）", subtitle="副标题"),)
    return obj_bar


# 在柱形图形上标注指定点
@obj_C.funcs
def bar_markpoint_type():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("A", Faker.values())
    obj_bar.add_yaxis("B", Faker.values())
    # 设置标签不显示
    obj_bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        # 标注指定类型的点
        markpoint_opts=opts.MarkPointOpts(
            data =[
                opts.MarkPointItem(type_="max",name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
                opts.MarkPointItem(type_="average", name="平均值")
            ]
        )
    )
    obj_bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（指定类型）", subtitle="副标题"))
    return obj_bar


# 在柱形图形上标注自定义点
@obj_C.funcs
def bar_markpoint_custom():
    x, y = Faker.choose(), Faker.values()
    obj_bar = Bar()
    obj_bar.add_xaxis(x)
    obj_bar.add_yaxis("A",
                      y,
                      # 自定义标注点,设置在这里obj_bar.add_yaxis，只有一个系列图标注，
                      # 如果该参数设置到obj_bar.set_series_opts，所有系列柱的指定柱就会标注该点，但值是一样的是第一个系列柱的值
                      markpoint_opts=opts.MarkPointOpts(
                          data=[opts.MarkPointItem(name="自定义标记点", coord=[x[2], y[2]], value=y[2])]
                      ))
    obj_bar.add_yaxis("B", Faker.values())
    # 设置标签不显示
    obj_bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
    )
    obj_bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（自定义）", subtitle="副标题"))
    return obj_bar


# 指定类型横线
@obj_C.funcs
def bar_markline_type():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("商家A",Faker.values())
    obj_bar.add_yaxis("商家B",Faker.values())
    obj_bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show = False),
        markline_opts=opts.MarkPointOpts(
            data = [
                opts.MarkLineItem(type_="min", name="最小值"),
                opts.MarkLineItem(type_="max", name="最大值"),
                opts.MarkLineItem(type_="average", name="平均值"),
            ]
        )
    )
    obj_bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkLine（指定类型）", subtitle="平均值的线"))
    return obj_bar


# 自定义横线
@obj_C.funcs
def bar_markline_type():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("商家A",Faker.values())
    obj_bar.add_yaxis("商家B",Faker.values())
    obj_bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show = False),
        markline_opts=opts.MarkPointOpts(
            data = [opts.MarkLineItem(y=50, name="yAxis=50")]
        )
    )
    obj_bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkLine（自定义）", subtitle="自定义的线"))
    return obj_bar


# datazoom组件显示，datazoom组件动态调整x轴日期区间，该组件水平展示，水平时控制x轴
@obj_C.funcs
def bar_datazoom_slider():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.days_attrs)
    obj_bar.add_yaxis("商家A", Faker.days_values)
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）", subtitle="副标题"),
        datazoom_opts=opts.DataZoomOpts()
    )
    return obj_bar


# datazoom组件显示，datazoom组件动态调整y轴区间，该组件垂直展示，垂直时控制y轴
@obj_C.funcs
def bar_datazoom_slider_vertical():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.days_attrs)
    obj_bar.add_yaxis("商家A", Faker.days_values)
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-垂直）", subtitle="副标题"),
        datazoom_opts=opts.DataZoomOpts(orient="vertical")
    )
    return obj_bar


# datazoom组件不显示，由鼠标动态调整x轴区间
@obj_C.funcs
def bar_datazoom_inside():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.days_attrs)
    obj_bar.add_yaxis("商家A", Faker.days_values)
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（inside）", subtitle="副标题"),
        datazoom_opts=opts.DataZoomOpts(type_='inside')
    )
    return obj_bar


# datazoom组件显示,既可以用该组件又可以用鼠标动态调整x轴区间
@obj_C.funcs
def bar_datazoom_both():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.days_attrs)
    obj_bar.add_yaxis("商家A", Faker.days_values)
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider+inside）", subtitle="副标题"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_='inside')]
    )
    return obj_bar


# 直方图
@obj_C.funcs
def bar_histogram():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    #直方图就是紧挨着的系列柱category_gap=0调节系列柱之间距离，color=Faker.rand_color()随机颜色
    obj_bar.add_yaxis("商家A", Faker.values(),category_gap=0, color=Faker.rand_color())
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-直方图", subtitle="副标题")
    )
    return obj_bar


# 直方图
@obj_C.funcs
def bar_histogram():
    x = Faker.dogs + Faker.animal
    xlen = len(x)
    y = []
    for idx, item in enumerate(x):
        if idx <= xlen / 2:
            bar_item = opts.BarItem(
                    name=item,
                    value=(idx + 1) * 10,
                    itemstyle_opts=opts.ItemStyleOpts(color="#749f83")
                )
        else:
            bar_item = opts.BarItem(
                    name=item,
                    value=(xlen + 1 - idx) * 10,
                    itemstyle_opts=opts.ItemStyleOpts(color="#d48265"),
                )
        y.append(bar_item)

    obj_bar = Bar()
    obj_bar.add_xaxis(x)
    #直方图就是紧挨着的系列柱category_gap=0调节系列柱之间距离，
    # color=Faker.rand_color()因为上面设置了柱的颜色，这里只对图例legend的颜色起作用
    obj_bar.add_yaxis("series0", y, category_gap=0,color=Faker.rand_color())
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-直方图（颜色区分）", subtitle="副标题")
    )
    return obj_bar


# 配置x轴标签旋转
@obj_C.funcs
def bar_rorate_xaxis_label():
    obj_bar = Bar()
    x_data = [
                "名字很长的X轴标签1",
                "名字很长的X轴标签2",
                "名字很长的X轴标签3",
                "名字很长的X轴标签4",
                "名字很长的X轴标签5",
                "名字很长的X轴标签6",
            ]
    obj_bar.add_xaxis(x_data)

    obj_bar.add_yaxis("商家A", [10, 20, 30, 40, 50, 40])
    obj_bar.add_yaxis("商家B", [20, 10, 40, 30, 40, 50])
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="旋转X轴标签", subtitle="解决标签名字过长的问题"),
        # 使之旋转-15度, 正度数 是逆时针，负度数 是顺时针
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15))
    )
    return obj_bar


#Graphic 组件示例
@obj_C.funcs
def bar_graphic_component():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("商家A", Faker.values())
    obj_bar.add_yaxis("商家B", Faker.values())
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-Graphic 组件示例", subtitle="副标题"),
        graphic_opts=opts.GraphicGroup(
                graphic_item=opts.GraphicItem(
                    rotation=JsCode("Math.PI / 4"),
                    bounding="raw",
                    right=110,
                    bottom=110,
                    z=100,
                ),
                children=[
                    opts.GraphicRect(
                        graphic_item=opts.GraphicItem(
                            left="center", top="center", z=100
                        ),
                        graphic_shape_opts=opts.GraphicShapeOpts(
                            width=400, height=50
                        ),
                        graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                            fill="rgba(0,0,0,0.3)"
                        ),
                    ),
                    opts.GraphicText(
                        graphic_item=opts.GraphicItem(
                            left="center", top="center", z=100
                        ),
                        graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                            text="pyecharts bar chart",
                            font="bold 26px Microsoft YaHei",
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="#fff"
                            ),
                        ),
                    )
                ]
            )

    )
    return obj_bar


# Bar-Brush示例
@obj_C.funcs
def bar_with_brush():
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())
    obj_bar.add_yaxis("商家A", Faker.values())
    obj_bar.add_yaxis("商家B", Faker.values())
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-Brush示例", subtitle="副标题"),
        brush_opts=opts.BrushOpts()
    )
    return obj_bar


# Bar-根据y轴的值自定义柱状的颜色
@obj_C.funcs
def bar_custom_bar_color():
    # 小于50红色，50-100蓝色，其他绿色
    color_function = """
            function (params) {
                if (params.value > 0 && params.value < 50) {
                    return 'red';
                } else if (params.value > 50 && params.value < 100) {
                    return 'blue';
                }
                return 'green';
            }
            """
    obj_bar = Bar()
    obj_bar.add_xaxis(Faker.choose())

    # 这里设置color不起作用
    obj_bar.add_yaxis("商家A", Faker.values(),color='#C1C1C1',itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))
    obj_bar.add_yaxis("商家B", Faker.values(),color='#909090',itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))
    obj_bar.add_yaxis("商家C", Faker.values(),color='#404040',itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))
    obj_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-自定义柱状颜色", subtitle="副标题"),
        brush_opts=opts.BrushOpts()
    )
    return obj_bar


if __name__ == '__main__':
    obj_page = Page()
    obj_page.add(*[fn() for fn, _ in obj_C.charts]).render('html/example_bar.html')