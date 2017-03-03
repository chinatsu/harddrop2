from wtforms import Form, TextField, PasswordField, SubmitField, SelectField, TextAreaField, validators

class LoginForm(Form):
    action = "Login"
    username = TextField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')        

class AddVideo(Form):
    action = "Add video"
    title = TextField('Title', [validators.required()])
    category = SelectField('Category', choices=[
                                           (1, "Other Tetris Videos"), 
                                           (16, "Tetris Guideline Games"),
                                           (13, "Tetris Grandmaster Series"),
                                           (17, "Fan Made Games")
                                       ], coerce=int)
    tags = TextField('Tags', [validators.optional()])
    details = TextAreaField('Details', [validators.optional()])
    url = TextField('URL', [validators.regexp('http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?', message="Must be a YouTube URL.")])
    submit = SubmitField('Submit')
    
class Register(Form):
    action = "Register"
    username = TextField('Username', [validators.required(), validators.Length(min=3, max=20)])
    password = PasswordField('Password', [validators.required(), validators.Length(min=6, max=32), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm password')
    email = TextField('Email', [validators.required(), validators.Email()])
    gender = SelectField('Gender', [validators.optional()], choices=[
                                        (328, "Male"),
                                        (329, "Female"),
                                        (327, "Undisclosed")
                                    ], coerce=int)
    dob = TextField('Date of birth', [validators.optional(), validators.regexp('(\d{4})\/(\d{2})\/(\d{2})', message="Must have the following format: YYYY/MM/DD")])
    submit = SubmitField('Register')
