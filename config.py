
# Eigenentwicklung in Anlehnung an Microblog
# Importe von benötigten Modulen und Klassen
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Eigenentwicklung in Anlehnung an Microblog
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    DATABASE_URL='mysql+pymysql://fitnessuser:C1xAhF!/^N402_@localhost:3306/fitnessapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
