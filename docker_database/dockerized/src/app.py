import json

from flask import request, render_template, redirect, flash, url_for

from . import create_app, database
from .models import (
    db,
    Player,
    Table,
    Title,
    Coach,
    Membership,
    Sponsoring,
    Team,
)

app = create_app()
app.debug = True  # receive better error messages


###############################################################################################################
# MAIN PAGES #
###############################################################################################################

# Test database connection
# render Startpage
@app.route("/", methods=["GET"])
def fetch():
    team_data = Team.query.all()
    return render_template("home.html", data=team_data), 200


# render CRUD
@app.route("/crud", methods=["GET"])
def crud():
    return render_template("crud.html"), 200


# render Query Index Page
@app.route("/index")
def Index2():
    return render_template("index.html"), 200


###############################################################################################################
# QUERIES #
###############################################################################################################

# Query by Player name (with input)
@app.route("/run", methods=["GET", "POST"])
def run():
    if request.method == "POST":
        name = request.form["submit_player_name"]
        data = db.session.query(Player).filter_by(lname=name).all()
    return render_template("show_user.html", data=data, name=name)


# Query Player by goals (ordered)
@app.route("/query_goalgetter", methods=["GET"])
def query_goalgetter():
    userss = db.session.query(Player).order_by(Player.pl_goals.desc()).all()
    return render_template("query_goalgetter.html", user=userss)


# Query Teams by number of goals
@app.route("/query_teamgoals", methods=["GET"])
def query_teamgoals():

    last_orders = (
        db.session.query(Player.team_id, db.func.sum(Player.pl_goals).label("goals"))
        .group_by(Player.team_id)
        .subquery()
    )

    query = (
        Team.query.join(last_orders, Team.id == last_orders.c.team_id)
        .add_columns(Team.id, Team.team_name, last_orders.c.goals)
        .order_by(last_orders.c.goals.desc(),)
    )
    return render_template("query_teamgoals.html", user=query)


# Query Teams by number of goals
@app.route("/query_table", methods=["GET"])
def query_table():

    query = (
        Team.query.join(Table, Team.id == Table.id)
        .add_columns(
            Team.team_name,
            Table.matches,
            Table.wins,
            Table.remis,
            Table.defeats,
            Table.points,
        )
        .order_by(Table.points.desc(),)
    )

    return render_template("query_table.html", user=query)


###############################################################################################################
# CRUD #
###############################################################################################################

##########
# Player ######################################################################################################
##########

# query on Player data (+ Team data for foreign constrains)
@app.route("/player")
def Players():
    all_data = Player.query.all()
    team_data = Team.query.all()

    return render_template("player.html", employees=all_data, team=team_data), 200


# This route is for inserting Player
@app.route("/insert_player", methods=["POST"])
def insert_player():

    if request.method == "POST":

        fname = request.form["fname"]
        lname = request.form["lname"]
        pl_no = request.form["pl_no"]
        nationality = request.form["nationality"]
        pl_goals = request.form["pl_goals"]
        team_id = request.form["team_id"]

        my_data = Player(fname, lname, pl_no, nationality, pl_goals, team_id)
        db.session.add(my_data)
        db.session.commit()

        flash("Player Inserted Successfully")
        return redirect(url_for("Players"))


# This route is for updating Player
@app.route("/update_player", methods=["GET", "POST"])
def update_player():

    if request.method == "POST":
        my_data = Player.query.get(request.form.get("id"))

        my_data.fname = request.form["fname"]
        my_data.lname = request.form["lname"]
        my_data.pl_no = request.form["pl_no"]
        my_data.nationality = request.form["nationality"]
        my_data.pl_goals = request.form["pl_goals"]
        my_data.team_id = request.form["team_id"]

        db.session.commit()
        flash("Player Updated Successfully")

        return redirect(url_for("Players"))


# This route is for deleting Player
@app.route("/delete_player/<id>/", methods=["GET", "POST"])
def delete_player(id):
    my_data = Player.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Player Deleted Successfully")

    return redirect(url_for("Players"))


