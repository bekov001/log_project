import os

from flask import Flask, redirect, render_template
from werkzeug.utils import secure_filename

from src.api import delivery_api
from src.data import db_session
from src.data.products import Products
from src.data.user import User
from src.forms.add_code import AddCodeForm
from src.forms.authentication_form import RegisterForm, LoginForm
from src.forms.input_form import FindForm

from flask_login import LoginManager, login_user, login_required, logout_user, \
    current_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/code.db?check_same_thread=False"
login_manager = LoginManager()
login_manager.init_app(app)
# img_path = "static/img/"
img_path = "/home/anuarka/logistic/static/img/"
# app.config['RESIZE_URL'] = 'https://mysite.com/'
# app.config['RESIZE_ROOT'] = '/static/img/'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/", methods=["POST", "GET"])
def index():
    """Найти товар по коду"""
    form = FindForm()
    result = []
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        result = db_sess.query(Products).filter(Products.code == form.code.data).all()
        data = ["volume", "delivery_type", "delivery_price", "amount",
                "weight"]
        print(result)
    return render_template("index.html", form=form, result=result)


@app.route("/add_code", methods=["POST", "GET"])
@login_required
def add_code():
    """Добавление кода"""
    form = AddCodeForm()

    if form.validate_on_submit():
        f = form.photos.data
        filename = secure_filename(f.filename)
        path = os.path.join(
            img_path, filename
        )
        f.save(path)

        db_sess = db_session.create_session()
        product = Products(title=form.title.data, about=form.about.data,
                           price=form.price.data, code=form.code.data,
                           path_to_image="/static/img/"+filename,
                           delivery_price=form.delivery_price.data,
                           weight=form.weight.data, volume=form.result.data,
                           amount=form.amount.data,
                           delivery_type=form.delivery_type.data)
        db_sess.add(product)
        db_sess.commit()
        return redirect("/")
    return render_template("add_code.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('authentication/login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('authentication/login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = User()
        user.email = form.email.data
        user.name = form.name.data
        user.surname = form.surname.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        login_user(user, remember=form.remember_me.data)
        return redirect("/")
    return render_template('authentication/register.html', title='Авторизация', form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')


def main():
    """Главная функция запуска"""
    db_session.global_init("db/code.db")
    app.register_blueprint(delivery_api.blueprint)
    app.debug = True
    app.run(host="0.0.0.0", port=5000)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()