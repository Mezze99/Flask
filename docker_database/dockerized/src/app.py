import json

from flask import request, render_template, redirect, flash, url_for

from . import create_app, database
from .models import Soccer, User, db

app = create_app()
app.debug = True


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