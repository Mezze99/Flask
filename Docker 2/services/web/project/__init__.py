from flask import Flask, jsonify, render_template, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from project.forms import LoginForm
from project.config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    #__tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    #active = db.Column(db.Boolean(), default=True, nullable=False)
    phone = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def __init__(self, email, name, phone):
        self.email = email
        self.name = name
        self.phone = phone


class Player(db.Model):
    #__tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(128), unique=True, nullable=False)
    lname = db.Column(db.String(100))
    pl_no = db.Column(db.Integer)
    nationality = db.Column(db.String(100))
    pl_goals = db.Column(db.Integer)

    def __init__(self, fname, lname, pl_no, nationality, pl_goals):
        self.fname = fname
        self.lname = lname
        self.pl_no = pl_no
        self.nationality = nationality
        self.pl_goals = pl_goals

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return '<Post {}>'.format(self.body)


@app.route("/")
def hello_world():
    return jsonify(hello="worldzzz")


@app.route('/index')
def index():
    user = {'username': 'Tim'}
    all_data = User.query.all()
    return render_template('index.html', title='Home', user=user, employees=all_data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


#  this route is for inserting data to mysql database via html forms
@app.route('/insert', methods=['POST'])
def insert():
 
    if request.method == 'POST':
 
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
 
        my_data = User(name, email, phone)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Employee Inserted Successfully")
 
        return redirect(url_for('Index'))


# query on all our employee data
@app.route('/index2')
def Index():
    all_data = User.query.all()

    return render_template("index2.html", employees=all_data)

# query on all our employee data
a = '/player'
@app.route(a)
def Players():
    all_data = Player.query.all()

    return render_template("player.html", employees=all_data)


#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = User.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
 
        db.session.commit()
        flash("Employee Updated Successfully")
 
        return redirect(url_for('Index'))

#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = User.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
 
    return redirect(url_for('Index'))