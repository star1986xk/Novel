import sys
from UI.Ui_mainWin import Ui_Form
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QApplication, QHeaderView, QFileDialog
from spider import spider
from ldamodel import ldamodel
from ciyun import ciyun
from htmlWin import htmlWin
from MyFigure import MyFigure

class DataAnalysis(Ui_Form, QWidget):
    def __init__(self, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        #实例界面
        super(DataAnalysis, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        #表格列均分
        headerView = self.tableWidget.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)

        self.pushButton_save.clicked.connect(self.save_btn)
        self.pushButton_spider.clicked.connect(self.spider_btn)
        self.pushButton_open.clicked.connect(self.open_btn)
        self.pushButton_train.clicked.connect(self.train_btn)
        self.pushButton_analysis.clicked.connect(self.analysis_btn)

    def save_btn(self):
        '''
        保存按钮
        '''
        filename, _ = QFileDialog.getSaveFileName(self, '保存文件', './', '文本文件 (*.txt')
        if filename:
            #保存路径显示到界面
            self.lineEdit_save.setText(filename)

    def spider_btn(self):
        '''
        爬虫开启按钮
        '''
        try:
            #清空日志及表格
            self.textBrowser_spider.clear()
            self.tableWidget.setRowCount(0)
            #得到开始结束id 保存路径
            start_id = self.lineEdit_start_id.text()
            end_id = self.lineEdit_end_id.text()
            filename = self.lineEdit_save.text()
            #实例爬虫对象 开启爬虫
            self.spiderObj = spider(start_id, end_id, filename)
            self.spiderObj.sig_one_end.connect(self.spider_end)
            self.spiderObj.sig_item_end.connect(self.spider_item)
            self.spiderObj.sig_end.connect(self.spider_end)
            self.spiderObj.start()
        except Exception as e:
            print(e)

    def open_btn(self):
        '''
        打开文件按钮
        '''
        filename, _ = QFileDialog.getOpenFileName(self, '打开文件', './', '文本文件 (*.txt)')
        if filename:
            self.lineEdit_open.setText(filename)

    def train_btn(self):
        '''
        训练按钮
        '''
        try:
            #清空日志 界面
            self.textBrowser_model.clear()
            for i in range(self.verticalLayout_6.count()):
                self.verticalLayout_6.itemAt(i).widget().deleteLater()
            for i in range(self.verticalLayout_2.count()):
                self.verticalLayout_2.itemAt(i).widget().deleteLater()
            filename = self.lineEdit_open.text()
            #实例训练对象开启训练
            self.ldamodelObj = ldamodel(filename)
            self.ldamodelObj.sig_one_end.connect(self.ldamodel_one_end)
            self.ldamodelObj.sig_img_end.connect(self.ldamodel_img)
            self.ldamodelObj.sig_img2_end.connect(self.ldamodel_img2)
            self.ldamodelObj.sig_end.connect(self.ldamodel_end)
            self.ldamodelObj.start()
        except Exception as e:
            print(e)

    def ldamodel_one_end(self, text):
        '''
        回传一个训练信号
        '''
        self.textBrowser_model.append(text)

    def ldamodel_img(self, x_list,y_list):
        '''
        回传一个训练模型图片
        '''
        self.MyFig = MyFigure()
        self.MyFig.axes.plot(x_list, y_list)
        self.MyFig.axes.legend(('perplexity'), loc='best')
        self.MyFig.axes.set_title('不同主题数模型困惑度',color='w')
        self.MyFig.axes.set_xlabel('主题数量',color='w')
        self.MyFig.axes.set_ylabel('模型困惑度',color='w')
        self.MyFig.axes.set_xticklabels(x_list)
        self.MyFig.fig.savefig("不同主题数模型困惑度.png")
        self.verticalLayout_6.addWidget(self.MyFig)

    def ldamodel_img2(self, x_list,y_list):
        '''
        回传一个训练模型图片
        '''
        self.MyFig = MyFigure()
        self.MyFig.axes.plot(x_list, y_list)
        self.MyFig.axes.legend(('coherence'), loc='best')
        self.MyFig.axes.set_title('相似度',color='w')
        self.MyFig.axes.set_xticklabels(x_list)
        self.MyFig.fig.savefig("相似度.png")
        self.verticalLayout_2.addWidget(self.MyFig)


    def ldamodel_end(self):
        '''
        训练结束打开web 展示可视化模型
        '''
        self.html = htmlWin()
        self.html.show()

    def spider_item(self, item):
        '''
        写入爬虫表格
        '''
        try:
            n = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(n + 1)
            self.tableWidget.setItem(n, 0, QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(n, 1, QTableWidgetItem(str(item[3])))
            self.tableWidget.setItem(n, 2, QTableWidgetItem(str(item[2])))
            self.tableWidget.setItem(n, 3, QTableWidgetItem(str(item[6])))
        except Exception as e:
            print(e)

    def spider_end(self, text):
        '''
        写入爬虫日志
        '''
        self.textBrowser_spider.append(text)

    def analysis_btn(self):
        '''
        分析按钮
        '''
        try:
            #清空界面
            self.textBrowser_analysis.clear()
            for i in range(self.verticalLayout_ciyun.count()):
                self.verticalLayout_ciyun.itemAt(i).widget().deleteLater()
            name = self.lineEdit_name.text()
            #实例词云对象 开启数据分析及生产词云
            self.ciyunObj = ciyun(name)
            self.ciyunObj.sig_img_end.connect(self.ciyun_img)
            self.ciyunObj.sig_one_end.connect(self.ciyun_end)
            self.ciyunObj.start()
        except Exception as e:
            print(e)

    def ciyun_img(self, img_list):
        '''
        回传一个词语图片
        '''
        self.verticalLayout_ciyun.addWidget(img_list[0])

    def ciyun_end(self, text):
        '''
        写入词云日志
        '''
        self.textBrowser_analysis.append(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DataAnalysis()
    win.show()
    sys.exit(app.exec_())
