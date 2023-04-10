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
    address = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Integer, nullable=False)
    has_wifi = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.String(10), nullable=False)
    coffee_price = db.Column(db.Float, nullable=False )
    vegan_snacks = db.Column(db.Integer, nullable=False)
    google_rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Cafe {self.name}>"

# with app.app_context():
#     db.create_all()
#     loyal_coffee = Cafes(
#         name="Loyal Coffee",
#         map_url="https://www.google.com/maps/place/Loyal+Coffee/@39.0024988,-104.7995794,15z/data=!4m2!3m1!1s0x0:0xf2e39d33d9e94468?sa=X&ved=2ahUKEwiPk734wpX-AhUFOH0KHQB2ArQQ_BJ6BQiCARAI",
#         img_url="https://live.staticflickr.com/65535/52803834792_1f2e3ef9a7_m.jpg",
#         address="408 S Nevada Ave",
#         has_sockets=1,
#         has_wifi=1,
#         seats="40+",
#         coffee_price=3.80,
#         vegan_snacks=0,
#         google_rating=4.7,
#     )
#
#     wayfinder = Cafes(
#         name="Wayfinder Coffee Co",
#         map_url="https://www.google.com/maps/place/Wayfinder+Coffee+Co./@38.9214839,-104.7394471,15z/data=!4m2!3m1!1s0x0:0x8a228a501f21c71b?sa=X&ved=2ahUKEwivxZXtwpX-AhXlFTQIHUDcAHgQ_BJ6BAh8EAg",
#         img_url="https://live.staticflickr.com/65535/52804795080_a061c1efeb_m.jpg",
#         address="6140 Austin Bluffs Pkwy",
#         has_sockets=1,
#         has_wifi=1,
#         seats="30",
#         coffee_price=3.00,
#         vegan_snacks=0,
#         google_rating=4.6,
#     )
#
#     mission_coffee = Cafes(
#         name="Mission Coffee Roasters Inc",
#         map_url="https://www.google.com/maps/place/Mission+Coffee+Roasters+Inc/@39.0011452,-104.7968649,15z/data=!4m6!3m5!1s0x87134cfd22497c1d:0xb14393830726ca4c!8m2!3d39.0011452!4d-104.7968649!16s%2Fg%2F1260x8bmv",
#         img_url="https://live.staticflickr.com/65535/52804649064_ae95666832_m.jpg",
#         address="11641 Ridgeline Dr, Suite 170",
#         has_sockets=0,
#         has_wifi=0,
#         seats="20",
#         coffee_price=2.35,
#         vegan_snacks=0,
#         google_rating=4.6,
#     )
#
#
#     hold_fast = Cafes(
#         name="Hold Fast Coffee Co",
#         map_url="https://www.google.com/maps/place/Hold+Fast+Coffee+Co+(we+just+rebranded+from+Peak+Place)/@38.9091484,-104.7828618,15z/data=!4m2!3m1!1s0x0:0xe3b8021bf99e4d31?sa=X&ved=2ahUKEwjmxJ6Ew5X-AhUyHjQIHbU2AJgQ_BJ6BAh8EAg",
#         img_url="https://live.staticflickr.com/65535/52804391526_a7eedde0d5_m.jpg",
#         address="2360 Montebello Square Drive",
#         has_sockets=0,
#         has_wifi=1,
#         seats="20+",
#         coffee_price=3.00,
#         vegan_snacks=0,
#         google_rating=4.7,
#     )
#
#     coffee_zone = Cafes(
#         name="Coffee and Tea Zone",
#         map_url="https://www.google.com/maps/place/Coffee+and+Tea+Zone/@39.0109237,-104.8063765,15z/data=!4m2!3m1!1s0x0:0xac29dfe3d662851?sa=X&ved=2ahUKEwid-tuQw5X-AhUvAjQIHVyPAmEQ_BJ6BQiKARAI",
#         img_url="https://live.staticflickr.com/65535/52803088581_8cca0c3903_m.jpg",
#         address="25 North Tejon, St. 101",
#         has_sockets=0,
#         has_wifi=1,
#         seats="20+",
#         coffee_price=2.50,
#         vegan_snacks=1,
#         google_rating=4.4,
#     )
#
#     story_coffee = Cafes(
#         name="Story Coffee Company",
#         map_url="https://www.google.com/maps/place/Story+Coffee+Company/@38.8368583,-104.8224927,15z/data=!4m6!3m5!1s0x8713453d6750f939:0xe770f0982a5d3d1b!8m2!3d38.8368583!4d-104.8224927!16s%2Fg%2F11cns9wfwf",
#         img_url="https://live.staticflickr.com/65535/52804662434_7a10ca43d7_m.jpg",
#         address="120 East Bijou Street",
#         has_sockets=0,
#         has_wifi=0,
#         seats="15+",
#         coffee_price=2.50,
#         vegan_snacks=0,
#         google_rating=4.9,
#     )
#
#     third_space = Cafes(
#         name="Third Space Coffee",
#         map_url="https://www.google.com/maps/place/Kairos+Coffee+House/@38.8979109,-104.8322053,15z/data=!4m2!3m1!1s0x0:0x9c836800abfdc8db?sa=X&ved=2ahUKEwjOqr65jZb-AhWcIjQIHWANC88Q_BJ6BQiLARAI",
#         img_url="https://live.staticflickr.com/65535/52803850262_74e04d96aa_m.jpg",
#         address="5670 N Academy Blvd",
#         has_sockets=0,
#         has_wifi=1,
#         seats="20+",
#         coffee_price=3.50,
#         vegan_snacks=0,
#         google_rating=4.7,
#     )
#
#     humble = Cafes(
#         name="Humble Coffee",
#         map_url="https://www.google.com/maps/place/Humble+Coffee/@38.8630943,-104.8102393,15z/data=!4m6!3m5!1s0x8713456350d23adb:0x46df7e55bfcd09f6!8m2!3d38.8630943!4d-104.8102393!16s%2Fg%2F11b5pjj70v",
#         img_url="https://live.staticflickr.com/65535/52803849402_0f99f0c02d_m.jpg",
#         address="2103 Templeton Gap Rd",
#         has_sockets=0,
#         has_wifi=0,
#         seats="0",
#         coffee_price=3.75,
#         vegan_snacks=0,
#         google_rating=4.8,
#     )
#
#     db.session.add(wayfinder)
#     db.session.add(mission_coffee)
#     db.session.add(hold_fast)
#     db.session.add(coffee_zone)
#     db.session.add(story_coffee)
#     db.session.add(third_space)
#     db.session.add(humble)
#     db.session.commit()


@app.route("/", methods=['GET', 'POST'])
def home():
    cafes = Cafes.query.order_by(Cafes.google_rating.desc()).all()
    return render_template("index.html", cafes=cafes)


if __name__ == "__main__":
    app.run(debug=True)
