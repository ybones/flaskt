# -*- coding: utf-8 -*-

import logging

import gevent

from common.datebase import redis_

logger = logging.getLogger()


def query_redis_cmd(*args):
    """
    同步接口
    """
    return redis_.g_redis_client.execute_command(*args)


def send_redis_cmd(*args):
    """
    异步接口
    """

    def send():
        redis_.g_redis_client.execute_command(*args)

    gevent.spawn(send)
    gevent.sleep(0)
