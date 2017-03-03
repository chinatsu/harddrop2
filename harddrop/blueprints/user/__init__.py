from flask import Blueprint, render_template, redirect, url_for, flash
from harddrop.models import phpfox
from flask_login import login_required, current_user

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/')
@login_required
def own_profile():
    return render_template('profile.tpl', user=current_user)

@user.route('/<userid>')
@login_required
def profile(userid):
    person = phpfox.User.query.filter_by(id=userid).first()
    if person == None:
        flash('User not found')
        return redirect(url_for('index'))
    return render_template('profile.tpl', user=person)
