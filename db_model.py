from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, ForeignKey
from flask_login import UserMixin

from db_config import db

# CONFIGURE TABLES
# TODO: Create a client table for all your customer/client.
class QClient(db.Model):
    __tablename__ = "qq_clients"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    create_date: Mapped[str] = mapped_column(String(70), nullable=False)

# TODO: Create a User table for all your registered users.
class QUser(UserMixin, db.Model):
    __tablename__ = "qq_users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)  # sqlite database unique meaning case insensitive
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(1000), nullable=False)
    # user profile for "admin" or "user", default to "user"
    profile: Mapped[str] = mapped_column(String(10), nullable=True, default="user")

# TODO: Create a Parts table
class QPart(db.Model):
    __tablename__ = "qq_parts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    manufacturer: Mapped[str] = mapped_column(String(100), nullable=False)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    serial_number: Mapped[str] = mapped_column(String(100), nullable=False)
    shipping_date: Mapped[str] = mapped_column(String(70), nullable=False)
    inspected_b: Mapped[str] = mapped_column(String(1), nullable=False)
    remark: Mapped[str] = mapped_column(String(500), nullable=True)
    photo_uri: Mapped[str] = mapped_column(String(500), nullable=True)
    edited_at: Mapped[str] = mapped_column(String(70), nullable=False)
    date: Mapped[str] = mapped_column(String(70), nullable=False)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("qq_clients.id"))

