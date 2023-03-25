# Importe von benötigten Modulen und Klassen
from app import app, db
from flask_httpauth import HTTPBasicAuth
from app.models import benutzer, maschine
from flask import jsonify, abort, url_for, request

# Übernommen aus Microblog
httpauth = HTTPBasicAuth()

# Eigenentwicklung in Anlehnung an Microblog
@app.route('/api/users/<int:id>', methods=['GET'])
@httpauth.login_required
def get_user(id):
    daten = benutzer.query.get_or_404(id).to_dict()
    return jsonify(daten)

# Eigenentwicklung in Anlehnung an Microblog
@app.route('/api/users', methods=['GET'])
@httpauth.login_required
def get_users():
    daten = benutzer.to_collection()
    return jsonify(daten)

# Eigenentwicklung in Anlehnung an Microblog
@app.route('/api/users/<int:id>/maschinen', methods=['GET'])
@httpauth.login_required
def get_maschinen(id):
    user = benutzer.query.get_or_404(id)
    data = user.maschinen_to_collection()
    return jsonify(data)

# Eigenentwicklung in Anlehnung an Microblog
@httpauth.verify_password
def verify_password(nutzer, password):
    nutzer = benutzer.query.filter_by(benutzername=nutzer).first()
    if nutzer and nutzer.passwort_pruefen(password):
       return nutzer

