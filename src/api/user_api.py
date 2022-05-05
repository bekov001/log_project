import flask
from flask import jsonify

from src.data import db_session
from src.data.user import User

blueprint = flask.Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)
src = ['id', 'name', 'surname', 'email', "password"]


@blueprint.route('/api/users')
def get_users():
    """API получить всех пользователей"""
    db_sess = db_session.create_session()
    news = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=src[:-1])
                 for item in news]
        }
    )


@blueprint.route('/api/user/<int:id>')
def get_user_one(id):
    """API получить одного пользователя по id"""
    db_sess = db_session.create_session()
    news = db_sess.query(User).get(id)
    if news:
        return jsonify(
            {
                'user':
                    news.to_dict(only=src[:-1])

            }
        )
    return "404"