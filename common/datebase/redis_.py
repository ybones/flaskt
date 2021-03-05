# -*- coding: utf-8 -*-
import logging

from gevent.lock import BoundedSemaphore
from redis import StrictRedis
from redis.exceptions import (
    ConnectionError,
    TimeoutError,
)
from redis.sentinel import Sentinel

logger = logging.getLogger()


class RedisClient(object):

    def __init__(self, conf):
        self.bse = BoundedSemaphore(1)
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
            result = cmd_func(*args[1:])
            if result is None:
                return result
            elif isinstance(result, bytes):
                result = result.decode("utf-8")
                return result
            else:
                return result
        except (ConnectionError, TimeoutError) as e:
            self._initConn(self.conf)
            logger.error("execute_command :%s" % e)

        except Exception as e:
            logger.error("execute_command :%s" % e)


class RedisClientTest(object):
    def __init__(self, conf):
        self.conf = conf['RedisConf']
        self.conn = None
        self._initConn(self.conf)

    def _initConn(self, conf):
        self.conn = StrictRedis(host=conf['host'], port=conf['port'], password=conf['password'],
                                db=conf['db'])

    def execute_command(self, *args):
        try:
            cmd = args[0].lower()
            cmd_func = getattr(self.conn, cmd)
            logger.info("execute_command cmd:[" + " ".join(str(i) for i in args) + "]")
            result = cmd_func(*args[1:])
            if result is None:
                return result
            elif isinstance(result, bytes):
                result = result.decode("utf-8")
                return result
            else:
                return result
        except (ConnectionError, TimeoutError) as e:
            self._initConn(self.conf)
            logger.error("execute_command :%s" % e)

        except Exception as e:
            logger.error("execute_command :%s" % e)


g_redis_client = None


def init(app, conf):
    global g_redis_client
    g_redis_client = RedisClient(conf)
    app.logger.info("redis init success :%s" % g_redis_client)
    app.logger.info("redis init success :%s" % g_redis_client.conn)
    app.logger.info("redis init success :%s" % g_redis_client.conn.ping())


def init_test(app, conf):
    global g_redis_client
    g_redis_client = RedisClientTest(conf)
    app.logger.info("redis init success :%s" % g_redis_client)
    app.logger.info("redis init success :%s" % g_redis_client.conn)
    app.logger.info("redis init success :%s" % g_redis_client.conn.ping())
