import json

from flask import request, render_template, redirect, flash, url_for

from . import create_app, database
from .models import db, Soccer, User, Player, Team

app = create_app()
app.debug = True #receive better error messages

# Test database connection
@app.route('/', methods=['GET'])
def fetch():
    # cats = database.get_all(Soccer)
    # all_cats = []
    # for cat in cats:
    #     new_cat = {
    #         "id": cat.id,
    #         "name": cat.name,
    #         "price": cat.price,
    #         "breed": cat.breed
    #     }

    #     all_cats.append(new_cat)
    return render_template('home.html'), 200

###############################################################################################################
@app.route('/run', methods=['GET'])
def run():
    # session = Session()
    all_users = []
    userss = db.session.query(User).filter_by(name="Success").all()
    for u in userss:
        all_users.append(u.id)
    # session.close()
    return render_template('show_user.html', user=all_users)

@app.route('/query_goalgetter', methods=['GET'])
def query_goalgetter():
    # session = Session()
    all_users = []
    x = 0
    userss = db.session.query(Player).order_by(Player.pl_goals.desc()).all()
    # for u in userss:
    #     all_users.append(u.fname)
        # goals.append(u.)
        # print(all_users)
        # x+=1
        # x_list
    # session.close()
    return render_template('query_goalgetter.html', user=userss)

###############################################################################################################
@app.route('/index')
def Index2():
    all_data = Player.query.all()

    return render_template("index.html", user=all_data), 200


@app.route('/index2')
def Index():
    all_data = User.query.all()

    return render_template("index2.html", employees=all_data), 200

 
@app.route('/insert', methods=['POST'])
def insert():
 
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
 
        my_data = User(name, email, phone)
        db.session.add(my_data)
        db.session.commit()
 
        #database.add_instance(model=Soccer, name, email, phone)
        flash("Employee Inserted Successfully")
        return redirect(url_for('Index'))

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

#################################################################################################################

# query on all our Player data
#a = '/player'
@app.route('/player')
def Players():
    all_data = Player.query.all()
    team_data = Team.query.all()

    return render_template("player.html", employees=all_data, team=team_data), 200

@app.route('/insert_player', methods=['POST'])
def insert_player():
 
    if request.method == 'POST':
        
        fname = request.form['fname']
        lname = request.form['lname']
        pl_no = request.form['pl_no']
        nationality = request.form['nationality']
        pl_goals = request.form['pl_goals']
        team_id = request.form['team_id']
     
 
        my_data = Player(fname, lname, pl_no, nationality, pl_goals, team_id)
        db.session.add(my_data)
        db.session.commit()
 
        #database.add_instance(model=Soccer, name, email, phone)
        flash("Player Inserted Successfully")
        return redirect(url_for('Players'))

#this is our update route where we are going to update our employee
@app.route('/update_player', methods = ['GET', 'POST'])
def update_player():

    if request.method == 'POST':
        my_data = Player.query.get(request.form.get('id'))
        #fname, lname, pl_no, nationality, 
        print('yes')
        my_data.fname = request.form['fname']
        my_data.lname = request.form['lname']
        my_data.pl_no = request.form['pl_no']
        my_data.nationality = request.form['nationality']
        my_data.pl_goals = request.form['pl_goals']

 
        db.session.commit()
        #flash("Player Updated Successfully")

        return redirect(url_for('Players'))

#This route is for deleting our employee
@app.route('/delete_player/<id>/', methods = ['GET', 'POST'])
def delete_player(id):
    my_data = Player.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Player Deleted Successfully")
 
    return redirect(url_for('Players'))

###############################################################################################################

# query on all our Team data
@app.route('/team')
def Teams():
    all_data = Team.query.all()

    return render_template("team.html", employees=all_data), 200

@app.route('/insert_team', methods=['POST'])
def insert_team():

    if request.method == 'POST':
        
        team_name = request.form['team_name']
        city = request.form['city']
     
        my_data = Team(team_name, city)
        db.session.add(my_data)
        db.session.commit()
 
        #database.add_instance(model=Soccer, name, email, phone)
        flash("Player Inserted Successfully")
        return redirect(url_for('Teams'))

#this is our update route where we are going to update our employee
@app.route('/update_team', methods = ['GET', 'POST'])
def update_team():

    if request.method == 'POST':
        my_data = Team.query.get(request.form.get('id'))
    
        my_data.team_name = request.form['team_name']
        my_data.city = request.form['city']
 
        db.session.commit()
        #flash("Player Updated Successfully")

        return redirect(url_for('Teams'))

#This route is for deleting our employee
@app.route('/delete_team/<id>/', methods = ['GET', 'POST'])
def delete_team(id):
    my_data = Team.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Player Deleted Successfully")
 
    return redirect(url_for('Teams'))