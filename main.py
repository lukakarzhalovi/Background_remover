from flask import Flask, request, render_template, redirect ,url_for, session
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

@app.route("/Log in",  methods = ["POST", "GET" ])
def sign_in():

    if request.method == "POST":
        mail = request.form["email"]
        password = request.form["password"]

        # აქ უნდა შეამოწმო შენს მიერ წაღებული მონაცემი ემთხვევა თუ არა აქ შეყვანილ მონაცემს"

    return render_template('Log in.html')

@app.route("/Sign up")
def sign_up():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]

        # წიე აქ უნდა დაწერო კონაცემთა ბაზას რო შექმნი მაგის კოდი რო ეს კონაცემები შეინახო ბაზაში

    return render_template('Sign up.html')

@app.route("/ImageDetection")
def Image_det():
    return render_template('ImageDetection.html')


if __name__ == "__main__":
    app.run(debug=True)