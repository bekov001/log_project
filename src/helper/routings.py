import os

from flask import Flask, redirect, render_template
from requests import get
from werkzeug.utils import secure_filename

from flask_login import login_user, login_required, logout_user

from data import db_session
from data.products import Products
from data.user import User
from forms import LoginForm, RegisterForm
from forms.add_code import AddCodeForm
from forms.input_form import FindForm
from helper import LOCAL, URL_PATH
from helper.func import init_app
app = Flask(__name__, root_path=os.getcwd() if os.environ.get("DEPLOY", "FALSE") else "src")
login_manager = init_app(app)
img_path = "src/static/img/"


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
        result = db_sess.query(Products).filter(Products.code ==
                                                form.code.data).all()
    return render_template("index.html", form=form, result=result)


@app.route("/add_code", methods=["POST", "GET"])
@login_required
def add_code():
    """страница Добавления товара в БД"""
    form = AddCodeForm()

    if form.validate_on_submit():
        # сохраняем изображение
        f = form.photos.data
        filename = secure_filename(f.filename)
        path = os.path.join(
            img_path, filename
        )
        f.save(path)

        db_sess = db_session.create_session()
        product = Products(title=form.title.data, about=form.about.data,
                           price=form.price.data, code=form.code.data,
                           path_to_image="/static/img/" + filename,
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
    """страница авторизации"""
    form = LoginForm()
    message = ""
    if form.validate_on_submit():
        data = {"email": form.email.data,
                "password": form.password.data,
                "remember": form.remember_me.data}
        if os.environ.get("DEPLOY", "FALSE") == "FALSE":
            path = LOCAL
        else:
            path = URL_PATH
        data = get(path + "/api/login", json=data).json()
        user_id, message = data["user_id"], data["message"]
        db_sess = db_session.create_session()
        if message == "success":
            login_user(db_sess.query(User).filter(User.id == user_id).first())
            return redirect("/")
    return render_template('authentication/login.html', title='Авторизация',
                           form=form, message=message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """страница Регистрации"""
    form = RegisterForm()
    message = ""
    if form.validate_on_submit():
        data = {"email": form.email.data,
                "name": form.name.data,
                "surname": form.surname.data,
                "password": form.password.data,
                "remember": form.remember_me.data}
        if os.environ.get("DEPLOY", "FALSE") == "FALSE":
            path = LOCAL
        else:
            path = URL_PATH
        data = get(path + "/api/register", json=data).json()
        user_id, message = data["user_id"], data["message"]
        db_sess = db_session.create_session()
        if message == "success":
            login_user(db_sess.query(User).filter(User.id == user_id).first())
            return redirect("/")
    return render_template('authentication/register.html',
                           title='Авторизация', form=form, message=message)


@app.route('/logout')
@login_required
def logout():
    """Функция выхода"""
    logout_user()
    return redirect("/")
