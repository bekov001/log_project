from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class FindForm(FlaskForm):
    """Форма для получения товара по трек коду"""
    code = StringField('Track Code', validators=[DataRequired()])
    submit = SubmitField('Submit')