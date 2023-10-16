from flask import request, jsonify, Blueprint


auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')


@auth_bp.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            # new_car = Business(name=data['name'], location=data['location'])
            # new_car.save()
            # return jsonify({"message": f"car {new_car.name} has been created successfully."})
        else:
            return jsonify({"error": "The request payload is not in JSON format"})
    # return render_template('core/index.html')
