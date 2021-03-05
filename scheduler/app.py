# -*- coding=utf-8 -*-
import logging

from flask import Flask

from scheduler.config import conf_app
from common.datebase import redisdb

app = Flask(__name__)

env = "production"
app.config.from_object(conf_app.config[env])
conf_app.config[env].init_app(app)

logger = logging.getLogger()
