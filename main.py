from flask import Flask, Request, render_template, redirect ,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/sign_in")
def sign_in():
    return render_template('sign_in.html')

@app.route("/sign_up")
def sign_up():
    return render_template('sign_up.html')


if __name__ == "__main__":
    app.run(debug=True)