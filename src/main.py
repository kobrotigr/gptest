import argparse

from flights import Flights


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("airport_from", help='airport from.', type=str)
    parser.add_argument("airport_to", help='airport to.', type=str)
    parser.add_argument("departure_date", help='departure date.', type=str)

    parser.add_argument("--return", default=None, help='return date (default: None).')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    airport_from = args.__dict__.get('airport_from')
    airport_to = args.__dict__.get('airport_to')
    departure_date = args.__dict__.get('departure_date')
    return_date = args.__dict__.get('return', None)

    flights = Flights(airport_from, airport_to, departure_date, return_date)
    flights.get_flights()
    flights.sort_by_time()

    print("Cheapest: " + str(flights.get_cheapest()))
    print("Cheapest BYN: " + str(flights.get_cheapest_byn()))
    
    print(flights)
