import requests

url = "http://localhost:5050/api/v1.0/equipment"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract the list of devices from the response
    devices = data['Equipment']
    
    # Filter devices to include only Cisco devices
    cisco_devices = [device for device in devices if device['Make'] == 'Cisco']
    
    if cisco_devices:
        print("Cisco Devices:")
        for device in cisco_devices:
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
        print("No Cisco devices found.")
        
else:
    # Print an error message if the request failed
    print(f"Error: {response.status_code} - {response.text}")
