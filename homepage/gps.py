import requests
# import websocket
import json
import base64


def encode_credentials(user_id, password):
    credentials = f"{user_id}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    return encoded_credentials


user_id = "developerbibek1997@gmail.com"
password = "Heyiknow777"

# Task 1: Get token using basic auth
url_token = "https://itsochvts.com/api/session/token"
payload = 'Content-Type=application%2Fx-www-form-urlencoded&expiration=2024-09-29T09%3A04%3A51Z'
headers_token = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': f'Basic {encode_credentials(user_id, password)}'
}

response = requests.request("POST", url_token, headers=headers_token, data=payload)
print(response.text)
token = response.text

# Task 2: Use token to create session
url_session = f"https://itsochvts.com/api/session?token={token}"
response_session = requests.get(url_session)

# Get session cookie
session_cookie = response_session.cookies.get_dict()['JSESSIONID']
print(session_cookie)



def get_devices():

    # Task 3: Use session to get device list
    url_devices = "https://itsochvts.com/api/devices"

    headers_devices = {
        'Cookie': f'JSESSIONID={session_cookie}'
    }
    response_devices = requests.get(url_devices, headers=headers_devices)
    devices = response_devices.json()


    return devices


def get_position():

    url_devices = "https://itsochvts.com/api/positions"

    headers_devices = {
        'Cookie': f'JSESSIONID={session_cookie}'
    }

    response_devices = requests.get(url_devices, headers=headers_devices)
    devices = response_devices.json()


    return devices


def get_details(track_no):

    # Task 3: Use session to get device list
    devices = get_devices()
    positions = get_position()

    specific_device = None
    for d in devices:
        print(d['uniqueId'])
        print(track_no)
        if int(d['uniqueId']) == int(track_no):
           specific_device = d
           print("yayayayay")

    if not specific_device:
        return None

    specific_position = None
    for position in positions:
        if position['deviceId'] == specific_device['id']:
            specific_position = position
            break

    if not specific_position:
        return None

    return {
        'device': specific_device,
        'position': specific_position
    }

    
    # device_position = {
        
    # }

    # # print(devices)

    # for i in devices:
    #     print(i)
    #     # devices[i]
        
    #     latitude = i['latitude']
    #     longitude = i['longitude']
    #     address = i['address']

    #     print(f"Latitude: {latitude}")
    #     print(f"Longitude: {longitude}")
    #     print(f"Address: {address}")


# def get_devices_location(track_no):
#     # Fetching devices
#     url_devices = "https://itsochvts.com/api/devices"
#     headers_devices = {
#         'Cookie': f'JSESSIONID={session_cookie}'
#     }
#     response_devices = requests.get(url_devices, headers=headers_devices)
#     devices = response_devices.json()
#     for i in devices:
#         latitude = i['latitude']
#         longitude = i['longitude']
#         address = i['address']

#         print(f"Latitude: {latitude}")
#         print(f"Longitude: {longitude}")
#         print(f"Address: {address}")

#     # return devices
    

#     for device in devices:
#         print(device)
#         if device['id'] == track_no:
#             print(f"Device found: {device}")

#             # Fetching device positions
#             url_positions = "https://itsochvts.com/api/positions"
#             response_positions = requests.get(url_positions, headers=headers_devices)
#             positions = response_positions.json()

#             for position in positions:
#                 if position['deviceId'] == track_no:
#                     latitude = position['latitude']
#                     longitude = position['longitude']
#                     address = position['address']

#                     print(f"Latitude: {latitude}")
#                     print(f"Longitude: {longitude}")
#                     print(f"Address: {address}")

#                     return position

#     print("Device not found")
#     return None

