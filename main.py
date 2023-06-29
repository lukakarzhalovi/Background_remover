from flask import Flask, request, render_template, redirect ,url_for, session,flash
from flask_sqlalchemy import SQLAlchemy
from API import API_remove
from image_detection import object_detenction_on_image
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user,logout_user,login_required,current_user
import shutil
import re



api = API_remove
app = Flask(__name__)
app.secret_key = 'user_secret_key'
app.config['SQLALCHEMY_BINDS'] = {'users': 'sqlite:///usersdatabse.db'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usersdatabse.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email


    def is_active(self):
        return True
      
@login_manager.user_loader
def load_users(user_id):
    return User.query.get(int(user_id))

db.create_all()

@app.route("/" ,  methods = ["POST", "GET" ])
@app.route("/home" ,  methods = ["POST", "GET" ])
def home():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            # შევინახოთ დროებით ლოკაციაზე
            image_path = 'static/uploaded_image.png'
            image.save(image_path)

            #ეიპიასი მეშვეობთ ამოვჭრათ სურათის ბექგრაუნდი
            api_key = "Vs5BJEfznmo4cdZ9cJP9EZ2M"
            result_image_path = api.remove_background(image_path, api_key)

            # შევინახოთ აწ უკვე ამოჭრილი ფოტო სადაც გვინდა
            shutil.move(result_image_path, "static/result.png")

            return render_template("b_remove.html")
    
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/Log in",  methods = ["POST", "GET" ])
def sign_in():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]


        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Invalid email or password', 'error')
            return redirect(url_for('sign_in'))

        # Check if the password is correct
        if not check_password_hash(user.password, password):
            flash('Invalid email or password', 'error')
            return redirect(url_for('sign_in'))
   
        session['username'] = user.email
        return redirect(url_for('home'))
    
    return render_template('Log in.html')

@app.route("/Sign up", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
            flash('Password must be at least 8 characters long and contain at least one uppercase letter and one digit', 'error')
            return redirect(url_for('sign_up'))
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('use another email', 'error')
            return redirect(url_for('sign_up'))
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, password=hashed_password, email=email)
        
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('Log in'))

    return render_template('Sign up.html')

@app.route("/ImageDetection",methods=["POST", "GET"])
def Image_det():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            image_path = 'static/uploaded_image.png'
            image.save(image_path)
            object_detenction_on_image()
            return render_template('detection.html')

    return render_template('ImageDetection.html')

@app.route("/log out")
def log_out():
    session.pop('username', None)
    return render_template('home.html')



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)