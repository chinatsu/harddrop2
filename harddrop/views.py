from harddrop import app, db, forms, nav
from harddrop.models import phpfox
from harddrop.blueprints.user import user
from harddrop.blueprints.video import video
from flask_login import login_user, login_required, logout_user, current_user
from flask_nav.elements import *
from harddrop.nav_elements import ExtendedNavbar, CustomBootstrapRenderer
from sqlalchemy import exc
from flask import request, redirect, url_for, render_template, flash
from datetime import datetime

app.register_blueprint(user)
app.register_blueprint(video)

@app.errorhandler(401)
def must_login(e):
    flash("Login required")
    return redirect(url_for('login'))

@app.route('/')
def index():
    return render_template('index.tpl')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('settings'))
    form = forms.LoginForm()
    if request.method == 'POST' and form.validate():
        form = forms.LoginForm(request.form)
        print(request.data)
        user = phpfox.User.query.filter_by(user=form.username.data).first()
        if user == None:
            flash('User not found')
            return redirect(url_for('login'))
        if user.password == form.password.data:
            login_user(user)
            flash('Logged in successfully')
            return redirect(url_for('index'))
    return render_template('form.tpl', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/settings')
@login_required
def settings():
    return render_template('settings.tpl')

@app.route('/register', methods=['POST', 'GET'])
def register_user():
    form = forms.Register()
    if request.method == 'POST':
        form = forms.Register(request.form)
        if form.validate():
            if form.dob.data:
                try:
                    dob = datetime.strptime(form.dob.data, '%Y/%m/%d')
                except:
                    return redirect(url_for('register_user'))
                user = phpfox.User(
                    form.username.data,
                    form.password.data,
                    form.email.data,
                    gender=form.gender.data,
                    year=dob.year,
                    month=dob.month,
                    day=dob.day,
                )
            else:
                user = phpfox.User(
                    form.username.data,
                    form.password.data,
                    form.email.data,
                    gender=form.gender.data
                )
            try:
                db.session.add(user)
                db.session.commit()
                flash('User successfully registered')
                return redirect(url_for('login'))
            except exc.IntegrityError:
                flash('{} has already been registered'.format(user.user))
                return redirect(url_for('register_user'))
    return render_template('form.tpl', form=form)

@nav.navigation()
def top_nav():
    if current_user.is_authenticated:
        return ExtendedNavbar(
            title=View('Hard Drop', 'index'),
            root_class='navbar navbar-inverse',
            right_items=(
                Text('The inbox icon should be here'),
                Subgroup(current_user.user,
                    View('Profile', 'user.own_profile'),
                    View('Settings', 'settings'),
                    Separator(),
                    View('Log out', 'logout')
                )
            )
        )
    else:
        return ExtendedNavbar(
            title=View('Hard Drop', 'index'),
            root_class='navbar navbar-inverse',
            right_items=(
                View('Log in', 'login'),
                View('Register', 'register_user'))
        )

nav.register_element('top_nav', top_nav)
