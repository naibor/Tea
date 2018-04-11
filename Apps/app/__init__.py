from flask import Flask ,render_template
from config import SECRET_KEY
from flask_sqlalchemy import SQLAlchemy 


apps = Flask(__name__)
apps.config['SERET_KEY'] = SECRET_KEY
apps.config.from_object('config')
db = SQLAlchemy(apps)



from Apps.app import views, models