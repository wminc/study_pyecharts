# -*- coding:utf8 -*-
"""
Created on 2019/10/9 14:44

@author: minc

Page-->多图在同一页面展示
Page.add_chart(图例对象)

Faker-->虚拟数据
Faker.choose()产生x轴的刻度对象列表
Faker.values()产生数值列表

"""

import pyecharts.options as opts
from pyecharts.charts import Line, Page
from pyecharts.faker import Collector, Faker

obj_C = Collector()

@obj_C.funcs
def line_base():
    obj_l = Line()
    obj_l.add_xaxis(Faker.choose())
    obj_l.add_yaxis("商家A",Faker.values())
    obj_l.add_yaxis("商家B", Faker.values())

    title_options = opts.TitleOpts(title="Line-基本示例", subtitle="副标题")
    obj_l.set_global_opts(title_opts=title_options)
    return obj_l


# 折线图，跳过空值 设置参数is_connect_nones=True
@obj_C.funcs
def line_connect_null():
    y = Faker.values()
    # 将随机生成的y值设置为空
    y[3], y[5] = None, None
    obj_l = Line()
    obj_l.add_xaxis(Faker.choose())
    obj_l.add_yaxis("商家A", y, is_connect_nones=True)
    obj_l.set_global_opts(title_opts=opts.TitleOpts(title="Line-连接空数据", subtitle="副标题"))
    return obj_l


# 平滑的曲线连接 设置参数is_smooth=True
@obj_C.funcs
def line_smooth():
    y = Faker.values()
    # 将随机生成的y值设置为空
    y[3], y[5] = None, None
    obj_l = Line()
    obj_l.add_xaxis(Faker.choose())
    obj_l.add_yaxis("商家A", Faker.values(), is_smooth=True)
    obj_l.add_yaxis("商家B", Faker.values(), is_smooth=True)
    obj_l.set_global_opts(title_opts=opts.TitleOpts(title="Line-smooth", subtitle="副标题"))
    return obj_l


# 折线面积图，曲线与x轴围成图形面积，且没有贴着y轴
@obj_C.funcs
def line_areastyle():
    obj_l = Line()
    obj_l.add_xaxis(Faker.choose())
    obj_l.add_yaxis("商家A", Faker.values(), areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
    obj_l.add_yaxis("商家B", Faker.values(), areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
    obj_l.set_global_opts(title_opts=opts.TitleOpts(title="Line-面积图", subtitle="副标题"))
    return obj_l


# 曲线面积图，平滑的曲线与x轴，y轴围成图形面积
@obj_C.funcs
def line_areastyle_boundary_gap():
    obj_l = Line()
    obj_l.add_xaxis(Faker.choose())
    obj_l.add_yaxis("商家A", Faker.values(), is_smooth=True)
    obj_l.add_yaxis("商家B", Faker.values(), is_smooth=True)
    obj_l.set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
    obj_l.set_global_opts(
            title_opts=opts.TitleOpts(title="Line-面积图（紧贴 Y 轴）",subtitle="副标题"),
            xaxis_opts=opts.AxisOpts(boundary_gap=False)
        )
    return obj_l


# 0-9以2的x次幂图像
@obj_C.funcs
def line_power():
    obj_l = Line()
    obj_l.add_xaxis(xaxis_data=["0","1", "2", "3", "4", "5", "6", "7", "8"])
    obj_l.add_yaxis("2的指数图像", y_axis=[1, 2, 4, 8, 16, 32, 64, 128, 256],linestyle_opts=opts.LineStyleOpts(width=2), is_smooth=True)
    obj_l.set_series_opts(
        # 设置该参数，则x对应的y值会显示出来，该参数默认为True
        label_opts=opts.LabelOpts(is_show=True),
    )
    obj_l.set_global_opts(
            title_opts=opts.TitleOpts(title="Line-2的指数图像",subtitle="副标题"),
            xaxis_opts=opts.AxisOpts(
                name="x轴",

                # 坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样,可设置x轴刻度顶格
                boundary_gap=False
                # 类目轴中在 boundaryGap 为 true 的时候有效，可以保证刻度线和标签对齐。
                # axistick_opts=opts.AxisTickOpts(is_align_with_label=True)
            ),
            yaxis_opts=opts.AxisOpts(
                # y轴名字
                name="y轴",

                # 根据y轴刻度的横线
                splitline_opts=opts.SplitLineOpts(is_show=True),

                # 只在数值轴中（type: 'value'）有效
                # is_scale = False
            )
        )
    return obj_l


# 标记折线图上某一点，着重显示
@obj_C.funcs
def line_markpoint_custom():
    x, y = Faker.choose(), Faker.values()
    obj_l = Line()
    obj_l.add_xaxis(x)
    obj_l.add_yaxis("商家A",
                    y,
                    markpoint_opts=opts.MarkPointOpts(
                        data=[opts.MarkPointItem(name="自定义标记点", coord=[x[2], y[2]], value=y[2])]
                    )
    )
    obj_l.set_series_opts(
        # 设置该参数，则x对应的y值会显示出来，该参数默认为True
        label_opts=opts.LabelOpts(is_show=False),
    )
    obj_l.set_global_opts(
        title_opts=opts.TitleOpts(title="Line-MarkPoint（自定义）",subtitle="自定义标注"),
        xaxis_opts=opts.AxisOpts(
            name="x轴",

            # 坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样,可设置x轴刻度顶格
            boundary_gap=True,
            # 类目轴中在 boundaryGap 为 true 的时候有效，可以保证刻度线和标签对齐。
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True)
        ),
    )
    return obj_l


# 标注折线上的最大最小值
@obj_C.funcs
def line_markpoint():
    obj_l = Line()
    obj_l.add_xaxis(Faker.choose())
    obj_l.add_yaxis("商家A",
                    Faker.values(),
                    markpoint_opts=opts.MarkPointOpts(
                        data=[opts.MarkPointItem(type_="min"),opts.MarkPointItem(type_="max")],

                        )
                    )
    obj_l.add_yaxis("商家B",
                    Faker.values(),
                    markpoint_opts=opts.MarkPointOpts(
                        data=[opts.MarkPointItem(type_="min"),opts.MarkPointItem(type_="max")]
                    )
                    )
    obj_l.set_series_opts(
        # 该参数设置在这里对商家A,商家B都起作用
        # 设置该参数，则x对应的y值会显示出来，该参数默认为True
        label_opts=opts.LabelOpts(is_show=False)
    )
    obj_l.set_global_opts(
        title_opts=opts.TitleOpts(title="Line-MarkPoint（最大最小值）", subtitle="最大最小值标注"),
        xaxis_opts=opts.AxisOpts(
            name="x轴",

            # 坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样,可设置x轴刻度顶格
            boundary_gap=True,
            # 类目轴中在 boundaryGap 为 true 的时候有效，可以保证刻度线和标签对齐。
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True)
        ),

    )
    return obj_l


