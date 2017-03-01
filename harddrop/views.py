from harddrop import app, db
from harddrop.models import phpfox
import flask_login
from sqlalchemy import exc
from flask import request, redirect, url_for, render_template

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@app.route('/')
def index():
    a = ""
    for user in phpfox.User.query.all():
        a += "<p>{}</p>".format(user.email)
    return a

@app.route('/config')
def configure():
    return render_template('config.tpl')

@app.route('/register', methods=['POST', 'GET'])
def register_user():
    if request.method == 'POST':
        form = request.form
        if len(form['username']) < 3:
            pass
            # do stuff
        user = phpfox.User(form['username'], form['password'], form['email'])
        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        except exc.IntegrityError:
            return "{} is already registered.".format(user.user)

@app.route('/videos')
def list_videos():
    videos = ""
    for video in phpfox.Video.query.all():
        videos += "<p>{} - {}</p>".format(video.vid_title, video.vid_url)
    return videos

@app.route('/add/video', methods=['POST', 'GET'])
def add_video():
    if request.method == 'POST':
        form = request.form
        if len(form['title']) == 0:
            return "Title cannot be empty"
        if len(form['url']) == 0:
            return "URL cannot be empty"
        video = phpfox.Video(form['title'], form['url'], type=form['type'], tags=form['tags'], details=form['details'])
        try:
            db.session.add(video)
            db.session.commit()
            return redirect(url_for('list_videos'))
        except exc.IntegrityError:
            return "{} has already been submitted".format(video.vid_url)

    else:
        return """
        <!doctype html>
        <title>Add video</title>
        <form method=post>
            <div>
                <label for="title">Title:</label>
                <input type="text" id="title" name="title">
            </div>
            <div>
                <label for="type">Category:</label>
                <select id="type" name="type">
                    <option value="1">Other Tetris Videos</option>
                    <option value="16">Tetris Guideline Games</option>
                    <option value="13">Tetris Grandmaster Series</option>
                    <option value="17">Fan Made Games</option>
                </select>
            </div>
            <div>
                <label for="tags">Tags:</label>
                <input type="text" id="tags" name="tags">
            </div>
            <div>
                <label for="details">Details:</label>
                <textarea name="details" id="details"></textarea>
            </div>
            <div>
                <label for="url">URL:</label>
                <input type="text" id="url" name="url">
            </div>
            <div>
                <input type="submit" value="Submit">
            </div>
        </form>
        """
