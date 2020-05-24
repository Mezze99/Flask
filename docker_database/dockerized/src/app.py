import json

from flask import request, render_template, redirect, flash, url_for

from . import create_app, database
from .models import db, Soccer, User, Player, Table, Title, Coach, Membership, Sponsoring

app = create_app()
app.debug = True #receive better error messages

# Test database connection
@app.route('/', methods=['GET'])
def fetch():
    cats = database.get_all(Soccer)
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed
        }

        all_cats.append(new_cat)
    return json.dumps(all_cats), 200

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
    #x = 0
    userss = db.session.query(Player).order_by(Player.pl_goals).all()
    for u in userss:
        all_users.append(u.fname)
        print(all_users)
        # x+=1
        # x_list
    # session.close()
    return render_template('query_goalgetter.html', user=all_users)


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    database.add_instance(Soccer, name=name, price=price, breed=breed)
    return json.dumps("Added"), 200


@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    database.delete_instance(Soccer, id=cat_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Soccer, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200

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

# query on all our employee data
#a = '/player'
@app.route('/player')
def Players():
    all_data = Player.query.all()

    return render_template("player.html", employees=all_data), 200

@app.route('/insert_player', methods=['POST'])
def insert_player():
 
    if request.method == 'POST':
        
        fname = request.form['fname']
        lname = request.form['lname']
        pl_no = request.form['pl_no']
        nationality = request.form['nationality']
        pl_goals = request.form['pl_goals']
     
 
        my_data = Player(fname, lname, pl_no, nationality, pl_goals)
        db.session.add(my_data)
        db.session.commit()
 
        #database.add_instance(model=Soccer, name, email, phone)
        flash("Player Inserted Successfully")
        return redirect(url_for('Players'))

#this is our update route where we are going to update our employee
@app.route('/update_player', methods = ['GET', 'POST'])
def update_player():
    print("hzurray")
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
        print("jahuu")
        return redirect(url_for('Players'))

#This route is for deleting our employee
@app.route('/delete_player/<id>/', methods = ['GET', 'POST'])
def delete_player(id):
    my_data = Player.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Player Deleted Successfully")
 
    return redirect(url_for('Players'))

#####################################################SVENS MURX#########################################
@app.route('/table')
def Tables():
    all_data = Table.query.all()

    return render_template("table.html", data=all_data), 200

@app.route('/insert_table', methods=['POST'])
def insert_table():
 
    if request.method == 'POST':
        position_last_year = request.form['position_last_year']
        position_this_year = request.form['position_this_year']
     
        my_data = Table(position_last_year, position_this_year)
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
    #flash("Player Deleted Successfully")
 
    return redirect(url_for('Tables'))

@app.route('/title')
def Titles():
    all_data = Title.query.all()

    return render_template("title.html", data=all_data), 200

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
        #flash("Table Inserted Successfully")
        return redirect(url_for('Titles'))

#this is our update route where we are going to update our employee
@app.route('/update_title', methods = ['GET', 'POST'])
def update_title():
    print("hzurray")
    if request.method == 'POST':
        my_data = Title.query.get(request.form.get('year'))

        print('yes')
        my_data.year = request.form['year']
        my_data.title = request.form['title']
        my_data.winning_team = request.form['winning_team']
 
        db.session.commit()
        #flash("Table Updated Successfully")
        print("jahuu")
        return redirect(url_for('Titles'))

#This route is for deleting our employee
@app.route('/delete_title/<year>/', methods = ['GET', 'POST'])
def delete_title(year):
    my_data = Title.query.get(year)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Player Deleted Successfully")
 
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
     
        my_data = Coach(first_name, last_name, nationality)
        db.session.add(my_data)
        db.session.commit()

        #database.add_instance(model=Soccer, name, email, phone)
        #flash("Table Inserted Successfully")
        return redirect(url_for('Coachs'))

#this is our update route where we are going to update our employee
@app.route('/update_coach', methods = ['GET', 'POST'])
def update_coach():
    print("hzurray")
    if request.method == 'POST':
        my_data = Coach.query.get(request.form.get('id'))

        print('yes')
        my_data.first_name = request.form['first_name']
        my_data.last_name = request.form['last_name']
        my_data.nationality = request.form['nationality']
 
        db.session.commit()
        #flash("Table Updated Successfully")
        print("jahuu")
        return redirect(url_for('Coachs'))

#This route is for deleting our employee
@app.route('/delete_coach/<id>/', methods = ['GET', 'POST'])
def delete_coach(id):
    my_data = Coach.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Player Deleted Successfully")
 
    return redirect(url_for('Coachs'))

@app.route('/membership')
def Memberships():
    all_data = Membership.query.all()

    return render_template("membership.html", data=all_data), 200

@app.route('/insert_membership', methods=['POST'])
def insert_membership():
 
    if request.method == 'POST':
        number_members = request.form['number_members']
     
        my_data = Membership(number_members)
        db.session.add(my_data)
        db.session.commit()

        #database.add_instance(model=Soccer, name, email, phone)
        #flash("Table Inserted Successfully")
        return redirect(url_for('Memberships'))

#this is our update route where we are going to update our employee
@app.route('/update_membership', methods = ['GET', 'POST'])
def update_membership():
    print("hzurray")
    if request.method == 'POST':
        my_data = Membership.query.get(request.form.get('id'))

        print('yes')
        my_data.number_members = request.form['number_members']
 
        db.session.commit()
        #flash("Table Updated Successfully")
        print("jahuu")
        return redirect(url_for('Memberships'))

#This route is for deleting our employee
@app.route('/delete_membership/<id>/', methods = ['GET', 'POST'])
def delete_membership(id):
    my_data = Membership.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Player Deleted Successfully")
 
    return redirect(url_for('Memberships'))

@app.route('/sponsoring')
def Sponsorings():
    all_data = Sponsoring.query.all()

    return render_template("sponsoring.html", data=all_data), 200

@app.route('/insert_sponsoring', methods=['POST'])
def insert_sponsoring():
 
    if request.method == 'POST':
        start_date = request.form['start_date']
        sponsor_name = request.form['sponsor_name']
     
        my_data = Sponsoring(start_date, sponsor_name)
        db.session.add(my_data)
        db.session.commit()

        #database.add_instance(model=Soccer, name, email, phone)
        #flash("Table Inserted Successfully")
        return redirect(url_for('Sponsorings'))

#this is our update route where we are going to update our employee
@app.route('/update_sponsoring', methods = ['GET', 'POST'])
def update_sponsoring():
    print("hzurray")
    if request.method == 'POST':
        my_data = Sponsoring.query.get(request.form.get('id'))

        print('yes')
        my_data.start_date = request.form['start_date']
        my_data.sponsor_name= request.form['sponsor_name']
 
        db.session.commit()
        #flash("Table Updated Successfully")
        print("jahuu")
        return redirect(url_for('Sponsorings'))

#This route is for deleting our employee
@app.route('/delete_sponsoring/<id>/', methods = ['GET', 'POST'])
def delete_sponsoring(id):
    my_data = Sponsoring.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Player Deleted Successfully")
 
    return redirect(url_for('Sponsorings'))