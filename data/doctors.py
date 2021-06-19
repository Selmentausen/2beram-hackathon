from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
import sqlalchemy
import datetime


class Doctor(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'doctors'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    middle_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sex = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    qualifications = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    specialization = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_years = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    online_appointment = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    appointment_times = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    workplace = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
