from app import myapp_obj
from flask import render_template, flash, Flask, request, redirect, url_for
from app.forms import LoginForm

name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myapp_obj.route("/", methods=['GET', 'POST'])
def home():
	form = LoginForm()
	if request.method == "POST":
		city = form.input.data
		flash(f'{city}')
		return render_template('home.html', name=name, city_names=city_names, form=form)
	return render_template('home.html', name=name, city_names=city_names, form=form)
