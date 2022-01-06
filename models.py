from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'].replace("postgres", "postgresql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cg = CoinGeckoAPI()


def save_to_db():
    db.session.commit()


class Coin(db.Model):
    __tablename__ = "coin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    symbol = db.Column(db.String)
    id_gecko = db.Column(db.String)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def quick_save(self):
        db.session.add(self)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)

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


class Favorites(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

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
