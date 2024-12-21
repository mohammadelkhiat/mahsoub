from flask_sqlalchemy import SQLAlchemy
from app import app

# Set up the database
db = SQLAlchemy(app)

# Define Exercise model
class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    repetitions = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=True)
    duration = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())

# Create all tables
db.create_all()
