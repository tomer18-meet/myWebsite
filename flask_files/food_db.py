from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://meet:123456@localhost/meet_db'
db = SQLAlchemy(app)

class Pizzas(db.Model):
    __tablename__ = "Pizzas"
    id = db.Column('id', db.Integer, primary_key=True)
    orederd_by = db.Column('ordered_by', db.Unicode)
    size = db.Column('size', db.Integer)
db.create_all()