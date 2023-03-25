# Importe von benötigten Modulen und Klassen
from flask import Flask, render_template, request, send_file, flash, redirect,url_for, session
from app import app, db
from app.models import benutzer, maschine
from app.forms import Loginformular, Registrierungsformular, Maschine
from flask_login import current_user, login_user, logout_user, login_required

# Eigenentwicklung in Anlehnung an Microblog
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html", title='Index')

# Eigenentwicklung in Anlehnung an Microblog
@app.route('/einloggen', methods=['GET', 'POST'])
def einloggen():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Loginformular()
    if form.validate_on_submit():
        nutzer = benutzer.query.filter_by(benutzername=form.Benutzername.data).first()
        if nutzer is None or not nutzer.passwort_pruefen(form.Passwort.data):
            flash('Ungültiger Nutzernamen')
            return redirect(url_for('einloggen'))
        login_user(nutzer, remember=form.Erinnere.data)
        return redirect('index')
    return render_template('einloggen.html', title='Einloggen', form=form)

# Eigenentwicklung in Anlehnung an Microblog
@app.route('/registrieren', methods=['GET', 'POST'])
def registrieren():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Registrierungsformular()
    if form.validate_on_submit():
        nutzer = benutzer(benutzername=form.Benutzername.data, email=form.Email.data)
        nutzer.passwort_setzen(form.Passwort.data)
        db.session.add(nutzer)
        db.session.commit()
        flash('Danke für Ihr Vertrauen!')
        return redirect(url_for('einloggen'))
    return render_template('registrieren.html', title='Registrieren', form=form)

# Eigenentwicklung in Anlehnung an Microblog
@app.route('/ausloggen', methods=['GET'])
def ausloggen():
    logout_user()
    return render_template("ausloggen.html", title='Aufwiedersehen')

# Eigenentwicklung in Anlehnung an Microblog
@app.route('/maschine_eintragen', methods=['GET', 'POST'])
@login_required
def eintragen():
    form = Maschine()
    if form.validate_on_submit():
        maschineimp = maschine(name=form.Maschinenname.data, einstellung1=form.Einstellung1.data, einstellung2=form.Einstellung2.data, Trainierender=current_user)
        db.session.add(maschineimp)
        db.session.commit()
        flash('Maschine oder Übung hinzugefügt.')
        return redirect(url_for('eintragen'))

    return render_template("eintragen.html", title='Maschine eintragen', form=form)

# Eigenentwicklung
@app.route('/trainingsplan', methods=['GET', 'POST'])
@login_required
def trainingsplan():
    uebung = current_user.eigene_uebung()
    return render_template("trainingsplan.html", title='Trainingsplan', uebung=uebung)