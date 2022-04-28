import requests

url = "http://localhost:7071/api/fetchItemData"

payload = {
    'name': "Harshik",
}
headers = {'content-type': 'application/json'}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.text)
