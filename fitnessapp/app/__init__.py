# Importe von benötigten Modulen und Klassen
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from config import Config
from flask_login import LoginManager

# Eigenentwicklung in Anlehnung an Microblog
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
einloggen = LoginManager(app)
einloggen.login_view = 'login'
bootstrap = Bootstrap(app)

# Eigenentwicklung in Anlehnung an Microblog
from app import routes, models, api