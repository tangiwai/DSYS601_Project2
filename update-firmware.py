import requests

url = "http://localhost:5050/api/v1.0/equipment"

# Send a GET request to the API to retrieve the devices
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the list of devices from the response
    devices = data['Equipment']

    # Filter devices to include only Cisco devices with firmware not equal to 15.4
    filtered_devices = [device for device in devices if device['Make'] == 'Cisco' and device['Firmware'] != 15.4]

    if filtered_devices:
        print("Devices matching the criteria:")
        for device in filtered_devices:
            # Update the firmware version to 15.4
            device['Firmware'] = 15.4

            # Send the updated device data back to the API
            response = requests.put(f"{url}/{device['id']}", json=device)
            if response.status_code == 200:
                print(f"Device with ID {device['id']} updated successfully.")
            else:
                print(f"Failed to update device with ID {device['id']}. Error: {response.status_code} - {response.text}")
    else:
        print("No devices found matching the criteria.")

else:
    # Print an error message if the request failed
    print(f"Error: {response.status_code} - {response.text}")
