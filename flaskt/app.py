# -*- coding=utf-8 -*-
import conf_app
from flask import Flask

app = Flask(__name__)
app.config.from_object(conf_app.config['production'])
conf_app.config['production'].init_app(app)

@app.route('/api')
def hello_world():
    return 'Hello, World!'

@app.route('/api/<int:id>')
def api_test(id):
    app.logger.info('api: id: %s', id)
    return "print: %d" % id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)