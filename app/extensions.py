from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager

ma = Marshmallow()
db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
login_manager = LoginManager()
