from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy()
db.init_app(app)

class Cafes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), unique=True)
    map_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Integer, nullable=False)
    has_wifi = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.String(10), nullable=False)
    coffee_price = db.Column(db.Float, nullable=False )
    vegan_snacks = db.Column(db.Integer, nullable=False)
    google_rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Cafe {self.name}>"


@app.route("/")
def home():
    cafes = Cafes.query.all()
    return render_template("index.html", cafes=cafes)


if __name__ == "__main__":
    app.run(debug=True)