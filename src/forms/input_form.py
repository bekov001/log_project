from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class FindForm(FlaskForm):
    """Форма для получения товара по трек коду"""
    code = StringField('Track Code', validators=[DataRequired()])
    submit = SubmitField('Submit')
