import os

from api import delivery_api, product_api, user_api

from data import db_session
from helper.routings import app


def main(app):
    """Главная функция запуска"""
    db_session.global_init("src/db/db.db")
    app.register_blueprint(delivery_api.blueprint)
    app.register_blueprint(product_api.blueprint)
    app.register_blueprint(user_api.blueprint)
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main(app)
