from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditorField


# WTForm for creating a client
class CreateClientForm(FlaskForm):
    name = StringField("New client name", validators=[DataRequired(),
                                                      Length(max=250, message="Input is too long (max 250 characters).")])
    description = StringField("Description", validators=[DataRequired(),
                                                         Length(max=500, message="Input is too long (max 500 characters).")])
    submit = SubmitField("Create Client")

# TODO: Create a RegisterForm to register new users


# TODO: Create a LoginForm to login existing users


# TODO: Create a CommentForm so users can leave comments below posts
