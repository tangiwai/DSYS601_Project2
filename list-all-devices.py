import requests

url = "http://localhost:5050/api/v1.0/equipment"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    devices = data['Equipment']
    for device in devices:
        print(f"ID: {device['id']}")
        print(f"Hostname: {device['Hostname']}")
        print(f"Type: {device['Type']}")
        print(f"Make: {device['Make']}")
        print(f"Model: {device['Model']}")
        print(f"Firmware: {device['Firmware']}")
        print(f"Management IP: {device['ManagementIP']}")
        print(f"Management VLAN: {device['ManagementVlan']}")
        print()
else:
    print(f"Error: {response.status_code} - {response.text}")
