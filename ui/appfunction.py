# -*- coding:utf-8 -*-
__author__ = 'linxinloningg'

# 导入下载器
from core.downloader import Downloader
# 导入参数
from core.args import DownloadArgs, DryRunArgs, OptionalArgs

# 下载参数
DownloadArgs = DownloadArgs()
# 预运行参数
DryRunArgs = DryRunArgs()
# 可选参数 版本与帮助
OptionalArgs = OptionalArgs()


# 暂不开启多线程下载
# from threading import Thread


class appfunction:
    def __init__(self, ui):
        # 界面
        self.ui = ui

        self.cookie = None
        self.directory = None
        self.fliename = None
        # 用于改变文件名按钮样式
        self.fliename_flag = False
        self.timeout = None
        # 用于改变设置按钮样式
        self.timeout_flag = False
        # 是否已解析
        self.analysis = False
        # 是否批量下载
        self.down_list = False
        self.url = None

        self.Downloader = Downloader()

    def fun_cookie(self, dig):
        """
        cookie按钮功能函数
        :param dig: 弹窗
        :return:
        """
        try:
            if dig[0] and dig[1]:
                self.cookie = dig[0]
        except Exception as e:
            self.ui.textBrowser.append(str(e))

    def fun_txt(self, dig):
        """
        txt按钮功能函数
        :param dig: 弹窗
        :return:
        """
        try:
            # 接受选中文件的路径，默认为列表
            # 列表中的第一个元素即是文件路径
            if dig.exec_():
                directorypath = dig.selectedFiles()[0]
                # 修改输入框的值
                self.ui.urledit.setText(directorypath)
            else:
                pass

        except Exception as e:
            self.ui.textBrowser.append(str(e))

    def fun_analysis(self):
        """
        解析按钮功能函数
        :return:
        """

        # 解析本地url文件信息
        def url_list_from_file(file):
            """
            :param file:
            :return: [https://www.bilibili.com/video/BV1hb411e75W?from=search&seid=11238379916538554538]
            """
            try:
                with open(file, 'r') as f:
                    content = f.read()
                    return content.split()
            except Exception as err:
                self.ui.textBrowser.append(str(err))
                return None

        try:
            # DryRunArgs.clear()
            # DryRunArgs.url_info()

            # 需要获取urledit输入框的url输入
            url = self.ui.urledit.text()

            # 有url信息的情况
            if url != "":
                # url是视频链接的情况
                if "http" in url:
                    if "?p=" in url:
                        self.ui.textBrowser.append("这个视频在一个视频合集里。\n如有需要请勾选批量下载，将一并下载全部视频。")
                    else:
                        self.ui.textBrowser.append("可以开始你的下载之旅。")
                    # 不会！！！，不知如何捕获终端输出
                    # Downloader.start(DryRunArgs, url)
                    self.url = url
                    self.analysis = True
                # url是本地链接的情况
                else:
                    # 解析本地url文件地址
                    urls = None
                    try:
                        urls = url_list_from_file(url)
                        self.ui.textBrowser.append("文件包含链接:{}".format(" ".join(urls)))
                    except Exception as e:
                        self.ui.textBrowser.append(str(e))

                    # 解析本地url文件地址没有出错
                    if urls is not None:
                        self.url = urls
                        self.analysis = True
                        self.ui.textBrowser.append("选择了本地urls文件路径：\n如果不勾选批量下载，将会仅进行第一个连接的下载！\n如果有需要切记勾选批量下载！\n\n")
                        for value in urls:
                            # 验证url是否可行
                            if "http" in value:
                                self.ui.textBrowser.append(str(value) + "\n")
                            else:
                                self.ui.textBrowser.append(str(value) + "\n" + "这是个错误的视频链接！！！")
                                self.analysis = False
                    # 解决本地url地址文件出错
                    else:
                        self.ui.textBrowser.append("url出错！！！\n请认真检查！！！\n")
            # 没有url信息的情况
            else:
                self.ui.textBrowser.append("没有输入任何视频地址！！！\n或者文件地址！！！")
        except Exception as e:
            self.ui.textBrowser.append(str(e))

    def fun_directory(self, dig):
        """
        设置目录按钮功能函数
        :param dig: 弹窗
        :return:
        """
        try:
            # 接受选中文件的路径，默认为列表
            # 列表中的第一个元素即是文件路径
            if dig.exec_():
                directorypath = dig.selectedFiles()[0]
                # 修改输入框的值
                self.ui.directoryedit.setText(directorypath)
                self.directory = directorypath
            else:
                pass

        except Exception as e:
            self.ui.textBrowser.append(str(e))

    def fun_fliename(self, dig):
        """
        设置文件名功能函数
        :param dig: 弹窗
        :return:
        """
        # 改变flag
        # 取反
        self.fliename_flag = bool(1 - self.fliename_flag)
        try:
            # 取值
            if self.ui.filenameedit.text() == "":
                # 接受选中文件的路径，默认为列表
                # 列表中的第一个元素即是文件路径
                if dig.exec_():
                    flienamepath = dig.selectedFiles()[0]
                    flienamepath = flienamepath.split("/")[-1].split(".")[0]

                    # 修改输入框的值
                    self.ui.filenameedit.setText(flienamepath)
                    self.fliename = flienamepath
            else:
                self.fliename = self.ui.filenameedit.text()

            if self.fliename_flag is False:
                # 当flag为Flase时：无论有无值都不启动
                self.fliename = None

            # 改变按钮样式
            if self.fliename_flag is True:
                # 激活时的样式
                self.ui.filename.setStyleSheet(
                    "QPushButton{background-color:rgba(255, 85, 127,0.3);color:rgb(85, 85, 85);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                    "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                    "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
                # 激活时不可修改
                self.ui.filenameedit.setReadOnly(True)
            else:
                # 未被激活时的样式
                self.ui.filename.setStyleSheet(
                    "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                    "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                    "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
                # w未被激活可以修改
                self.ui.filenameedit.setReadOnly(False)

        except Exception as e:
            self.ui.textBrowser.append(str(e))

    def fun_timeout(self):
        """
        设置超时时间功能函数
        :return:
        """
        # 改变flag
        # 取反
        self.timeout_flag = bool(1 - self.timeout_flag)
        try:
            # 取值
            if self.ui.timespinBox.value() != 0:
                self.timeout = str(self.ui.timespinBox.value())

            if self.timeout_flag is False:
                # 当flag为Flase时：无论有无值都不启动
                self.timeout = None

            # 改变按钮样式
            if self.timeout_flag is True:
                # 激活时的样式
                self.ui.timeout.setStyleSheet(
                    "QPushButton{background-color:rgba(255, 85, 127,0.3);color:rgb(85, 85, 85);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                    "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                    "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
                # 激活时不可修改
                self.ui.timespinBox.setReadOnly(True)
            else:
                # 未被激活时的样式
                self.ui.timeout.setStyleSheet(
                    "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                    "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                    "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
                # 未被激活时可以修改
                self.ui.timespinBox.setReadOnly(False)

        except Exception as e:
            self.ui.textBrowser.append(str(e))

    def fun_info(self):
        """
        版本按钮功能函数
        :return:
        """
        # OptionalArgs.version()
        try:
            self.ui.textBrowser.append("作者：小偷小摸小林人\n版本：V1.0\n特点：1.烂到爆炸的界面;2.不稳定的功能\n\n")
            # Downloader.start(OptionalArgs)
        except Exception as e:
            self.ui.textBrowser.append(str(e))

    def fun_reset(self):
        """
        重置按钮功能函数
        :return:
        """
        try:
            self.ui.urledit.setText("")
            self.ui.directoryedit.setText("")
            self.ui.filenameedit.setText("")

            self.ui.hostedit.setText("HOST:PORT")

            self.ui.timespinBox.setValue(0)

            self.ui.caption.setChecked(False)
            self.ui.merge.setChecked(False)
            self.ui.ignore_ssl_errors.setChecked(False)
            self.ui.debug.setChecked(False)
            self.ui.playlist.setChecked(False)
            self.ui.host.setChecked(False)

            self.down_list = False
            self.analysis = False
            self.ui.textBrowser.append("所有设置均已取消！\n请重新设置！")
        except Exception as e:
            self.ui.textBrowser.append(str(e))

    def fun_suspend(self, QTthread):
        """
        暂停按钮功能函数
        :param QTthread:Qt线程
        :return:
        """
        try:
            # 判断线程是否正在运行
            QTthread.terminate()
        except Exception as e:
            self.ui.textBrowser.append(str(e))

    def fun_start(self):
        """
        开始按钮功能函数
        :return:
        """

        # 改变开始下载按钮样式

        # 获取下载参数
        def get_args():

            # 先清空参数列表
            DownloadArgs.clear()

            # 获取下载参数
            # 默认自开启：
            # 自动更改重复名
            DownloadArgs.auto_renam()

            # cookie
            if self.cookie is not None:
                DownloadArgs.cookies_file(self.cookie)
            # 输出目录
            if self.directory is not None:
                DownloadArgs.output_dir(self.directory)
            # 文件名
            if self.fliename is not None:
                DownloadArgs.filename(self.fliename)

            # 超时时间
            if self.timeout is not None:
                DownloadArgs.timeout(self.timeout)

            # 输出格式
            if self.ui.format.currentText() != '默认':
                DownloadArgs.format(self.ui.format.currentText())

            # 字幕
            if self.ui.caption.isChecked() is False:
                DownloadArgs.no_caption()

            # 是否合并
            if self.ui.merge.isChecked() is False:
                DownloadArgs.no_merge()

            # 是否忽略ssl错误
            if self.ui.ignore_ssl_errors.isChecked() is False:
                DownloadArgs.ignore_ssl_errors()

            # 是否调试
            if self.ui.debug.isChecked() is True:
                DownloadArgs.debug()

            # 是否批量下载
            if self.ui.playlist.isChecked() is True:
                # 交给下载按钮事件处理参数
                self.down_list = True

            # 是否启用代理
            if self.ui.host.isChecked() is True:
                if self.ui.hostedit != "HOST:PORT":
                    DownloadArgs.http_proxy(self.ui.hostedit.text())

                else:
                    self.ui.textBrowser.append("代理选项失效：没有填写代理信息！！！\n")

        try:
            # 有url信息的情况
            if self.ui.urledit.text() != "":

                # 已经解析url的情况
                if self.analysis is True:

                    # 获取下载参数
                    get_args()

                    # 判断url是本地文件目录还是视频url地址
                    # 视频地址
                    if type(self.url) == str:
                        # 是否批量下载
                        if self.down_list is True:
                            DownloadArgs.download_list()
                            self.ui.textBrowser.append("正在开启下载！！！\n\n请耐心等候下载完毕！！！\n\n此期间你可以去干你自己的事情！！！\n\n")
                            try:
                                # 激活时的样式
                                self.ui.start.setStyleSheet(
                                    "QPushButton{background-color:rgba(100, 100, 100,0.3);color:rgb(85, 85, 85);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                                    "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                                    "QPushButton:pressed{background-color:transparent;border:1px solid red;}")

                                self.Downloader.start(DownloadArgs, self.url)
                                # 设置下载完毕提示窗口
                                # 。。。

                                self.ui.start.setStyleSheet(
                                    "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                                    "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                                    "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
                                self.ui.textBrowser.append("下载完毕！！！\n\n请开始另一视频的下载之旅，或者关闭此应用！！！\n\n")
                            except Exception as e:
                                self.ui.textBrowser.append(str(e))
                            return
                        else:
                            self.ui.textBrowser.append("正在开启下载！！！\n\n请耐心等候下载完毕！！！\n\n此期间你可以去干你自己的事情！！！\n\n")
                            try:
                                # 激活时的样式
                                self.ui.start.setStyleSheet(
                                    "QPushButton{background-color:rgba(100, 100, 100,0.3);color:rgb(85, 85, 85);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                                    "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                                    "QPushButton:pressed{background-color:transparent;border:1px solid red;}")

                                self.Downloader.start(DownloadArgs, self.url)

                                # 设置下载完毕提示窗口
                                # 。。。

                                self.ui.start.setStyleSheet(
                                    "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                                    "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                                    "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
                                self.ui.textBrowser.append("下载完毕！！！\n\n请开始另一视频的下载之旅，或者关闭此应用！！！\n\n")
                            except Exception as e:
                                self.ui.textBrowser.append(str(e))
                            return

                    # 本地目录
                    if type(self.url) == list:
                        # 是否批量下载
                        if self.down_list is True:
                            # 暂不开启多线程
                            """
                            threadtasks = list()
                            for value in self.url:
                                threadtasks.append(Thread(target=Downloader.start, args=[DownloadArgs, value]))

                            # 线程全启动
                            self.ui.textBrowser.append("正在开启下载！！！\n\n请耐心等候下载完毕！！！\n\n此期间你可以去干你自己的事情！！！\n\n")
                            for task in threadtasks:
                                task.start()

                            for task in threadtasks:
                                task.join()
                            return
                            """
                            for value in self.url:
                                try:
                                    # 激活时的样式
                                    self.ui.start.setStyleSheet(
                                        "QPushButton{background-color:rgba(100, 100, 100,0.3);color:rgb(85, 85, 85);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                                        "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                                        "QPushButton:pressed{background-color:transparent;border:1px solid red;}")

                                    self.ui.textBrowser.append("第{}个视频开始下载\n\n".format(self.url.index(value)))
                                    self.Downloader.start(DownloadArgs, value)

                                    # 设置下载完毕提示窗口
                                    # 。。。

                                    self.ui.start.setStyleSheet(
                                        "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                                        "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                                        "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
                                    self.ui.textBrowser.append(
                                        "第{}个视频下载已完毕:{}\n\n".format(self.url.index(value), value))
                                except Exception:
                                    continue
                            # 设置下载完毕提示窗口
                            # 。。。
                            self.ui.start.setStyleSheet(
                                "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                                "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                                "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
                            self.ui.textBrowser.append("全部视频已经下载完毕！！！\n\n请开始另一视频的下载之旅，或者关闭此应用！！！\n\n")
                            return
                        else:
                            self.ui.textBrowser.append("正在开启下载！！！\n\n请耐心等候下载完毕！！！\n\n此期间你可以去干你自己的事情！！！\n\n")
                            try:
                                # 激活时的样式
                                self.ui.start.setStyleSheet(
                                    "QPushButton{background-color:rgba(100, 100, 100,0.3);color:rgb(85, 85, 85);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                                    "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                                    "QPushButton:pressed{background-color:transparent;border:1px solid red;}")

                                self.Downloader.start(DownloadArgs, self.url[0])

                                # 设置下载完毕提示窗口
                                # 。。。

                                self.ui.start.setStyleSheet(
                                    "QPushButton{background-color:transparent;color:rgb(255, 85, 127);border:1px solid pink;font-family: 微软雅黑;font-size:15px;}"

                                    "QPushButton:hover{opacity:0.2;border:2px solid black;}"

                                    "QPushButton:pressed{background-color:transparent;border:1px solid red;}")
                                self.ui.textBrowser.append("下载完毕！！！\n\n请开始另一视频的下载之旅，或者关闭此应用！！！\n\n")
                            except Exception as e:
                                self.ui.textBrowser.append(str(e))
                            return

                # 没有解析url的情况（或者视频链接出错的情况）
                else:
                    self.ui.textBrowser.append("下载出错！！！\n请先解析url信息！！！\n或者查看视频url地址是否出错！！！")

            # 没有url信息的情况
            else:
                self.ui.textBrowser.append("没有url信息\n")

        except Exception as e:
            self.ui.textBrowser.append(str(e))
