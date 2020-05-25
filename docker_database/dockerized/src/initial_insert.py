
import flask_sqlalchemy
from .models import Team, Player

db = flask_sqlalchemy.SQLAlchemy()

teams = [Team(team_name="FC Barcelona", city="Barcelona"),
        Team(team_name="Real Madrid", city="Madrid"),
        Team(team_name="Bayern Munich", city="Munich"),
        Team(team_name="Manchester City", city="Manchester"),
        Team(team_name="AC Milano", city="Milano"),
        Team(team_name="Eintracht Frankfurt", city="Frankfurt")]

players = [Player(fname='Lionel', lname='Messi', pl_no=10, nationality="Argentina", pl_goals=16, team_id=1),
        Player(fname='Christiano', lname='Ronaldo', pl_no=7, nationality="Portugal", pl_goals=17, team_id=2),
        Player(fname='Thomas', lname='Müller', pl_no=13, nationality="Germany", pl_goals=13, team_id=3),
        Player(fname='Jerome', lname='Boateng', pl_no=17, nationality="Germany", pl_goals=2, team_id=3),
        Player(fname='Manuel', lname='Neuer', pl_no=1, nationality="Germany", pl_goals=0, team_id=3),
        Player(fname='David', lname='Alaba', pl_no=27, nationality="Austria", pl_goals=4, team_id=3),
        Player(fname='Kevin', lname='De Bruyne', pl_no=10, nationality="Belgium", pl_goals=11, team_id=4),
        Player(fname='Zlatan', lname='Ibrahimovic', pl_no=21, nationality="Sweden", pl_goals=99, team_id=5),
        Player(fname='Martin', lname='Hinteregger', pl_no=13, nationality="Austria", pl_goals=3, team_id=6)]

def run_insert(teams=teams, players=players):
    for team in teams:
        db.session.add(team)
        db.session.commit()
    
    for player in players:
        db.session.add(player)
        db.session.commit()