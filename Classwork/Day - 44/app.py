# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    @app.route('/hello', methods=['GET'])
    def hello():
        return "hello"
    app.run(host='0.0.0.0', debug=True, port=5000)
