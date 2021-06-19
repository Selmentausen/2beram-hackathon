from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
import sqlalchemy
from sqlalchemy import orm
import datetime


class MedicalCard(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'medical_cards'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    height = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    weight = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sex = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    illnesses = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    symptoms = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    patient_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('patients.id'))
