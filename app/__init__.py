# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_pyfile('config.py')

    # Import and register blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.purchase_ticket import purchase_ticket_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(purchase_ticket_bp)

    return app
