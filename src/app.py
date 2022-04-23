import os

from flask import Flask, redirect, render_template
from werkzeug.utils import secure_filename

from src.api import delivery_api
from src.data import db_session
from src.data.products import Products
from src.forms.add_code import AddCodeForm
from src.forms.input_form import FindForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/code.db?check_same_thread=False"
# img_path = "static/img/"
img_path = "/home/anuarka/logistic/static/img/"
# app.config['RESIZE_URL'] = 'https://mysite.com/'
# app.config['RESIZE_ROOT'] = '/static/img/'

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


def main():
    """Главная функция запуска"""
    db_session.global_init("src/db/code.db")
    app.register_blueprint(delivery_api.blueprint)
    app.debug = True
    app.run(host="0.0.0.0", port=5000)


if __name__ == '__main__':
    main()