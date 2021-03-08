# -*- coding: utf-8 -*-
import functools
import logging
import sys
import traceback

import gevent

logger = logging.getLogger()


def on_panic(etype, value, tb):
    logging.critical(traceback.format_exception(etype, value, tb))


def go_func(func, *args, **kwargs):
    """生成一个Greenlet
    """

    def safe_wrap(f):
        try:
            f(*args, **kwargs)
        except:
            on_panic(*sys.exc_info())

    gevent.spawn(safe_wrap, func)


def go_delay_func(delay, func, *args, **kwargs):
    """延迟生成一个Greenlet
    :param delay: 延迟时间
    :param func: 延迟函数
    """

    def safe_wrap(f):
        try:
            f(*args, **kwargs)
        except:
            on_panic(*sys.exc_info())

    gevent.spawn_later(delay, safe_wrap, func)


def async_func(func):
    """gevent异步装饰器 ：）
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        go_func(func, *args, **kwargs)

    return wrapper
