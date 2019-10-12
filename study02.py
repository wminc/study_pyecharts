# -*- coding:utf8 -*-
"""
Created on 2019/9/25 15:23

@author: minc

使用 options 配置项，在 pyecharts 中，一切皆 Options。
"""

from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

# from pyecharts.render import make_snapshot
#
# # 使用 snapshot-selenium 渲染图片
# from snapshot_selenium import snapshot
#
# bar = (
#     Bar()
#     .add_xaxis(["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"])
#     .add_yaxis("商家A",[5,20,36,10,75,90])
# )
# # 需要配置谷歌chromedriver到环境变量
# # make_snapshot(snapshot,bar.render(),'study02_bar.png')
#
# bar.render('study02.html')

init_options = opts.InitOpts(theme=ThemeType.LIGHT)
bar = Bar(init_opts=init_options)

bar.add_xaxis(["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"])
bar.add_yaxis("商家A",[5,20,36,10,75,90])
bar.add_yaxis("商家B",[15,6,45,20,35,66])

title_options = opts.TitleOpts(title="主主题",subtitle="副标题")
bar.set_global_opts(title_opts=title_options)

bar.render("html/study02.html")
