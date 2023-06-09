import requests

url = 'http://localhost:5050/api/v1.0/equipment'  # Replace with the URL of your RESTful server

response = requests.options(url)

allowed_methods = response.headers.get('allow', '')

if 'PUT' in allowed_methods:
    print("PUT method is allowed.")
else:
    print("PUT method is not allowed.")
