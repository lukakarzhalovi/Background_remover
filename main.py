from flask import Flask, Request, render_template, redirect ,url_for
from flask_sqlalchemy import SQLAlchemy
from API import API_remove

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/Log in")
def sign_in():
    return render_template('Log in.html')

@app.route("/Sign up")
def sign_up():
    return render_template('Sign up.html')

@app.route("/ImageDetection")
def Image_det():
    return render_template('ImageDetection.html')


if __name__ == "__main__":
    app.run(debug=True)