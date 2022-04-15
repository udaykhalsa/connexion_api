from email.mime import application
import connexion
from db import db
from connexion.resolver import RestyResolver
import os

basedir = os.path.abspath(os.path.dirname(__path__))

app = connexion.FlaskApp(__name__)
app.url_map.strict_slashes = False
app.add_api('api_routing.yaml', resolver=RestyResolver('api'))
application = app.app
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'db.sqlite')

