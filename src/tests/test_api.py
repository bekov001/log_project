from requests import get
from json import load, loads

from src.helper.variables import URL_PATH, TRANSPORT_DATA


def test_empty():
    print(loads(get(URL_PATH).json()["info"]) == TRANSPORT_DATA)


test_empty()