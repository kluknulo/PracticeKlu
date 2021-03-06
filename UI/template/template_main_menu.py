# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 750)
        MainWindow.setMinimumSize(QtCore.QSize(870, 750))
        MainWindow.setMaximumSize(QtCore.QSize(870, 750))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(23, 33, 43);")
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 681, 761))
        self.stackedWidget.setStyleSheet("background-color: rgb(14, 22, 33);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.top10 = QtWidgets.QWidget()
        self.top10.setObjectName("top10")
        self.textBrowser = QtWidgets.QTextBrowser(self.top10)
        self.textBrowser.setGeometry(QtCore.QRect(10, 80, 661, 661))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: rgb(245, 245, 245);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.top10)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 681, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(24, 37, 51);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.top10)
        self.realtime = QtWidgets.QWidget()
        self.realtime.setObjectName("realtime")
        self.label_6 = QtWidgets.QLabel(self.realtime)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 681, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(24, 37, 51);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.realtime)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 80, 661, 661))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("color: rgb(245, 245, 245);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.stackedWidget.addWidget(self.realtime)
        self.usertop = QtWidgets.QWidget()
        self.usertop.setObjectName("usertop")
        self.label_7 = QtWidgets.QLabel(self.usertop)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 681, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(24, 37, 51);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.usertop)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.usertop)
        self.lineEdit.setGeometry(QtCore.QRect(270, 90, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(245, 245, 245);")
        self.lineEdit.setMaxLength(3)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label_9 = QtWidgets.QLabel(self.usertop)
        self.label_9.setGeometry(QtCore.QRect(330, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.usertop)
        self.label_10.setGeometry(QtCore.QRect(30, 130, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.usertop)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 130, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(245, 245, 245);")
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_11 = QtWidgets.QLabel(self.usertop)
        self.label_11.setGeometry(QtCore.QRect(140, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.usertop)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 190, 661, 551))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("color: rgb(245, 245, 245);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.usertop)
        self.pushButton_10.setGeometry(QtCore.QRect(490, 100, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(43, 82, 120);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.stackedWidget.addWidget(self.usertop)
        self.welcome = QtWidgets.QWidget()
        self.welcome.setObjectName("welcome")
        self.label_12 = QtWidgets.QLabel(self.welcome)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 681, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(24, 37, 51);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.welcome)
        self.label_13.setGeometry(QtCore.QRect(20, 340, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.stackedWidget.addWidget(self.welcome)
        self.info_chats = QtWidgets.QWidget()
        self.info_chats.setObjectName("info_chats")
        self.label_14 = QtWidgets.QLabel(self.info_chats)
        self.label_14.setGeometry(QtCore.QRect(100, 280, 481, 431))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.info_chats)
        self.label_15.setGeometry(QtCore.QRect(270, 100, 150, 150))
        self.label_15.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.pushButton_13 = QtWidgets.QPushButton(self.info_chats)
        self.pushButton_13.setGeometry(QtCore.QRect(610, 480, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(43, 82, 120);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.info_chats)
        self.pushButton_14.setGeometry(QtCore.QRect(30, 480, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(43, 82, 120);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_16 = QtWidgets.QLabel(self.info_chats)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 681, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(24, 37, 51);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.info_chats)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 681, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(24, 37, 51);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(170, 210, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_17.setObjectName("label_17")
        self.pushButton_15 = QtWidgets.QPushButton(self.page)
        self.pushButton_15.setGeometry(QtCore.QRect(180, 300, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_15.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(43, 82, 120);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.page)
        self.pushButton_16.setGeometry(QtCore.QRect(380, 300, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(24, 37, 51);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.stackedWidget.addWidget(self.page)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(700, 100, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(43, 82, 120);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(710, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(245, 245, 245);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 150, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_2.setFont(font)
        self.label_2.setWhatsThis("")
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 270, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_3.setFont(font)
        self.label_3.setWhatsThis("")
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 220, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(43, 82, 120);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(700, 350, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(43, 82, 120);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(710, 400, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_4.setFont(font)
        self.label_4.setWhatsThis("")
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(700, 600, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(43, 82, 120);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(700, 680, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(49, 36, 42);\n"
"color: rgb(219, 53, 59);")
        self.pushButton_12.setObjectName("pushButton_12")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "kluknulo Parser"))
        self.label_5.setText(_translate("MainWindow", "?????? 10 ???????????????? ???? ?????????????????? 24 ????????"))
        self.label_6.setText(_translate("MainWindow", "?????????????????? ?? ???????????????? ??????????????"))
        self.label_7.setText(_translate("MainWindow", "?????? ???? ????????????????????"))
        self.label_8.setText(_translate("MainWindow", "?????????????? ?????? ??????????????????"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "10"))
        self.label_9.setText(_translate("MainWindow", "??????????????????"))
        self.label_10.setText(_translate("MainWindow", "???? "))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "24"))
        self.label_11.setText(_translate("MainWindow", "????????(-????)"))
        self.pushButton_10.setText(_translate("MainWindow", "???????????? ??????????"))
        self.label_12.setText(_translate("MainWindow", "Welcome!"))
        self.label_13.setText(_translate("MainWindow", "???????????????? ?????????? ?????? ???????????? ????????????"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><br/></p><p><br/></p><p><br/></p><p>?????????????????????? ?????????? ?????? ???????????? ?????? ????????????</p></body></html>"))
        self.pushButton_13.setText(_translate("MainWindow", ">"))
        self.pushButton_14.setText(_translate("MainWindow", "<"))
        self.label_16.setText(_translate("MainWindow", "???????????????????? ?? ??????????"))
        self.label_18.setText(_translate("MainWindow", "???????????????????? ????????????"))
        self.label_17.setText(_translate("MainWindow", "???? ?????????????????????????? ???????????? ???????????"))
        self.pushButton_15.setText(_translate("MainWindow", "????"))
        self.pushButton_16.setText(_translate("MainWindow", "??????"))
        self.pushButton_7.setText(_translate("MainWindow", "Top 10"))
        self.label.setText(_translate("MainWindow", "????????????"))
        self.label_2.setText(_translate("MainWindow", "*?????????????? ?????? 10 ??????????????????"))
        self.label_3.setText(_translate("MainWindow", "*?????????????? ?????????????????? ?? ???????????? ?????????????????? ??????????????"))
        self.pushButton_8.setText(_translate("MainWindow", "RealTime"))
        self.pushButton_9.setText(_translate("MainWindow", "User Top"))
        self.label_4.setText(_translate("MainWindow", "*?????????????? ?????? ???? ???????????????????????????????? ????????????????????"))
        self.pushButton_11.setText(_translate("MainWindow", "Info Chats"))
        self.pushButton_12.setText(_translate("MainWindow", "Exit"))
