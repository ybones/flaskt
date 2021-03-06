# -*- coding: utf-8 -*-

def get_log_conf(projectname):
    _conf = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(process)d.%(thread)d] [%(levelname)s] [%(module)s.%(funcName)s.%(lineno)d] %(message)s',
                'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
                'class': 'logging.Formatter'
            },

            'generic': {
                'format': '%(asctime)s [%(process)d.%(thread)d] [%(levelname)s] [%(module)s.%(funcName)s.%(lineno)d] %(message)s',
                'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
                'class': 'logging.Formatter'
            },
        },

        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },

            'filelog': {
                'class': 'concurrent_log.ConcurrentTimedRotatingFileHandler',
                'when': 'D',
                'backupCount': 7,
                'filename': f'/var/log/{projectname}/{projectname}.log',
                'encoding': 'utf-8',
                'formatter': 'generic',
            },
        },

        'root': {
            'level': 'INFO',
            'handlers': ['filelog', 'console']
        }
    }
    return _conf