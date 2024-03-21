import json
from werkzeug.security import generate_password_hash, check_password_hash

USERS_FILE = 'users.json'

class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

    @staticmethod
    def from_json(json_data):
        return User(json_data['username'], json_data['password_hash'])

    def to_json(self):
        return {
            'username': self.username,
            'password_hash': self.password_hash
        }

    def save(self):
        users = self.load_users()
        users[self.username] = self.to_json()
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f)

    @staticmethod
    def load_users():
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
