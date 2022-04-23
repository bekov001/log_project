from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, \
    RadioField, FileField, FloatField
from wtforms.validators import DataRequired


class AddCodeForm(FlaskForm):
    """
    Форма для добавления товара
    """
    choices = ("авиаперевозки", "авиапочты", "транспортная перевозка", "контейнерная перевозка")
    # choices = [el[0] for el in get(f"{PROTOCOL}://{URL}//api/weight_info").json()["info"]]
    title = StringField('название', validators=[DataRequired()])
    about = TextAreaField('Описание', validators=[DataRequired()])
    code = StringField('Код клиента', validators=[DataRequired()])
    amount = IntegerField('Количевство', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    delivery_type = RadioField('Типы доставки', choices=[(el,) * 2 for el in choices], default=choices[0])
    result = FloatField('Объем', render_kw={'readonly': True})
    weight = FloatField('Вес', validators=[DataRequired()])
    photos = FileField("Фото", validators=[FileRequired()])
    delivery_price = FloatField("Цена доставки", render_kw={'readonly': True})
    submit = SubmitField('Добавить')