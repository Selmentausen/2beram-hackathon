import requests
import json
from requests import get
from pprint import pprint

# Testing rest api
patient = {'name': 'a', 'surname': 'b', 'middle_name': 'c', 'about': 'hello',
           'email': 'abc@def.gh', 'phone': '1234567890'}
doctor = {'name': 'a', 'surname': 'b', 'middle_name': 'c', 'about': 'hello',
          'email': 'abc@def.gh', 'phone': '1234567890', 'work_years': '5',
          'qualifications': 'd', 'specialization': 'e', 'workplace': 'f',
          'appointment_time': 'g'}
# print(requests.post('http://127.0.0.1:8080/api/patients', data=patient).json())
# print(requests.get('http://127.0.0.1:8080/api/patients').json())
# print(requests.get('http://127.0.0.1:8080/api/patients/1').json())
# print(requests.post('http://127.0.0.1:8080/api/doctors', json=doctor).json())
print(requests.get('http://127.0.0.1:8080/api/doctors').json())
print(requests.get('http://127.0.0.1:8080/api/doctors/1').json())

# token = 'd3fYRiq6NPqM'
# payload = f"grant_type=client_credentials&client_id={token}&client_secret=marshmallow"
# print(requests.post(f'https://auth-stage.medlinx.online/connect/token', payload).content)


# answer = requests.get('http://127.0.0.1:8080/api/symptoms/suggestions/кашель').json()[0]
#
# data = {
#     'answer': answer,
#     'patient': {
#         'gender': 'male',
#         'birthDate': '1999-01-12'
#     }
# }
# pprint(requests.post('http://127.0.0.1:8080/api/symptoms/start_diagnosis', data=json.dumps(data)))
#
# patient_resource = {
#     'resourceType': 'Patient',
#     'gender': 'male',  # male/female
#     'birthDate': '1999'  # string YYYY-MM-DD
# }
# observation_resource = {
#     'resource': answer,  # suggestion answer json object
#     'id': "",
#     'resourceType': 'Observation',
#     'status': 'final',
#     "valueCodeableConcept": {
#         "coding": [
#             {
#                 "code": "373066001",
#                 "system": "http://snomed.info/sct"
#             }
#         ]
#     }
# }
# observations_bundle = {
#     'entry': [observation_resource],
#     'resourceType': 'Bundle',
#     'type': 'collection'
# }
#
# cds_request_json = {
#     'hook': 'symptom-checker',
#     "hookInstance": "586c73ff-1518-41b7-b4f0-590b10120a1c",
#     "fhirServer": None,
#     "fhirAuthorization": None,
#     "context": {},
#     "prefetch": {
#         'patient': patient_resource,
#         "observations": observations_bundle
#     }
# }
#
# pprint(requests.post('https://lod.medlinx.online/cds/cds/1.0/cds-services/symptom-checker',
#                      data=json.dumps(cds_request_json)))
