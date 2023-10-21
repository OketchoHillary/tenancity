from flask import render_template, redirect, flash, url_for
from flask.views import MethodView

from apps.admin.forms import AddBusinessForm
from models.core import Business


class AdminDashboardView(MethodView):

    def get(self):
        return render_template('admin/dashboard.html')


class BusinessesView(MethodView):
    def get(self):
        form = AddBusinessForm()
        businesses = Business.query.all()
        return render_template('admin/businesses.html', businesses=businesses, form=form)

    def post(self):
        form = AddBusinessForm()
        if form.validate_on_submit():
            name = form.name.data
            location = form.location.data
            business = Business(name=name, location=location)
            business.save()
            flash('Successfully added a business', 'success')
            return redirect(url_for('admin.businesses'))
        else:
            flash('Business creation failed.', 'error')
            return redirect(url_for('admin.businesses'))
