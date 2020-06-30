import os
from flask import Flask, render_template, url_for
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

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
