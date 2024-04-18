import requests
import json

password = "123"
text = "screenshot"


ip = 'localhost:10000'

url = f'http://{ip}/'

headers = {
    'Content-Type': 'application/json',
}

data = {'password': password, 'text': text}
response = requests.post(url, headers=headers, json=data)

# response = requests.get(url)
# print(response.text)