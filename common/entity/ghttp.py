# -*- coding: utf-8 -*-
import logging

from geventhttpclient import HTTPClient
from geventhttpclient.header import Headers
from geventhttpclient.url import URL

from common.entity import gtools

logger = logging.getLogger()
FORM_HEADERS = {"Content-type": "application/x-www-form-urlencoded"}
OTC_HEADERS = {"Content-type": "application/octet-stream"}
JSON_HEADERS = {"Content-type": "application/json;charset=utf8"}


def queryHttp(method: str, url: str, header=None, body="", connection_timeout=6, try_count=3):
    """

    :param method: "GET" or "POST"
    :param url: url地址
    :param header: 请求头信息
    :param body:
    :param connection_timeout:
    :param try_count:
    :return:
    code:http状态码, page：body内容
    """
    # method处理
    method = method.upper()

    # header处理
    if not header:
        header = JSON_HEADERS
    _header = Headers(header)

    # url处理
    _url = URL(url)

    try_count = int(try_count) if try_count else 1
    for i in range(try_count):
        try:
            _http = HTTPClient(_url.host, connection_timeout=connection_timeout)

            _response = _http.request(method, _url.request_uri, body, _header)

            if _response:
                return _response.status_code, _response.read().decode('utf-8')

        except Exception as e:
            logging.error(e, exc_info=True)
        finally:
            _http.close()


def sendHttp(method: str, url: str, header=None, body="", connection_timeout=6, try_count=3):
    """
    异步请求
    """

    def _query():
        queryHttp(method, url, header, body, connection_timeout, try_count)

    gtools.go_delay_func(0.01, _query)
