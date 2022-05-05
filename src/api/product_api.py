import flask
from flask import jsonify

from src.data import db_session
from src.data.products import Products

blueprint = flask.Blueprint(
    'product_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/products')
def get_products():
    """API получить все товары"""
    db_sess = db_session.create_session()
    news = db_sess.query(Products).all()
    return jsonify(
        {
            'products':
                [item.to_dict()
                 for item in news]
        }
    )


@blueprint.route('/api/product/<int:id>')
def get_product(id):
    """API получить один товар по id"""
    db_sess = db_session.create_session()
    news = db_sess.query(Products).get(id)
    if news:
        return jsonify(
            {
                'product':
                    news.to_dict()

            }
        )
    return "404"