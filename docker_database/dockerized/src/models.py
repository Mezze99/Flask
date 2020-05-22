
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Soccer(db.Model):
    __tablename__ = 'soccer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    breed = db.Column(db.String(100))

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    #active = db.Column(db.Boolean(), default=True, nullable=False)
    phone = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def __init__(self, email, name, phone):
        self.email = email
        self.name = name
        self.phone = phone

    def __repr__(self):
        return '<User %r>' % (self.name)

class Player(db.Model):
    __tablename__ = "player"

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
    
    def __repr__(self):
        return '<Player %r>' % (self.name)
