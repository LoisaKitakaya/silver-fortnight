from flask import Flask

from config import Config

# Flask extensions

from app.extensions import ma, db, cors, migrate, login_manager

# app blueprints

from app.algebra import bp as algebra_bp
from app.arithmetics import bp as arithmetics_bp
from app.calculus import bp as calculus_bp
from app.finance import bp as finance_bp
from app.geometry import bp as geometry_bp
from app.logic import bp as logic_bp
from app.matrices import bp as matrices_bp
from app.numerics import bp as numerics_bp
from app.statistics import bp as statistics_bp
from app.trigonometry import bp as trigonometry_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Flask extensions

    ma.init_app(app)

    db.init_app(app)

    cors.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    # app blueprints

    app.register_blueprint(algebra_bp)

    app.register_blueprint(arithmetics_bp)

    app.register_blueprint(calculus_bp)

    app.register_blueprint(finance_bp)

    app.register_blueprint(geometry_bp)

    app.register_blueprint(logic_bp)

    app.register_blueprint(matrices_bp)

    app.register_blueprint(numerics_bp)

    app.register_blueprint(statistics_bp)

    app.register_blueprint(trigonometry_bp)

    return app
