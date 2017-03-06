from harddrop import db, login
from flask_login import UserMixin
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

@login.user_loader
def get_user(ident):
  return User.query.get(int(ident))

# modeled after the current phpfox tables

class User(db.Model, UserMixin):
    __tablename__ = 'phpfox_user'
    id = db.Column('id', INTEGER(11), primary_key=True)
    type = db.Column('type', TINYINT(4), default=3)
    user = db.Column('user', VARCHAR(25), unique=True)
    password = db.Column('password', VARCHAR(90))
    email = db.Column('email', VARCHAR(50))
    gender = db.Column('gender', MEDIUMINT(9), default=0)
    age = db.Column('age', CHAR(2), default='')
    day = db.Column('day', CHAR(2), default='')
    month = db.Column('month', CHAR(2), default='')
    year = db.Column('year', VARCHAR(4), default='')
    location = db.Column('location', MEDIUMINT(9), default=0)
    signup = db.Column('signup', INTEGER(11), default=0)
    signup_ip = db.Column('signup_ip', VARCHAR(20), default=0)
    login = db.Column('login', INTEGER(11), default=0)
    login_ip = db.Column('login_ip', VARCHAR(20), default='')
    rec = db.Column('rec', VARCHAR(20), default='')
    update = db.Column('update', VARCHAR(20), default='')
    headline = db.Column('headline', TEXT, default='')
    views = db.Column('views', INTEGER(11), default=0)
    css = db.Column('css', INTEGER(11), default=0)
    rateon = db.Column('rateon', CHAR(1), default='')
    verify = db.Column('verify', TINYINT(1), default='')
    verifycode = db.Column('verifycode', VARCHAR(20), default='')
    videon = db.Column('videon', CHAR(1), default='')
    p_update = db.Column('p_update', VARCHAR(10), default='')
    music_video = db.Column('music_video', VARCHAR(8), default='')
    not_1 = db.Column('not_1', CHAR(1), default='')
    not_2 = db.Column('not_2', CHAR(1), default='')
    not_3 = db.Column('not_3', CHAR(1), default='')
    not_4 = db.Column('not_4', CHAR(1), default='')
    not_5 = db.Column('not_5', CHAR(1), default='')
    feature = db.Column('feature', TINYINT(1), default=0)
    state = db.Column('state', VARCHAR(20), default='')
    zip = db.Column('zip', VARCHAR(20), default='')
    city = db.Column('city', VARCHAR(30), default='')
    user_online = db.Column('user_online', TINYINT(4), default=0)
    user_rating = db.Column('user_rating', DECIMAL(4, 2), default=0.0)
    friends_only = db.Column('friends_only', TINYINT(4), default=0)
    friends_comment = db.Column('friends_comment', TINYINT(4), default=0)
    setting_gb_html = db.Column('setting_gb_html', TINYINT(4), default=0)
    remember_me = db.Column('remember_me', CHAR(1), default='')
    new_pass = db.Column('new_pass', VARCHAR(25), default='')
    is_banned = db.Column('is_banned', TINYINT(1, unsigned=True), default=0)
    last_payment = db.Column('last_payment', DATETIME(), default='0000-00-00 00:00:00')
    total_points = db.Column('total_points', INTEGER(11), default=0)
    actual_song_id = db.Column('actual_song_id', INTEGER(10, unsigned=True), default=0)
    lang_file = db.Column('lang_file', TINYINT(1), default=0)
    c_friends = db.Column('c_friends', INTEGER(11), default=0)
    c_comments = db.Column('c_comments', INTEGER(11), default=0)
    im_status = db.Column('im_status', TINYINT(3, unsigned=True), default=0)
    plugin_style = db.Column('plugin_style', INTEGER(10, unsigned=True), default=0)
    msg_event = db.Column('msg_event', TINYINT(1, unsigned=True), default=0)
    total_friends = db.Column('total_friends', TINYINT(2, unsigned=True), default=0)
    votesgiven = db.Column('votesgiven', INTEGER(11), default=0)
    votestotal = db.Column('votestotal', INTEGER(11), default=0)
    newstotal = db.Column('newstotal', INTEGER(11), default=0)
    CityId = db.Column('CityId', INTEGER(11), default=0)
    RegionId = db.Column('RegionId', INTEGER(11), default=0)
    CountryId = db.Column('CountryId', INTEGER(11), default=0)
    latitude = db.Column('latitude', VARCHAR(255), default='')
    longitude = db.Column('longitude', VARCHAR(255), default=0)
    showmap = db.Column('showmap', INTEGER(1), default=1)
    imBan = db.Column('imBan', TINYINT(1), default='')
    dblon = db.Column('dblon', TEXT, default='')
    dblat = db.Column('dblat', TEXT, default='')

    def __init__(self, user, password, email, **kwargs):
        self.user = user
        self.password = password
        self.email = email
        if 'gender' in kwargs:
            self.gender = kwargs['gender']
        if 'year' in kwargs:
            self.year = kwargs['year']
        if 'month' in kwargs:
            self.month = kwargs['month']
        if 'day' in kwargs:
            self.day = kwargs['day']

    def __repr__(self):
        return '<User %r>' % self.user


class Video(db.Model):
    __tablename__ = 'phpfox_videos'
    vid_id = db.Column('vid_id', INTEGER(11), primary_key=True)
    vid_list_id = db.Column('vid_list_id', INTEGER(11), default=0)
    vid_userid = db.Column('vid_userid', INTEGER(11), default=0)
    vid_title = db.Column('vid_title', VARCHAR(50), default='')
    vid_info = db.Column('vid_info', TEXT, default='')
    vid_type = db.Column('vid_type', VARCHAR(6), default='')
    vid_time = db.Column('vid_time', INTEGER(11), default=0)
    vid_total = db.Column('vid_total', INTEGER(11), default=0)
    vid_rating = db.Column('vid_rating', DECIMAL(4, 2), default=0.0)
    vid_rating_count = db.Column('vid_rating_count', INTEGER(11), default=0)
    vid_url = db.Column('vid_url', TEXT, default='')
    stream_id = db.Column('stream_id', TINYINT(4), default=0)
    vid_tags = db.Column('vid_tags', VARCHAR(100), default='')
    reported = db.Column('reported', INTEGER(1), default=0)
    featured = db.Column('featured', INTEGER(11), default=0)
    comments = db.Column('comments', INTEGER(11), default=0)
    duration = db.Column('duration', INTEGER(11), default=0)
    filesize = db.Column('filesize', INTEGER(11), default=0)

    def __init__(self, title, url, type, **kwargs):
        self.vid_title = title
        self.vid_url = url
        self.vid_list_id = type
        if 'tags' in kwargs:
            self.vid_tags = kwargs['tags']
        if 'details' in kwargs:
            self.vid_info = kwargs['details']

    def __repr__(self):
        return '<Video %r - %r>' % (self.vid_id, self.vid_title)
