import json
import requests as rq

base_url = 'http://127.0.0.1:8000/'
output_template = 'Status Code: %s\nResult: %s'

# Send a GET using the URL http://127.0.0.1:8000
r1 = rq.get(base_url)
print(f'Status Code: {r1.status_code}\nResult{r1.text})')

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Send a POST using the data above
r2 = rq.post(f'{base_url}data', json=data)
print(f'Status Code: {r2.status_code}\nResult{r2.text})')
