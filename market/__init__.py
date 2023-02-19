from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
DATABASE_URL = 'postgresql://market_diba_user:v4Q2zWoojCkdLyy82C3piI01kN8jLDNR@dpg-cfor28g2i3mo4buptv2g-a.oregon-postgres.render.com/market_diba'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

app.config['SECRET_KEY'] = '826a8b27acf76da67281a678'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
app.app_context().push()

from market import routes