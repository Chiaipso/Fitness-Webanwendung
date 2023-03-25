# Importe von benötigten Modulen und Klassen
from app import app, db, einloggen
from flask_wtf import FlaskForm
from flask_login import UserMixin
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from app.models import benutzer

# Eigenentwicklung in Anlehnung an Microblog
class Loginformular(FlaskForm):
    Benutzername = StringField('Benutzer', validators=[DataRequired()])
    Passwort = PasswordField('Passwort', validators=[DataRequired()])
    Erinnere = BooleanField('Erinnere dich an mich')
    Einreichen = SubmitField('Einloggen')

# Eigenentwicklung in Anlehnung an Microblog
class Registrierungsformular(FlaskForm):
    Benutzername = StringField('Benutzer', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Passwort = PasswordField('Passwort', validators=[DataRequired()])
    Passwort2 = PasswordField(
        'Wiederholen Sie ihr Passwort', validators=[DataRequired(), EqualTo('Passwort')])
    Einreichen = SubmitField('Registrieren')

    def validiere_benutzernamen(self, Benutzername):
        user = benutzer.query.filter_by(Benutzername=Benutzername.data).first()
        if user is not None:
            raise ValidationError('Bitte wählen Sie einen anderen Benutzernamen.')

    def validiere_email(self, Email):
        user = benutzer.query.filter_by(Email=Email.data).first()
        if user is not None:
            raise ValidationError('Diese Mail Adresse wurde bereits verwendet. Wählen Sie eine andere.')

# Eigenentwicklung
class Maschine(FlaskForm):
        Maschinenname = StringField('Maschinen- oder Übungsname', validators=[DataRequired()])
        Einstellung1 = IntegerField('Einstellung 1 oder Gewicht 1', validators=[NumberRange(min=0, max=1000, message="Bitte Zahl eingeben")])
        Einstellung2 = IntegerField('Einstellung 2 oder Gewicht 2', validators=[NumberRange(min=0, max=1000, message="Bitte Zahl eingeben")])
        Einreichen = SubmitField('Maschine oder Übung speichern')