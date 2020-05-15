
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Soccer(db.Model):
    __tablename__ = 'soccer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    breed = db.Column(db.String(100))
    