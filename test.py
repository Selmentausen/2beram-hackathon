import requests
from requests import get
from pprint import pprint


answer = requests.get('http://127.0.0.1:8080/api/symptoms/suggestions/кашель').json()[0]
pprint(answer)
pprint(requests.post('http://127.0.0.1:8080/api/symptoms/start_diagnosis', data=answer).)