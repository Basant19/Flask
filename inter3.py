from flask import Flask, render_template, redirect, url_for, request, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '19991208'
app.config['MONGO_URI'] = 'mongodb+srv://Basant:<19991208>@cluster0.xin6utz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'  

mongo = PyMongo(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, username):
        self.username = username
    
    @property
    def id(self):
        return self.username

@login_manager.user_loader
def load_user(username):
    user = mongo.db.users.find_one({"username": username})
    if not user:
        return None
    return User(username=user['username'])

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')

        
        existing_user = mongo.db.users.find_one({"username": username})
        if existing_user:
            flash('Username already exists', category='danger')
        else:
           
            mongo.db.users.insert_one({'username': username, 'password': hashed_password})
            flash('Account created successfully!', category='success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = mongo.db.users.find_one({"username": username})
        if user and check_password_hash(user['password'], password):
            user_obj = User(username=user['username'])
            login_user(user_obj)
            flash('Logged in successfully!', category='success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials, please try again', category='danger')

    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome, {current_user.username}!'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', category='success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
