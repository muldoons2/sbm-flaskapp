import os
import requests
from flask import Flask, render_template, url_for
from datetime import datetime
app = Flask(__name__)

# def ye_says():
#     a = """{% extends 'base.html' %}
#     {% block head %}
#     <h3>Kanye says:</h3>
#     {% endblock %}
#     {% block body %}"""
#     b = "{% endblock %}"
#     c = a+requests.get("https://api.kanye.rest").json()['quote']+b
#     f = open('templates/kanye2.html', 'w+')
#     f.write(c)

@app.route("/")
def home(): return render_template('home.html')

@app.route("/index")
def index(): return render_template('index.html')

@app.route("/base")
def base(): return render_template('base.html')

@app.route("/kanye2")
def kanye2():
    return render_template('kanye.html')

@app.route("/kanye")
def kanye(): return """<!DOCTYPE html>
<html lang="en">
<head>
		<title>SBM FlaskApp</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="static/css/main.css">
	</head>
	<body>

		<!-- Header -->
			<header id="header">
				<a href="index.html" class="logo"><strong>MuldoonAds</strong></a>
				<nav>
					<a href="#menu">Menu</a>
				</nav>
			</header>
	<!-- Nav -->
			<nav id="menu">
				<ul class="links">
					<li><a href="index.html">Home</a></li>
					<li><a href="generic.html">Generic</a></li>
					<li><a href="elements.html">Elements</a></li>
				</ul>
			</nav


<!-- Main -->
			<section id="main">
				<div class="inner">
				
					
					<h1>Kanye Says:</h1>
    
					<header>""" + requests.get("https://api.kanye.rest").json()['quote'] + """</div>
			</section>

<!-- Footer -->
			<footer id="footer">
<!-- 				<ul class="icons">
					<li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
					<li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
					<li><a href="#" class="icon fa-instagram"><span class="label">Instagram</span></a></li>
				</ul> -->
				<div class="copyright">
					<a href="https://muldoonadvertising.com/">&copy;Sean Muldoon 2020</a> </a>
				</div>
			</footer>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

</body>
</html>"""

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# Credits: https://kanye.rest/
