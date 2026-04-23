from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, ForeignKey
from flask_login import UserMixin

from db_config import db

# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    # author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # Create Foreign Key, "users.id" the users refers to the table name of User.
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("blog_users.id"))
    # Create reference to the User object. The "posts" refers to the posts property in the User class.
    author = relationship("User", back_populates="posts")



# TODO: Create a User table for all your registered users.
class User(UserMixin, db.Model):
    __tablename__ = "blog_users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)  # sqlite database unique meaning case insensitive
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(1000), nullable=False)
    # user profile for "admin" or "user", default to "user"
    profile: Mapped[str] = mapped_column(String(10), nullable=True, default="user")
    # This will act like a List of BlogPost objects attached to each User.
    # The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")
    # *******Add parent relationship*******#
    # "comment_author" refers to the comment_author property in the BlogComment class.
    comments = relationship("BlogComment", back_populates="comment_author")


# TODO: Create a Comments table
class BlogComment(db.Model):
    __tablename__ = "blog_comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    # *******Add child relationship*******#
    # "blog_users.id" The users refers to the tablename of the Users class.
    # "comments" refers to the comments property in the User class.
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("blog_users.id"))
    comment_author = relationship("User", back_populates="comments")