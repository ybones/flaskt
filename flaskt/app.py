# -*- coding=utf-8 -*-
import conf_app
import gevent
from flask import Flask

app = Flask(__name__)
app.config.from_object(conf_app.config['production'])
conf_app.config['production'].init_app(app)

@app.route('/api')
def hello_world():
    return 'Hello, World!'

@app.route('/api/<int:index>')
def api_test(index):
    app.logger.info('api: index: %s' % index)
    app.logger.info('geventId: %s' % id(gevent.getcurrent()))
    return "print: %d" % index

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)