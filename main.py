import uuid
from flask import Flask, request, jsonify
from flask_restful import Api
from data import db_session
from requests import get, post

from resources import patients, doctors

app = Flask(__name__)
app.config['SECRET_KEY'] = '6BCfEqNsyWwZUgdvt6RD'
api = Api(app)
api.add_resource(patients.PatientListResource, '/api/patients')
api.add_resource(patients.PatientResource, '/api/patients/<int:patient_id>')
api.add_resource(doctors.DoctorListResource, '/api/doctors')
api.add_resource(doctors.DoctorResource, '/api/doctors/<int:doctor_id>')

symptom_checker_api_token = 'd3fYRiq6NPqM'

@app.route('/api/symptoms/suggestions/<filter_word>')
def get_suggestions(filter_word):
    response = get(f'https://lod.medlinx.online/terminology/api/v1/fhir/ValueSet/$expand?'
                   f'url=http://terminology.medlinx.online/ValueSet/helzy-search-vs&displayLanguage=ru&offset=0&'
                   f'count=10&filter={filter_word}').json()
    suggestions = response['expansion']['contains']
    return jsonify(suggestions)


@app.route('/api/symptoms/start_diagnosis', methods=['POST'])
def start_diagnosis():
    data = request.json()
    patient_resource = {
        'resourceType': 'Patient',
        'gender': data['gender'],  # male/female
        'birthDate': data['birthDate']  # string YYYY-MM-DD
    }
    observation_resource = {
        'resource': data['answer'],  # suggestion answer json object
        'id': "",
        'resourceType': 'Observation',
        'status': 'final',
        "valueCodeableConcept": {
            "coding": [
                {
                    "code": "373066001",
                    "system": "http://snomed.info/sct"
                }
            ]
        }
    }
    observations_bundle = {
        'entry': [observation_resource],
        'resourceType': 'Bundle',
        'type': 'collection'
    }

    cds_request_json = {
        'hook': 'symptom-checker',
        "hookInstance": "586c73ff-1518-41b7-b4f0-590b10120a1c",
        "fhirServer": None,
        "fhirAuthorization": None,
        "context": {},
        "prefetch": {
            'patient': patient_resource,
            "observations": observations_bundle
        }
    }
    response = post(f'https://lod.medlinx.online/cds/cds/1.0/cds-services/symptom-checker+{symptom_checker_api_token}',
                    data=cds_request_json)
    return response




def main():
    db_session.global_init('db/data.sqlite')
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
