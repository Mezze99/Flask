
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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))

    fname = db.Column(db.String(128), nullable=False)
    lname = db.Column(db.String(100))
    pl_no = db.Column(db.Integer)
    nationality = db.Column(db.String(100))
    pl_goals = db.Column(db.Integer)

    

    def __init__(self, fname, lname, pl_no, nationality, pl_goals, team_id):
        self.fname = fname
        self.lname = lname
        self.pl_no = pl_no
        self.nationality = nationality
        self.pl_goals = pl_goals
        self.team_id = team_id
    
    def __repr__(self):
        return '<Player %r>' % (self.name)

class Team(db.Model):
    __tablename__ = "team"

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(128), unique=True, nullable=False)
    city = db.Column(db.String(100))

    #references
    playerss = db.relationship("Player", cascade='all, delete', backref='player')
    coaches = db.relationship("Coach", backref='coach', cascade='all, delete', uselist=False)
    sponsorships = db.relationship("Sponsoring", cascade='all, delete', backref='sponsoring')
    titles = db.relationship("Title", cascade='all, delete', backref='titled')
    memberships = db.relationship("Membership", cascade='all, delete', backref='membership', uselist=False, lazy='joined')

    def __init__(self, team_name, city):
        self.team_name = team_name
        self.city = city
    
    def __repr__(self):
        return '<Team %r>' % (self.name)

class Title(db.Model):
    __tablename__ = "titled"

    year = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    #winning_team = db.Column(db.String(30))
    winning_team=db.Column(db.String(128), db.ForeignKey('team.team_name'), nullable=False)

    def __init__(self, title, year, winning_team):
        self.title = title
        self.year = year
        self.winning_team = winning_team

    def __repr__(self):
        return '<Title %r>' % (self.title)

class Table(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True, nullable=False)

    position_last_year = db.Column(db.Integer)
    Position_this_year = db.Column(db.Integer)

    def __init__(self, position_last_year, position_this_year):
        self.position_last_year = position_last_year
        self.position_this_year = position_this_year


    def __repr__(self):
        return '<Table %r>' % (self.id)

class Coach(db.Model):
    __tablename__ = "coach"

    id = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    nationality = db.Column(db.String(30))

    def __init__(self, id, first_name, last_name, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.id = id
    
    def __repr__(self):
        return '<Coach %r>' % (self.id)

class Membership(db.Model):
    __tablename__ = "membership"

    id = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True)
    number_members = db.Column(db.Integer)
    
    def __init__(self, number_members, id):
        self.number_members= number_members
        self.id = id
    
    def __repr__(self):
        return '<Membership %r>' % (self.id)

class Sponsoring(db.Model):
    __tablename__ = "sponsoring"

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime(timezone=True))
    sponsor_name = db.Column(db.String(30))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))


    def __init__(self, start_date, sponsor_name, team_id):
        self.start_date = start_date
        self.sponsor_name = sponsor_name
        self.id = id
    
    def __repr__(self):
        return '<Sponsoring %r>' % (self.id)

