# -*- coding: utf-8 -*-
import functools
import time

import gevent


def async_func(func):
    """gevent异步装饰器
    不会立马执行，但确实是异步的 ：）
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        gevent.spawn(func, *args, **kwargs)

    return wrapper


def async_switch_func(func):
    """gevent异步装饰器
    会立马执行，手动切换了协程 ：）
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        gevent.spawn(func, *args, **kwargs)
        gevent.sleep()
    return wrapper
