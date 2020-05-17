from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

############################################################
#### This part is related to creating a Database, which is not complete
#### Video instructions are here: https://www.youtube.com/watch?v=Z1RJmh_OqeA
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
# class todo(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Integer, default=0)
#     date_created = db.Column(db.DateTime, default = datetime.utcnow)
# def __repr__(self):
#     return '<task %r>' % self.id
############################################################
    
@app.route("/")
def home(): return render_template('home.html')

@app.route("/index")
def index(): return render_template('index.html')

@app.route("/base")
def base(): return render_template('base.html')

@app.route("/hello_sean")
def hello_sean(): return ("Hello, Sean!")

if __name__ == "__main__":
    app.run(host='localhost',port=5000)
#     app.run(host='localhost',port=5000,debug=True)
