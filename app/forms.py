from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    file = FileField('Upload Image', validators=[
        InputRequired(), 
        FileAllowed(['jpg', 'png'], 'Only JPG and PNG images are allowed!')
    ])
    submit = SubmitField('Upload')