from requests import get
from json import load, loads

from src.helper.variables import URL_PATH, TRANSPORT_DATA


def test_weight_info():
    assert (loads(get(URL_PATH + "/api/weight_info").content)["info"] ==
          TRANSPORT_DATA)

def test_api():
    assert (loads(get(URL_PATH + "/api/weight_info").content)["info"] ==
          TRANSPORT_DATA)
