import flask_login
from flask import render_template, abort
from flask.views import MethodView
from flask_login import login_required

from models.core import Business
from utils import login_manager


class IndexView(MethodView):
    def get(self):
        return render_template('core/index.html')


class DashboardView(MethodView):

    @login_manager.user_loader
    def get(self):
        user = flask_login.current_user
        print(user)
        # business = Business.query.filter_by(id=pk).first()
        # if business is not None:
        #     user = flask_login.current_user
        #     print(user)
        return render_template('core/dashboard.html')



# class DashboardView(MethodView):
#
#     @login_required
#     def get(self, pk):
#         business = Business.query.filter_by(id=pk).first()
#         if business is not None:
#             user = flask_login.current_user
#             print(user)
#             return render_template('core/dashboard.html')
#         else:
#             return abort(404)
