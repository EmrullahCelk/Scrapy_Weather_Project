# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel,QPushButton,QMainWindow,QMessageBox

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 850)
        MainWindow.setMinimumSize(QtCore.QSize(900, 850))
        MainWindow.setMaximumSize(QtCore.QSize(900, 850))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 208, 0, 255), stop:1 rgba(68, 255, 16, 255));\n"
"\nborder-image: url(:/icons/wp_nl.png) 0 0 0 0 stretch stretch;\nborder-width: 0px;"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 470, 700))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_nl = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_nl.sizePolicy().hasHeightForWidth())
        self.btn_nl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_nl.setFont(font)
        self.btn_nl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_nl.setStyleSheet("\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.516304, stop:0 rgba(132, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: none")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/netherlands.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nl.setIcon(icon)
        self.btn_nl.setObjectName("btn_nl")
        self.horizontalLayout.addWidget(self.btn_nl)
        self.btn_usa = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_usa.sizePolicy().hasHeightForWidth())
        self.btn_usa.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_usa.setFont(font)
        self.btn_usa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_usa.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 209, 93, 255));\n"
"border: none")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/usa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_usa.setIcon(icon1)
        self.btn_usa.setObjectName("btn_usa")
        self.horizontalLayout.addWidget(self.btn_usa)
        self.btn_tr = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tr.sizePolicy().hasHeightForWidth())
        self.btn_tr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_tr.setFont(font)
        self.btn_tr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_tr.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 209, 93, 255));\n"
