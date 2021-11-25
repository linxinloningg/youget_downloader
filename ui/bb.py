# -*- coding:utf-8 -*-
__author__ = 'linxinloningg'

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(450, 400)
        window.setWindowOpacity(1.0)
        window.setAutoFillBackground(False)
        window.setStyleSheet("background:rgba(85, 85, 127,0.4)")
        window.setWindowOpacity(0.8)  # 设置窗口透明度

        window.setWindowIcon(QtGui.QIcon("ui/iocn.ico"))
        window.setWindowTitle("小偷小摸下载器")

        self.label_top = QtWidgets.QLabel(window)
        self.label_top.setGeometry(QtCore.QRect(0, 0, 450, 20))
        self.label_top.setText("")
        self.label_top.setObjectName("label_top")
        self.label_bottom = QtWidgets.QLabel(window)
        self.label_bottom.setGeometry(QtCore.QRect(0, 380, 450, 20))
        self.label_bottom.setText("")
        self.label_bottom.setObjectName("label_bottom")
        self.urledit = QtWidgets.QLineEdit(window)
        self.urledit.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.urledit.setStyleSheet(
            "QLineEdit{border:1px rgb(124,124,124);background-color: rgba(124,124,124, 0%);padding:1px 2px;border-style: solid;font-size : 15px ;color:rgb(255, 170, 0);}")
        self.urledit.setObjectName("urledit")
        self.cookie = QtWidgets.QPushButton(window)
        self.cookie.setGeometry(QtCore.QRect(150, 40, 75, 23))
        self.cookie.setStyleSheet(
            "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

            "QPushButton:hover{opacity:0.2;border:2px solid black;}"

            "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
        self.cookie.setObjectName("cookie")
        self.txt = QtWidgets.QPushButton(window)
        self.txt.setGeometry(QtCore.QRect(240, 40, 75, 23))
        self.txt.setStyleSheet(
            "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

            "QPushButton:hover{opacity:0.2;border:2px solid black;}"

            "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
        self.txt.setObjectName("txt")
        self.analysis = QtWidgets.QPushButton(window)
        self.analysis.setGeometry(QtCore.QRect(330, 40, 75, 23))
        self.analysis.setStyleSheet(
            "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

            "QPushButton:hover{opacity:0.2;border:2px solid black;}"

            "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
        self.analysis.setObjectName("analysis")
        self.directoryedit = QtWidgets.QLineEdit(window)
        self.directoryedit.setGeometry(QtCore.QRect(20, 90, 113, 20))
        self.directoryedit.setStyleSheet(
            "QLineEdit{border:1px rgb(124,124,124);background-color: rgba(124,124,124, 0%);padding:1px 2px;border-style: solid;font-size : 15px ;color:rgb(255, 170, 0);}")
        self.directoryedit.setObjectName("directoryedit")
        self.textBrowser = QtWidgets.QTextBrowser(window)
        self.textBrowser.setGeometry(QtCore.QRect(0, 170, 256, 192))
        self.textBrowser.setStyleSheet("QTextBrowser{background-color : rgba(85, 85, 255,0.3);}")
        self.textBrowser.setObjectName("textBrowser")
        self.filename = QtWidgets.QPushButton(window)
        self.filename.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.filename.setStyleSheet(
            "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

            "QPushButton:hover{opacity:0.2;border:2px solid black;}"

            "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
        self.filename.setObjectName("fliename")
        self.timeout = QtWidgets.QPushButton(window)
        self.timeout.setGeometry(QtCore.QRect(360, 140, 75, 23))
        self.timeout.setStyleSheet(
            "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

            "QPushButton:hover{opacity:0.2;border:2px solid black;}"

            "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
        self.timeout.setObjectName("timeout")
        self.ignore_ssl_errors = QtWidgets.QCheckBox(window)
        self.ignore_ssl_errors.setGeometry(QtCore.QRect(270, 240, 81, 16))
        self.ignore_ssl_errors.setStyleSheet(
            "QCheckBox{border-radius:15px;width: 20px;height:20px;font-size:10px;color:rgb(255, 170, 0);}")
        self.ignore_ssl_errors.setObjectName("ignore_ssl_errors")
        self.merge = QtWidgets.QCheckBox(window)
        self.merge.setGeometry(QtCore.QRect(270, 210, 81, 16))
        self.merge.setStyleSheet(
            "QCheckBox{border-radius:15px;width: 20px;height:20px;font-size:10px;color:rgb(255, 170, 0);}")
        self.merge.setObjectName("merge")
        self.debug = QtWidgets.QCheckBox(window)
        self.debug.setGeometry(QtCore.QRect(270, 270, 81, 16))
        self.debug.setStyleSheet(
            "QCheckBox{border-radius:15px;width: 20px;height:20px;font-size:10px;color:rgb(255, 170, 0);}")
        self.debug.setObjectName("debug")
        self.directory = QtWidgets.QPushButton(window)
        self.directory.setGeometry(QtCore.QRect(150, 90, 75, 23))
        self.directory.setStyleSheet(
            "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

            "QPushButton:hover{opacity:0.2;border:2px solid black;}"

            "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
        self.directory.setObjectName("directory")
        self.timespinBox = QtWidgets.QSpinBox(window)
        self.timespinBox.setGeometry(QtCore.QRect(240, 141, 111, 21))
        self.timespinBox.setStyleSheet("QSpinBox{height:30px;width:30px;}"

                                       "QSpinBox::up-button{height: 15px;subcontrol-position:left;}"

                                       "QSpinBox::down-button{height: 15px;subcontrol-position:right;}")
        self.timespinBox.setObjectName("timespinBox")
        self.filenameedit = QtWidgets.QLineEdit(window)
        self.filenameedit.setGeometry(QtCore.QRect(20, 140, 113, 20))
        self.filenameedit.setStyleSheet(
            "QLineEdit{border:1px rgb(124,124,124);background-color: rgba(124,124,124, 0%);padding:1px 2px;border-style: solid;font-size : 15px ;color:rgb(255, 170, 0);}")
        self.filenameedit.setObjectName("filenameedit")
        self.caption = QtWidgets.QCheckBox(window)
        self.caption.setGeometry(QtCore.QRect(270, 180, 81, 16))
        self.caption.setStyleSheet(
            "QCheckBox{border-radius:15px;width: 20px;height:20px;font-size:10px;color:rgb(255, 170, 0);}")
        self.caption.setObjectName("caption")
        self.progressBar = QtWidgets.QProgressBar(window)
        self.progressBar.setGeometry(QtCore.QRect(0, 360, 450, 20))
        self.progressBar.setStyleSheet("QProgressBar {border-radius: 5px;background-color:rgba(85, 85, 127,0.4);}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.start = QtWidgets.QPushButton(window)
        self.start.setGeometry(QtCore.QRect(320, 330, 75, 23))
        self.start.setStyleSheet(
            "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

            "QPushButton:hover{opacity:0.2;border:2px solid black;}"

            "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
        self.start.setObjectName("start")
        self.hostedit = QtWidgets.QLineEdit(window)
        self.hostedit.setGeometry(QtCore.QRect(260, 300, 113, 20))
        self.hostedit.setStyleSheet(
            "QLineEdit{border:1px rgb(124,124,124);background-color: rgba(124,124,124, 0%);padding:1px 2px;border-style: solid;font-size : 15px ;color:rgb(255, 170, 0);}")
        self.hostedit.setObjectName("hostedit")
        self.host = QtWidgets.QCheckBox(window)
        self.host.setGeometry(QtCore.QRect(380, 300, 71, 16))
        self.host.setStyleSheet(
            "QCheckBox{border-radius:15px;width: 20px;height:20px;font-size:10px;color:rgb(255, 170, 0);}")
        self.host.setObjectName("host")
        self.reset = QtWidgets.QPushButton(window)
        self.reset.setGeometry(QtCore.QRect(370, 220, 75, 23))
        self.reset.setStyleSheet(
            "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

            "QPushButton:hover{opacity:0.2;border:2px solid black;}"

            "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
        self.reset.setObjectName("reset")
        self.info = QtWidgets.QPushButton(window)
        self.info.setGeometry(QtCore.QRect(370, 190, 75, 23))
        self.info.setStyleSheet(
            "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

            "QPushButton:hover{opacity:0.2;border:2px solid black;}"

            "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
        self.info.setObjectName("info")
        self.format = QtWidgets.QComboBox(window)
        self.format.setGeometry(QtCore.QRect(240, 90, 171, 22))
        self.format.setObjectName("format")
        self.suspend = QtWidgets.QPushButton(window)
        self.suspend.setGeometry(QtCore.QRect(370, 250, 75, 23))
        self.suspend.setStyleSheet(
            "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

            "QPushButton:hover{opacity:0.2;border:2px solid black;}"

            "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
        self.suspend.setObjectName("suspend")

        self.playlist = QtWidgets.QCheckBox(window)
        self.playlist.setGeometry(QtCore.QRect(380, 280, 71, 16))
        self.playlist.setStyleSheet(
            "QCheckBox{border-radius:15px;width: 20px;height:20px;font-size:10px;color:rgb(255, 170, 0);}")
        self.playlist.setObjectName("playlist")

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", " "))
        self.cookie.setText(_translate("window", "附加cookie"))
        self.txt.setText(_translate("window", "选择txt文件"))
        self.analysis.setText(_translate("window", "解析"))
        self.filename.setText(_translate("window", "文件名"))
        self.timeout.setText(_translate("window", "设置"))
        self.ignore_ssl_errors.setText(_translate("window", "忽略ssl错误"))
        self.merge.setText(_translate("window", "合并"))
        self.debug.setText(_translate("window", "调试"))
        self.directory.setText(_translate("window", "保存目录"))
        self.caption.setText(_translate("window", "字幕"))
        self.start.setText(_translate("window", "开始下载"))
        self.host.setText(_translate("window", "启用代理"))
        self.reset.setText(_translate("window", "重置"))
        self.info.setText(_translate("window", "版本信息"))
        self.suspend.setText(_translate("window", "暂停"))
        self.playlist.setText(_translate("window", "批量下载"))
