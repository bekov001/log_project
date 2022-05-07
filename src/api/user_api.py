import flask
from flask import jsonify, request
from flask_login import login_required, login_user, current_user, LoginManager

from data import db_session
from data.user import User
blueprint = flask.Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)
src = ['id', 'name', 'surname', 'email', "password"]

login_manager = LoginManager()


@blueprint.record_once
def on_load(state):
    login_manager.init_app(state.app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@blueprint.route('/api/users')
@login_required
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
@login_required
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


@blueprint.route('/api/register')
def api_register():
    """API регистрация"""
    data = request.json
    src = ["email", "name", "surname", "password", "remember"]
    message = "Произошла ошибка"
    user_id = ""
    if not data or not (all(i in src for i in data.keys()) and
                        len(src) + 1 > len(data.keys()) >=
                        len(src) - 1):
        message = "Неверный json запрос"
    else:
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == data["email"]).first():
            message = "Такой email уже существует"
        else:
            user = User()
            user.email = data["email"]
            user.name = data["name"]
            user.surname = data["surname"]
            user.set_password(data["password"])
            db_sess.add(user)
            db_sess.commit()
            user_id = user.id
            login_user(user, remember=data.get("remember", False))
            message = "success"
    return {"message": message, "user_id": user_id}


@blueprint.route('/api/login')
def api_login():
    """API получить одного пользователя по id"""
    data = request.json
    src = ["email", "password", "remember"]
    message = "Произошла ошибка"
    user_id = -1
    if not data or not (all(i in src for i in data.keys()) and
                        len(src) + 1 > len(data.keys()) >=
                        len(src) - 1):
        message = "Неверный json запрос"
    else:
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == data["email"]).first()
        if user and user.check_password(data["password"]):
            user_id = user.id
            message = "success"
            login_user(user, remember=data.get("remember", False))
        else:
            message = "Неправильный логин или пароль"
    return {"message": message, "user_id": user_id}
