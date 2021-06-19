from data.patients import Patient
from flask import abort, jsonify
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from data import db_session

parser = RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('surname')
parser.add_argument('middle_name')
parser.add_argument('about')
parser.add_argument('email')
parser.add_argument('phone')


def abort_if_patient_not_found(patient_id):
    session = db_session.create_session()
    patient = session.query(Patient).get(patient_id)
    if not patient:
        abort(404, message=f"Patient {patient_id} not found")


class PatientResource(Resource):
    def get(self, patient_id):
        abort_if_patient_not_found(patient_id)
        session = db_session.create_session()
        patient = session.query(Patient).get(patient_id)
        return jsonify({'Patient': patient.to_dict()})

    def delete(self, patient_id):
        abort_if_patient_not_found(patient_id)
        session = db_session.create_session()
        patient = session.query(Patient).get(patient_id)
        session.delete(patient)
        session.commit()
        return jsonify({'success': 'OK'})


class PatientListResource(Resource):
    def get(self):
        session = db_session.create_session()
        patients = session.query(Patient).all()
        return jsonify({'patients': [item.to_dict(only=('name', 'surname', 'middle_name',
                                                        'email', 'phone')) for item in patients]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        patient = Patient()
        patient.name = args['name']
        patient.surname = args['surname']
        patient.middle_name = args['middle_name']
        patient.about = args['about']
        patient.email = args['email']
        patient.phone = args['phone']
        session.add(patient)
        session.commit()
        return jsonify({'success': 'OK'})
