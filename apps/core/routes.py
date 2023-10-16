from flask import request, jsonify, Blueprint

# from models.core import Business

core_bp = Blueprint('core', __name__, template_folder='templates', static_folder='static')


@core_bp.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            # new_car = Business(name=data['name'], location=data['location'])
            # new_car.save()
            # return jsonify({"message": f"car {new_car.name} has been created successfully."})
        else:
            return jsonify({"error": "The request payload is not in JSON format"})
    # return render_template('core/index.html')
