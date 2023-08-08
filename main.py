
from flask import Flask
from database import Database
from flight_checker import FlightChecker

# -------------------Flask------------------#
app = Flask(__name__)


# -------------------CONTROL------------------#
fc = FlightChecker()

db = Database()
