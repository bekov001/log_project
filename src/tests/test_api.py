from requests import get
from json import loads

from src.helper import TRANSPORT_DATA, LOCAL


def test_weight_info():
    """Проверка на корректность данных"""
    assert (loads(get(LOCAL + "/api/weight_info").content)["info"] ==
            TRANSPORT_DATA)


def test_api_users():
    """Информацию нельзя получить без авторизации"""
    assert get(LOCAL + "/api/users").status_code == 401


def test_api_user():
    """Информацию об пользователе нельзя получить без авторизации"""
    assert get(LOCAL + "/api/user/1").status_code == 401


def test_register():
    """Информацию об пользователе нельзя получить без авторизации"""
    assert (get(LOCAL + "/api/register", json={"email": "hello123@example.com",
                                               "name": "Anuarka",
                                               "surname": "Bekov",
                                               "password": "1234"}).json())[
               "message"] == 'success'


def test_register_repeat_email():
    """Информацию об пользователе нельзя получить без авторизации"""
    assert (get(LOCAL + "/api/register", json={"email": "hello123@example.com",
                                               "name": "Anuarka",
                                               "surname": "Bekov",
                                               "password": "1234"}).json())[
               "message"] == 'Такой email уже существует'


def test_login():
    """Информацию об пользователе нельзя получить без авторизации"""
    assert (get(LOCAL + "/api/login",
                json={"email": "hello@example.com",
                      "password": "1234"}).json())["message"] == 'success'


def test_api_wrong_id():
    """Информацию об пользователе нельзя получить без авторизации"""
    assert get(LOCAL + "/api/user/99").status_code == 401


def test_api_wrong_word():
    """Такого маршрута нет, поэтому должно выйти 404"""
    assert get(LOCAL + "/api/user/hello").status_code == 404


def test_api_product_wrong_word():
    """Такого тоже маршрута нет, поэтому должно выйти 404"""
    assert get(LOCAL + "/api/product/hello").status_code == 404


def test_api_product_wrong_id():
    """Информацию об товаре нельзя получить без авторизации,
     поэтому должно выйти 401"""
    assert get(LOCAL + "/api/product/999").status_code == 401


def test_api_product():
    """Информацию об товаре нельзя получить без авторизации,
     поэтому должно выйти 401"""
    assert get(LOCAL + "/api/product/1").status_code == 401
