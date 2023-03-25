# Importe von benötigten Modulen und Klassen
from app import einloggen
from app import db, einloggen
from time import time
from flask import url_for
from flask_login import UserMixin
from datetime import datetime, timedelta
import base64
import os
from werkzeug.security import generate_password_hash, check_password_hash

# Eigenentwicklung in Anlehnung an Microblog
class benutzer(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    benutzername = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    passwort = db.Column(db.String(128))
    maschine_uebung = db.Relationship("maschine", backref='Trainierender', lazy='dynamic')

    def __repr__(self):
        return '<Benutzer {}>'.format(self.benutzername)

    def passwort_setzen(self, passwort):
        self.passwort = generate_password_hash(passwort)

    def passwort_pruefen(self, Passwort):
        return check_password_hash(self.passwort, Passwort)

    def eigene_uebung(self):
        eigene = maschine.query.filter_by(athlet=self.id)
        return eigene.order_by()

    # Eigenentwicklung in Anlehnung an Microblog
    def to_dict(self):
        data = {
            'id': self.id,
            'benutzername': self.benutzername,
            'email': self.email
        }
        return data

    # Eigenentwicklung in Anlehnung an Microblog
    @staticmethod
    def to_collection():
        benutzers = benutzer.query.all()
        daten = {'items': [item.to_dict() for item in benutzers]}
        return(daten)

    # Eigenentwicklung in Anlehnung an Microblog
    def maschinen_to_collection(self):
        data = {'items': [item.to_dict() for item in self.maschine_uebung]}
        return data

#Übernommen aus den Beispielen
@einloggen.user_loader
def nutzer_laden(id):
    return benutzer.query.get(int(id))

# Eigenentwicklung in Anlehnung an Microblog
class maschine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    einstellung1 = db.Column(db.String(10))
    einstellung2 = db.Column(db.String(10))
    athlet = db.Column(db.Integer, db.ForeignKey('benutzer.id'))

    # Eigenentwicklung
    def to_dict(self):
        data = {
            'id' : self.id,
            'name': self.name,
            'einstellung1': self.einstellung1,
            'einstellung2': self.einstellung2
                }
        return data

    # Eigenentwicklung in Anlehnung an Microblog
    @staticmethod
    def to_collection():
        resources = maschine.query.all()
        data = {'items': [item.to_dict() for item in resources]}
        return(data)

