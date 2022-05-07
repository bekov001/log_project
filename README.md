# Описание
Идея моего проекта создать похожий сайт на сайт логистических услуг
То есть на главное странице можно ввести трек код и получить информацию о товаре. А трек код в базу данных вносит администрация, для получения которой необходимо авторизоваться.
Можно указать текст, время и фото товара, а также увидеть цену доставки и его обьем
# Основные функции

1. Добавление товара
2. Авторизация/Регистрация
3. Просмотр товара по трек коду
Хотя главная функция - это получение информации о товаре по его трек коду

# Запуск
```
pip install -r requirements.txt
python app.py
```

# Для тестов
```
python -m pytest src/tests/test_api.py
```

# Подход к веткам
есть главная ветка main, также есть ветка work для основной работы, тестирования и релиза

# api в проекте
/api/weight_info - для получения транспортных данных (также самоиспользуется в js файлах)

/api/login (json={email, password}) - авторизация, необходимо json с ключами почты и пароля (используется при авторизации на сайте)

/api/register (json={"email", "name", "surname", "password"}) - регистрация, необходимо json с указанными ключами (используется при авторизации на сайте)
** при авторизации можно ввести необязательный параметр remember (True либо False)

### нужна авторизация
/api/users - получить всех пользователей

/api/user/{id} - получить пользователя по id

/api/products - получить все товары

/api/product/{id} - получить товар по id

# СРОКИ

27.03 - Заложена основа, созданы папки, сформирована идея  
27.03 - 15.04 -- я отдыхаю в лагере  
17.04 - Сделано добавление товара и его отображение по трек коду  
21.04 - Создание авторизации  
24.04 - Создание API и тестов  
1.05 - Чистка проекта, создание документации (комментарии в классах и функциях)  
5.05 - Публикация на Heroku, создание README, PEP8

# Особенность

Изначально это был фриланс проект и был под полным кураторством заказчика из Узбекистана, который имел в этом опыт, но после лагеря заказчик потерялся (