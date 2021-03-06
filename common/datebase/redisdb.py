# -*- coding: utf-8 -*-

import logging

import gevent

from common.datebase import redis_
from common.entity.util import async_func, async_switch_func

logger = logging.getLogger()


def query_redis_cmd(*args):
    """
    同步接口
    """
    return redis_.g_redis_client.execute_command(*args)


@async_switch_func
def send_redis_cmd(*args):
    """
    异步接口
    """
    redis_.g_redis_client.execute_command(*args)
