import flask
from flask import jsonify

blueprint = flask.Blueprint(
    'delivery_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/weight_info', methods=['GET'])
def get_data():
    """Дает информацию о транспортных значениях, (название, обьемный вес и цена)"""
    data = [("авиаперевозки", 167, 7), ("авиапочты", 167, 10),
            ("транспортная перевозка", 200, 300),
            ("контейнерная перевозка", 250, 250)]

    return jsonify({"info": data})