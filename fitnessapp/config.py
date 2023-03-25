# Importe von benötigten Modulen und Klassen
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# Eigenentwicklung in Anlehnung an Microblog
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Uncharted43v3r@127.0.0.1/fitnessapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
