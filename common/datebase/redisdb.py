# -*- coding: utf-8 -*-

from common.datebase import redis_
from common.entity.gtools import async_func


def query_redis_cmd(*args):
    """
    同步接口
    """
    return redis_.g_redis_client.execute_command(*args)


@async_func
def send_redis_cmd(*args):
    """
    异步接口
    """
    redis_.g_redis_client.execute_command(*args)
