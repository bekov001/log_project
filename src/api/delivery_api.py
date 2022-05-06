import flask
from flask import jsonify

from src.helper.variables import TRANSPORT_DATA

blueprint = flask.Blueprint(
    'delivery_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/weight_info', methods=['GET'])
def get_data():
    """Дает информацию о транспортных значениях, (название, обьемный вес и цена)"""
    return jsonify({"info": TRANSPORT_DATA})