from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app.models import User
from werkzeug.security import generate_password_hash
from flask import render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        # Handle GET request, for example, render the signup form
        return render_template('signup.html')

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    users = User.load_users()
    if username in users:
        return jsonify({'message': 'Username already exists'}), 400

    new_user = User(username, generate_password_hash(password))
    new_user.save()

    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Handle GET request, for example, render the login form
        return render_template('login.html')

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    users = User.load_users()
    if username not in users or not check_password_hash(users[username]['password_hash'], password):
        return jsonify({'message': 'Invalid username or password'}), 401

    return jsonify({'message': 'Login successful'}), 200
