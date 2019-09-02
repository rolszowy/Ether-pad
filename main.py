import requests
resp = requests.get('http://10.48.26.114:9001/p/cases/export/txt')
payload = resp.content.decode("ascii")
print(type(payload))
print(payload)
