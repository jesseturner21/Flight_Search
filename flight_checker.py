import requests


class FlightChecker():
    def __init__(self):
        self.API_KEY = 'ow2UEViSjaLV3A-umCnZ8MrU0vdni6JG'
        self.SEARCH_URL = 'https://api.tequila.kiwi.com/v2/search'
        self.IATA_URL = 'https://api.tequila.kiwi.com/locations/query'

        self.header = {
            'apikey': self.API_KEY,
        }

    def get_codes(self, places):
        codes = []
        for name_of_place in places:
            parameters = {
                'term': name_of_place,
            }
            iata_code = requests.get(self.IATA_URL, headers=self.header, params=parameters).json()['locations'][0]['code']
            codes.append(iata_code)

        return codes

    def check_flight(self, user):
        for i in range(len(user['fly_to'])):
            parameters = {
                "fly_from": user['fly_from'],
                "fly_to": user['fly_to'][i],
                "date_from": user['date_from'],
                "date_to": user["date_to"],
            }
            response = requests.get(self.SEARCH_URL, headers=self.header, params=parameters).json()
            print(response)