#!/usr/bin/env python3
import os
from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

x = []

@app.route("/")
def home(): return render_template('home.html')

@app.route("/index")
def index(): return render_template('index.html')

@app.route("/base")
def base(): return render_template('base.html')

@app.route("/hello_sean")
def hello_sean(): return ("Hello, Sean!")

# @app.route("/register", methods=["POST"])
# def register():
#     fname = request.form.get("fname")
#     lname = request.form.get("lname")
#     y = [{fname},{lname}]
#     x.append(y)
#     return (x)

@app.route("/success")
def success(): 
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    return render_template('success.html', fname=fname, lname=lname)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
