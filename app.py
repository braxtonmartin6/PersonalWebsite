from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>This is the home page of my website! See the <a href=""http://34.211.192.188:5000/about"">second</a> here!</p>"

@app.route("/about")
def page2():
    return "<p>This is my second linked page for Unit 3.1 Assignment! Hi Dr. Jones! Go back <a href=""http://34.211.192.188:5000"">home</a>!</p>"