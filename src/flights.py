import requests
from datetime import datetime
from operator import attrgetter

from utils import Flight


class Flights:
    KIWI_API_URL = 'https://api.skypicker.com/flights'
    kiwi_params = {
        "flyFrom": None,
        "to": None,
        "dateFrom": None,
        "partner": "picky",
    }
    _flights = None

    def __init__(self, airport_from, airport_to, departure_date, return_date=None):
        self._airport_from = airport_from
        self._airport_to = airport_to
        self._departure_date = departure_date
        self._return_date = return_date
        self._kiwi_dep_date = '/'.join(reversed(departure_date.split('-')))
        self._flights = []

    def __repr__(self):
        """Itinerary representation human-readable formatted should include:
      - price
      - flights details:
          flight numbers, dates and time of each flight."""
        if self._flights:
            return str(self._flights[:10])
        return 'No Flights'

    def get_cheapest(self):
        if self._flights:
            cheapest_flights = sorted(self._flights, key=attrgetter('price'))
            return cheapest_flights[0]
        return self.__str__()

    def sort_by_time(self):
        """to sort all itineraries received from both APIs by departure time."""
        self._flights = sorted(self._flights, key=attrgetter('datetime'))

    def get_flights(self):
        self.get_kiwi_flights()
        self.get_dohop_flights()
        return self._flights

    def get_kiwi_flights(self):
        self.kiwi_params['flyFrom'] = self._airport_from
        self.kiwi_params['to'] = self._airport_to
        self.kiwi_params['dateFrom'] = self._kiwi_dep_date
        if self._return_date:
            self.kiwi_params['dateTo'] = '/'.join(reversed(self._return_date.split('-')))

        r = requests.get(url=self.KIWI_API_URL, params=self.kiwi_params)
        if r.status_code == requests.codes.ok:
            response_date = r.json()

            for f in response_date['data']:
                timestamp = f['dTime']
                dtime = datetime.fromtimestamp(timestamp)
                flight = Flight(f['price'], f['id'], str(dtime))
                self._flights.append(flight)
            return response_date
        # recordings of raw requests and responses from kiwi API
        with open('rawrequests.txt', 'a') as f:
            f.write(r.url + '\n')

    def get_dohop_flights(self):
        pass
