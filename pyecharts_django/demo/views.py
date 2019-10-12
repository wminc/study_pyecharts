from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.template import loader

from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from pyecharts import options as opts
from pyecharts.charts import Bar,Line

import datetime,json
from random import randrange

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))


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


# 使用默认模板文件simple_chart.html
# 首先把位于python环境中pyecharts/render/templates中的macro和simple_chart.html拷贝至的templates文件夹下
# (这里只用到simple_chart.html但是里面导入了macro，所以也得拷贝进来)
# 在当前文件配置CurrentConfig.GLOBAL_ENV即配置simple_chart.html所在的目录
def test_demo(request):
    bar = bar_base()
    return HttpResponse(bar.render_embed())


# 使用index01.html自定义模板文件
def show_demo01(request):
    template = loader.get_template("index01.html")
    bar = bar_base()
    context = dict(
        data=bar.render_embed()
    )
    return HttpResponse(template.render(context))


# 展示静态页面index02.html
def index02(request):
    return render(request,'index02.html')


# 在index02.html上ajax请求，定时全量更新图表
def show_demo02(request):
    bar = bar_base()
    result = {
        # bar.dump_options_with_quotes()结果为JSON格式，首先先解析出来，然后再返回
        "data":json.loads(bar.dump_options_with_quotes())
    }
    return JsonResponse(result)


# 展示静态页面index03.html
def index03(request):
    return render(request,'index03.html')


# 曲线图
def line_base():
    line = Line()
    x_values = ["{}".format(i) for i in range(10)]
    line.add_xaxis(x_values)
    line.add_yaxis(
            series_name="动态曲线demo",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
    line.set_global_opts(
            title_opts=opts.TitleOpts(title="动态数据"),
            # 动态的关键，如果注释掉，就不会往后增加数据
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    return line


# 在index03.html上ajax请求，定时增量更新图表
def show_demo03(request):
    line = line_base()
    result = {
        # bar.dump_options_with_quotes()结果为JSON格式，首先先解析出来，然后再返回
        "data": json.loads(line.dump_options_with_quotes())
    }
    return JsonResponse(result)


cnt = 8
# ajax请求，返回增量数据
def demo03DynamicData(request):
    global cnt
    cnt = cnt + 1
    return JsonResponse({"name": cnt, "value": randrange(50, 80)})