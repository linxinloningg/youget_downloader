# -*- coding:utf-8 -*-
__author__ = 'linxinloningg'


class DownloadArgs:
    """
    下载参数
    """

    def __init__(self):
        self.data = list()
        self.data.append('you_get')

    def clear(self):
        """
        清空已有参数
        :return:
        """
        self.data = list()
        self.data.append('you_get')

    def no_merge(self):
        """
        不合并
        :return:
        """
        self.data.append('--no-merge')
        return self

    def no_caption(self):
        """
        不下载字幕
        :return:
        """
        self.data.append('--no-caption')
        return self

    def force(self):
        """
        强制覆盖已存在文件
        :return:
        """
        self.data.append('--force')
        return self

    def skip(self):
        """
        跳过已存在文件的大小检查
        :return:
        """
        self.data.append('--skip-existing-file-size-check')
        return self

    def format(self, stream_id):
        """
        指定下载格式 可选不同清晰度，需要--info 先查看有那些格式
        :param stream_id: 视频格式，如flv，MP4
        :return:
        """
        self.data.append('--format=' + stream_id)
        return self

    def filename(self, filename):
        """
        指定文件名：不用加后缀如.mp4
        :param filename: 文件名
        :return:
        """
        self.data.append('--output-filename')
        self.data.append(filename)
        return self

    def output_dir(self, output_dir):
        """
        指定目录输出目录
        :param output_dir: 文件目录，例子：output_dir='D:\test'
        :return:
        """
        self.data.append('--output-dir')
        self.data.append(output_dir)
        return self

    def player(self, player):
        """
        指定播放器
        :param player: 已下载播放器,如vlc（多见于linus系统使用）
        :return:
        """
        self.data.append('--player')
        self.data.append(player)
        return self

    def cookies_file(self, cookies_file):
        """
        指定cookies file
        :param cookies_file:
        :return:
        """
        self.data.append('--cookies')
        self.data.append(cookies_file)
        return self

    def timeout(self, seconds):
        """
        设置连接 timeout
        :param seconds:
        :return:
        """
        self.data.append('--timeout')
        self.data.append(seconds)
        return self

    def debug(self):
        """
        开启调试
        :return:
        """
        self.data.append('--debug')
        return self

    def input_file(self, input_file):
        """
        获取input_file文件的所有url
        :param input_file: 本地urls.txt文件路径
        :return:
        """
        self.data.append('--input-file')
        self.data.append(input_file)
        return self

    def password(self, password):
        """
        “视频访问密码”设置为“密码”
        :param password:
        :return:
        """
        self.data.append('--password')
        self.data.append(password)
        return self

    def download_list(self):
        """
        下载列表里的视频
        :return:
        """
        self.data.append('--playlist')
        return self

    def auto_renam(self):
        """
        对拥有相同名字的不同文件自动重命名
        :return:
        """
        self.data.append('--auto-rename')

    def ignore_ssl_errors(self):
        """
        忽略ssl错误
        :return:
        """
        self.data.append('--insecure')
        return self

    def http_proxy(self, host):
        """
        下载使用的代理host
        :param host:  HOST:PORT
        :return:
        """
        self.data.append('--http-proxy')
        self.data.append(host)
        return self

    def sock5_proxy(self, host):
        """
        sock5代理
        :param host:HOST:PORT or USERNAME:PASSWORD@HOST:PORT
        :return:
        """
        self.data.append('--socks-proxy')
        self.data.append(host)
        return self

    def no_proxy(self):
        """
        无代理
        :return:
        """
        self.data.append('--no-proxy')
        return self


class DryRunArgs:
    """
    预运行参数
    """

    def __init__(self):
        self.data = list()
        self.data.append('you_get')

    def clear(self):
        """
        清空已有参数
        :return:
        """
        self.data = list()
        self.data.append('you_get')

    def info(self):
        """
        打印提取的信息
        :return:
        """
        self.data.append('--info')
        return self

    def url_info(self):
        """
        打印提取的信息与url
        :return:
        """
        self.data.append('--url')
        return self

    def json(self):
        """
        以JSON格式打印提取的URL
        :return:
        """
        self.data.append('--json')
        return self

    def proxy(self, host):
        """
        代理
        :param host: HOST:PORT
        :return:
        """
        self.data.append('--extractor-proxy')
        self.data.append(host)
        return self


class OptionalArgs:
    """
    选项信息
    """

    def __init__(self):
        self.data = list()
        self.data.append('you_get')

    def clear(self):
        """
        清空已有参数
        :return:
        """
        self.data = list()
        self.data.append('you_get')

    def version(self):
        """
        版本信息
        :return:
        """
        self.data.append('--version')

    def help(self):
        """
        帮助信息
        :return:
        """
        self.data.append('--help')
