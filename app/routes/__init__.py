from flask import Flask
from flask_login import LoginManager
from .auth import auth_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random secret key

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from ..models import User

@login_manager.user_loader
def load_user(user_id):
    # Here, you would load the user from your JSON data
    # For example:
    # return User.load_user(user_id)
    pass

app.register_blueprint(auth_bp)

# Add more configurations and imports as needed
