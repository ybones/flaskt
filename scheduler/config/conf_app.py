# -*- coding: utf-8 -*-
'''
app 的配置
'''


class Config(object):
    '''base'''
    PROJECT_NAME = "scheduler"

    @classmethod
    def init_app(cls, app):
        pass


class TestConfig(Config):

    @classmethod
    def init_app(cls, app):
        pass


class ProductionConfig(Config):
    REDIS_CONF = {
        "SentinelConf": [{
            "host": "redis-sentinel-1",
            "port": 16379,
        }, {
            "host": "redis-sentinel-2",
            "port": 16379,
        }, {
            "host": "redis-sentinel-3",
            "port": 16379,
        }],

        # 暂时先不分库了。
        "RedisConf": {
            "service_name": "mymaster",
            "db_info": {
                "db": 1,
                "password": "123456",
            }
        }
    }

    @classmethod
    def init_app(cls, app):
        import logging.config
        from common.config import conf_log
        log_conf = conf_log.get_log_conf(cls.PROJECT_NAME)
        logging.config.dictConfig(log_conf)

        # 初始化redis
        from common.datebase import redis_
        redis_.init(app, cls.REDIS_CONF)


config = {
    'test': TestConfig,
    'production': ProductionConfig,
}
