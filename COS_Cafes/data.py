# https://laptopfriendly.co/london
#
# class Cafes(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(250), unique=True)
#     map_url = db.Column(db.String(250), nullable=False)
#     img_url = db.Column(db.String(250), nullable=False)
#     has_sockets = db.Column(db.Integer, nullable=False)
#     has_wifi = db.Column(db.Integer, nullable=False)
#     seats = db.Column(db.String(10), nullable=False)
#     coffee_price = db.Column(db.Float, nullable=False )
#     vegan_snacks = db.Column(db.Integer, nullable=False)
#     google_rating = db.Column(db.Float, nullable=False)
#
#     def __repr__(self):
#         return f"<Cafe {self.title}>"
#
#
# with app.app_context():
#     db.create_all()
#     loyal_coffee = Cafes(
#         name="Loyal Coffee",
#         map_url="https://www.google.com/maps/place/Loyal+Coffee/@39.0024988,-104.7995794,15z/data=!4m2!3m1!1s0x0:0xf2e39d33d9e94468?sa=X&ved=2ahUKEwiPk734wpX-AhUFOH0KHQB2ArQQ_BJ6BQiCARAI",
#         img_url="https://www.google.com/maps/uv?pb=!1s0x87134d237e490bc7%3A0xf2e39d33d9e94468!3m1!7e115!4shttps%3A%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipMBeyHA5gO8-YAerL8uEnoKaIBgK1Gpp5VTO9BP%3Dw260-h175-n-k-no!5scolorado%20springs%20coffee%20shops%20-%20Google%20Search!15sCgIgAQ&imagekey=!1e10!2sAF1QipOeeJTklkUEoPbIl3h8ReuPml7PuPKWETsC709X&hl=en&sa=X&ved=2ahUKEwiC45Oa2ZP-AhVglmoFHb-BDKcQ7ZgBKAB6BAggEAI",
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
#         img_url="https://www.google.com/maps/uv?pb=!1s0x8713498376dca035%3A0x8a228a501f21c71b!3m1!7e115!4shttps%3A%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPd6DM3PXa_uvSgPHKdtWkRDBZ1rSUYP1IairND%3Dw260-h175-n-k-no!5scolorado%20springs%20coffee%20shops%20-%20Google%20Search!15sCgIgAQ&imagekey=!1e10!2sAF1QipO6FYTLqt5LzrMNpxRW0IbDU5ffxLQQSzTcidCC&hl=en&sa=X&ved=2ahUKEwjQ7OWC25P-AhUfm2oFHeX6DR8Q7ZgBKAB6BAgcEAI",
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
#         img_url="https://www.google.com/maps/uv?pb=!1s0x87134cfd22497c1d%3A0xb14393830726ca4c!3m1!7e115!4shttps%3A%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipO5thWsQSWknNd3OhHLyK8CGnL20vPeA1mzB3iP%3Dw260-h175-n-k-no!5scolorado%20springs%20coffee%20shops%20-%20Google%20Search!15sCgIgAQ&imagekey=!1e10!2sAF1QipPoyBKH3K4IbIiEiUEOlr2aLUu1-04yRiNtE-lB&hl=en&sa=X&ved=2ahUKEwjS4szz25P-AhXMmWoFHXMoBFsQ7ZgBKAB6BAgbEAI",
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
#         img_url="https://www.google.com/maps/uv?pb=!1s0x87134f1c44a2de39%3A0xe3b8021bf99e4d31!3m1!7e115!4shttps%3A%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOxc_GTRhuhUlSfgCY6yS7O3TUFxxW7W8VT22gX%3Dw260-h175-n-k-no!5scolorado%20springs%20coffee%20shops%20-%20Google%20Search!15sCgIgAQ&imagekey=!1e10!2sAF1QipPE1iLgEgFz8_mez9DV_MaxjtADi01A1BNwx4vW&hl=en&sa=X&ved=2ahUKEwjqwbKf3ZP-AhUsnGoFHd58DngQ7ZgBKAB6BAggEAI",
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
#         img_url="https://www.google.com/maps/place/Coffee+and+Tea+Zone/@39.0108152,-104.8065537,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipPjxWl-fMtjdKIVjaU2r0KQWQxzIARiZm2ArN23!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPjxWl-fMtjdKIVjaU2r0KQWQxzIARiZm2ArN23%3Dw203-h114-k-no!7i2048!8i1152!4m7!3m6!1s0x87134d1897b0065d:0xac29dfe3d662851!8m2!3d39.0109237!4d-104.8063765!10e5!16s%2Fg%2F1263yybnt",
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
#         img_url="https://lh3.googleusercontent.com/p/AF1QipNELih9eUa3hN1i_JKdb_fgW13QHn8xUA4tNijU=s680-w680-h510",
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
#         img_url="https://lh3.googleusercontent.com/p/AF1QipNnJmHZiuxkvXDBj0-KSKhALRmAVf7Tu76lee1s=s680-w680-h510",
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
#         img_url="https://lh3.googleusercontent.com/p/AF1QipN8gC9Om9SExLE1jeWD2_UE9Tn6-Ia4FtyK_0wV=s680-w680-h510",
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
#
