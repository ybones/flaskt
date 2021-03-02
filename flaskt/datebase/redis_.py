# -*- coding: utf-8 -*-
import redis
from redis.sentinel import Sentinel
from redis.exceptions import (
    ConnectionError,
    DataError,
    ExecAbortError,
    NoScriptError,
    PubSubError,
    RedisError,
    ResponseError,
    TimeoutError,
    WatchError,
)

from gevent.lock import BoundedSemaphore
from flask import current_app as app


class RedisClient(object):

    def __init__(self, conf):
        self.bse = BoundedSemaphore(2)
        self.s = Sentinel([(item['host'], item['port']) for item in conf['SentinelConf']],
                          socket_timeout=0.5)
        self.conf = conf['RedisConf']
        self.conn = None
        self._initConn(self.conf)

    def _initConn(self, conf):
        with self.bse:
            if self.conn:
                self.conn.close()
            self.conn = self.s.master_for(
                conf['service_name'], **conf['db_info'])

    def execute_command(self, *args):
        try:
            cmd = args[0].lower()
            cmd_func = getattr(self.conn, cmd)
            return cmd_func(*args[1:])
        except (ConnectionError, TimeoutError) as e:
            self._initConn(self.conf)
            app.logger.error("execute_command :%s" % e)

        except Exception as e:
            app.logger.error("execute_command :%s" % e)


redisClient_ = None


def init(conf):
    global redisClient_
    redisClient_ = RedisClient(conf)
