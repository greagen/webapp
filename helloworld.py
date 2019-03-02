#!/usr/bin/env python
#encoding=utf-8

from flask import Flask
from flask import render_template
from flask import request
import sys


app = Flask(__name__)

reload(sys)
sys.setdefaultencoding("utf-8")


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        save(data)
        return 'ok'
    else:
        return render_template('index.html')


def save(data):
    pass


if __name__ == '__main__':
    app.run(debug=True)
    