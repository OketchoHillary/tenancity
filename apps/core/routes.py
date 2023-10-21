from flask import request, jsonify, Blueprint

from apps.core.views import IndexView, DashboardView


# from models.core import Business

core_bp = Blueprint('core', __name__, template_folder='templates', static_folder='static')

# Register the class-based view with the blueprint
core_bp.add_url_rule('/', view_func=IndexView.as_view('index'))
core_bp.add_url_rule('/<int:pk>/', view_func=DashboardView.as_view('dashboard'))

