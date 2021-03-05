# -*- coding: utf-8 -*-
"""
详细信息 gunicorn.config
"""
import gevent.monkey

gevent.monkey.patch_all()

import platform

# 工作进程数
workers = 1

# 使用的工作模型（: 可自定义
# 提供的工作模型 sync Eventlet Gevent tornado gthread
worker_class = 'gevent'

# 每个进程的并发量, 只用于 eventlet and gevent 两种模式下
worker_connections = 1000

# 重新启动之前，工作将处理的最大请求数。默认值为0
max_requests = 0

# 要添加到max_requests的最大抖动。
# 抖动将导致每个工作的重启被随机化，这是为了避免所有workers进程被重启。
max_requests_jitter = 0

# 超过后worker将被杀掉，并重新启动。
timeout = 60

# 接收到restart信号后，worker可以在graceful_timeout时间内，
# 继续处理完当前requests。
graceful_timeout = 30

# 监听内网端口5000
bind = "0.0.0.0:5000"

# True：在master work 加载app
# False: 只有子进程会加载 app
preload_app = False

# 进程名字
proc_name = "scheduler"

# 设置访问日志和错误信息日志路径
_sys = platform.system()
if _sys == "Windows":
    pass
if _sys == "Darwin":
    accesslog = "./log/gun/access.log"
    errorlog = "./log/gun/error.log"
else:
    accesslog = "/var/log/gun/access.log"
    errorlog = "/var/log/gun/error.log"

# 参考 gunicorn.config.AccessLogFormat
access_log_format = '[%(h)s] [%(u)s] [%(r)s] [%(s)s] [%(b)s] [%(f)s] [%(a)s] [%(D)s]'

logconfig_dict = dict(
    version=1,
    disable_existing_loggers=False,

    root={"level": "INFO", "handlers": ["console"]},
    loggers={
        "gunicorn.error": {
            "level": "DEBUG",
            "handlers": ["error_console"],
            "propagate": False,  # 其默认是为1，表示消息将会传递给高层次logger的handler，通常我们需要指定其值为0
            "qualname": "gunicorn.error"  # 返回当前对象的所有父级对象的名称
        },

        "gunicorn.access": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
            "qualname": "gunicorn.access"
        }
    },
    handlers={
        "console": {
            "class": "concurrent_log.ConcurrentTimedRotatingFileHandler",
            "when": "D",
            "backupCount": 7,
            "filename": accesslog,
            'encoding': 'utf-8',
            "formatter": "generic"
        },
        "error_console": {
            "class": "concurrent_log.ConcurrentTimedRotatingFileHandler",
            "when": "D",
            "backupCount": 7,
            "filename": errorlog,
            'encoding': 'utf-8',
            "formatter": "generic"
        },
    },
    formatters={
        "generic": {
            "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        }
    }
)
