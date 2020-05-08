# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1098, 595)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ico/数据.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget{background-color: #212121;}\n"
"\n"
"QTableWidget{\n"
"color:#DCDCDC;\n"
"background:#444444;\n"
"border:1px solid #242424;\n"
"alternate-background-color:#525252;/*交错颜色*/\n"
"gridline-color:#242424;\n"
"}\n"
"\n"
"/*选中item*/\n"
"QTableWidget::item:selected{\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);\n"
"}\n"
"\n"
"/*\n"
"悬浮item*/\n"
"QTableWidget::item:hover{\n"
"background:#5B5B5B;\n"
"}\n"
"/*表头*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"background:#5E5E5E;\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#DCDCDC;\n"
"border:1px solid #242424;\n"
"border-left-width:0;\n"
"}\n"
"\n"
"/*表右侧的滑条*/\n"
"QScrollBar:vertical{\n"
"background:#484848;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"/*滑块*/\n"
"QScrollBar::handle:vertical{\n"
"background:#CCCCCC;\n"
"}\n"
"/*\n"
"滑块悬浮，按下*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:#A7A7A7;\n"
"}\n"
"/*\n"
"滑块已经划过的区域*/\n"
"QScrollBar::sub-page:vertical{\n"
"background:444444;\n"
"}\n"
"\n"
"/*\n"
"滑块还没有划过的区域*/\n"
"QScrollBar::add-page:vertical{\n"
"background:5B5B5B;\n"
"}\n"
"\n"
"/*页面下移的按钮*/\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"/*页面上移的按钮*/\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"QGroupBox{\n"
"background-color:rgb(80, 80, 80);color:white;border-radius: 5px;border: 1px solid rgb(255, 170, 0);margin-top: 5px;\n"
"}\n"
"QWidget QGroupBox QLineEdit{\n"
"background-color: rgb(0, 0, 0);\n"
"color:white;\n"
"border: 1px solid #333333;\n"
"border-radius: 5px;\n"
"}\n"
"QGroupBox::title{top:-5px;left:10px;}\n"
"QGroupBox QWidget{background-color: rgb(80, 80, 80);color:white;}\n"
"QTextBrowser{background-color: rgb(68, 68, 68);}\n"
"QLabel{color:white;}\n"
"QPushButton{border-radius: 10px;}\n"
"QPushButton:hover{\n"
"color:black;\n"
"background-color: rgb(150, 150, 150);\n"
"}")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setStyleSheet("#tabWidget>QWidget>QWidget{/*tab页*/\n"
"background-color: rgb(80, 80, 80);\n"
"}\n"
"#tabWidget::tab-bar{\n"
"alignment:left;/*tab位置*/\n"
"}\n"
"#tabWidget::pane { /*内容区域*/\n"
"background-color: rgb(80, 80, 80);/*背景色-空隙颜色*/\n"
"\n"
"} \n"
"#tabWidget QTabBar{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"#tabWidget QTabBar::tab{/*页签*/\n"
"min-height:20px;\n"
"width:120px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"margin-right:1px;\n"
"margin-bottom:1px;\n"
"background-color:rgb(80, 80, 80);\n"
"}\n"
"#tabWidget QTabBar::tab:hover{\n"
"color:black;\n"
"background-color: rgb(255, 170, 0);\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"#tabWidget QTabBar::tab:selected{\n"
"color:rgb(255, 170, 0);\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"#tabWidget QTabBar::tab:selected:hover{\n"
"color:black;\n"
"}\n"
"#tabWidget QTabBar::tear{/*选项过多时的。。。*/\n"
"imag:;\n"
"}\n"
"#tabWidget QTabBar::scroller{\n"
"width:60px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setMinimumSize(QtCore.QSize(200, 0))
        self.widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget.setStyleSheet("background-color: rgb(80, 80, 80)")
        self.widget.setObjectName("widget")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.groupBox_8 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_8.setMinimumSize(QtCore.QSize(200, 200))
        self.groupBox_8.setMaximumSize(QtCore.QSize(200, 200))
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.widget_7 = QtWidgets.QWidget(self.groupBox_8)
        self.widget_7.setMinimumSize(QtCore.QSize(150, 40))
        self.widget_7.setMaximumSize(QtCore.QSize(150, 40))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_5 = QtWidgets.QLabel(self.widget_7)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_22.addWidget(self.label_5)
        self.lineEdit_start_id = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_start_id.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lineEdit_start_id.setObjectName("lineEdit_start_id")
        self.horizontalLayout_22.addWidget(self.lineEdit_start_id)
        self.verticalLayout_18.addWidget(self.widget_7, 0, QtCore.Qt.AlignHCenter)
        self.widget_8 = QtWidgets.QWidget(self.groupBox_8)
        self.widget_8.setMinimumSize(QtCore.QSize(150, 40))
        self.widget_8.setMaximumSize(QtCore.QSize(150, 40))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_6 = QtWidgets.QLabel(self.widget_8)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_23.addWidget(self.label_6)
        self.lineEdit_end_id = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_end_id.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lineEdit_end_id.setObjectName("lineEdit_end_id")
        self.horizontalLayout_23.addWidget(self.lineEdit_end_id)
        self.verticalLayout_18.addWidget(self.widget_8, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_spider = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_spider.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_spider.setMaximumSize(QtCore.QSize(80, 30))
        self.pushButton_spider.setStyleSheet("QPushButton:hover{\n"
"color:black;\n"
"background-color: rgb(150, 150, 150);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/蜘蛛网万圣节.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_spider.setIcon(icon1)
        self.pushButton_spider.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_spider.setObjectName("pushButton_spider")
        self.verticalLayout_18.addWidget(self.pushButton_spider, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_17.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_9.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.textBrowser_spider = QtWidgets.QTextBrowser(self.groupBox_9)
        self.textBrowser_spider.setStyleSheet("")
        self.textBrowser_spider.setObjectName("textBrowser_spider")
        self.horizontalLayout_24.addWidget(self.textBrowser_spider)
        self.verticalLayout_17.addWidget(self.groupBox_9)
        self.horizontalLayout_3.addWidget(self.widget)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.groupBox_7)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_save = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_save.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_save.setMaximumSize(QtCore.QSize(80, 25))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon2)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_5.addWidget(self.pushButton_save)
        self.lineEdit_save = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_save.setReadOnly(True)
        self.lineEdit_save.setObjectName("lineEdit_save")
        self.horizontalLayout_5.addWidget(self.lineEdit_save)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_3.addWidget(self.groupBox_7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_open = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_open.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_open.setMaximumSize(QtCore.QSize(80, 25))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/打开.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_open.setIcon(icon3)
        self.pushButton_open.setObjectName("pushButton_open")
        self.horizontalLayout_6.addWidget(self.pushButton_open)
        self.lineEdit_open = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_open.setReadOnly(True)
        self.lineEdit_open.setObjectName("lineEdit_open")
        self.horizontalLayout_6.addWidget(self.lineEdit_open)
        self.pushButton_train = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_train.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton_train.setMaximumSize(QtCore.QSize(60, 25))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/训练.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_train.setIcon(icon4)
        self.pushButton_train.setObjectName("pushButton_train")
        self.horizontalLayout_6.addWidget(self.pushButton_train)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.widget_3 = QtWidgets.QWidget(self.tab_2)
        self.widget_3.setStyleSheet("background-color: rgb(80, 80, 80);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_11 = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox_11.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_11.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.textBrowser_model = QtWidgets.QTextBrowser(self.groupBox_11)
        self.textBrowser_model.setObjectName("textBrowser_model")
        self.horizontalLayout_10.addWidget(self.textBrowser_model)
        self.horizontalLayout_7.addWidget(self.groupBox_11)
        self.groupBox_12 = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_4 = QtWidgets.QWidget(self.groupBox_12)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_11.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.groupBox_12)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11.addWidget(self.widget_5)
        self.horizontalLayout_7.addWidget(self.groupBox_12)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setContentsMargins(-1, 30, -1, -1)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.pushButton_analysis = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_analysis.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_analysis.setMaximumSize(QtCore.QSize(80, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/分析.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_analysis.setIcon(icon5)
        self.pushButton_analysis.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_analysis.setObjectName("pushButton_analysis")
        self.verticalLayout.addWidget(self.pushButton_analysis, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textBrowser_analysis = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_analysis.setObjectName("textBrowser_analysis")
        self.horizontalLayout_8.addWidget(self.textBrowser_analysis)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_ciyun = QtWidgets.QVBoxLayout()
        self.verticalLayout_ciyun.setSpacing(0)
        self.verticalLayout_ciyun.setObjectName("verticalLayout_ciyun")
        self.horizontalLayout_9.addLayout(self.verticalLayout_ciyun)
        self.horizontalLayout_2.addWidget(self.groupBox_10)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "网络小说分析器"))
        self.groupBox_8.setTitle(_translate("Form", "运行程序"))
        self.label_5.setText(_translate("Form", "开始ID："))
        self.label_6.setText(_translate("Form", "结束ID："))
        self.pushButton_spider.setText(_translate("Form", "抓取"))
        self.groupBox_9.setTitle(_translate("Form", "运行日志"))
        self.groupBox_7.setTitle(_translate("Form", "抓取结果"))
        self.pushButton_save.setText(_translate("Form", "保存文件"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "标题"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "作者"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "类型"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "更新时间"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "数据抓取"))
        self.groupBox.setTitle(_translate("Form", "选取样本"))
        self.pushButton_open.setText(_translate("Form", "打开文件"))
        self.pushButton_train.setText(_translate("Form", "训练"))
        self.groupBox_11.setTitle(_translate("Form", "训练日志"))
        self.groupBox_12.setTitle(_translate("Form", "可视化模型"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "模型训练"))
        self.groupBox_5.setTitle(_translate("Form", "数据选取"))
        self.label_3.setText(_translate("Form", "输入小说名称："))
        self.pushButton_analysis.setText(_translate("Form", "分析"))
        self.groupBox_6.setTitle(_translate("Form", "分析结果"))
        self.groupBox_10.setTitle(_translate("Form", "生成词云"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "数据分析"))
import img_rc
