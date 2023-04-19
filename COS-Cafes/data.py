from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime
import pendulum
db = SQLAlchemy()


class Cafes(db.Model):
    __tablename__ = "Cafes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), unique=True)
    map_coords = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    monday = db.Column(db.String(250), nullable=False)
    tuesday = db.Column(db.String(250), nullable=False)
    wednesday = db.Column(db.String(250), nullable=False)
    thursday = db.Column(db.String(250), nullable=False)
    friday = db.Column(db.String(250), nullable=False)
    saturday = db.Column(db.String(250), nullable=False)
    sunday = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Integer, nullable=False)
    has_wifi = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.String(10), nullable=False)
    coffee_price = db.Column(db.Float, nullable=False )
    vegan_snacks = db.Column(db.Integer, nullable=False)
    google_rating = db.Column(db.Float, nullable=False)


    # def __repr__(self):
    #     return f"<Cafe {self.title}>"


class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(30), nullable=False)

loyal_coffee = Cafes(
    name="Loyal Coffee",
    map_coords="39.0024988, -104.7995794",
    img_url="https://live.staticflickr.com/65535/52803834792_1f2e3ef9a7_m.jpg",
    address="408 S Nevada Ave",
    monday="6am-6pm",
    tuesday="6am-6pm",
    wednesday="6am-6pm",
    thursday="6am-6pm",
    friday="6am-6pm",
    saturday="6am-6pm",
    sunday="6am-6pm",
    has_sockets=1,
    has_wifi=1,
    seats="40+",
    coffee_price=3.80,
    vegan_snacks=0,
    google_rating=4.7,
)

wayfinder = Cafes(
    name="Wayfinder Coffee Co",
    map_coords="38.9214839,-104.7394471",
    img_url="https://live.staticflickr.com/65535/52804795080_a061c1efeb_m.jpg",
    address="6140 Austin Bluffs Pkwy",
    monday="6:30am-6pm",
    tuesday="6:30am-6pm",
    wednesday="6:30am-6pm",
    thursday="6:30am-6pm",
    friday="6:30am-6pm",
    saturday="8am-6pm",
    sunday="8am-3pm",
    has_sockets=1,
    has_wifi=1,
    seats="30",
    coffee_price=3.00,
    vegan_snacks=0,
    google_rating=4.6,
)

mission_coffee = Cafes(
    name="Mission Coffee Roasters Inc",
    map_coords="39.0011452,-104.7968649",
    img_url="https://live.staticflickr.com/65535/52804649064_ae95666832_m.jpg",
    address="11641 Ridgeline Dr, Suite 170",
    monday="7am-4pm",
    tuesday="7am-4pm",
    wednesday="7am-4pm",
    thursday="7am-4pm",
    friday="Closed",
    saturday="9am-4pm",
    sunday="9am-4pm",
    has_sockets=0,
    has_wifi=0,
    seats="20",
    coffee_price=2.35,
    vegan_snacks=0,
    google_rating=4.6,
)


hold_fast = Cafes(
    name="Hold Fast Coffee Co",
    map_coords="38.9091484,-104.7828618",
    img_url="https://live.staticflickr.com/65535/52804391526_a7eedde0d5_m.jpg",
    address="2360 Montebello Square Drive",
    monday="6:30am-6pm",
    tuesday="6:30am-6pm",
    wednesday="6:30am-6pm",
    thursday="6:30am-6pm",
    friday="6:30am-6pm",
    saturday="6:30am-6pm",
    sunday="8am-4pm",
    has_sockets=0,
    has_wifi=1,
    seats="20+",
    coffee_price=3.00,
    vegan_snacks=0,
    google_rating=4.7,
)

coffee_zone = Cafes(
    name="Coffee and Tea Zone",
    map_coords="39.0109237,-104.8063765",
    img_url="https://live.staticflickr.com/65535/52803088581_8cca0c3903_m.jpg",
    address="25 North Tejon, St. 101",
    monday="10:30am-8pm",
    tuesday="10:30am-8pm",
    wednesday="10:30am-8pm",
    thursday="10:30am-8pm",
    friday="10:30am-8pm",
    saturday="10:30am-8:30pm",
    sunday="10:30am-8pm",
    has_sockets=0,
    has_wifi=1,
    seats="20+",
    coffee_price=2.50,
    vegan_snacks=1,
    google_rating=4.4,
)

story_coffee = Cafes(
    name="Story Coffee Company",
    map_coords="38.8368583,-104.8224927",
    img_url="https://live.staticflickr.com/65535/52804662434_7a10ca43d7_m.jpg",
    address="120 East Bijou Street",
    monday="7am-4pm",
    tuesday="7am-4pm",
    wednesday="7am-4pm",
    thursday="7am-4pm",
    friday="Closed",
    saturday="9am-4pm",
    sunday="9am-4pm",
    has_sockets=0,
    has_wifi=0,
    seats="15+",
    coffee_price=2.50,
    vegan_snacks=0,
    google_rating=4.9,
)

third_space = Cafes(
    name="Third Space Coffee",
    map_coords="38.8979109,-104.8322053",
    img_url="https://live.staticflickr.com/65535/52803850262_74e04d96aa_m.jpg",
    address="5670 N Academy Blvd",
    monday="7am-6pm",
    tuesday="7am-6pm",
    wednesday="7am-6pm",
    thursday="7am-6pm",
    friday="Closed",
    saturday="7am-6pm",
    sunday="8am-6pm",
    has_sockets=0,
    has_wifi=1,
    seats="20+",
    coffee_price=3.50,
    vegan_snacks=0,
    google_rating=4.7,
)

humble = Cafes(
    name="Humble Coffee",
    map_coords="38.8630943,-104.8102393",
    img_url="https://live.staticflickr.com/65535/52803849402_0f99f0c02d_m.jpg",
    address="2103 Templeton Gap Rd",
    monday="6am-6pm",
    tuesday="6am-6pm",
    wednesday="6am-6pm",
    thursday="6am-6pm",
    friday="6am-6pm",
    saturday="6am-6pm",
    sunday="6am-6pm",
    has_sockets=0,
    has_wifi=0,
    seats="0",
    coffee_price=3.75,
    vegan_snacks=0,
    google_rating=4.8,
)


