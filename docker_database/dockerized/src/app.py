import json

from flask import request, render_template, redirect, flash, url_for

from . import create_app, database
from .models import db, Soccer, User, Player, Table, Title, Coach, Membership, Sponsoring, Team

app = create_app()
app.debug = True #receive better error messages

# Test database connection
@app.route('/', methods=['GET'])
def fetch():
        return render_template('home.html'), 200

###############################################################################################################
@app.route('/run', methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        name = request.form["submit_player_name"]
        #all_users = []
        data = db.session.query(Player).filter_by(lname=name).all()
        # for u in userss:
        #     all_users.append(u.id)
    return render_template('show_user.html', data=data, name=name)

@app.route('/query_goalgetter', methods=['GET'])
def query_goalgetter():
    userss = db.session.query(Player).order_by(Player.pl_goals.desc()).all()
    return render_template('query_goalgetter.html', user=userss)

###############################################################################################################
@app.route('/index')
def Index2():
    all_data = Team.query.all()

    return render_template("index.html", data=all_data), 200


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
        my_data.fname = request.form['fname']
        my_data.lname = request.form['lname']
        my_data.pl_no = request.form['pl_no']
        my_data.nationality = request.form['nationality']
        my_data.pl_goals = request.form['pl_goals']
        my_data.team_id = request.form['team_id']

 
        db.session.commit()
        flash("Player Updated Successfully")

        return redirect(url_for('Players'))

#This route is for deleting our employee
@app.route('/delete_player/<id>/', methods = ['GET', 'POST'])
def delete_player(id):
    my_data = Player.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Player Deleted Successfully")
 
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
        flash("Team Inserted Successfully")
        return redirect(url_for('Teams'))

#this is our update route where we are going to update our employee
@app.route('/update_team', methods = ['GET', 'POST'])
def update_team():

    if request.method == 'POST':
        my_data = Team.query.get(request.form.get('id'))
    
        my_data.team_name = request.form['team_name']
        my_data.city = request.form['city']
 
        db.session.commit()
        flash("Team Updated Successfully")

        return redirect(url_for('Teams'))

#This route is for deleting our employee
@app.route('/delete_team/<id>/', methods = ['GET', 'POST'])
def delete_team(id):
    my_data = Team.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Team Deleted Successfully")

    return redirect(url_for('Teams'))

#####################################################SVENS MURX#########################################
@app.route('/table')
def Tables():
    all_data = Table.query.all()
    team_data = Team.query.all()
    return render_template("table.html", data=all_data, team_data=team_data), 200

@app.route('/insert_table', methods=['POST'])
def insert_table():
 
    if request.method == 'POST':
        position_last_year = request.form['position_last_year']
        position_this_year = request.form['position_this_year']
        idx = request.form['id']
        
     
        my_data = Table(position_last_year, position_this_year, idx)
        db.session.add(my_data)
        db.session.commit()

        #database.add_instance(model=Soccer, name, email, phone)
        #flash("Table Inserted Successfully")
        return redirect(url_for('Tables'))

#this is our update route where we are going to update our employee
@app.route('/update_table', methods = ['GET', 'POST'])
def update_table():
    print("hzurray")
    if request.method == 'POST':
        my_data = Table.query.get(request.form.get('id'))

        print('yes')
        my_data.position_last_year = request.form['position_last_year']
        my_data.position_this_year = request.form['position_this_year']
 
        db.session.commit()
        #flash("Table Updated Successfully")
        print("jahuu")
        return redirect(url_for('Tables'))

#This route is for deleting our employee
@app.route('/delete_table/<id>/', methods = ['GET', 'POST'])
def delete_table(id):
    my_data = Table.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Player Deleted Successfully")
 
    return redirect(url_for('Tables'))

@app.route('/title')
def Titles():
    all_data = Title.query.all()
    team_data = Team.query.all()

    return render_template("title.html", data=all_data, team=team_data), 200

@app.route('/insert_title', methods=['POST'])
def insert_title():
 
    if request.method == 'POST':
        year = request.form['year']
        title = request.form['title']
        winning_team = request.form['winning_team']
     
        my_data = Title(year, title, winning_team)
        db.session.add(my_data)
        db.session.commit()

        #database.add_instance(model=Soccer, name, email, phone)
        flash("Table Inserted Successfully")
        return redirect(url_for('Titles'))

#this is our update route where we are going to update our employee
@app.route('/update_title', methods = ['GET', 'POST'])
def update_title():
    if request.method == 'POST':
        my_data = Title.query.get(request.form.get('year'))

        my_data.year = request.form['year']
        my_data.title = request.form['title']
        my_data.winning_team = request.form['winning_team']
 
        db.session.commit()
        flash("Table Updated Successfully")
        return redirect(url_for('Titles'))

#This route is for deleting our employee
@app.route('/delete_title/<year>/', methods = ['GET', 'POST'])
def delete_title(year):
    my_data = Title.query.get(year)
    db.session.delete(my_data)
    db.session.commit()
    flash("Player Deleted Successfully")
 
    return redirect(url_for('Titles'))

@app.route('/coach')
def Coachs():
    all_data = Coach.query.all()

    return render_template("coach.html", data=all_data), 200

@app.route('/insert_coach', methods=['POST'])
def insert_coach():
 
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        nationality = request.form['nationality']
        idx = request.form['id']
     
        my_data = Coach(idx, first_name, last_name, nationality)
        db.session.add(my_data)
        db.session.commit()

        flash("Table Inserted Successfully")
        return redirect(url_for('Coachs'))

#this is our update route where we are going to update our employee
@app.route('/update_coach', methods = ['GET', 'POST'])
def update_coach():
    print("hzurray")
    if request.method == 'POST':
        my_data = Coach.query.get(request.form.get('id'))
       
        my_data.first_name = request.form['first_name']
        my_data.last_name = request.form['last_name']
        my_data.nationality = request.form['nationality']
 
        db.session.commit()
        flash("Table Updated Successfully")
     
        return redirect(url_for('Coachs'))

#This route is for deleting our employee
@app.route('/delete_coach/<id>/', methods = ['GET', 'POST'])
def delete_coach(id):
    my_data = Coach.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Player Deleted Successfully")
 
    return redirect(url_for('Coachs'))

@app.route('/membership')
def Memberships():
    all_data = Membership.query.all()

    return render_template("membership.html", data=all_data), 200

@app.route('/insert_membership', methods=['POST'])
def insert_membership():
 
    if request.method == 'POST':
        number_members = request.form['number_members']
        some_id = request.form['id']

     
        my_data = Membership(number_members, some_id)
        db.session.add(my_data)
        db.session.commit()

        flash("Table Inserted Successfully")
        return redirect(url_for('Memberships'))

#this is our update route where we are going to update our employee
@app.route('/update_membership', methods = ['GET', 'POST'])
def update_membership():
    if request.method == 'POST':
        my_data = Membership.query.get(request.form.get('id'))

        my_data.number_members = request.form['number_members']
 
        db.session.commit()
        flash("Table Updated Successfully")
        return redirect(url_for('Memberships'))

#This route is for deleting our employee
@app.route('/delete_membership/<id>/', methods = ['GET', 'POST'])
def delete_membership(id):
    my_data = Membership.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Player Deleted Successfully")
 
    return redirect(url_for('Memberships'))

@app.route('/sponsoring')
def Sponsorings():
    all_data = Sponsoring.query.all()
    team_data = Team.query.all()

    return render_template("sponsoring.html", data=all_data, team=team_data), 200

@app.route('/insert_sponsoring', methods=['POST'])
def insert_sponsoring():
 
    if request.method == 'POST':
        start_date = request.form['start_date']
        sponsor_name = request.form['sponsor_name']
        team_id = request.form['team_id']
     
        my_data = Sponsoring(start_date, sponsor_name, team_id)
        db.session.add(my_data)
        db.session.commit()

        #database.add_instance(model=Soccer, name, email, phone)
        flash("Table Inserted Successfully")
        return redirect(url_for('Sponsorings'))

#this is our update route where we are going to update our employee
@app.route('/update_sponsoring', methods = ['GET', 'POST'])
def update_sponsoring():
    print("hzurray")
    if request.method == 'POST':
        my_data = Sponsoring.query.get(request.form.get('id'))

        my_data.start_date = request.form['start_date']
        my_data.sponsor_name= request.form['sponsor_name']
        my_data.team_id = request.form['team_id']
 
        db.session.commit()
        flash("Table Updated Successfully")
        return redirect(url_for('Sponsorings'))

#This route is for deleting our employee
@app.route('/delete_sponsoring/<id>/', methods = ['GET', 'POST'])
def delete_sponsoring(id):
    my_data = Sponsoring.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Player Deleted Successfully")

    return redirect(url_for('Sponsorings'))
