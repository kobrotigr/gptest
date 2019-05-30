import requests
from collections import namedtuple
from xml.etree import ElementTree


Flight = namedtuple('Flight', 'price number datetime')


NBRB_API_URL = 'https://www.nbrb.by/Services/XmlExRates.aspx'


def eur_to_byn_converter(eur):
    response = requests.get(NBRB_API_URL)
    tree = ElementTree.fromstring(response.content)
    eur_rate = float(tree[5][4].text)
    return round(eur*eur_rate, 1)
