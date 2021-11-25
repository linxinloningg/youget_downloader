# -*- coding:utf-8 -*-
__author__ = 'linxinloningg'

from you_get import main
import sys


# you-get下载器
class Downloader:
    def __init__(self):
        pass

    # 重构执行方法
    @staticmethod
    def start(args, url=None):
        """
        :param args:参数
        :param url: 视频地址
        :return:
        """
        if url is not None:
            args.data.append(url)
        sys.argv = args.data
        print(sys.argv)
        main()
