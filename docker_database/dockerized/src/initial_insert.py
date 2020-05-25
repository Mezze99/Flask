
import flask_sqlalchemy
from .models import Team, Player

db = flask_sqlalchemy.SQLAlchemy()

teams = [Team()]

players = [Player(fname='Lionel', lname='Messi', pl_no=10, nationality="Argentina"),
    Player(fname='Christiano', lname='Ronaldo', pl_no=7, nationality="Portugal"),
    Player(fname='Thomas', lname='Müller', pl_no=13, nationality="Germany"),
    Player(fname='Jerome', lname='Boateng', pl_no=17, nationality="Germany"),
    Player(fname='Manuel', lname='Neuer', pl_no=1, nationality="Germany"),
    Player(fname='David', lname='Alaba', pl_no=27, nationality="Austria"),
    Player(fname='Kevin', lname='De Bruyne', pl_no=10, nationality="Belgium"),
    Player(fname='Zlatan', lname='Ibrahimovic', pl_no=21, nationality="Sweden")]
db.session.add(me)
db.session.commit()