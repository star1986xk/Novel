import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pylab as mpl
from matplotlib import style

# 创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        try:
            # 创建一个创建Figure
            self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor='#505050')
            # 在父类中激活Figure窗口
            super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
            # style.use("dark_background")
            # 指定字体,显示中文
            mpl.rcParams['font.sans-serif'] = ['FangSong']
            mpl.rcParams['axes.unicode_minus'] = False

            # 创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
            self.axes = self.fig.add_subplot(111)

            self.axes.patch.set_facecolor("#505050")
            self.axes.patch.set_alpha(0.5)
            # 设置想x,y轴颜色
            ya = self.axes.yaxis
            xa = self.axes.xaxis  # you modify x ticks indepently
            ya.set_tick_params(labelcolor='white')  # label
            ya.set_tick_params(color='white')  # ticks
            xa.set_tick_params(labelcolor='white')  # label
            xa.set_tick_params(color='white')  # ticks

        except Exception as e:
            print(e)
