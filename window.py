# -*- coding:utf-8 -*-
__author__ = 'linxinloningg'

from ui.bb import Ui_window
from ui.appfunction import appfunction
from PyQt5 import QtWidgets, QtCore, QtGui
from sys import argv, exit
from os import getcwd


class QtThread(QtCore.QThread):
    def __init__(self, func, args):
        super().__init__()
        self.flag = True
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

    def stop(self):
        self.flag = bool(1 - self.flag)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # UI调用
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_window()
        self.ui.setupUi(self)
        # 禁用最大化
        self.setFixedSize(self.width(), self.height())

        self.app = appfunction(self.ui)

        # 设置进度条
        self.ui.progressBar.setRange(0, 0)

        # 设置文件格式下拉框
        # 设置可编辑
        self.ui.format.setEditable(True)
        self.ui.format.addItem('默认')
        self.ui.format.addItem('flv')
        self.ui.format.addItem('mp4')
        self.ui.format.addItem('avi')

        # 设置文件输出目录软件启动本目录
        self.ui.directoryedit.setText(getcwd())

        # 设置host编辑框
        self.ui.hostedit.setText('HOST:PORT')

        # 绑定信号到功能函数
        self.ui.cookie.clicked.connect(lambda: self.app.fun_cookie(self.editbrower()))

        self.ui.txt.clicked.connect(lambda: self.app.fun_txt(self.file_dig()))

        # 创建一个Qt工作线程
        analysisthread = QtThread(func=self.app.fun_analysis, args=[])

        self.ui.analysis.clicked.connect(lambda: analysisthread.start())

        self.ui.directory.clicked.connect(lambda: self.app.fun_directory(self.directory_dig()))

        self.ui.filename.clicked.connect(lambda: self.app.fun_fliename(self.file_dig()))

        self.ui.timeout.clicked.connect(lambda: self.app.fun_timeout())

        self.ui.info.clicked.connect(lambda: self.app.fun_info())

        self.ui.reset.clicked.connect(lambda: self.app.fun_reset())

        self.ui.suspend.clicked.connect(lambda: self.app.fun_suspend())

        # 创建一个Qt工作线程
        startthread = QtThread(func=self.app.fun_start, args=[])

        self.ui.start.clicked.connect(lambda: startthread.start())

        self.ui.suspend.clicked.connect(lambda: self.app.fun_suspend(startthread))

        # 连接下拉框选项右键事件
        self.ui.format.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)
        # 启用此功能（默认关闭）
        # 设置列表选项具有右键弹出菜单功能
        self.ui.format.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.format.contextMenuPolicy()

    # 无须绑定触发调用
    def closeEvent(self, event):  # 关闭窗口触发以下事件
        reply = QtWidgets.QMessageBox.question(self, '退出询问', '你确定要退出吗?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()  # 接受关闭事件
        else:
            event.ignore()  # 忽略关闭事件

    # 需要绑定触发调用
    # 信息弹窗
    def message(self, text):
        QtWidgets.QMessageBox.information(self, "信息弹窗", text, QtWidgets.QMessageBox.Yes)

    # 错误信息弹窗
    def errmessage(self):
        QtWidgets.QMessageBox.critical(self, "错误", "”错误信息“")

    # 警告信息
    def warningmessage(self):
        QtWidgets.QMessageBox.warning(self, "警告", "警告信息", QtWidgets.QMessageBox.Cancel)

    # 关于信息
    def aboutmessage(self):
        QtWidgets.QMessageBox.about(self, "关于", "关于信息")

    # 目录路径选择器
    @staticmethod
    def directory_dig():
        # 实例化QFileDialog
        dig = QtWidgets.QFileDialog()
        # 设置可以打开任何文件
        dig.setFileMode(QtWidgets.QFileDialog.Directory)
        # 文件过滤
        dig.setFilter(QtCore.QDir.Files)
        return dig

    # 文件路径选择器
    @staticmethod
    def file_dig():
        # 实例化QFileDialog
        dig = QtWidgets.QFileDialog()
        # 设置可以打开任何文件
        dig.setFileMode(QtWidgets.QFileDialog.FileMode())
        # 文件过滤
        dig.setFilter(QtCore.QDir.Files)
        return dig

    # 右键弹出菜单
    def rightMenuShow(self):
        def CreateNewItem():
            # 添加控件
            try:
                self.ui.format.addItem("自定义(修改值)")
            except Exception as e:
                self.ui.textBrowser.append(str(e))

        def DeleteItem():
            self.ui.format.removeItem(self.ui.format.currentIndex())

        def ReadItem():
            dig = self.file_dig()
            try:
                # 接受选中文件的路径，默认为列表
                # 列表中的第一个元素即是文件路径
                if dig.exec_():
                    directorypath = dig.selectedFiles()[0]
                    formattext = directorypath.split("/")[-1].split(".")[1]
                    # 添加一项
                    self.ui.format.addItem(formattext)
                else:
                    pass

            except Exception as e:
                self.ui.textBrowser.append(str(e))

        # 右键弹出菜单
        popMenu = QtWidgets.QMenu()
        popMenu.addAction(QtWidgets.QAction(u'新增', self, triggered=CreateNewItem))
        popMenu.addAction(QtWidgets.QAction(u'删除', self, triggered=DeleteItem))
        popMenu.addAction(QtWidgets.QAction(u'读取', self, triggered=ReadItem))
        popMenu.exec_(QtGui.QCursor.pos())

    # 弹出文本输入框
    @staticmethod
    def editbrower():
        return QtWidgets.QInputDialog().getText(QtWidgets.QWidget(), 'Cookie：', '输入')


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    win = MainWindow()
    win.show()
    exit(app.exec_())
