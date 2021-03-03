# -*- coding: utf-8 -*-
from flask import current_app
from gevent.lock import BoundedSemaphore
from redis.exceptions import (
    ConnectionError,
    TimeoutError,
)
from redis.sentinel import Sentinel


class RedisClient(object):

    def __init__(self, conf):
        self.bse = BoundedSemaphore(2)
        self.s = Sentinel([(item['host'], item['port']) for item in conf['SentinelConf']],
                          socket_timeout=1)
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
            current_app.logger.error("execute_command :%s" % e)

        except Exception as e:
            current_app.logger.error("execute_command :%s" % e)


redisClient_ = None


def init(app, conf):
    global redisClient_
    redisClient_ = RedisClient(conf)
    app.logger.info("redis init success :%s" % redisClient_.s)
