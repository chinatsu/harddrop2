from harddrop import db, forms
from harddrop.models import phpfox
from flask_login import login_required
from sqlalchemy import exc
from flask import Blueprint, request, flash, redirect, url_for, render_template

video = Blueprint('video', __name__, url_prefix='/video')

@video.route('/add', methods=['POST', 'GET'])
@login_required
def add_video():
    form = forms.AddVideo()
    if request.method == 'POST':
        form = forms.AddVideo(request.form)
        if form.validate():
            video = phpfox.Video(form.title.data, form.url.data, type=form.category.data, tags=form.tags.data, details=form.details.data)
            try:
                db.session.add(video)
                db.session.commit()
                flash("{} successfully submitted".format(video.vid_url))
                return redirect(url_for('list_videos'))
            except exc.IntegrityError:
                flash("{} has already been submitted".format(video.vid_url))
    return render_template('form.tpl', form=form)

@video.route('/list')
def list_videos():
    return "wew"
