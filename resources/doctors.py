from data.doctors import Doctor
from flask import abort, jsonify
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from data import db_session

parser = RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('surname')
parser.add_argument('middle_name')
parser.add_argument('sex')
parser.add_argument('work_years')
parser.add_argument('qualifications')
parser.add_argument('specialization')
parser.add_argument('online_appointment', type=bool)
parser.add_argument('workplace')
parser.add_argument('appointment_times')
parser.add_argument('about')
parser.add_argument('email')
parser.add_argument('phone')


def abort_if_doctor_not_found(doctor_id):
    session = db_session.create_session()
    doctor = session.query(Doctor).get(doctor_id)
    if not doctor:
        abort(404, message=f"Doctor {doctor_id} not found")


class DoctorResource(Resource):
    def get(self, doctor_id):
        abort_if_doctor_not_found(doctor_id)
        session = db_session.create_session()
        doctor = session.query(Doctor).get(doctor_id)
        return jsonify({'Doctor': doctor.to_dict()})

    def delete(self, doctor_id):
        abort_if_doctor_not_found(doctor_id)
        session = db_session.create_session()
        doctor = session.query(Doctor).get(doctor_id)
        session.delete(doctor)
        session.commit()
        return jsonify({'success': 'OK'})


class DoctorListResource(Resource):
    def get(self):
        session = db_session.create_session()
        doctors = session.query(Doctor).all()
        return jsonify({'doctors': [item.to_dict(only=('name', 'about', 'email')) for item in doctors]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        doctor = Doctor()
        doctor.name = args['name']
        doctor.surname = args['surname']
        doctor.middle_name = args['middle_name']
        doctor.specialization = args['specialization']
        doctor.appointment_times = args['appointment_times']
        doctor.work_years = args['work_years']
        doctor.qualifications = args['qualifications']
        doctor.online_appointment = args['online_appointment']
        doctor.workplace = args['workplace']
        doctor.about = args['about']
        doctor.sex = args['sex']
        doctor.email = args['email']
        doctor.phone = args['phone']
        session.add(doctor)
        session.commit()
        return jsonify({'success': 'OK'})
