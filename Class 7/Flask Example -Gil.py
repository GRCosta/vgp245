# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:28:55 2018

@author: grcosta
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

