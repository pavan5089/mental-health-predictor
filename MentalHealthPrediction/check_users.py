from models import db, User
from app import app

with app.app_context():
    users = User.query.all()
    if users:
        print("Registered Users:")
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
    else:
        print("No users found.")