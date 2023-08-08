import requests
from flask import Flask
from database import Database
from flight_checker import FlightChecker

# -------------------Flask------------------#
app = Flask(__name__)


# -------------------IATA CODE------------------#
fc = FlightChecker()
# places = ['phoenix', 'san diego', 'barcelona']
# iata = fc.get_codes(places=places)
# print(iata)

# -----------------SUPABASE DATABASE-----------------#

db = Database()
user = db.get_user('jesse.turner2021@gmail.com')
# db.add_user(email='jesse.turner2021@gmail.com', fly_from='PHX', fly_to=["MCO", 'LON'], date_from='2024-4-13', date_to='2024-4-13',return_from='2024-4-20', return_to='2024-4-20', price_to=[1, 4])
# TODO: HAD PROBLEM WITH SAYING RETURN FROM IN USERS DOES NOT EXIST


# -----------------FLIGHT CHECK-----------------#
print(user)
fc.check_flight(user=user)
# TODO: FINISHING ON FLIGHT CHECKER
# MAKE SURE THE PRICE WORKS