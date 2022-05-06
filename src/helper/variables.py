import os

PROTOCOL = "https"
URL = os.environ.get("URL", "yandexlyc.herokuapp.com")
URL_PATH = PROTOCOL + "://" + URL

TRANSPORT_DATA = [['авиаперевозки', 167, 7], ['авиапочты', 167, 10],
                  ['транспортная перевозка', 200, 300],
                  ['контейнерная перевозка', 250, 250]]
CHOICES = ("авиаперевозки", "авиапочты", "транспортная перевозка",
               "контейнерная перевозка")