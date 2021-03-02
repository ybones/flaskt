# -*- coding: utf-8 -*-
from datebase import redis_ 


def queryRedisCmd(*args):
    return redis_.redisClient_.execute_command(*args)