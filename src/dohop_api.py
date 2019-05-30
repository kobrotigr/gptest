import requests
import json

from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

from utils import Flight


# retry request up to five times if 500/503 status codes are returned
session = requests.Session()
retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 503])
session.mount('https://', HTTPAdapter(max_retries=retries))


def requests_get(url):
    r = session.get(url, params={'ticketing-partner': "36fd0d405f4541b7be72d117b574a70f"})
    r.raise_for_status()
    return r.json()


def get_dohop_flights_api(airport_from, airport_to, departure_date, return_date=None):
    params = {
        'airport_from': airport_from,
        'to': airport_to,
        'dep_date': departure_date,
    }
    
    url = 'https://partners-api.dohop.com/api/v3/ticketing/dohop-connect/DE/EUR/{airport_from}/{to}/{dep_date}'
    url = url.format(**params)
    if return_date:
        url = url + '/%s' % (return_date)
    r_dep = requests_get(url)
    with open('data/dohop_data.json', 'w') as f:
        json.dump(r_dep, f)
        
    for fare in r_dep['fares']:
        yield Flight(fare['fare'], 'None', 'None')


if __name__ == '__main__':
    get_dohop_flights_api('KEF', 'NCE', '2019-08-13')
