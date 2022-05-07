import flask
from flask import jsonify
from flask_login import login_required

from data import db_session
from data.products import Products

blueprint = flask.Blueprint(
    'product_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/products')
@login_required
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
@login_required
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
