from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


# classes
class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True)
    species = db.Column(db.String(50))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'))
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeeper.id'))

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(50))
    open_to_visitors = db.Column(db.Boolean)
    animals = db.relationship('Animal', backref='enclosure', lazy=True)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    birthday = db.Column(db.Date)
    animals = db.relationship('Animal', backref='zookeeper', lazy=True)

'''db :
with app.app_context():



    
    #  instances
    a_1 = Animal(name='Lion',from models import db, Zookeeper, Enclosure, Animal
 species='Big Cat')
    a_2 = Animal(name='Giraffe', species='Tall Animal')
    e = Enclosure(environment='Safari', open_to_visitors=True)
    z = Zookeeper(name='John', birthday='1990-01-01')

    
    e.animals = [a_1, a_2]
    z.animals = [a_1, a_2]

    db.session.add_all([a_1, a_2, e, z])
    db.session.commit()'''