########
# Team ######################################################################################################
########

# query on all our Team data
@app.route("/team")
def Teams():
    all_data = Team.query.all()
    return render_template("team.html", employees=all_data), 200


# This route is for inserting Teams
@app.route("/insert_team", methods=["POST"])
def insert_team():

    if request.method == "POST":

        team_name = request.form["team_name"]
        city = request.form["city"]

        my_data = Team(team_name, city)
        db.session.add(my_data)
        db.session.commit()

        flash("Team Inserted Successfully")
        return redirect(url_for("Teams"))


# This route is for updating Teams
@app.route("/update_team", methods=["GET", "POST"])
def update_team():

    if request.method == "POST":
        my_data = Team.query.get(request.form.get("id"))

        my_data.team_name = request.form["team_name"]
        my_data.city = request.form["city"]

        db.session.commit()
        flash("Team Updated Successfully")

        return redirect(url_for("Teams"))


# This route is for deleting Teams
@app.route("/delete_team/<id>/", methods=["GET", "POST"])
def delete_team(id):
    my_data = Team.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Team Deleted Successfully")
    return redirect(url_for("Teams"))


#########
# Table ######################################################################################################
#########

# Query Table data
@app.route("/table")
def Tables():
    all_data = Table.query.all()
    team_data = Team.query.all()
    return render_template("table.html", data=all_data, team_data=team_data), 200


# This route is for inserting Teams
@app.route("/insert_table", methods=["POST"])
def insert_table():

    if request.method == "POST":
        matches = request.form["matches"]
        wins = request.form["wins"]
        remis = request.form["remis"]
        defeats = request.form["defeats"]
        points = request.form["points"]
        idx = request.form["id"]

        my_data = Table(matches, wins, remis, defeats, points, idx)
        db.session.add(my_data)
        db.session.commit()
        flash("Table Inserted Successfully")
        return redirect(url_for("Tables"))


# This route is for updating Tables
@app.route("/update_table", methods=["GET", "POST"])
def update_table():

    if request.method == "POST":
        my_data = Table.query.get(request.form.get("id"))

        my_data.matches = request.form["matches"]
        my_data.wins = request.form["wins"]
        my_data.remis = request.form["remis"]
        my_data.defeats = request.form["defeats"]
        my_data.points = request.form["points"]

        db.session.commit()
        flash("Table Updated Successfully")

        return redirect(url_for("Tables"))


# This route is for deleting Tables
@app.route("/delete_table/<id>/", methods=["GET", "POST"])
def delete_table(id):
    my_data = Table.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Player Deleted Successfully")

    return redirect(url_for("Tables"))


#########
# Title ######################################################################################################
#########

# query title
@app.route("/title")
def Titles():
    all_data = Title.query.all()
    team_data = Team.query.all()

    return render_template("title.html", data=all_data, team=team_data), 200


# This route is for inserting Title
@app.route("/insert_title", methods=["POST"])
def insert_title():

    if request.method == "POST":
        year = request.form["year"]
        title = request.form["title"]
        winning_team = request.form["winning_team"]

        my_data = Title(year, title, winning_team)
        db.session.add(my_data)
        db.session.commit()

        # database.add_instance(model=Soccer, name, email, phone)
        flash("Title Inserted Successfully")
        return redirect(url_for("Titles"))


# This route is for updating Titles
@app.route("/update_title", methods=["GET", "POST"])
def update_title():
    if request.method == "POST":
        my_data = Title.query.get(request.form.get("year"))

        my_data.year = request.form["year"]
        my_data.title = request.form["title"]
        my_data.winning_team = request.form["winning_team"]

        db.session.commit()
        flash("Title Updated Successfully")
        return redirect(url_for("Titles"))


# This route is for deleting Titles
@app.route("/delete_title/<year>/", methods=["GET", "POST"])
def delete_title(year):
    my_data = Title.query.get(year)
    db.session.delete(my_data)
    db.session.commit()
    flash("Title Deleted Successfully")

    return redirect(url_for("Titles"))


