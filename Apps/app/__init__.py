from flask import Flask ,render_template
from config import SECRET_KEY

apps = Flask(__name__)
apps.config['SECRET_KEY'] = SECRET_KEY

from Apps.app import views