# -*- coding: utf-8 -*-
'''
app 的配置
'''


class Config(object):
    '''base'''

    @staticmethod
    def init_app(app):
        pass


class TestConfig(Config):

    @classmethod
    def init_app(cls, app):
        pass


class ProductionConfig(Config):
    LOG_CONF = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(process)d] [%(levelname)s] [%(module)s.%(funcName)s.%(lineno)d] %(message)s',
                'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
                'class': 'logging.Formatter'
            },

            'generic': {
                'format': '%(asctime)s [%(process)d] [%(levelname)s] [%(module)s.%(funcName)s.%(lineno)d] %(message)s',
                'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
                'class': 'logging.Formatter'
            },
        },

        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },

            'hunger': {
                'class': 'concurrent_log.ConcurrentTimedRotatingFileHandler',
                'when': 'D',
                'backupCount': 7,
                'filename': '/var/log/hunger/hunger.log',
                'encoding': 'utf-8',
                'formatter': 'generic',
            },
        },

        'root': {
            'level': 'INFO',
            'handlers': ['hunger', 'console']
        }
    }

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
                "password": "r123456",
            }
        }
    }

    @classmethod
    def init_app(cls, app):
        import logging.config
        logging.config.dictConfig(cls.LOG_CONF)

        # 初始化redis
        from datebase import redis_
        redis_.init(cls.REDIS_CONF)


config = {
    'test': TestConfig,
    'production': ProductionConfig,
}
