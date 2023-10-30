from flask import Blueprint

from apps.auth.views import SignupView, SigninView, activate

auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

auth_bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))
auth_bp.add_url_rule('/login/', view_func=SigninView.as_view('login'))
auth_bp.add_url_rule('/activate/<string:token>/', 'activate', activate)