# 标注两条折线的平均值的线
@obj_C.funcs
def line_markline():
    obj_l = Line()
    obj_l.add_xaxis(Faker.choose())
    obj_l.add_yaxis("商家A",
                    Faker.values(),
                    markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
                    # 该参数设置在这里只对商家A起作用
                    label_opts=opts.LabelOpts(is_show=False)
                    )
    obj_l.add_yaxis("商家B",
                    Faker.values(),
                    markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
                    )

    obj_l.set_series_opts(
        # 该参数设置在这里对商家A,商家B都起作用
        # 设置该参数，则x对应的y值会显示出来，该参数默认为True
        label_opts=opts.LabelOpts(is_show=False),
    )
    obj_l.set_global_opts(
        title_opts=opts.TitleOpts(title="Line-MarkLine", subtitle="平均值的线"),
        xaxis_opts=opts.AxisOpts(
            name="x轴",

            # 坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样,可设置x轴刻度顶格
            boundary_gap=True,
            # 类目轴中在 boundaryGap 为 true 的时候有效，可以保证刻度线和标签对齐。
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True)
        ),
    )
    return obj_l


# 阶梯图，先上升或下降再保持下一个值的状态
@obj_C.funcs
def line_step():
    obj_l = Line()
    obj_l.add_xaxis(Faker.choose())
    obj_l.add_yaxis("商家A", Faker.values(), is_step=True)
    obj_l.set_global_opts(title_opts=opts.TitleOpts(title="Line-阶梯图", subtitle="副标题"))
    return obj_l


# 自定义样式配置
@obj_C.funcs
def line_itemstyle():
    obj_l = Line()
    obj_l.add_xaxis(Faker.choose())
    obj_l.add_yaxis("商家A",
                    Faker.values(),
                    symbol="triangle",
                    symbol_size=20,
                    linestyle_opts=opts.LineStyleOpts(color="green", width=4, type_="dashed"),
                    itemstyle_opts=opts.ItemStyleOpts(
                        border_width=3,
                        border_color="yellow",
                        color="blue"
                    )
                    )
    obj_l.set_global_opts(title_opts=opts.TitleOpts(title="Line-ItemStyle", subtitle="副标题"))
    return obj_l


if __name__ == '__main__':
    # line1 = line_base()
    # line1.render('html/line_base.html')
    # line2 = line_connect_null()
    # line2.render('html/line_connect_null.html')

    # 将多个图展示到同一页面
    # obj_page = Page()
    # obj_page.add(*[line_base(),line_connect_null(),line_smooth(),line_areastyle()]).render('html/example_line.html')

    # 更多图的时候，需要用到Collector()
    obj_page = Page()
    obj_page.add(*[fn() for fn, _ in obj_C.charts]).render('html/example_line.html')