from flask_project.app import db
from flask_project.models import User, Post

u = User(username="john", email="john@example.com")
db.session.add(u)
db.session.commit()

users = User.query.all()
print(users)
