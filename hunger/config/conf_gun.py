# -*- coding: utf-8 -*-
"""
继承 common.config.conf_gun
详细信息 gunicorn.config
"""
import gevent.monkey

gevent.monkey.patch_all()

from common.config.conf_gun import *

# 工作进程数
workers = 4
# 进程名字
proc_name = "hunger"