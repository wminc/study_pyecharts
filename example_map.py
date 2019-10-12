# -*- coding:utf8 -*-
"""
Created on 2019/10/12 12:56

@author: minc

地理图表
"""
from pyecharts import options as opts
from pyecharts.charts import Page, Map
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Collector, Faker

obj_C = Collector()

@obj_C.funcs
def map_base():
    obj_map = Map()
    obj_map.add("中国", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    obj_map.set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例",subtitle ="副标题"))
    return obj_map


@obj_C.funcs
def map_without_label():
    obj_map = Map()
    obj_map.add("中国", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    obj_map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    obj_map.set_global_opts(title_opts=opts.TitleOpts(title="Map-不显示Label",subtitle ="副标题"))
    return obj_map


@obj_C.funcs
def map_visualmap():
    obj_map = Map()
    obj_map.add("中国", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    obj_map.set_global_opts(
        title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）",subtitle ="副标题"),
        visualmap_opts=opts.VisualMapOpts(max_=500)
    )
    return obj_map


@obj_C.funcs
def map_visualmap_piecewise():
    obj_map = Map()
    obj_map.add("中国", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    obj_map.set_global_opts(
        title_opts=opts.TitleOpts(title="Map-VisualMap（分段型）",subtitle ="副标题"),
        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
    )
    return obj_map


@obj_C.funcs
def map_world():
    obj_map = Map()
    obj_map.add("世界", [list(z) for z in zip(Faker.country, Faker.values())], "world")
    obj_map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    obj_map.set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图",subtitle ="副标题"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
    return obj_map


# 因为指定省份地图
@obj_C.funcs
def map_province():
    obj_map = Map()
    # Faker.guangdong_city数据生成只有这一个省的城市列表
    # henan_city是通过修改Faker文件自定义的
    obj_map.add("河南", [list(z) for z in zip(Faker.henan_city, Faker.values())], "河南")
    obj_map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    obj_map.set_global_opts(
        title_opts=opts.TitleOpts(title="Map-河南",subtitle ="副标题"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    return obj_map





if __name__ == '__main__':
    obj_page = Page()
    obj_page.add(*[fn() for fn, _ in obj_C.charts]).render('html/example_map.html')