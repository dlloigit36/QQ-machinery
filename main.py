import os
from datetime import date

import werkzeug
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreateClientForm, CreatePartForm, RegisterForm, LoginForm
from dotenv import load_dotenv

from db_config import db, init_db
from db_model import QUser, QClient, QPart
'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY', "8BYkEfBA6O6donzWlSihBXox7C0sKR6b")
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
# authentication
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(QUser, user_id)

# decorator functions
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


# TODO: Init db and create table for all data.
init_db(app, "inventory.db")
with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET', 'POST'])
def register():
    new_user_form = RegisterForm()
    if new_user_form.validate_on_submit():
        # hash and salt user entered password
        hash_salt_password = werkzeug.security.generate_password_hash(
            new_user_form.password.data,
            method='pbkdf2:sha256',
            salt_length=8)
        entered_email = new_user_form.email.data.strip().lower()
        register_user = QUser(
            name=new_user_form.name.data,
            email=entered_email,
            password=hash_salt_password)
        # check if new register user email already exist
        result = db.session.execute(db.select(QUser).where(QUser.email == entered_email))
        found_db_user = result.scalar()
        # print(f"result scalar={db_user}")
        if found_db_user:
            flash(f"Email address {entered_email} already registered!", 'error')
        else:
            try:
                # add new user into db table
                db.session.add(register_user)
                db.session.commit()
            except IntegrityError as e:
                # catch error
                db.session.rollback()
                # flash message for error
                flash(f'error: {e}', 'error')
            else:
                # if add user return no error
                login_user(register_user)
                # flash('Logged in successfully.', 'info')
                return redirect(url_for("home"))
    return render_template("register.html", form=new_user_form)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        entered_email = login_form.email.data
        entered_password = login_form.password.data
        # check db for entered email
        result = db.session.execute(db.select(QUser).where(QUser.email == entered_email))
        found_db_user = result.scalar()
        if not found_db_user:
            flash(message="User email address not found! Please register.", category='error')
        else:
            password_matched = werkzeug.security.check_password_hash(found_db_user.password, entered_password)
            if password_matched:
                # flash(message="Verified entered password. Login successfully.", category='info')
                login_user(found_db_user)
                return redirect(url_for('home'))
            else:
                flash(message="Wrong password. Please try again.", category='error')
    return render_template("login.html", form=login_form, current_user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/')
@login_required
def home():
    return redirect(url_for('get_all_client'))

@app.route('/client')
@login_required
def get_all_client():
    result = db.session.execute((db.select(QClient)))
    clients = result.scalars().all()
    client_t_header = ["Name", "Description", "Created", "Parts count"]
    return render_template(
        "list-client.html",
        table_header=client_t_header,
        all_client=clients,
        current_user=current_user
    )


# TODO: Route to list part for selected client.
@app.route("/client-part/<int:client_id>")
@login_required
def get_client_part(client_id):
    requested_client = db.get_or_404(QClient, client_id)
    part_t_header=["Manufacturer", "Model", "Serial number", "Shipping date", "Inspected", "Remark",
                   "Photo URL", "Edited", "Created"]
    result = db.session.execute(db.select(QPart).where(QPart.client_id == int(client_id)))
    parts = result.scalars().all()
    return render_template(
        "list-part.html",
        table_header=part_t_header,
        all_part=parts,
        client=requested_client,
        current_user=current_user
    )


# TODO: Route to add new client.
@app.route("/new-client", methods=["GET", "POST"])
@login_required
def add_new_client():
    form = CreateClientForm()
    if form.validate_on_submit():
        new_client = QClient(
            name=form.name.data,
            description=form.description.data,
            create_date=date.today().strftime("%Y-%m-%d")
        )
        try:
            db.session.add(new_client)
            db.session.commit()
        except IntegrityError as e:
            # catch error
            db.session.rollback()
            # flash message for error
            print(f"db commit error= {e}")
            msg = f"duplicate client name {form.name.data}"
            flash(f'error: {msg}', 'error')
        else:
            return redirect(url_for("get_all_client"))
    return render_template(
        "make-client.html",
        form=form,
        current_user=current_user
    )

# TODO: Route to add new part for selected client. clientId passed in as URL argument.
@app.route("/new-part", methods=["GET", "POST"])
@login_required
def add_new_part():
    client_id = request.args.get("clientId", type=str)
    requested_client = db.get_or_404(QClient, client_id)
    create_part_form = CreatePartForm()
    if create_part_form.validate_on_submit():
        new_part = QPart(
            manufacturer=create_part_form.manufacturer.data,
            model=create_part_form.model.data,
            serial_number=create_part_form.serial_number.data,
            shipping_date=create_part_form.shipping_date.data,
            inspected_b=create_part_form.inspected_b.data,
            remark=create_part_form.remark.data,
            photo_uri=create_part_form.photo_uri.data,
            edit_date=create_part_form.edit_date.data,
            create_date=create_part_form.create_date.data,
            client_id=int(client_id)
        )
        db.session.add(new_part)
        db.session.commit()
        return redirect(url_for("get_client_part", client_id=client_id))
    return render_template(
        "make-part.html",
        form=create_part_form,
        action="create",
        client=requested_client,
        current_user=current_user
    )

# route to test Bootstrap5 dataset table template
@app.route('/table')
def table_sample():
    return render_template('test-table.html')

# route to test Bootstrap5 dataset table sample
@app.route('/table2')
def table_sample2():
    return render_template('test-table-2.html')


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-list-part.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=7002)
