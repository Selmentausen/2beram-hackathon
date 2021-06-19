from data.medical_cards import MedicalCard
from flask import abort, jsonify
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from data import db_session

parser = RequestParser()
parser.add_argument('patient_id', required=True)
parser.add_argument('height')
parser.add_argument('weight')
parser.add_argument('age', type=int)
parser.add_argument('illnesses')
parser.add_argument('symptoms')


def abort_if_medical_card_not_found(medical_card_id):
    session = db_session.create_session()
    medical_card = session.query(MedicalCard).get(medical_card_id)
    if not medical_card:
        abort(404, message=f"MedicalCard {medical_card_id} not found")


class MedicalCardResource(Resource):
    def get(self, medical_card_id):
        abort_if_medical_card_not_found(medical_card_id)
        session = db_session.create_session()
        medical_card = session.query(MedicalCard).get(medical_card_id)
        return jsonify({'MedicalCard': medical_card.to_dict()})

    def delete(self, medical_card_id):
        abort_if_medical_card_not_found(medical_card_id)
        session = db_session.create_session()
        medical_card = session.query(MedicalCard).get(medical_card_id)
        session.delete(medical_card)
        session.commit()
        return jsonify({'success': 'OK'})


class MedicalCardListResource(Resource):
    def get(self):
        session = db_session.create_session()
        medical_cards = session.query(MedicalCard).all()
        return jsonify({'medical_cards': [
            item.to_dict(only=('patient_id',)) for item in
            medical_cards]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        medical_card = MedicalCard()
        medical_card.patient_id = args['patient_id']
        medical_card.height = args['height']
        medical_card.weight = args['weight']
        medical_card.age = args['age']
        medical_card.illnesses = args['illnesses']
        medical_card.symptoms = args['symptoms']
        session.add(medical_card)
        session.commit()
        return jsonify({'success': 'OK'})
