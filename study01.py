# -*- coding:utf8 -*-
"""
Created on 2019/9/25 15:19

@author: minc

首先开始来绘制你的第一个图表
"""

from pyecharts.charts import Bar

# 方式一
bar = Bar()
bar.add_xaxis(["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"])
# bar.add_xaxis(["", "", "", "", "", ""])
bar.add_yaxis("商家A",[5,20,36,10,75,90])
# bar.add_yaxis("", [0, 0, 0, 0, 0, 0])

# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()


# 方式二，链式调用
# bar = (
#     Bar()
#     .add_xaxis(["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"])
#     .add_yaxis("商家A",[5,20,36,10,75,90])
# )
# bar.render()