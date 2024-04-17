import requests

password = "123"
text = "cnsl ping google.com"

ip = 'localhost:10000'

url = f'http://{ip}/'

headers = {
    'Content-Type': 'application/json',
}

data = {'password': password, 'text': text}
response = requests.post(url, headers=headers, json=data)

response = requests.get(url)
print(response.text)