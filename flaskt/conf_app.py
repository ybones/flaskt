# -*- coding: utf-8 -*-
'''
app 的配置
'''

class Config(object):
    '''base'''
    @staticmethod
    def init_app(app):
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

            'flaskt': {
                'class': 'concurrent_log.ConcurrentTimedRotatingFileHandler',
                'when': 'D',
                'backupCount': 7,
                'filename': '/var/log/flaskt/flask.log',
                'encoding': 'utf-8',
                'formatter': 'generic',
            },
        },

        'root': {
            'level': 'DEBUG',
            'handlers': ['flaskt', 'console']
        }
    }

    @classmethod
    def init_app(cls, app):
        import logging
        import logging.config
        logging.config.dictConfig(cls.LOG_CONF)


config = {
    'production': ProductionConfig,
}
