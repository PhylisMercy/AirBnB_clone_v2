#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 9 8:48:00 2023

@author: Phylis Mercy
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
