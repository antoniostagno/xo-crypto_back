from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'].replace("postgres", "postgresql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Forecast(db.Model):
    __tablename__ = "forecast"
    id = db.Column(db.Integer, primary_key=True)
    crypto = db.Column(db.String)
    forecast_price = db.Column(db.Float)
    current_price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def first(self):
        self.query.first()

