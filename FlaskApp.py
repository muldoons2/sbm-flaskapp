#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, url_for
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home(): return render_template('home.html')

@app.route("/index")
def index(): return render_template('index.html')

@app.route("/base")
def base(): return render_template('base.html')

@app.route("/hello_sean")
def hello_sean(): return ("Hello, Sean!")

if __name__ == "__main__":
    app.run(debug=True)
