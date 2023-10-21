from flask import render_template, abort
from flask.views import MethodView

from models.core import Business
from utils import login_manager


class IndexView(MethodView):
    def get(self):
        return render_template('core/index.html')


class DashboardView(MethodView):

    def get(self, pk):
        business = Business.query.filter(id=pk).first()
        if not business is None:

            return render_template('core/dashboard.html')
        else:
            return abort(404)
