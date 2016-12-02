from PyQt4 import QtCore, QtGui
import sys
import OddsApp
import Prefer
import Avoid
import Routine
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import os
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(491, 420)
        MainWindow.setMinimumSize(QtCore.QSize(491, 420))
        MainWindow.setMaximumSize(QtCore.QSize(491, 420))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imageformats/smines_favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("#pushButton, #pushButton_3, #pushButton_4, #pushButton_5, #pushButton_6, #pushButton_7{\n"
"    background-color:purple;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-size:13px;\n"
"    height: 50px;\n"
"    width: 150px;\n"
"}\n"
"\n"
"QTabWidget::pane{\n"
"    border: 1px solid rgb(160, 194, 204);\n"
"}\n"
"\n"
"\n"
"QTabBar::tab4 {\n"
"    background: gray;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    min-width:100px;\n"
"    font-weight:bold;\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"\n"
"QWidget{\n"
"    background-color: rgb(17, 17, 17); \n"
"}\n"
"\n"
"QTextBrowser{\n"
"    color: white;\n"
"    border: 1px solid rgb(160, 194, 204);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: white;\n"
"    border: 1px solid rgb(160, 194, 204);\n"
"}\n"
"\n"
"#phantomjs{\n"
"    background-color:  rgb(27, 27, 27);\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"QGroupBox{\n"
"    border:2px solid rgb(160, 194, 204); \n"
"    color: white;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: white;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox{\n"
"    color: white;\n"
"}\n"
"\n"
"#Start {\n"
"    color: white;\n"
"    background-color: rgb(144, 199, 57); \n"
"    font-size:16px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"#Stop {\n"
"    color: White;\n"
"    background-color: rgb(238, 17, 17); \n"
"    font-size:16px;\n"
"    font-weight:bold;\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Start = QtGui.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(160, 380, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.Start.setFont(font)
        self.Start.setStyleSheet(_fromUtf8(""))
        self.Start.setObjectName(_fromUtf8("Start"))
        self.Stop = QtGui.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(270, 380, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.Stop.setFont(font)
        self.Stop.setObjectName(_fromUtf8("Stop"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 350, 508, 23))
        self.progressBar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFormat(_fromUtf8(""))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 5, 180, 26))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/smines.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 408, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(465, 410, 31, 10))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gameHappening = QtGui.QTextBrowser(self.centralwidget)
        self.gameHappening.setGeometry(QtCore.QRect(10, 190, 151, 151))
        self.gameHappening.setObjectName(_fromUtf8("gameHappening"))
        self.tile1 = QtGui.QLabel(self.centralwidget)
        self.tile1.setGeometry(QtCore.QRect(170, 190, 25, 25))
        self.tile1.setText(_fromUtf8(""))
        self.tile1.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile1.setObjectName(_fromUtf8("tile1"))
        self.tile2 = QtGui.QLabel(self.centralwidget)
        self.tile2.setGeometry(QtCore.QRect(201, 190, 25, 25))
        self.tile2.setText(_fromUtf8(""))
        self.tile2.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile2.setObjectName(_fromUtf8("tile2"))
        self.tile3 = QtGui.QLabel(self.centralwidget)
        self.tile3.setGeometry(QtCore.QRect(232, 190, 25, 25))
        self.tile3.setText(_fromUtf8(""))
        self.tile3.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile3.setObjectName(_fromUtf8("tile3"))
        self.tile4 = QtGui.QLabel(self.centralwidget)
        self.tile4.setGeometry(QtCore.QRect(263, 190, 25, 25))
        self.tile4.setText(_fromUtf8(""))
        self.tile4.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile4.setObjectName(_fromUtf8("tile4"))
        self.tile5 = QtGui.QLabel(self.centralwidget)
        self.tile5.setGeometry(QtCore.QRect(295, 190, 25, 25))
        self.tile5.setText(_fromUtf8(""))
        self.tile5.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile5.setObjectName(_fromUtf8("tile5"))
        self.tile6 = QtGui.QLabel(self.centralwidget)
        self.tile6.setGeometry(QtCore.QRect(170, 221, 25, 25))
        self.tile6.setText(_fromUtf8(""))
        self.tile6.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile6.setObjectName(_fromUtf8("tile6"))
        self.tile7 = QtGui.QLabel(self.centralwidget)
        self.tile7.setGeometry(QtCore.QRect(201, 221, 25, 25))
        self.tile7.setText(_fromUtf8(""))
        self.tile7.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile7.setObjectName(_fromUtf8("tile7"))
        self.tile10 = QtGui.QLabel(self.centralwidget)
        self.tile10.setGeometry(QtCore.QRect(295, 221, 25, 25))
        self.tile10.setText(_fromUtf8(""))
        self.tile10.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile10.setObjectName(_fromUtf8("tile10"))
        self.tile9 = QtGui.QLabel(self.centralwidget)
        self.tile9.setGeometry(QtCore.QRect(263, 221, 25, 25))
        self.tile9.setText(_fromUtf8(""))
        self.tile9.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile9.setObjectName(_fromUtf8("tile9"))
        self.tile8 = QtGui.QLabel(self.centralwidget)
        self.tile8.setGeometry(QtCore.QRect(232, 221, 25, 25))
        self.tile8.setText(_fromUtf8(""))
        self.tile8.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile8.setObjectName(_fromUtf8("tile8"))
        self.tile17 = QtGui.QLabel(self.centralwidget)
        self.tile17.setGeometry(QtCore.QRect(201, 285, 25, 25))
        self.tile17.setText(_fromUtf8(""))
        self.tile17.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile17.setObjectName(_fromUtf8("tile17"))
        self.tile20 = QtGui.QLabel(self.centralwidget)
        self.tile20.setGeometry(QtCore.QRect(295, 285, 25, 25))
        self.tile20.setText(_fromUtf8(""))
        self.tile20.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile20.setObjectName(_fromUtf8("tile20"))
        self.tile11 = QtGui.QLabel(self.centralwidget)
        self.tile11.setGeometry(QtCore.QRect(170, 253, 25, 25))
        self.tile11.setText(_fromUtf8(""))
        self.tile11.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile11.setObjectName(_fromUtf8("tile11"))
        self.tile12 = QtGui.QLabel(self.centralwidget)
        self.tile12.setGeometry(QtCore.QRect(201, 253, 25, 25))
        self.tile12.setText(_fromUtf8(""))
        self.tile12.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile12.setObjectName(_fromUtf8("tile12"))
        self.tile15 = QtGui.QLabel(self.centralwidget)
        self.tile15.setGeometry(QtCore.QRect(295, 253, 25, 25))
        self.tile15.setText(_fromUtf8(""))
        self.tile15.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile15.setObjectName(_fromUtf8("tile15"))
        self.tile19 = QtGui.QLabel(self.centralwidget)
        self.tile19.setGeometry(QtCore.QRect(263, 285, 25, 25))
        self.tile19.setText(_fromUtf8(""))
        self.tile19.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile19.setObjectName(_fromUtf8("tile19"))
        self.tile16 = QtGui.QLabel(self.centralwidget)
        self.tile16.setGeometry(QtCore.QRect(170, 285, 25, 25))
        self.tile16.setText(_fromUtf8(""))
        self.tile16.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile16.setObjectName(_fromUtf8("tile16"))
        self.tile14 = QtGui.QLabel(self.centralwidget)
        self.tile14.setGeometry(QtCore.QRect(263, 253, 25, 25))
        self.tile14.setText(_fromUtf8(""))
        self.tile14.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile14.setObjectName(_fromUtf8("tile14"))
        self.tile18 = QtGui.QLabel(self.centralwidget)
        self.tile18.setGeometry(QtCore.QRect(232, 285, 25, 25))
        self.tile18.setText(_fromUtf8(""))
        self.tile18.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile18.setObjectName(_fromUtf8("tile18"))
        self.tile13 = QtGui.QLabel(self.centralwidget)
        self.tile13.setGeometry(QtCore.QRect(232, 253, 25, 25))
        self.tile13.setText(_fromUtf8(""))
        self.tile13.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile13.setObjectName(_fromUtf8("tile13"))
        self.tile21 = QtGui.QLabel(self.centralwidget)
        self.tile21.setGeometry(QtCore.QRect(170, 316, 25, 25))
        self.tile21.setText(_fromUtf8(""))
        self.tile21.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile21.setObjectName(_fromUtf8("tile21"))
        self.tile22 = QtGui.QLabel(self.centralwidget)
        self.tile22.setGeometry(QtCore.QRect(201, 316, 25, 25))
        self.tile22.setText(_fromUtf8(""))
        self.tile22.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile22.setObjectName(_fromUtf8("tile22"))
        self.tile25 = QtGui.QLabel(self.centralwidget)
        self.tile25.setGeometry(QtCore.QRect(295, 316, 25, 25))
        self.tile25.setText(_fromUtf8(""))
        self.tile25.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile25.setObjectName(_fromUtf8("tile25"))
        self.tile24 = QtGui.QLabel(self.centralwidget)
        self.tile24.setGeometry(QtCore.QRect(263, 316, 25, 25))
        self.tile24.setText(_fromUtf8(""))
        self.tile24.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile24.setObjectName(_fromUtf8("tile24"))
        self.tile23 = QtGui.QLabel(self.centralwidget)
        self.tile23.setGeometry(QtCore.QRect(232, 316, 25, 25))
        self.tile23.setText(_fromUtf8(""))
        self.tile23.setPixmap(QtGui.QPixmap(_fromUtf8("imageformats/tileNew.png")))
        self.tile23.setObjectName(_fromUtf8("tile23"))
        self.phantomjs = QtGui.QPushButton(self.centralwidget)
        self.phantomjs.setGeometry(QtCore.QRect(235, 385, 31, 23))
        self.phantomjs.setObjectName(_fromUtf8("phantomjs"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 471, 141))
        self.tabWidget.setStyleSheet(_fromUtf8("QTabBar::tab {\n"
"    background: rgb(54,54,54);\n"
"    color: white;\n"
"    padding: 5px;\n"
"    min-width:85px;\n"
"    font-weight:bold;\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: purple;\n"
"}\n"
""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gameAmount = QtGui.QLineEdit(self.tab)
        self.gameAmount.setGeometry(QtCore.QRect(370, 80, 51, 20))
        self.gameAmount.setInputMask(_fromUtf8(""))
        self.gameAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.gameAmount.setObjectName(_fromUtf8("gameAmount"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(360, 60, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.userid = QtGui.QLineEdit(self.tab)
        self.userid.setGeometry(QtCore.QRect(145, 30, 181, 20))
        self.userid.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userid.setText(_fromUtf8(""))
        self.userid.setAlignment(QtCore.Qt.AlignCenter)
        self.userid.setObjectName(_fromUtf8("userid"))
        self.increase = QtGui.QLineEdit(self.tab)
        self.increase.setGeometry(QtCore.QRect(44, 80, 51, 20))
        self.increase.setInputMask(_fromUtf8(""))
        self.increase.setAlignment(QtCore.Qt.AlignCenter)
        self.increase.setObjectName(_fromUtf8("increase"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(185, 5, 111, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.initBet = QtGui.QLineEdit(self.tab)
        self.initBet.setGeometry(QtCore.QRect(40, 30, 61, 20))
        self.initBet.setAlignment(QtCore.Qt.AlignCenter)
        self.initBet.setObjectName(_fromUtf8("initBet"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(160, 65, 151, 41))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.mine24 = QtGui.QRadioButton(self.groupBox)
        self.mine24.setGeometry(QtCore.QRect(110, 15, 32, 17))
        self.mine24.setObjectName(_fromUtf8("mine24"))
        self.mine5 = QtGui.QRadioButton(self.groupBox)
        self.mine5.setEnabled(True)
        self.mine5.setGeometry(QtCore.QRect(78, 15, 30, 17))
        self.mine5.setChecked(True)
        self.mine5.setObjectName(_fromUtf8("mine5"))
        self.mine3 = QtGui.QRadioButton(self.groupBox)
        self.mine3.setGeometry(QtCore.QRect(45, 15, 30, 17))
        self.mine3.setObjectName(_fromUtf8("mine3"))
        self.mine1 = QtGui.QRadioButton(self.groupBox)
        self.mine1.setGeometry(QtCore.QRect(10, 15, 30, 17))
        self.mine1.setObjectName(_fromUtf8("mine1"))
        self.clicksPerRound = QtGui.QLineEdit(self.tab)
        self.clicksPerRound.setGeometry(QtCore.QRect(370, 30, 51, 20))
        self.clicksPerRound.setInputMask(_fromUtf8(""))
        self.clicksPerRound.setAlignment(QtCore.Qt.AlignCenter)
        self.clicksPerRound.setObjectName(_fromUtf8("clicksPerRound"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(355, 10, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.checkBox = QtGui.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(30, 10, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 35, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(105, 8, 41, 20))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(105, 33, 41, 20))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(105, 58, 61, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.checkBox_3 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 60, 70, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(105, 83, 61, 20))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.checkBox_4 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 85, 70, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(150, 10, 46, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(150, 35, 46, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(170, 60, 46, 13))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(170, 85, 46, 13))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(315, 8, 41, 20))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(360, 10, 71, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.checkBox_5 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_5.setGeometry(QtCore.QRect(240, 10, 70, 17))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_6.setGeometry(QtCore.QRect(240, 35, 70, 17))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.lineEdit_6 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(315, 33, 41, 20))
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(360, 35, 81, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_16 = QtGui.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(330, 85, 101, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.checkBox_8 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_8.setGeometry(QtCore.QRect(240, 85, 41, 17))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.lineEdit_8 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(285, 83, 41, 20))
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.checkBox_21 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_21.setGeometry(QtCore.QRect(240, 60, 91, 17))
        self.checkBox_21.setObjectName(_fromUtf8("checkBox_21"))
        self.lineEdit_9 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(330, 60, 41, 20))
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(397, 60, 41, 20))
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(379, 62, 16, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.pushButton = QtGui.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(305, 10, 71, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_30 = QtGui.QLabel(self.tab_3)
        self.label_30.setGeometry(QtCore.QRect(210, 10, 81, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.lineEdit_17 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_17.setGeometry(QtCore.QRect(160, 8, 41, 20))
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.checkBox_17 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_17.setGeometry(QtCore.QRect(30, 10, 127, 17))
        self.checkBox_17.setObjectName(_fromUtf8("checkBox_17"))
        self.label_31 = QtGui.QLabel(self.tab_3)
        self.label_31.setGeometry(QtCore.QRect(210, 35, 81, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.lineEdit_18 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_18.setGeometry(QtCore.QRect(160, 33, 41, 20))
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.checkBox_18 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_18.setGeometry(QtCore.QRect(30, 35, 121, 17))
        self.checkBox_18.setObjectName(_fromUtf8("checkBox_18"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(305, 45, 71, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_15 = QtGui.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(170, 60, 71, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.lineEdit_7 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(120, 58, 41, 20))
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.checkBox_7 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 60, 88, 17))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.label_32 = QtGui.QLabel(self.tab_3)
        self.label_32.setGeometry(QtCore.QRect(135, 85, 121, 16))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.checkBox_19 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_19.setGeometry(QtCore.QRect(30, 85, 51, 17))
        self.checkBox_19.setObjectName(_fromUtf8("checkBox_19"))
        self.lineEdit_19 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_19.setGeometry(QtCore.QRect(85, 83, 41, 20))
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.lineEdit_20 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_20.setEnabled(False)
        self.lineEdit_20.setGeometry(QtCore.QRect(360, 83, 41, 20))
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.label_33 = QtGui.QLabel(self.tab_3)
        self.label_33.setGeometry(QtCore.QRect(410, 85, 31, 20))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.checkBox_20 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_20.setEnabled(False)
        self.checkBox_20.setGeometry(QtCore.QRect(270, 85, 85, 17))
        self.checkBox_20.setObjectName(_fromUtf8("checkBox_20"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(385, 10, 71, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(385, 45, 71, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 70, 121, 31))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.lineEdit_21 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_21.setGeometry(QtCore.QRect(150, 13, 301, 20))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.lineEdit_22 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_22.setGeometry(QtCore.QRect(250, 75, 201, 20))
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.label_34 = QtGui.QLabel(self.tab_4)
        self.label_34.setGeometry(QtCore.QRect(210, 75, 38, 20))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.lineEdit_23 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_23.setGeometry(QtCore.QRect(152, 75, 51, 20))
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.lineEdit_24 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_24.setGeometry(QtCore.QRect(150, 38, 301, 20))
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(330, 190, 151, 151))
        self.tabWidget_2.setStyleSheet(_fromUtf8("QTabBar::tab {\n"
"    background: rgb(54,54,54);\n"
"    color: white;\n"
"    padding: 5px;\n"
"    min-width:62px;\n"
"    font-weight:bold;\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: purple;\n"
"}\n"
""))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gameStats = QtGui.QTextBrowser(self.tab_5)
        self.gameStats.setGeometry(QtCore.QRect(-1, -1, 151, 131))
        self.gameStats.setObjectName(_fromUtf8("gameStats"))
        self.tabWidget_2.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gameStats_2 = QtGui.QTextBrowser(self.tab_6)
        self.gameStats_2.setGeometry(QtCore.QRect(-1, -1, 151, 131))
        self.gameStats_2.setObjectName(_fromUtf8("gameStats_2"))
        self.tabWidget_2.addTab(self.tab_6, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_3.clicked.connect(self.openRoutine)
        self.pushButton_4.clicked.connect(self.openAvoid)
        self.pushButton_5.clicked.connect(self.openPrefer)
        self.pushButton_6.clicked.connect(self.createAccount)
        self.pushButton_7.clicked.connect(self.withdraw)
        self.pushButton.clicked.connect(self.openOdds)
        #QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"), self.openOdds)
        self.Start.clicked.connect(self.startBot)
        self.Stop.clicked.connect(self.stopBot)
        self.phantomjs.clicked.connect(self.showDialog)

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        global fname
        fname = "unset"

    def openOdds(self):
        global second
        second = OddsApp.OddsForm()
        second.show()

    def openPrefer(self):
        global third
        third = Prefer.PreferForm()
        third.show()

    def openAvoid(self):
        global third
        third = Avoid.AvoidForm()
        third.show()

    def openRoutine(self):
        global third
        third = Routine.RoutineForm()
        third.show()

    def withdraw(self):

        #Get withdrawAmount
        withdrawAmount = self.lineEdit_23.text()
        try:
            withdrawAmount = int(withdrawAmount)
        except:
            self.gameHappening.setText("Invalid Withdraw Amount.")
            raise

        if int(withdrawAmount) < 28:
            self.gameHappening.setText("Min. Withdraw Amount = 28 Bits.")

        else:
            #Get targetAddr
            targetAddr = self.lineEdit_22.text()

            #Get User PhantomJS Path
            chrdr_loc = fname

            #Get User Account Hash
            account_hash = self.userid.text()
            link = "http://www.satoshimines.com/play/"+account_hash+"/"

            #Start PhantomJS
            if chrdr_loc == "unset":
                try:
                    self.driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
                except:
                    self.gameHappening.setText("Please Set A Path To PhantomJS.exe Before You Start.")
                    raise
            else:
                try:
                    self.driver = webdriver.PhantomJS(executable_path=chrdr_loc, service_log_path=os.path.devnull)
                except:
                    self.gameHappening.setText("Your Path To PhantomJS.exe Is Invalid.")
                    raise

            #Connect to Useraccount
            self.driver.get(link)

            #Wait for Window to Open
            time.sleep(1)
            QtCore.QCoreApplication.processEvents()

            #Click Deposit/Withdraw
            self.driver.find_element_by_xpath("//div[2]/div/button").click()

            #Wait for Window to Open
            time.sleep(0.5)
            QtCore.QCoreApplication.processEvents()

            #Click Withdraw Tab
            self.driver.find_element_by_xpath("//div[7]/div/ul/li[2]").click()

            #Wait for Window to Open
            time.sleep(0.5)
            QtCore.QCoreApplication.processEvents()

            #Enter Amount
            elem = self.driver.find_element_by_class_name("amount")
            elem.clear()
            elem.send_keys(int(withdrawAmount))

            #Enter Target Addr
            elem = self.driver.find_element_by_class_name("payto_address")
            elem.send_keys(targetAddr)

            #self.driver.get_screenshot_as_file("test.png")

            #Click Withdraw Button
            self.driver.find_element_by_xpath("//div[3]/button[2]").click()

            withdrawDone = False
            self.gameHappening.append("Withdrawing - This might take a few seconds.")

            #Wait for Window to Open
            while withdrawDone == False:
                time.sleep(1)
                QtCore.QCoreApplication.processEvents()
                try:
                    elem = self.driver.find_element_by_xpath("//div[4]/div[2]/button").click()

                    #Notice Player
                    self.gameHappening.append(str(withdrawAmount) + " Bits Withdrawn to " + str(targetAddr))

                    withdrawDone = True
                except:
                    pass

            QtCore.QCoreApplication.processEvents()

            #Close & Quit Webdriver
            self.driver.close()
            self.driver.quit()

    def createAccount(self):

        #Get User PhantomJS Path
        chrdr_loc = fname
        link = "https://satoshimines.com/newplayer.php"

        #Start PhantomJS
        if chrdr_loc == "unset":
            try:
                self.driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
            except:
                self.gameHappening.setText("Please Set A Path To PhantomJS.exe Before You Start.")
                raise
        else:
            try:
                self.driver = webdriver.PhantomJS(executable_path=chrdr_loc, service_log_path=os.path.devnull)
            except:
                self.gameHappening.setText("Your Path To PhantomJS.exe Is Invalid.")
                raise

        #Connect to Useraccount
        self.driver.get(link)

        QtCore.QCoreApplication.processEvents()

        #Visit newaccout.php
        url = self.driver.current_url
        #Click Deposit/Withdraw
        self.driver.find_element_by_class_name("dw").click()

        #Wait for Window to Open
        time.sleep(1)
        QtCore.QCoreApplication.processEvents()

        #Fetch Deposit Address
        elem = self.driver.find_element_by_class_name("btcaddr").text

        #Display New Account Data
        self.lineEdit_21.setText(url)
        self.lineEdit_24.setText(elem)

        QtCore.QCoreApplication.processEvents()

        #Close & Quit Webdriver
        self.driver.close()
        self.driver.quit()

    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'phantomjs.exe location',
                '/home')

    def startBot(self):
        #Set Global Variables
        turn = 1
        bet_changed = False
        current_cash = 0
        session_wins = 0
        session_losses = 0
        session_turns = 0
        session_tiles_win = 0
        session_tiles_lost = 0
        session_wage_total = 0
        session_profit_total = 0
        global_wins = 0
        global_losses = 0
        global_turns = 0
        global_tiles_win = 0
        global_tiles_lost = 0
        global_wage_total = 0
        global_profit_total = 0

        #Set Tiles List
        global tiles
        tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6
                     , self.tile7, self.tile8, self.tile9, self.tile10, self.tile11, self.tile12, self.tile13
                     , self.tile14, self.tile15, self.tile16, self.tile17, self.tile18, self.tile19, self.tile20
                     , self.tile21, self.tile22, self.tile23, self.tile24, self.tile25]

        #Get User PhantomJS Path
        chrdr_loc = fname

        #Get User Init Bet Amount
        bet_amount = self.initBet.text()

        try:
            bet_amount = int(bet_amount)
        except:
            self.gameHappening.setText("Invalid Initial Bet Amount.")
            raise

        #Set Late Global Variables
        new_bet_amount = bet_amount

        #Get User Account Hash
        account_hash = self.userid.text()
        account_link = "http://www.satoshimines.com/play/"+account_hash+"/"

        #Get User Mines Setting
        if self.mine1.isChecked():
            mines_xpath = "//div[3]/div[2]/div/button"
        elif self.mine3.isChecked():
            mines_xpath = "//div[2]/div[2]/button"
        elif self.mine5.isChecked():
            mines_xpath = "//div[3]/button"
        elif self.mine24.isChecked():
            mines_xpath = "//div[4]/button"

        #Create TileGUI List
        GUITiles = []
        for i in range(1, 26):
            GUITiles.append("//div[2]/div/ul/li["+ str(i) +"]")

        clicks = self.clicksPerRound.text()

        #Get User Max Clicks
        try:
            clicks = int(clicks)
        except:
            self.gameHappening.setText("Invalid Amount Of Clicks Per Round.")
            raise

        global games
        games = self.gameAmount.text()

        #Get User Max Games
        try:
            games = int(games)
        except:
            self.gameHappening.setText("Invalid Amount Of Total Games.")
            raise

        increment = self.increase.text()

        #Get User Increment on Lose
        try:
            increment = int(increment)
        except:
            self.gameHappening.setText("Invalid Amount Of Increment On Loss.")
            raise

        #Get stopAtWins
        if self.checkBox.isChecked():
            stopAtWins = self.lineEdit.text()
            try:
                stopAtWins = int(stopAtWins)
            except:
                self.gameHappening.setText("Invalid Stop Amount for Total Wins.")
                raise

        #Get stopAtLoss
        if self.checkBox_2.isChecked():
            stopAtLoss = self.lineEdit_2.text()
            try:
                stopAtLoss = int(stopAtLoss)
            except:
                self.gameHappening.setText("Invalid Stop Amount for Total Losses.")
                raise

        #Get stopAtBitsHit0
        if self.checkBox_3.isChecked():
            stopAtBitsHit0 = self.lineEdit_3.text()
            try:
                stopAtBitsHit0 = int(stopAtBitsHit0)
            except:
                self.gameHappening.setText("Invalid Stop Limit for Bits Hit.")
                raise

        #Get stopAtBitsHit1
        if self.checkBox_4.isChecked():
            stopAtBitsHit1 = self.lineEdit_4.text()
            try:
                stopAtBitsHit1 = int(stopAtBitsHit1)
            except:
                self.gameHappening.setText("Invalid Stop Limit for Bits Hit.")
                raise

        #Get stopAfterWinRow
        if self.checkBox_5.isChecked():
            stopAfterWinRow = self.lineEdit_5.text()
            try:
                stopAfterWinRow = int(stopAfterWinRow)
            except:
                self.gameHappening.setText("Invalid Stop Amount for Wins in a row.")
                raise

        #Get stopAfterLossRow
        if self.checkBox_6.isChecked():
            stopAfterLossRow = self.lineEdit_6.text()
            try:
                stopAfterLossRow = int(stopAfterLossRow)
            except:
                self.gameHappening.setText("Invalid Stop Amount for Losses in a row.")
                raise

        #Get extra ms Delay
        if self.checkBox_8.isChecked():
            extraDelay = self.lineEdit_8.text()
            try:
                extraDelay = int(extraDelay)
            except:
                self.gameHappening.setText("Invalid Amount of ms to add as Delay")
                raise

        #Get delayedIncrease
        if self.checkBox_17.isChecked():
            delayedIncrease = self.lineEdit_17.text()
            try:
                delayedIncrease = int(delayedIncrease)
            except:
                self.gameHappening.setText("Invalid Amount for delayed increasing.")
                raise

        #Get lowerIncrease
        if self.checkBox_18.isChecked():
            lowerIncrease = self.lineEdit_18.text()
            try:
                lowerIncrease = int(lowerIncrease)
            except:
                self.gameHappening.setText("Invalid Amount for 'Lower Increasement X% after failure'.")
                raise

        #Get maxIncrease
        if self.checkBox_7.isChecked():
            maxIncrease = self.lineEdit_7.text()
            try:
                maxIncrease = int(maxIncrease)
            except:
                self.gameHappening.setText("Invalid Amount for Max Increasements in a row.")
                raise

        #Get practiceLossAmount
        if self.checkBox_19.isChecked():
            practiceLossAmount = self.lineEdit_19.text()
            try:
                practiceLossAmount = int(practiceLossAmount)
            except:
                self.gameHappening.setText("Invalid Amount for 'Loose X practice Games in a row'.")
                raise

        #Get repeatIntervall
        if self.checkBox_20.isChecked():
            repeatIntervall = self.lineEdit_20.text()
            try:
                repeatIntervall = int(repeatIntervall)
            except:
                self.gameHappening.setText("Invalid Amount for 'Repeat after X Win(s)'.")
                raise

        #Get autoWithdrawAmount & Trigger
        if self.checkBox_21.isChecked():
            autoWithdrawAmount = self.lineEdit_9.text()
            autoWithdrawTrigger = self.lineEdit_10.text()
            try:
                autoWithdrawAmount = int(autoWithdrawAmount)
            except:
                self.gameHappening.setText("Invalid Auto Withdraw Amount.")
                raise

            try:
                autoWithdrawTrigger = int(autoWithdrawTrigger)
            except:
                self.gameHappening.setText("Invalid Auto Withdraw Trigger.")
                raise

        #Get autoWithdrawAddress
        autoWithdrawAddress = self.lineEdit_22.text()


        #Start PhantomJS
        if chrdr_loc == "unset":
            try:
                self.driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
            except:
                self.gameHappening.setText("Please Set A Path To PhantomJS.exe Before You Start.")
                raise
        else:
            try:
                self.driver = webdriver.PhantomJS(executable_path=chrdr_loc, service_log_path=os.path.devnull)
            except:
                self.gameHappening.setText("Your Path To PhantomJS.exe Is Invalid.")
                raise

        #Connect to Useraccount
        self.driver.get(account_link)

        #Check if Website was reached
        assert "Satoshi Mines" in self.driver.title

        self.gameHappening.setText("")

        try:
            #Select Bet Textbox
            elem = self.driver.find_element_by_id("bet")

            #Set Init Bet Amount
            elem.send_keys(int(bet_amount))

            #Set Mines
            self.driver.find_element_by_xpath(mines_xpath).click()

            #Mute Game
            self.driver.find_element_by_xpath("//i").click()

        except:
            #Sleep for Try Again
            time.sleep(1)

            #Select Bet Textbox
            elem = self.driver.find_element_by_id("bet")

            #Set Init Bet Amount
            elem.send_keys(int(bet_amount))

            #Set Mines
            self.driver.find_element_by_xpath(mines_xpath).click()

            #Mute Game
            self.driver.find_element_by_xpath("//i").click()

        #Iterate through Game Amount
        while games >= 1 or games <= -1:



            QtCore.QCoreApplication.processEvents()

            #Reset Turns
            turn = 1

            #Print Game Turn
            if games > 0:

                if self.gameHappening.toPlainText() == "":
                    self.gameHappening.append(" - Games left: " + str(games) + " - ")
                else:
                    self.gameHappening.append("\n - Games left: " + str(games) + " - ")

            else:
                if self.gameHappening.toPlainText() == "":
                    self.gameHappening.append(" - Games left: Unlimited - ")
                else:
                    self.gameHappening.append("\n - Games left: Unlimited - ")

            QtCore.QCoreApplication.processEvents()

            #Cashload Buffer
            time.sleep(0.5)

            #Get Current Cash
            current_cash = self.driver.find_element_by_class_name("num")

            #Print Cash & Bet Amount
            self.gameHappening.append("\nCurrent Bits  : " + str(current_cash.text.replace(",", "")))
            self.gameHappening.append("Betting Amount: " + str(new_bet_amount))

            QtCore.QCoreApplication.processEvents()

            #Check if Bet needs to be modified
            if bet_changed == True and bet_amount != 0:

                try:
                    #Select Bet Textbox
                    elem = self.driver.find_element_by_id("bet")

                    #Clear Bet Textbox
                    elem.clear()

                    #Set new Bet Amount
                    elem.send_keys(int(new_bet_amount))

                except:
                    #Sleep for Try Again
                    time.sleep(1)

                    #Select Bet Textbox
                    elem = self.driver.find_element_by_id("bet")

                    #Clear Bet Textbox
                    elem.clear()

                    #Set new Bet Amount
                    elem.send_keys(int(new_bet_amount))

                #Reset Variable
                bet_changed = False

            #Empty guesses tiles list
            guessed_tiles = []

            try:
                #Start a Game
                self.driver.find_element_by_xpath('//div[2]/button').click()

            except:
                #Sleep for Try Again
                time.sleep(1)

                #Start a Game
                self.driver.find_element_by_xpath('//div[2]/button').click()

            #New Game Sleep
            time.sleep(1)

            #Iterate through Click Amount
            while turn <= clicks:

                QtCore.QCoreApplication.processEvents()

                #Print Current Turn
                self.gameHappening.append("\n#" + str(turn) + " Turn")

                QtCore.QCoreApplication.processEvents()

                #Define next random Tile
                next_tile = randint(1, 25)

                #Ensure Tile is unique
                while next_tile in guessed_tiles:
                    next_tile = randint(1, 25)

                #Save guesses Tile
                guessed_tiles += [next_tile]

                #Define Xpath & Bomb Path for next Tile
                xpath = "//div[2]/div/div/ul/li["+str(next_tile)+"]"
                bomb_xpath = ".//button[@class='cashout']"

                #Buffer between Tile Clicks
                time.sleep(0.5)

                try:
                    #Click Tile
                    self.driver.find_element_by_xpath(xpath).click()

                except:
                    #Sleep for Try Again
                    time.sleep(1)

                    #Click Tile
                    self.driver.find_element_by_xpath(xpath).click()

                #Print Clicked Tile
                self.gameHappening.append("Clicking Tile [" + str(next_tile) + "].")

                QtCore.QCoreApplication.processEvents()

                #Buffer between Tile Clicks
                time.sleep(1)

                #Check if Game Over
                a = self.driver.find_element_by_xpath("//div[2]/div/div/ul/li[" + str(next_tile) + "]")
                if a.get_attribute("class") == "tile pressed bomb reveal":
                    #Bomb Hit
                    self.gameHappening.append("Bomb Hit")

                    for i in range(1, 26):
                        b = self.driver.find_element_by_xpath("//div[2]/div/div/ul/li[" + str(i) + "]")
                        if b.get_attribute("class") == "tile pressed bomb reveal":

                            pixmap = QtGui.QPixmap("tileHit.png")
                            counter = 0
                            for tile in tiles:
                                counter += 1
                                if i == counter:
                                    tile.setPixmap(pixmap)

                        elif b.get_attribute("class") == "tile reveal":

                            pixmap = QtGui.QPixmap("tileReveal.png")
                            counter = 0
                            for tile in tiles:
                                counter += 1
                                if i == counter:
                                    tile.setPixmap(pixmap)

                        QtCore.QCoreApplication.processEvents()

                    break
                else:
                    #Won
                    self.gameHappening.append("Safe")
                    pixmap = QtGui.QPixmap("tileClear.png")
                    counter = 0
                    for tile in tiles:
                        counter += 1
                        if next_tile == counter:
                            tile.setPixmap(pixmap)

                    QtCore.QCoreApplication.processEvents()

                #Turn Increment
                turn += 1

            #Cashout Button Sleep
            time.sleep(1)

            #Check for Cashout Button & Set new Bet Amount if needed
            try:
                #Click Cashout Button
                self.driver.find_element_by_xpath("//div[2]/div/div[2]/button").click()

                #Get Won Cash
                won_cash = int(self.driver.find_element_by_class_name("stake").text) - new_bet_amount

                #Modify Bet Amount if needed
                if new_bet_amount != bet_amount:
                    new_bet_amount = bet_amount
                    bet_changed = True

                self.gameHappening.append("\nCashed Out: " + str(won_cash) + " Bits.")
                QtCore.QCoreApplication.processEvents()

            except:
                self.gameHappening.append("\nNo Cashout Available.")
                QtCore.QCoreApplication.processEvents()

                #Compare Betting Amounts
                if new_bet_amount == bet_amount:

                    #Check if Cash Empty
                    if int(current_cash.text.replace(",", "")) < new_bet_amount + round(bet_amount * (1 + (0.01*increment))):
                        self.gameHappening.append("\nNot enough Bits to play further.")
                        QtCore.QCoreApplication.processEvents()
                        break

                    #Modify Bet Amount
                    new_bet_amount = round(bet_amount * (1 + (0.01*increment)))
                    bet_changed = True
                else:
                    #Check if Cash Empty
                    if int(current_cash.text.replace(",", "")) < new_bet_amount + round(bet_amount * (1 + (0.01*increment))):
                        self.gameHappening.append("\nNot enough Bits to play further.")
                        QtCore.QCoreApplication.processEvents()
                        break

                    #Modify Bet Amount
                    new_bet_amount = round(new_bet_amount * (1 + (0.01*increment)))
                    bet_changed = True

            #Decrement Games Count
            games -= 1

            #Reset GUITiles
            pixmap = QtGui.QPixmap("tileNew.png")
            for tile in tiles:
                tile.setPixmap(pixmap)

        self.driver.close()
        self.driver.quit()

    def stopBot(self):
        #Stop Game to next possible moment
        games = 0

        #Notice User
        self.gameHappening.append("\n\nThe Bot has been stopped.")

        #Close & Quit Webdriver
        self.driver.close()
        self.driver.quit()

        #Reset GUITiles
        pixmap = QtGui.QPixmap("tileNew.png")
        for tile in tiles:
            tile.setPixmap(pixmap)
        #sys.exit()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Satoshi Mines Bot", None))
        self.Start.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Starts the Bot</span></p></body></html>", None))
        self.Start.setText(_translate("MainWindow", "Play", None))
        self.Stop.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Stops the Bot</span></p></body></html>", None))
        self.Stop.setText(_translate("MainWindow", "Stop", None))
        self.progressBar.setToolTip(_translate("MainWindow", "<html><head/><body><p>See your desired Progress here.</p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "v0.6", None))
        self.label_8.setToolTip(_translate("MainWindow", "<html><head/><body><p>HF UID: 1712994</p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "Shiva", None))
        self.gameHappening.setToolTip(_translate("MainWindow", "<html><head/><body><p>See here what\'s currently happening.</p></body></html>", None))
        self.phantomjs.setToolTip(_translate("MainWindow", "Select phantomjs.exe!", None))
        self.phantomjs.setText(_translate("MainWindow", "...", None))
        self.gameAmount.setToolTip(_translate("MainWindow", "<html><head/><body><p>Negative Value = Infinite Games</p></body></html>", None))
        self.gameAmount.setText(_translate("MainWindow", "-1", None))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>You start the Bot with this amount.</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "Initial Bet Amount:", None))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>Negative Value = Infinite Games</p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "Games to Play:", None))
        self.userid.setToolTip(_translate("MainWindow", "<html><head/><body><p>User ID is found in your Account URL.</p></body></html>", None))
        self.increase.setText(_translate("MainWindow", "100", None))
        self.label_3.setText(_translate("MainWindow", "Increase in % on Loss:", None))
        self.label_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>User ID is found in your Account URL.</p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "Satoshi Mines User ID:", None))
        self.initBet.setToolTip(_translate("MainWindow", "<html><head/><body><p>You start the Bot with this amount.</p></body></html>", None))
        self.initBet.setText(_translate("MainWindow", "30", None))
        self.groupBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>With how many Mines are you going to play?</p></body></html>", None))
        self.groupBox.setTitle(_translate("MainWindow", "Mines", None))
        self.mine24.setText(_translate("MainWindow", "24", None))
        self.mine5.setText(_translate("MainWindow", "5", None))
        self.mine3.setText(_translate("MainWindow", "3", None))
        self.mine1.setText(_translate("MainWindow", "1", None))
        self.clicksPerRound.setText(_translate("MainWindow", "3", None))
        self.label_4.setText(_translate("MainWindow", "Clicks per Round:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic Settings", None))
        self.checkBox.setText(_translate("MainWindow", "Stop after:", None))
        self.checkBox_2.setText(_translate("MainWindow", "Stop after:", None))
        self.lineEdit.setText(_translate("MainWindow", "50", None))
        self.lineEdit_2.setText(_translate("MainWindow", "50", None))
        self.lineEdit_3.setText(_translate("MainWindow", "500", None))
        self.checkBox_3.setText(_translate("MainWindow", "Stop after:", None))
        self.lineEdit_4.setText(_translate("MainWindow", "5000", None))
        self.checkBox_4.setText(_translate("MainWindow", "Stop after:", None))
        self.label_9.setText(_translate("MainWindow", "Wins.", None))
        self.label_10.setText(_translate("MainWindow", "Losses.", None))
        self.label_11.setText(_translate("MainWindow", "Bits Hit.", None))
        self.label_12.setText(_translate("MainWindow", "Bits Hit.", None))
        self.lineEdit_5.setText(_translate("MainWindow", "10", None))
        self.label_13.setText(_translate("MainWindow", "Wins in a row.", None))
        self.checkBox_5.setText(_translate("MainWindow", "Stop after:", None))
        self.checkBox_6.setText(_translate("MainWindow", "Stop after:", None))
        self.lineEdit_6.setText(_translate("MainWindow", "5", None))
        self.label_14.setText(_translate("MainWindow", "Losses in a row.", None))
        self.label_16.setToolTip(_translate("MainWindow", "<html><head/><body><p>Use this if your Internet is slow.</p></body></html>", None))
        self.label_16.setText(_translate("MainWindow", "ms Delay to Actions.", None))
        self.checkBox_8.setToolTip(_translate("MainWindow", "<html><head/><body><p>Use this if your Internet is slow.</p></body></html>", None))
        self.checkBox_8.setText(_translate("MainWindow", "Add:", None))
        self.lineEdit_8.setToolTip(_translate("MainWindow", "<html><head/><body><p>Use this if your Internet is slow.</p></body></html>", None))
        self.lineEdit_8.setText(_translate("MainWindow", "10", None))
        self.checkBox_21.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enable Auto Withdrawing Bits as soon as the Limit is hit.</p></body></html>", None))
        self.checkBox_21.setText(_translate("MainWindow", "Auto Cashout:", None))
        self.lineEdit_9.setText(_translate("MainWindow", "5", None))
        self.lineEdit_10.setText(_translate("MainWindow", "5", None))
        self.label_17.setText(_translate("MainWindow", "at", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Adv. Settings", None))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Show the Odds for every Setting.</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Odds", None))
        self.label_30.setText(_translate("MainWindow", "Losses in a row.", None))
        self.lineEdit_17.setText(_translate("MainWindow", "3", None))
        self.checkBox_17.setText(_translate("MainWindow", "Start Increasing after:", None))
        self.label_31.setText(_translate("MainWindow", "% after failure.", None))
        self.lineEdit_18.setText(_translate("MainWindow", "10", None))
        self.checkBox_18.setText(_translate("MainWindow", "Lower Increasement:", None))
        self.pushButton_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Pick a Routine the Bot will play every Round.</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("MainWindow", "Routine", None))
        self.label_15.setText(_translate("MainWindow", "times in a row.", None))
        self.lineEdit_7.setText(_translate("MainWindow", "5", None))
        self.checkBox_7.setText(_translate("MainWindow", "Max Increase:", None))
        self.label_32.setText(_translate("MainWindow", "practice Games in a row.", None))
        self.checkBox_19.setText(_translate("MainWindow", "Loose:", None))
        self.lineEdit_19.setText(_translate("MainWindow", "3", None))
        self.lineEdit_20.setText(_translate("MainWindow", "1", None))
        self.label_33.setToolTip(_translate("MainWindow", "<html><head/><body><p>i.a.r. = in a row</p></body></html>", None))
        self.label_33.setText(_translate("MainWindow", "Wins", None))
        self.checkBox_20.setText(_translate("MainWindow", "Repeat after:", None))
        self.pushButton_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Pick on the Playboard which Tiles to avoid.</span></p></body></html>", None))
        self.pushButton_4.setText(_translate("MainWindow", "Avoid", None))
        self.pushButton_5.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Pick on the Playboard which Tiles to prefer.</span></p></body></html>", None))
        self.pushButton_5.setText(_translate("MainWindow", "Prefer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tactics", None))
        self.pushButton_6.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Click here to create a new Account</span></p></body></html>", None))
        self.pushButton_6.setText(_translate("MainWindow", "Create Account", None))
        self.pushButton_7.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click here to manually Withdraw Bits.</p></body></html>", None))
        self.pushButton_7.setText(_translate("MainWindow", "Withdraw", None))
        self.lineEdit_21.setToolTip(_translate("MainWindow", "<html><head/><body><p>See your Account URL here.</p></body></html>", None))
        self.lineEdit_22.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter your Bitcoin Address here.</p></body></html>", None))
        self.label_34.setText(_translate("MainWindow", "Bits to:", None))
        self.lineEdit_23.setToolTip(_translate("MainWindow", "<html><head/><body><p>Amount of Bits to Withdraw, also serves as Limit for Autowithdraw.</p></body></html>", None))
        self.lineEdit_23.setText(_translate("MainWindow", "1000", None))
        self.lineEdit_24.setToolTip(_translate("MainWindow", "<html><head/><body><p>See your Deposit Address here.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Accout Stuff", None))
        self.gameStats.setToolTip(_translate("MainWindow", "<html><head/><body><p>See Statistics here.</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Session", None))
        self.gameStats_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>See Statistics here.</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Global", None))

class ExampleApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)

    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Background,QtGui.QColor(17, 17, 17))

    form = ExampleApp()
    form.setPalette(palette)
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

