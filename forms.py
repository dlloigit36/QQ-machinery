from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL, Length, Optional
from flask_ckeditor import CKEditorField


# WTForm for creating a client
class CreateClientForm(FlaskForm):
    name = StringField("New client name", validators=[DataRequired(),
                                                      Length(max=250, message="Input is too long (max 250 characters).")])
    description = StringField("Description", validators=[DataRequired(),
                                                         Length(max=500, message="Input is too long (max 500 characters).")])
    submit = SubmitField("Create Client")

# TODO: Create a parts Form
class CreatePartForm(FlaskForm):
    manufacturer = StringField(
        "Manufacturer",
        validators=[DataRequired(), Length(max=100)]
    )
    model = StringField(
        "Model",
        validators=[DataRequired(), Length(max=100)]
    )
    serial_number = StringField(
        "Serial Number",
        validators=[DataRequired(), Length(max=100)]
    )
    shipping_date = DateField(
        "Shipping Date",
        format="%Y-%m-%d",
        validators=[DataRequired()],
        render_kw={"placeholder": "YYYY-MM-DD"}
    )
    inspected_b = SelectField(
        "Inspected",
        choices=[("Y", "Yes"), ("N", "No")],
        validators=[DataRequired()]
    )
    remark = TextAreaField(
        "Remark",
        validators=[Optional(), Length(max=500)]
    )
    photo_uri = StringField(
        "Photo URI",
        validators=[Optional(), Length(max=500), URL()]
    )
    edit_date = DateField(
        "Edit Date",
        format="%Y-%m-%d",
        validators=[DataRequired()],
        render_kw={"placeholder": "YYYY-MM-DD"}
    )
    create_date = DateField(
        "Create Date",
        format="%Y-%m-%d",
        validators=[DataRequired()],
        render_kw={"placeholder": "YYYY-MM-DD"}
    )
    submit = SubmitField("Create Part")

# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign me up.")

# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let me in.")



