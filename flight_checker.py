import requests
import os


class FlightChecker:
    def __init__(self):
        self.TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY')
        self.SEARCH_URL = 'https://api.tequila.kiwi.com/v2/search'
        self.IATA_URL = 'https://api.tequila.kiwi.com/locations/query'

        self.header = {
            'apikey': self.TEQUILA_API_KEY,
        }

    def get_codes(self, places):
        codes = []
        for name_of_place in places:
            parameters = {
                'term': name_of_place,
            }
            iata_code = requests.get(self.IATA_URL, headers=self.header, params=parameters).json()['locations'][0][
                'code']
            codes.append(iata_code)

        return codes

    def get_names(self, codes):
        names = []
        for code in codes:
            parameters = {
                'term': code,
            }
            try:
                name = requests.get(self.IATA_URL, headers=self.header, params=parameters).json()['locations'][0]['city'][
                    'name']
            except:
                name = requests.get(self.IATA_URL, headers=self.header, params=parameters).json()['locations'][0][
                    'name']
            names.append(name)

        return names

    def check_flight(self, user):
        flights = []
        for i in range(len(user['fly_to'])):
            parameters = {
                "fly_from": user['fly_from'],
                "fly_to": user['fly_to'][i],
                "date_from": user['date_from'],
                "date_to": user["date_to"],
                "return_from": user['return_from '],
                "return_to": user["return_to"],
                "price_to": user['price_to'][i],
                'curr': 'USD',
            }
            response = requests.get(self.SEARCH_URL, headers=self.header, params=parameters).json()

            if len(response['data']) > 0:
                flight_dict = {
                    'cityFrom': response['data'][0]['cityFrom'],
                    'cityTo': response['data'][0]['cityTo'],
                    'price': response['data'][0]['price'],
                }
                flights.append(flight_dict)

        return flights
