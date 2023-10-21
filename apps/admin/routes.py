from flask import Blueprint
from apps.admin import views

admin_bp = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

admin_bp.add_url_rule('/dashboard/', view_func=views.AdminDashboardView.as_view('admin_dashboard'))
admin_bp.add_url_rule('/businesses/', view_func=views.BusinessesView.as_view('businesses'))
