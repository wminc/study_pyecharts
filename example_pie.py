# -*- coding:utf8 -*-
"""
Created on 2019/10/12 10:51

@author: minc
饼图
"""

from pyecharts import options as opts
from pyecharts.charts import Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Collector, Faker

obj_C = Collector()

@obj_C.funcs
def pie_base():
    obj_pie = Pie()
    obj_pie.add("",[list(z) for z in zip(Faker.choose(), Faker.values())])
    obj_pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    obj_pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例",subtitle ="副标题"))
    return obj_pie


# 设置颜色
@obj_C.funcs
def pie_set_colors():
    obj_pie = Pie()
    obj_pie.add("",[list(z) for z in zip(Faker.choose(), Faker.values())])
    obj_pie.set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    obj_pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    obj_pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色",subtitle ="副标题"))
    return obj_pie

# 调整饼图位置
@obj_C.funcs
def pie_position():
    obj_pie = Pie()
    # center=["35%", "50%"]
    # 饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
    # 默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
    obj_pie.add("",[list(z) for z in zip(Faker.choose(), Faker.values())],center=["35%", "50%"])
    obj_pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    obj_pie.set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-设置位置",subtitle ="副标题"),
        legend_opts=opts.LegendOpts(pos_left="15%"),
    )
    return obj_pie


# 设置为圆环
@obj_C.funcs
def pie_radius():
    obj_pie = Pie()
    # radius=["40%", "75%"]饼图的半径，数组的第一项是内半径，第二项是外半径
    obj_pie.add("",[list(z) for z in zip(Faker.choose(), Faker.values())],radius=["40%", "75%"],)
    obj_pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    obj_pie.set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-Radius",subtitle ="副标题"),
        # 让图例legend显示到左侧
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
    return obj_pie

# 多饼图
@obj_C.funcs
def pie_multiple_base():
    fn = """
        function(params) {
            if(params.name == '其他')
                return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
            return params.name + ' : ' + params.value + '%';
        }
        """
    obj_pie = Pie()
    obj_pie.add(
        "",
        [list(z) for z in zip(["剧情", "其他"], [25, 75])],
        center=["20%", "30%"],
        radius=[60, 80],
        label_opts=opts.LabelOpts(formatter=JsCode(fn), position="center")
    )
    obj_pie.add(
        "",
        [list(z) for z in zip(["奇幻", "其他"], [24, 76])],
        center=["55%", "30%"],
        radius=[60, 80],
        label_opts=opts.LabelOpts(formatter=JsCode(fn), position="center")
    )
    obj_pie.add(
        "",
        [list(z) for z in zip(["爱情", "其他"], [14, 86])],
        center=["20%", "70%"],
        radius=[60, 80],
        label_opts=opts.LabelOpts(formatter=JsCode(fn), position="center")
    )
    obj_pie.add(
        "",
        [list(z) for z in zip(["惊悚", "其他"], [11, 89])],
        center=["55%", "70%"],
        radius=[60, 80],
        label_opts=opts.LabelOpts(formatter=JsCode(fn), position="center")
    )
    obj_pie.set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-多饼图基本示例",subtitle ="副标题"),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
        )
    )
    return obj_pie


# 玫瑰图示例
@obj_C.funcs
def pie_rosetype():
    v = Faker.choose()
    obj_pie = Pie()
    obj_pie.add(
        "",
        [list(z) for z in zip(v, Faker.values())],
        radius=["30%", "75%"],
        center=["20%", "50%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=False),
    )
    obj_pie.add(
        "",
        [list(z) for z in zip(v, Faker.values())],
        radius=["30%", "75%"],
        center=["70%", "50%"],
        rosetype="area",
    )
    obj_pie.set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-玫瑰图示例",subtitle ="副标题"),
    )
    return obj_pie


# 图例过多，以滚动条形式展示
@obj_C.funcs
def pie_scroll_legend():
    obj_pie = Pie()
    obj_pie.add(
        "",
        [
            list(z) for z in zip(
                Faker.choose() + Faker.choose() + Faker.choose(),
                Faker.values() + Faker.values() + Faker.values(),
            )
        ],
        center=["40%", "50%"],
    )
    obj_pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    obj_pie.set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-Legend 滚动",subtitle ="副标题"),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_left="80%", orient="vertical"
        ),
    )
    return obj_pie



@obj_C.funcs
def pie_rich_label():
    obj_pie = Pie()
    obj_pie.add(
        "",
        [list(z) for z in zip(Faker.choose(), Faker.values())],
        radius=["40%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    obj_pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie-富文本示例",subtitle ="副标题"),)
    return obj_pie



if __name__ == '__main__':
    obj_page = Page()
    obj_page.add(*[fn() for fn, _ in obj_C.charts]).render('html/example_pie.html')