import os

from flask_login import LoginManager

PROTOCOL = "https"
URL = os.environ.get("URL", "yandexlyc.herokuapp.com")
URL_PATH = PROTOCOL + "://" + URL
LOCAL = os.environ.get("LOCAL", "http://192.168.1.164:5000/")
TRANSPORT_DATA = [['авиаперевозки', 167, 7], ['авиапочты', 167, 10],
                  ['транспортная перевозка', 200, 300],
                  ['контейнерная перевозка', 250, 250]]
CHOICES = ("авиаперевозки", "авиапочты", "транспортная перевозка",
           "контейнерная перевозка")