#########
# Coach ######################################################################################################
#########

# query Coach
@app.route("/coach")
def Coachs():
    all_data = Coach.query.all()
    return render_template("coach.html", data=all_data), 200


# This route is for inserting Title
@app.route("/insert_coach", methods=["POST"])
def insert_coach():

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        nationality = request.form["nationality"]
        idx = request.form["id"]

        my_data = Coach(idx, first_name, last_name, nationality)
        db.session.add(my_data)
        db.session.commit()

        flash("Coach Inserted Successfully")
        return redirect(url_for("Coachs"))


# This route is for updating Coach
@app.route("/update_coach", methods=["GET", "POST"])
def update_coach():
    if request.method == "POST":
        my_data = Coach.query.get(request.form.get("id"))

        my_data.first_name = request.form["first_name"]
        my_data.last_name = request.form["last_name"]
        my_data.nationality = request.form["nationality"]

        db.session.commit()
        flash("Coach Updated Successfully")

        return redirect(url_for("Coachs"))


# This route is for deleting Coach
@app.route("/delete_coach/<id>/", methods=["GET", "POST"])
def delete_coach(id):
    my_data = Coach.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Coach Deleted Successfully")

    return redirect(url_for("Coachs"))


##############
# Membership ######################################################################################################
##############

# query Membership
@app.route("/membership")
def Memberships():
    all_data = Membership.query.all()

    return render_template("membership.html", data=all_data), 200


# This route is for inserting Membership
@app.route("/insert_membership", methods=["POST"])
def insert_membership():

    if request.method == "POST":
        number_members = request.form["number_members"]
        some_id = request.form["id"]

        my_data = Membership(number_members, some_id)
        db.session.add(my_data)
        db.session.commit()

        flash("Membership Inserted Successfully")
        return redirect(url_for("Memberships"))


# This route is for updating Membership
@app.route("/update_membership", methods=["GET", "POST"])
def update_membership():
    if request.method == "POST":
        my_data = Membership.query.get(request.form.get("id"))

        my_data.number_members = request.form["number_members"]

        db.session.commit()
        flash("Membership Updated Successfully")
        return redirect(url_for("Memberships"))


# This route is for deleting Membership
@app.route("/delete_membership/<id>/", methods=["GET", "POST"])
def delete_membership(id):
    my_data = Membership.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Membership Deleted Successfully")

    return redirect(url_for("Memberships"))


##############
# Sponsorship ######################################################################################################
##############


@app.route("/sponsoring")
def Sponsorings():
    all_data = Sponsoring.query.all()
    team_data = Team.query.all()

    return render_template("sponsoring.html", data=all_data, team=team_data), 200


# This route is for inserting Sponsorship
@app.route("/insert_sponsoring", methods=["POST"])
def insert_sponsoring():

    if request.method == "POST":
        start_date = request.form["start_date"]
        sponsor_name = request.form["sponsor_name"]
        team_id = request.form["team_id"]
        contract = request.form["contract"]

        my_data = Sponsoring(start_date, sponsor_name, team_id, contract)
        db.session.add(my_data)
        db.session.commit()

        flash("Sponsorship Inserted Successfully")
        return redirect(url_for("Sponsorings"))


# This route is for updating Sponsorship
@app.route("/update_sponsoring", methods=["GET", "POST"])
def update_sponsoring():
    if request.method == "POST":
        my_data = Sponsoring.query.get(request.form.get("id"))

        my_data.start_date = request.form["start_date"]
        my_data.sponsor_name = request.form["sponsor_name"]
        my_data.team_id = request.form["team_id"]
        my_data.contract = request.form["contract"]

        db.session.commit()
        flash("Sponsorship Updated Successfully")
        return redirect(url_for("Sponsorings"))


# This route is for deleting Sponsorship
@app.route("/delete_sponsoring/<id>/", methods=["GET", "POST"])
def delete_sponsoring(id):
    my_data = Sponsoring.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Sponsorship Deleted Successfully")

    return redirect(url_for("Sponsorings"))
