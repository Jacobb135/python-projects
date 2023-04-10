from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from data import Cafes
import folium

import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy()
db.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def home():
    cafes = Cafes.query.order_by(Cafes.google_rating.desc()).all()

    map = folium.Map(
        location=[38.8630943, -104.8102393],
        zoom_start=12,
    )
    map.save('templates/map.html')

    return render_template("index.html", cafes=cafes, map=map._repr_html_())


@app.route('/map')
def map():
    return render_template('map.html')


if __name__ == "__main__":
    app.run(debug=True)
