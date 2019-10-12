# -*- coding:utf8 -*-
"""
Created on 2019/9/26 17:18

@author: minc
"""

from flask import Flask, render_template
from flask.json import jsonify

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line

from random import randrange
import datetime,os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__)


# 柱状图
def bar_base():
    # 今天日期
    todaydate = datetime.date.today()

    # 时间周期-横坐标
    date_periods = []
    for i in range(6, 0, -1):
        date_i = todaydate - datetime.timedelta(days=i)
        date_periods.append(date_i)
    date_periods_day = [str(date.day) + '日' for date in date_periods]

    bar = Bar()
    bar.add_xaxis(date_periods_day)
    bar.add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
    bar.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
    title_options = opts.TitleOpts(title="群发数据统计", subtitle="最近7日数据")
    bar.set_global_opts(title_opts=title_options)
    return bar


# 使用index01.html自定义模板文件
@app.route("/show_demo01/")
def show_demo01():
    bar = bar_base()
    data = bar.dump_options_with_quotes()
    return render_template("index01.html", bar_data= data)


# 展示静态页面index02.html
@app.route("/index02/")
def index02():
    return render_template("index02.html")


# 在index02.html上ajax请求，定时全量更新图表
@app.route("/show_demo02/")
def show_demo02():
    bar = bar_base()
    data = bar.dump_options_with_quotes()
    return data


# 展示静态页面index03.html
@app.route("/index03/")
def index03():
    return render_template("index03.html")


# 曲线图
def line_base():
    line = Line()
    line.add_xaxis(["{}".format(i) for i in range(10)])
    line.add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
    line.set_global_opts(
            title_opts=opts.TitleOpts(title="动态数据"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    return line


# 在index03.html上ajax请求，定时增量更新图表
@app.route("/show_demo03/")
def show_demo03():
    line = line_base()
    data = line.dump_options_with_quotes()
    return data


idx = 9
# ajax请求，返回增量数据
@app.route("/demo03DynamicData")
def demo03DynamicData():
    global idx
    idx = idx + 1
    return jsonify({"name": idx, "value": randrange(50, 80)})


if __name__ == "__main__":
    app.run()
    # print(BASE_DIR)
    # print(randrange(50, 80))