"border: none")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/turkey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tr.setIcon(icon2)
        self.btn_tr.setObjectName("btn_tr")
        self.horizontalLayout.addWidget(self.btn_tr)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\ncolor: rgb(255, 255, 255);\nfont: 8pt 'Arial Rounded MT Bold';")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 20)
        self.edt_search = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_search.setGeometry(QtCore.QRect(500, 60, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edt_search.setFont(font)
        self.edt_search.setStyleSheet("border-radius: 15px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.516304, stop:0 rgba(132, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid red\n"
"")
        self.edt_search.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_search.setObjectName("edt_search")
        self.btn_weather = QtWidgets.QPushButton(self.centralwidget)
        self.btn_weather.setGeometry(QtCore.QRect(600, 120, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_weather.setFont(font)
        self.btn_weather.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_weather.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 209, 93, 255));\n"
"border: none;\n"
"border-radius: 15px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/cloudy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_weather.setIcon(icon3)
        self.btn_weather.setIconSize(QtCore.QSize(20, 20))
        self.btn_weather.setObjectName("btn_weather")
        self.txt_cloud = QtWidgets.QLabel(self.centralwidget)
        self.txt_cloud.setGeometry(QtCore.QRect(460, 660, 420, 20))
        self.txt_cloud.setStyleSheet("color: rgb(255, 209, 93);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_cloud.setFont(font)
        self.txt_cloud.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_cloud.setObjectName("txt_cloud")
        self.txt_country_city = QtWidgets.QLabel(self.centralwidget)
        self.txt_country_city.setGeometry(QtCore.QRect(460, 740, 420, 20))
        self.txt_country_city.setStyleSheet("color: rgb(255, 209, 93);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_country_city.setFont(font)
        self.txt_country_city.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_country_city.setObjectName("txt_country_city")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(510, 210, 321, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("color: rgb(255, 209, 93);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 209, 93);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(255, 209, 93);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.txt_city = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txt_city.setStyleSheet("color: rgb(255, 209, 93);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_city.setFont(font)
        self.txt_city.setObjectName("txt_city")
        self.gridLayout.addWidget(self.txt_city, 0, 1, 1, 1)
        self.txt_province = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txt_province.setStyleSheet("color: rgb(255, 209, 93);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_province.setFont(font)
        self.txt_province.setObjectName("txt_province")
        self.gridLayout.addWidget(self.txt_province, 1, 1, 1, 1)
        self.txt_population = QtWidgets.QLabel(self.gridLayoutWidget)
        
        self.txt_population.setStyleSheet("color: rgb(255, 209, 93);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_population.setFont(font)
        self.txt_population.setObjectName("txt_population")
        self.gridLayout.addWidget(self.txt_population, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 800, 281, 31))
        font = QtGui.QFont()
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font.setFamily("Courier")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border:none;\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_cloud_icon = QtWidgets.QLabel(self.centralwidget)
        self.label_cloud_icon.setGeometry(QtCore.QRect(630, 440, 80, 80))
        self.label_cloud_icon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_cloud_icon.setText("")
        # self.label_cloud_icon.setPixmap(QtGui.QPixmap(":/icons/cloudy.png"))
        self.label_cloud_icon.setScaledContents(True)
        self.label_cloud_icon.setObjectName("label_cloud_icon")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 780, 111, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color: rgb(255, 209, 93);")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.txt_total = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.txt_total.setStyleSheet("color: rgb(255, 209, 93);")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txt_total.setFont(font)
        self.txt_total.setObjectName("txt_total")
        self.gridLayout_2.addWidget(self.txt_total, 0, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(519, 550, 361, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txt_celcius = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.txt_celcius.setStyleSheet("color: rgb(255, 209, 93);")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_celcius.sizePolicy().hasHeightForWidth())
        self.txt_celcius.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.txt_celcius.setFont(font)
        self.txt_celcius.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_celcius.setObjectName("txt_celcius")
        self.horizontalLayout_2.addWidget(self.txt_celcius)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setStyleSheet("color: rgb(255, 209, 93);")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.txt_fahr = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.txt_fahr.setStyleSheet("color: rgb(255, 209, 93);")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_fahr.sizePolicy().hasHeightForWidth())
        self.txt_fahr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.txt_fahr.setFont(font)
        self.txt_fahr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_fahr.setObjectName("txt_fahr")
        self.horizontalLayout_2.addWidget(self.txt_fahr)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setStyleSheet("color: rgb(255, 209, 93);")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        
        
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 0, 871, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(30, 30))
        self.label_8.setMaximumSize(QtCore.QSize(30, 30))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/idea.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(30, 30))
        self.label_11.setMaximumSize(QtCore.QSize(30, 30))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/icons/idea.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        
        
        self.label_net = QtWidgets.QLabel(self.centralwidget)
        self.label_net.setGeometry(QtCore.QRect(520, 170, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_net.setFont(font)
        self.label_net.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgba(255, 0, 0, 150);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_net.setAlignment(QtCore.Qt.AlignCenter)
        self.label_net.setObjectName("label_net")
        self.btn_info = QtWidgets.QPushButton(self.centralwidget)
        self.btn_info.setGeometry(QtCore.QRect(860, 800, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy)
        self.btn_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_info.setFont(font)
        self.btn_info.setStyleSheet("border:none;\n"
"border-radius: 15px;\n"
"background-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.btn_info.setObjectName("btn_info")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_nl.setText(_translate("MainWindow", "NL"))
        self.btn_usa.setText(_translate("MainWindow", "USA"))
        self.btn_tr.setText(_translate("MainWindow", "TR"))
        self.btn_weather.setText(_translate("MainWindow", "WEATHER"))
        self.txt_cloud.setText(_translate("MainWindow", "Broken Clouds"))
        self.txt_country_city.setText(_translate("MainWindow", "Delft,NL"))
        self.label.setText(_translate("MainWindow", "Region"))
        self.label_3.setText(_translate("MainWindow", "Population"))
        self.label_2.setText(_translate("MainWindow", "City"))
        self.txt_city.setText(_translate("MainWindow", "DELFT"))
        self.txt_province.setText(_translate("MainWindow", "Zuid-Holland"))
        self.txt_population.setText(_translate("MainWindow", "123456"))
        self.pushButton_2.setText(_translate("MainWindow", "QUIT"))
        self.label_4.setText(_translate("MainWindow", "TOTAL :"))
        self.txt_total.setText(_translate("MainWindow", "15"))
        self.txt_celcius.setText(_translate("MainWindow", "32.5"))
        self.label_6.setText(_translate("MainWindow", "°C"))
        self.txt_fahr.setText(_translate("MainWindow", "100.5"))
        self.label_7.setText(_translate("MainWindow", "°F"))
        self.label_5.setText(_translate("MainWindow", "ketadev"))
        self.label_9.setText(_translate("MainWindow", "Weather App"))
        self.label_10.setText(_translate("MainWindow", "ketadev"))
        self.label_net.setText(_translate("MainWindow", "No Internet Connection"))
        self.btn_info.setText(_translate("MainWindow", "i"))

import weather_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())