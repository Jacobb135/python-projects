from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from data import Cafes, User, db, loyal_coffee, wayfinder, hold_fast, mission_coffee, coffee_zone, story_coffee, third_space, humble
import folium
import datetime
from loginform import LoginForm, RegisterForm
import pendulum
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

# with app.app_context():
#     db.create_all()
#     db.session.add(loyal_coffee)
#     db.session.add(wayfinder)
#     db.session.add(mission_coffee)
#     db.session.add(hold_fast)
#     db.session.add(coffee_zone)
#     db.session.add(story_coffee)
#     db.session.add(third_space)
#     db.session.add(humble)
#     db.session.commit()


@login_manager.user_loader
def load_user(User_id):
    return User.query.get(User_id)


@app.route("/", methods=['GET', 'POST'])
def home():
    cafes = Cafes.query.order_by(Cafes.google_rating.desc()).all()
    map_pins = Cafes.query.order_by(Cafes.map_coords).all()

    day_of_the_week_array = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    date = str(datetime.datetime.today()).split(" ")[0]
    today = pendulum.parse(date)
    day = day_of_the_week_array[today.day_of_week - 1]

    map = folium.Map(
        location=[38.8630943, -104.8102393],
        zoom_start=11,
    )

    for cafe in map_pins:
        num = cafe.map_coords
        num1 = num.split(',')[0]
        num2 = num.split(',')[1]
        num3 = float(num1), float(num2)
        folium.Marker(num3, popup=f"<i>{cafe.name}</i>").add_to(map)
    map.save('templates/map.html')

    return render_template("index.html", cafes=cafes, map=map._repr_html_(), day=day)


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        if User.query.filter_by(email=form.email.data).first():
            flash("You've signed up with that email! Login instead")
            return redirect(url_for('login'))

        hashed_pw = generate_password_hash(
            form.password.data,
            method="pbkdf2:sha256",
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            password=hashed_pw,
            name=form.name.data,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('home'))

    return render_template('register.html', form=form, current_user=current_user)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist. Try again")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again.")
        else:
            login_user(user)
            return redirect(url_for('home'))
    return render_template("login.html", form=form, current_user=current_user)

    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
