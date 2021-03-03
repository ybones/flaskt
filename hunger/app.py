# -*- coding=utf-8 -*-
import logging

from flask import Flask

import conf_app
from datebase import redisdb

app = Flask(__name__)

env = "production"
app.config.from_object(conf_app.config[env])
conf_app.config[env].init_app(app)

logger = logging.getLogger()


@app.route('/api')
def hello_world():
    return 'Hello, World!'


@app.route('/api/<int:index>')
def api_test(index):
    redisdb.send_redis_cmd("set", "index", index)
    r_index = redisdb.query_redis_cmd("get", "index")
    logger.info("api test get %s" % r_index)
    return "print: %d %s" % (index, r_index)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
